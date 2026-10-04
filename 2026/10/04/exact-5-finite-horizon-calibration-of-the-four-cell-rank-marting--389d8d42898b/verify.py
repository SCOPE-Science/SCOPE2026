#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
import math

Q=4
N=128
ALPHA=Fraction(1,20)
PREV=(10,2,2,1)       # n=15
CAND=(22,22,13,5)      # n=62

facts=[math.factorial(i) for i in range(N+Q+1)]

def m_numden(state):
    n=sum(state)
    num=(Q**n)*facts[Q-1]
    for c in state:
        num*=facts[c]
    den=facts[n+Q-1]
    g=math.gcd(num,den)
    return num//g, den//g

def M(state):
    a,b=m_numden(state)
    return Fraction(a,b)

def less_M(s,t):
    # exact M(s) < M(t)
    ns,ds=m_numden(s); nt,dt=m_numden(t)
    return ns*dt < nt*ds

def safe_path_count(threshold_state, N=N):
    states={(0,0,0,0):1}
    for n in range(1,N+1):
        nxt={}
        for s,count in states.items():
            i=0
            while i<Q:
                j=i+1
                while j<Q and s[j]==s[i]:
                    j+=1
                multiplicity=j-i
                u=list(s)
                u[i]+=1
                u.sort(reverse=True)
                u=tuple(u)
                if less_M(u,threshold_state):
                    nxt[u]=nxt.get(u,0)+multiplicity*count
                i=j
        states=nxt
    return sum(states.values())

def crossing_prob(threshold_state):
    safe=safe_path_count(threshold_state)
    return Fraction(Q**N-safe,Q**N)

def partitions4(n):
    for a in range(n,-1,-1):
        r1=n-a
        if r1>3*a:
            continue
        for b in range(min(a,r1),-1,-1):
            r2=r1-b
            if r2>2*b:
                continue
            for c in range(min(b,r2),-1,-1):
                d=r2-c
                if d<=c:
                    yield (a,b,c,d)

def brute_cross(Nsmall,threshold_state):
    crossed=0
    for seq in product(range(Q), repeat=Nsmall):
        counts=[0]*Q
        hit=False
        for z in seq:
            counts[z]+=1
            s=tuple(sorted(counts,reverse=True))
            if not less_M(s,threshold_state):
                hit=True
                break
        crossed+=hit
    return Fraction(crossed,Q**Nsmall)

def dp_cross_small(Nsmall,threshold_state):
    states={(0,0,0,0):1}
    for n in range(1,Nsmall+1):
        nxt={}
        for s,count in states.items():
            i=0
            while i<Q:
                j=i+1
                while j<Q and s[j]==s[i]: j+=1
                mult=j-i
                u=list(s);u[i]+=1;u.sort(reverse=True);u=tuple(u)
                if less_M(u,threshold_state):
                    nxt[u]=nxt.get(u,0)+mult*count
                i=j
        states=nxt
    safe=sum(states.values())
    return Fraction(Q**Nsmall-safe,Q**Nsmall)

# 1. Formula sanity: M_0=M_1=1, a repeated cell at n=2 gives 8/5.
assert M((0,0,0,0))==1
assert M((1,0,0,0))==1
assert M((2,0,0,0))==Fraction(8,5)
assert M((1,1,0,0))==Fraction(4,5)

# 2. Recurrence is checked against all 4^8 labelled paths at a nontrivial threshold.
assert dp_cross_small(8,(5,1,1,1)) == brute_cross(8,(5,1,1,1))

# 3. Exhaustively certify that there is no martingale support value strictly between PREV and CAND through N.
mp=M(PREV); mc=M(CAND)
assert mp < mc
between=[]
for n in range(1,N+1):
    for s in partitions4(n):
        ms=M(s)
        if mp < ms < mc:
            between.append((n,s,ms))
assert not between, between[:5]

# 4. Exact finite-horizon sizes at the consecutive support levels.
p_prev=crossing_prob(PREV)
p_cand=crossing_prob(CAND)
assert p_prev > ALPHA
assert p_cand <= ALPHA

print('PREVIOUS_THRESHOLD', mp)
print('PREVIOUS_THRESHOLD_DECIMAL', format(float(mp),'.15f'))
print('PREVIOUS_SIZE', p_prev)
print('PREVIOUS_SIZE_DECIMAL', format(float(p_prev),'.15f'))
print('CALIBRATED_THRESHOLD', mc)
print('CALIBRATED_THRESHOLD_DECIMAL', format(float(mc),'.15f'))
print('CALIBRATED_SIZE', p_cand)
print('CALIBRATED_SIZE_DECIMAL', format(float(p_cand),'.15f'))
print('VERIFY_OK')
