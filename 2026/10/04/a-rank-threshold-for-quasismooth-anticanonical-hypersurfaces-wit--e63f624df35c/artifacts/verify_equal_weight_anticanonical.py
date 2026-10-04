from itertools import combinations
from math import gcd

def semigroup_reachable(weights, target):
    if target < 0: return False
    if target == 0: return True
    reach=[False]*(target+1); reach[0]=True
    for t in range(target+1):
        if not reach[t]: continue
        for w in weights:
            if t+w<=target: reach[t+w]=True
    return reach[target]

def fletcher_qs(r,m,a):
    weights=[1]*r+[a]*m
    d=sum(weights)
    n=len(weights)
    # Fletcher 1.5.1, non-linear-cone case. Here d>all weights for r,m>=2.
    for k in range(1,n+1):
        for I in combinations(range(n),k):
            I=set(I)
            wi=[weights[i] for i in I]
            if semigroup_reachable(wi,d):
                continue
            good=[]
            for e in range(n):
                if e in I: continue
                if semigroup_reachable(wi,d-weights[e]):
                    good.append(e)
            if len(good)<k:
                return False
    return True

def predicted_qs(r,m,a):
    return (r%a==0) or (r>=m and (r-1)%a==0)

def age_canonical(r,a):
    # generic singular stratum type 1/a(1^r) x A^(m-1); m irrelevant
    if a==1: return True,True
    ages=[r*t/a for t in range(1,a)]
    return min(ages)>=1, min(ages)>1

def predicted_can_term(r,a):
    return a<=r, a<r

def tau(n):
    return sum(n%d==0 for d in range(1,n+1))

def count_formula(r,m):
    can=tau(r)+(tau(r-1)-1 if r>=m else 0)
    term=(tau(r)-1)+(tau(r-1)-1 if r>=m else 0)
    return can,term

# Full generic Fletcher subset replay on manageable boxes.
checked=0
for r in range(2,6):
    for m in range(2,6):
        for a in range(1,9):
            q=fletcher_qs(r,m,a)
            p=predicted_qs(r,m,a)
            assert q==p,(r,m,a,q,p)
            c,t=age_canonical(r,a)
            pc,pt=predicted_can_term(r,a)
            assert (c,t)==(pc,pt),(r,m,a,c,t,pc,pt)
            checked+=1

# Broader exact formula/count replay without exponential subset enumeration.
for r in range(2,101):
    for m in range(2,101):
        can=[]; term=[]
        for a in range(1,r+1):
            if predicted_qs(r,m,a):
                can.append(a)
                if a<r: term.append(a)
        assert (len(can),len(term))==count_formula(r,m),(r,m,len(can),len(term),count_formula(r,m))
        # canonical nonterminal quasismooth member is always uniquely a=r
        assert [a for a in can if a==r]==[r]

print('VERIFY_OK',checked,'generic Fletcher cases; counts through r,m<=100')
