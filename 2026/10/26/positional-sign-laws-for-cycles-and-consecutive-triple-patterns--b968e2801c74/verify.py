"""Exact independent checks for conditional cycles and consecutive triples.
Run: python3 verify.py
"""
from fractions import Fraction as F
from itertools import permutations, combinations
from math import comb
import random

PATTERNS = tuple(permutations((1, 2, 3)))

def cycles(p):
    n = len(p)
    seen = set()
    c = 0
    for i in range(n):
        if i not in seen:
            c += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = p[j] - 1
    return c

def pattern(a):
    return tuple(sorted(a).index(v) + 1 for v in a)

def tau(n, a, pat):
    return {
        (1,2,3):3*n-2,
        (1,3,2):-12*a+9*n-14,
        (2,1,3):12*a-3*n-2,
        (2,3,1):12*a-9*n+10,
        (3,1,2):-12*a+3*n-2,
        (3,2,1):-3*n+10,
    }[pat]

def fcycle(n):
    return sum((F(1,k) for k in range(1,n+1)), F())

def fixed_cycle_count(f):
    c=0; seen=set()
    for start in f:
        if start in seen:continue
        cur=start; path=set()
        while cur in f and cur not in seen and cur not in path:
            path.add(cur);cur=f[cur]
        if cur in path:c+=1
        seen.update(path)
    return c

checks = 0
for n in range(3,9):
    sums = {(a,p):0 for a in range(1,n-1) for p in PATTERNS}
    counts = {(a,p):0 for a in range(1,n-1) for p in PATTERNS}
    E = F()
    N = 0
    for p in permutations(range(1,n+1)):
        c=cycles(p)
        E+=c;N+=1
        for a in range(1,n-1):
            pat=pattern(p[a-1:a+2]);sums[a,pat]+=c;counts[a,pat]+=1
    assert E/N == fcycle(n);checks+=1
    for a in range(1,n-1):
        for pat in PATTERNS:
            assert counts[a,pat]*6==N
            checks+=1
            pred=F(tau(n,a,pat),6*comb(n,3))
            got=F(sums[a,pat],counts[a,pat])-E/N
            assert got==pred,(n,a,pat,got,pred)
            checks+=1
            cov=(F(sums[a,pat],N)-E/N*F(1,6))
            assert cov==F(tau(n,a,pat),36*comb(n,3))
            checks+=1
    for pat in PATTERNS:
        global_cov=sum((F(sums[a,pat],N)-E/N*F(1,6) for a in range(1,n-1)),F())
        global_predict=sum((F(tau(n,a,pat),36*comb(n,3)) for a in range(1,n-1)),F())
        assert global_cov==global_predict
        checks+=1

# Independent finite test of the contraction lemma for assorted partial injections.
rng=random.Random(119827)
for n in range(2,8):
    trials=80
    for _ in range(trials):
        r=rng.randrange(n+1)
        dom=rng.sample(range(1,n+1),r)
        cod=rng.sample(range(1,n+1),r)
        f=dict(zip(dom,cod))
        domain_rest=[i for i in range(1,n+1) if i not in f]
        codomain_rest=[i for i in range(1,n+1) if i not in f.values()]
        mean=F()
        num=0
        for vals in permutations(codomain_rest):
            d=dict(f);d.update(zip(domain_rest,vals))
            p=tuple(d[i] for i in range(1,n+1))
            mean+=cycles(p);num+=1
        mean/=num
        assert mean==fixed_cycle_count(f)+fcycle(n-r),(n,f,mean)
        checks+=1

print(f'PASS: {checks} exact checks, including complete enumeration up to n=8 and sampled partial-injection completions through n=7')
