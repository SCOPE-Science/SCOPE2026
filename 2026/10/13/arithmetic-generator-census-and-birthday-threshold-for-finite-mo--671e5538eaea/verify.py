"""Standalone checks for the finite monadic MV generator classification."""
from itertools import product
from math import gcd
from functools import reduce
from collections import Counter


def mobius(d):
    if d == 1: return 1
    p = 2
    signs = 1
    while p*p <= d:
        if d % p == 0:
            d //= p
            signs = -signs
            if d % p == 0: return 0
            while d % p == 0: d //= p
        p += 1
    if d > 1: signs = -signs
    return signs


def fall(a,n):
    z=1
    for j in range(n):z*=a-j
    return z


def formula(m,n,r):
    return sum(mobius(d)*fall((m//d+1)**r,n) for d in range(1,m+1) if m%d==0)


def criterion(m,n,vecs):
    signatures=list(zip(*vecs)) if vecs else [() for _ in range(n)]
    return len(set(signatures))==n and reduce(gcd, (v for z in vecs for v in z),m)==1


def mv_closure(m,n,vecs):
    z=(0,)*n
    o=(m,)*n
    S={z,o, *vecs}
    todo=list(S)
    while todo:
        a=todo.pop()
        new={tuple(m-x for x in a), (max(a),)*n, (min(a),)*n}
        for b in list(S):
            new.add(tuple(min(m,x+y) for x,y in zip(a,b)))
        for b in new-S:
            S.add(b)
            todo.append(b)
    return len(S)==(m+1)**n

exhausted=0
param=0
for m,n,r in [(1,1,0),(1,1,1),(1,2,1),(1,3,2),(1,4,2),
              (2,1,0),(2,1,1),(2,2,1),(2,2,2),(2,3,1),(2,3,2),
              (3,1,0),(3,1,1),(3,2,1),(3,2,2),(3,3,1),
              (4,1,1),(4,2,1),(4,2,2),
              (5,1,1),(5,2,1),(5,2,2),
              (6,1,1),(6,2,1),(6,2,2)]:
    yes=0
    for raw in product(range(m+1),repeat=n*r):
        vecs=[tuple(raw[j*n:(j+1)*n]) for j in range(r)]
        pred=criterion(m,n,vecs)
        obs=mv_closure(m,n,vecs)
        assert pred==obs,(m,n,r,vecs,pred,obs)
        yes+=int(pred)
        exhausted+=1
    assert yes==formula(m,n,r), (m,n,r,yes,formula(m,n,r))
    param+=1

# Additional independent combinatorial census without algebra closures.
counts=0
for m in range(1,7):
    for n in range(1,4):
        for r in range(0,3):
            if (m+1)**(n*r)>60000: continue
            obs=sum(criterion(m,n,[tuple(raw[j*n:(j+1)*n]) for j in range(r)]) for raw in product(range(m+1),repeat=n*r))
            assert obs == formula(m,n,r)
            counts+=1
print('VERIFY_OK direct_mv_generation_tuples',exhausted,'direct_parameter_cases',param,'independent_signature_censuses',counts)
print('samples',(formula(2,3,1),formula(2,3,2),formula(3,2,2),formula(4,2,2),formula(6,1,1)))

# A separate unary-term closure test for the exact integer-affine peak functions
# required by the interpolation proof (small truth chains only).
peaks=0
for m in range(1,5):
    k=m+1
    S={tuple(0 for _ in range(k)),tuple(m for _ in range(k)),tuple(range(k))}
    todo=list(S)
    goals={tuple(max(0,m-abs(x-a)*m) for x in range(k)) for a in range(k)}
    # The intended peaked functions have height m at their own grid value.
    assert goals == {tuple(m if x==a else 0 for x in range(k)) for a in range(k)}
    while todo and not goals.issubset(S):
        a=todo.pop()
        new={tuple(m-x for x in a)}
        new.update(tuple(min(m,x+y) for x,y in zip(a,b)) for b in S)
        for b in new-S:
            S.add(b);todo.append(b)
    assert goals.issubset(S),(m,len(S),len(goals-S))
    peaks+=len(goals)

from math import exp,log,sqrt
asymp=[]
for r in (8,10,12):
    N=3**r
    n=round(sqrt(N))
    p_distinct=exp(sum(log(1-j/N) for j in range(n)))
    # for m=2, count of nonprimitive distinct samples is <= (2^r)_n/3^(rn)
    p_nonprimitive=0.0 if n>2**r else exp(sum(log(1-j/(2**r)) for j in range(n))+n*log((2/3)**r))
    assert 0<=p_nonprimitive<=((2/3)**(n*r))*(1+1e-10)
    asymp.append((r,n,round(p_distinct-p_nonprimitive,5)))
print('PEAK_TERMS_OK',peaks,'BIRTHDAY_SAMPLES',asymp,'limit',round(exp(-0.5),5))
