#!/usr/bin/env python3
"""Independent prime-field test of Gauss-dual incidence for diagonal Sziklai-optimal curves."""
from itertools import product
from collections import Counter
for p in (5,7,11,13):
    coeff=(1,1,p-2)
    assert sum(coeff)%p==0
    def norm(t):
        v=next(x for x in t if x)
        return tuple(x*pow(v,-1,p)%p for x in t)
    P={norm(x) for x in product(range(p),repeat=3) if any(x)}
    C={x for x in P if sum(a*pow(b,p-1,p) for a,b in zip(coeff,x))%p==0}
    assert len(C)==(p-1)**2
    L={norm(tuple(a*(p-1)*pow(b,p-2,p)%p for a,b in zip(coeff,x))) for x in C}
    assert len(L)==(p-1)**2
    H=Counter(sum(sum(l[k]*x[k] for k in range(3))%p==0 for l in L) for x in P)
    assert H=={0:3,p-2:(p-1)**2,p-1:3*(p-1)},(p,H)
    print(f'q={p}: points={(p-1)**2}, tangents={(p-1)**2}, incidence={dict(sorted(H.items()))}, missing=3')
print('ALL_PRIME_TESTS_PASS')
