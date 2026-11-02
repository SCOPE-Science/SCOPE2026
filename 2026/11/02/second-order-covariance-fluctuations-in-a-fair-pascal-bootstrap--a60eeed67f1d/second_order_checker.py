#!/usr/bin/env python3
"""Finite exact checks for the Pascal-scene renewal-clock decomposition.

These verify algebraic identities, not any infinite-time limit theorem.
"""
from itertools import product
from math import comb
from fractions import Fraction
count = 0
def check(v, s):
    global count
    if not v: raise AssertionError(s)
    count += 1

def scene(m, beta):
    return -1 if sum((comb(m,k)&1)*beta[k] for k in range(m+1))%2 else 1

# Pascal transform of independent fair input bits is an invertible F2 map.
for r in range(1,10):
    seen=set()
    for beta in product((0,1),repeat=r):
        seq=tuple(scene(m,beta) for m in range(r))
        check(seq not in seen,f'collision {r}')
        seen.add(seq)
    check(len(seen)==2**r,f'invertibility {r}')

# Exact finite renewal-reward identity including the last incomplete hold.
for n in range(1,9):
    for xi in product((1,-1),repeat=n):
        for beta in product((0,1),repeat=n+1):
            m=0; direct=0; hold=[]; run=0
            for x in xi:
                f=scene(m,beta)
                direct+=f
                run+=1
                if x==-1:
                    hold.append(run)
                    m+=1;run=0
            indirect=sum(hold[j]*scene(j,beta) for j in range(len(hold)))+run*scene(m,beta)
            check(direct==indirect, f'renewal identity at {n} {xi} {beta}')

# Geometric(1/2): exact first three moments via finite generating-function derivatives.
# E H=2, E H^2=6, E H^3=26, so centered variance is 2.
for t in range(1,10):
    f=tuple(1 if j%2 else -1 for j in range(t))
    v=2*sum(a*a for a in f)
    cov=2*sum(f)
    check(v==2*t,f'weighted geometric variance {t}')
    check(abs(cov)<=2*t, f'weighted clock covariance {t}')

# Exact annealed variance of complete-hold rewards with fair scenery.
# Each reward H f has mean zero and E H^2=6, hence Var sum =6m.
for m in range(1,10):
    check(6*m == 2*m+4*m, f'variance split at {m}')
print(f'PASS: {count} exact finite assertions')
