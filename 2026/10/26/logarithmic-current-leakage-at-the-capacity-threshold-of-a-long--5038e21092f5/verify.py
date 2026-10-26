"""Independent finite-state checks of long-branch exclusion current asymptotics.

Run: python verify.py
Requires: Python standard library, NumPy, SciPy.
"""
import itertools
import math
import numpy as np
from scipy.special import logsumexp

TESTS = 0

def check(flag, description):
    global TESTS
    TESTS += 1
    if not flag:
        raise AssertionError(description)


def log_probabilities(L, M, q, N):
    # Canonical weights conditional on K occupied sites of the L-vertex backbone.
    # For general N, the remaining N-K particles occupy the M-depth tree.
    K_min, K_max = max(0, N-M), min(L, N)
    values=[]
    for K in range(K_min,K_max+1):
        r=N-K
        log_ways=math.lgamma(L+1)-math.lgamma(K+1)-math.lgamma(L-K+1)
        # elementary symmetric polynomial of q^1,...,q^M
        logs=np.full(r+1,-np.inf)
        logs[0]=0.0
        for d in range(1,M+1):
            for j in range(min(d,r),0,-1):
                logs[j]=np.logaddexp(logs[j],logs[j-1]+d*math.log(q))
        values.append(log_ways+logs[r])
    vals=np.array(values,dtype=float)
    return np.arange(K_min,K_max+1),np.exp(vals-logsumexp(vals))


def fast_law_at_threshold(L,M,q):
    a=1.0/q
    upper=min(L,M)
    logs=np.zeros(upper+1)
    for k in range(upper):
        logr=math.log(L-k)-math.log(k+1)-(k+1)*math.log(q)
        logr+=math.log1p(-a**(M-k))-math.log1p(-a**(k+1))
        logs[k+1]=logs[k]+logr
    p=np.exp(logs-logsumexp(logs))
    ks=np.arange(upper+1,dtype=float)
    e=float(p@ks)
    e2=float(p@(ks**2))
    return e,e2,p


def exact_current(L,M,q,N,hf=1.4,hb=0.4):
    ks,p=log_probabilities(L,M,q,N)
    return float((hf-hb)*(p@(ks*(L-ks)))/(L*(L-1)))

# Direct 2^M enumeration vs q-binomial ratios for the critical particle count.
for L,M,q in [(4,3,1.5),(5,4,2.0),(6,4,3.0),(7,6,1.2)]:
    ks,pe=log_probabilities(L,M,q,M)
    e,e2,p=fast_law_at_threshold(L,M,q)
    check(np.max(np.abs(pe-p))<1e-12,"q-binomial ratio disagrees with direct canonical counting")
    check(abs(float(pe@ks)-e)<1e-12,"backbone mean mismatch")

# Direct CTMC generator: periodic backbone, one path-shaped closed side branch.
for L,M,q,hf,hb in [(4,3,2.,1.4,.4),(5,3,1.25,2.,.6)]:
    N=M
    states=list(itertools.combinations(range(L+M),N))
    order={s:i for i,s in enumerate(states)}
    Q=np.zeros((len(states),len(states)))
    weights=np.array([q**sum(d for d in range(1,M+1) if L+d-1 in s) for s in states],float)
    pi=weights/weights.sum()
    edge_rates=[]
    for i in range(L):
        j=(i+1)%L
        edge_rates.extend([(i,j,hf),(j,i,hb)])
    edge_rates.extend([(0,L,q),(L,0,1.)])
    for depth in range(1,M):
        u,v=L+depth-1,L+depth
        edge_rates.extend([(u,v,q),(v,u,1.)])
    for index,s in enumerate(states):
        occupied=set(s)
        for u,v,r in edge_rates:
            if u in occupied and v not in occupied:
                s2=tuple(sorted((occupied-{u})|{v}))
                dest=order[s2]
                Q[index,dest]+=r
                Q[index,index]-=r
    check(np.max(np.abs(pi@Q))<1e-11,"claimed product weights not stationary for finite CTMC")
    direct=(hf-hb)*sum(pi[index]*(1 in s and 2 not in s) for index,s in enumerate(states))
    formula=exact_current(L,M,q,N,hf,hb)
    check(abs(direct-formula)<1e-12,"current differs from direct finite CTMC")
    check(abs(pi.sum()-1)<1e-12,"stationary weights do not sum to one")

# Exact particle-hole and reciprocal-bias duality.
for L,M,q in [(5,4,2.),(7,5,1.5),(8,6,3.),(10,8,1.11)]:
    v1=exact_current(L,M,q,M)
    v2=exact_current(L,M,1/q,L)
    check(abs(v1-v2)<1e-11,"particle-hole reciprocal duality fails")

# Critical logarithmic leakage, including the log-log correction.
for q in (1.25,1.8,2.,4.):
    c=math.log(q)
    errs=[]
    for L in (300,600,1200,2400,4800):
        M=L
        e,e2,_=fast_law_at_threshold(L,M,q)
        lead=(math.log(L)-math.log(math.log(L))+math.log(c))/c
        errs.append(e-lead)
        check(e2>=e*e-1e-9,"negative variance")
        check(e>0,"backbone mean should be positive")
        check(abs((e-e2/L)/(L-1)-e/L)<4*(math.log(L)**2)/(c*c*L*L),"exact current/mean relation")
    check(abs(errs[-1])<max(5.,2./c),"log-log centering unexpectedly inaccurate")
    check(abs(errs[-1]-errs[-2])<2.0,"centering error not stable")

print(f"PASS: {TESTS} independent deterministic assertions")
