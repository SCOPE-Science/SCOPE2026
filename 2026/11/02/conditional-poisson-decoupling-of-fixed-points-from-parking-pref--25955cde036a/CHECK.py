"""Independent exact small-size checks for preference fixed points and frequencies."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import factorial, comb

def poisson_fact_moment(c, r):
    e = [1] + [0]*r
    for x in c:
        for j in range(r,0,-1):
            e[j] += x*e[j-1]
    denom=1
    for j in range(r): denom*=len(c)-j
    return Fraction(factorial(r)*e[r], denom)

checks = 0
for n in range(2,7):
    aggregate = defaultdict(list)
    hist_pf = Counter()
    pf_count = 0
    for a in product(range(1,n+1), repeat=n):
        s=sorted(a)
        if any(x>i+1 for i,x in enumerate(s)): continue
        pf_count+=1
        c=tuple(a.count(i) for i in range(1,n+1))
        F=sum(a[i]==i+1 for i in range(n))
        aggregate[c].append(F)
        hist_pf[tuple(sorted(Counter(c+(0,)).items()))]+=1
    assert pf_count==(n+1)**(n-1)
    checks+=1
    for c, fs in aggregate.items():
        assert len(fs)==factorial(n)// __import__('math').prod(factorial(z) for z in c)
        for r in range(min(4,n)+1):
            ex=Fraction(sum(__import__('math').prod(range(f-r+1,f+1)) for f in fs),len(fs))
            assert ex==poisson_fact_moment(c,r), (n,c,r,ex)
            checks+=1
    hist_circle=Counter()
    for a in product(range(1,n+2), repeat=n):
        c=tuple(a.count(i) for i in range(1,n+2))
        key=tuple(sorted(Counter(c).items()))
        hist_circle[key]+=1
    assert {k:v*(n+1) for k,v in hist_pf.items()}==hist_circle
    checks+=1
    print(f'n={n}, functions={pf_count}, spectra={len(aggregate)}, checks={checks}')
print('ALL ASSERTIONS PASSED:', checks)
