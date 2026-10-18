"""Deterministic finite checks for the explicit Aluthge-star formulas.
Scientific proof is in RESULT.md; these checks are corroborative, not certificates.
Uses only the Python standard library. Run: python3 verify.py
"""
import math
import random

N = 0

def near(x,y,tol=1e-10):
    global N
    assert math.isfinite(x) and math.isfinite(y), (x,y)
    assert abs(x-y) <= tol * max(1.0,abs(x),abs(y)), (x,y,tol)
    N += 1

def info(t,a,c):
    C=max(c); a2=[x*x for x in a]
    upper=sum(a2[i] for i in range(len(c)) if c[i]==C)
    qs=[(a2[i]/upper,(c[i]/C)**(2*t)) for i in range(len(c)) if c[i]<C]
    def z(n): return math.log1p(sum(q*r**n for q,r in qs))
    def branch(p):
        zval=z(p)
        return [C*(a[i]/math.sqrt(upper))*math.exp((h(p)-zval)/2) * (c[i]/C)**(t*p) for i in range(len(a))]
    memo={0:math.log(sum(a2)/(C*C))}
    def h(n):
        if n not in memo:
            for j in range(max(memo)+1,n+1):
                memo[j]=(1-t)*memo[j-1]+z(j)-z(j-1)
        return memo[n]
    def err(n):
        hh=h(n);zz=z(n)
        return C*math.sqrt(math.expm1((hh-zz)/2)**2+math.exp(hh)*(-math.expm1(-zz)))
    return C,upper,qs,z,h,branch,err

def tree_weights(a,c,depth):
    root=('root',0)
    children={root:[(i,1) for i in range(len(a))]}
    weights={(root,(i,1)):a[i] for i in range(len(a))}
    for i in range(len(a)):
        for k in range(1,depth):
            children[(i,k)]=[(i,k+1)]
            weights[((i,k),(i,k+1))]=c[i]
        children[(i,depth)]=[]
    return root,children,weights

def direct_aluthge(weights, children, t):
    # Implementation from the defining polar decomposition of a tree shift:
    # |T| is diagonal, its entries being the norms of the corresponding columns.
    gamma={u:math.sqrt(sum(weights[(u,v)]**2 for v in vs)) for u,vs in children.items()}
    return {(u,v):w*((gamma[v]/gamma[u])**t if gamma[u] else 0.0)
            for (u,v),w in weights.items()}

rng=random.Random(20261011)
for case in range(120):
    d=2+case%4
    c=[0.4+3*rng.random() for _ in range(d)]
    if case%5==0: c[0]=c[1]=max(c)
    a=[0.3+2*rng.random() for _ in range(d)]
    t=[.2,.5,.72][case%3]
    C,upper,qs,z,h,branch,err=info(t,a,c)
    root,child,W=tree_weights(a,c,16)
    for m in range(7):
        b=branch(m)
        for i in range(d): near(W[(root,(i,1))],b[i])
        for i in range(d):
            near(W[((i,1),(i,2))],c[i])
        target=[C*a[i]/math.sqrt(upper) if c[i]==C else 0. for i in range(d)]
        direct=math.sqrt(sum((b[i]-target[i])**2 for i in range(d)))
        near(direct,err(m))
        W=direct_aluthge(W,child,t)

# Three asymptotic regimes, with independent exact-recursion checks.
regimes=[
    ('slow-dominated',.5,[1.,2.],[2.,1.6]),
    ('root-dominated',.25,[2.,1.],[2.,.2]),
    ('critical',.5,[2.,1.],[2.,.5]),
    ('tied-fast',.5,[1.,2.,1.],[2.,2.,.5]),
]
for label,t,a,c in regimes:
    C,upper,qs,z,h,branch,err=info(t,a,c)
    rho=math.sqrt(max(r for _,r in qs)); eta=1-t
    Q=sum(q for q,r in qs if abs(math.sqrt(r)-rho)<1e-12)
    H=None
    if rho*rho<eta:
        H=math.log(sum(x*x for x in a)/(C*C))
        for j in range(220):
            H+=(z(j+1)-z(j))/eta**(j+1)
    if eta<rho: rate=rho; coefficient=C*math.sqrt(Q)
    elif eta==rho: rate=rho; coefficient=C*math.sqrt(Q+H*H/4)
    elif abs(H)>1e-9: rate=eta; coefficient=C*abs(H)/2
    else: rate=rho; coefficient=C*math.sqrt(Q)
    m=65 if label == 'slow-dominated' else 35
    approx=err(m)/rate**m
    near(approx,coefficient,1.5e-3)

# Exactly tuned fast-mode cancellation: common scaling changes H but not q_i.
t=.25;a=[2.,1.];c=[2.,.2]
C,U,qs,z,h,branch,err=info(t,a,c)
eta=1-t
H=math.log(sum(x*x for x in a)/C**2)
for j in range(160): H+=(z(j+1)-z(j))/eta**(j+1)
a_tuned=[x*math.exp(-H/2) for x in a]
C,U,qs,z,h,branch,err=info(t,a_tuned,c)
rho=math.sqrt(max(r for _,r in qs));Q=sum(q for q,r in qs if abs(math.sqrt(r)-rho)<1e-12)
near(err(35)/rho**35,C*math.sqrt(Q),2e-4)

# Equal-tail boundary: the recurrence becomes a single exponential.
for t in [.2,.5,.8]:
    a=[.4,1.8,2.1]; c=[1.4]*len(a)
    C,U,qs,z,h,branch,err=info(t,a,c)
    h0=math.log(sum(x*x for x in a)/C**2)
    for m in range(25):
        near(err(m),C*abs(math.expm1(h0*(1-t)**m/2)))

print('PASS',N,'deterministic scalar checks; direct finite-tree Aluthge recurrences, exact error identity, asymptotic regimes, and equal-tail boundary')
