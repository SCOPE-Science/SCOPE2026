"""Independent finite enumeration checks for Ewens cycle-count factorial moments.
Run: python verify.py. Requires only the Python standard library.
The finite checks complement, but do not replace, the analytic proof.
"""
from fractions import Fraction as Q
from itertools import permutations, combinations
from collections import defaultdict
from math import factorial

THETAS = (Q(1,2), Q(1), Q(3,2), Q(2), Q(3))
checks = 0

def count_cycles(perm):
    n = len(perm)
    seen = [False]*n
    out = [0]*(n+1)
    for u in range(n):
        if seen[u]: continue
        v=u; length=0
        while not seen[v]:
            seen[v]=True
            length+=1
            v=perm[v]
        out[length]+=1
    return out

def falling(x,k):
    a=1
    for i in range(k):a*=x-i
    return a

def f(n,t,k):
    out=Q(1)
    for j in range(k):
        out*=Q(n-j)/(t+n-1-j)
    return out

def moment(n,t,ks):
    m=sum(j*kj for j,kj in ks.items())
    if m>n:return Q(0)
    ans=f(n,t,m)
    for j,k in ks.items():ans*= (t/j)**k
    return ans

for n in range(2,8):
    summaries=[]
    for p in permutations(range(n)):
        c=count_cycles(p)
        summaries.append((c,sum(c)))
    for t in THETAS:
        weights=[t**cycles for c,cycles in summaries]
        den=sum(weights,Q(0))
        want=Q(1)
        for j in range(n):want*=t+j
        assert den==want
        checks+=1
        observed={}
        for r in range(1,n+1):
            observed[r]=sum((w*c[r] for (c,_),w in zip(summaries,weights)),Q(0))/den
            assert observed[r]==moment(n,t,{r:1})
            checks+=1
        for r,s in combinations(range(1,n+1),2):
            joint=sum((w*c[r]*c[s] for (c,_),w in zip(summaries,weights)),Q(0))/den
            assert joint==moment(n,t,{r:1,s:1})
            cov=joint-observed[r]*observed[s]
            if r+s<=n:
                if t<1: assert cov>0
                elif t==1: assert cov==0
                else: assert cov<0
                if t==2: assert cov==-Q(4,(n+1)**2)
            else: assert cov<0
            checks+=3
        # Three distinct positive-length groups: actual mixed factorial moment
        for lengths in combinations(range(1,n+1),3):
            if sum(lengths)>n:continue
            triple=sum((w*c[lengths[0]]*c[lengths[1]]*c[lengths[2]]
                        for (c,_),w in zip(summaries,weights)),Q(0))/den
            pred=moment(n,t,{lengths[0]:1,lengths[1]:1,lengths[2]:1})
            assert triple==pred
            prod=Q(1)
            for j in lengths:prod*=observed[j]
            if t<1:assert triple>prod
            elif t==1:assert triple==prod
            else:assert triple<prod
            checks+=2
        # Repeated falling-factorial checks, e.g. C_1(C_1-1)C_s
        for s in range(2,n-1):
            jnt=sum((w*falling(c[1],2)*c[s] for (c,_),w in zip(summaries,weights)),Q(0))/den
            assert jnt==moment(n,t,{1:2,s:1})
            checks+=1

# Exact factor identity for the rigidity witness, verified at many rational θ,
# n=4..13. The argument in the paper derives it algebraically for all real θ>0.
for n in range(4,14):
    for t in (Q(1,3),Q(1,2),Q(1),Q(5,4),Q(3,2),Q(2),Q(3),Q(7)):
        cov12=t*t/Q(2)*(f(n,t,3)-f(n,t,1)*f(n,t,2))
        cov13=t*t/Q(3)*(f(n,t,4)-f(n,t,1)*f(n,t,3))
        predicted=(-Q(n*(n-1))*t*t*(t-1)*(t-2)
                   /((t+n-4)*(t+n-3)*(t+n-2)*(t+n-1)**2))
        assert cov12-cov13==predicted
        checks+=1

print(f'PASS {checks} exact assertions; complete enumeration n=2,...,7 for five rational Ewens parameters.')
