"""Finite checks for the endpoint-height theorem in the ordered critical beta-splitting tree.

This verifies exact finite identities and numerical recurrences, not the asymptotic CLT.
Only the Python standard library is needed.
"""
from fractions import Fraction
from functools import lru_cache
from collections import defaultdict
from math import log, factorial

checks = 0

def check(statement, message):
    global checks
    checks += 1
    if not statement:
        raise AssertionError(message)

@lru_cache(None)
def harmonic(n):
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction(0))

def transition(m, i):
    assert 1 <= i < m
    return (Fraction(1, i) + Fraction(1, m-i)) / (2*harmonic(m-1))

@lru_cache(None)
def shape_law(m):
    if m == 1:
        return {(None,): Fraction(1)}
    out = {}
    for i in range(1, m):
        p = transition(m, i)
        for l, lp in shape_law(i).items():
            for r, rp in shape_law(m-i).items():
                out[(l, r)] = p*lp*rp
    return out

def boundary_height(tree):
    depth = 0
    while tree != (None,):
        depth += 1
        tree = tree[0]
    return depth

@lru_cache(None)
def height_law(m):
    if m == 1:
        return {0: Fraction(1)}
    out = defaultdict(Fraction)
    for i in range(1, m):
        for height, p in height_law(i).items():
            out[height+1] += transition(m, i)*p
    return dict(out)

for n in range(2, 9):
    check(sum((transition(n, i) for i in range(1,n)), Fraction(0)) == 1,
          f'non-normalized transition n={n}')
    weights = shape_law(n)
    check(sum(weights.values(), Fraction(0)) == 1, f'shape total n={n}')
    exact = defaultdict(Fraction)
    for tree, p in weights.items():
        exact[boundary_height(tree)] += p
    for height in range(1, n):
        check(exact[height] == height_law(n).get(height, Fraction(0)),
              f'tree enumeration and path law differ for n={n}, height={height}')
    check(sum(height_law(n).values(), Fraction(0)) == 1, f'height total n={n}')

# The simple mixture representation is checked with exact arithmetic.
for m in range(2, 26):
    h = harmonic(m-1)
    for i in range(1,m):
        mixture = (Fraction(1,i)/h + Fraction(1,m-i)/h)/2
        check(mixture == transition(m,i), f'mixture m={m},i={i}')

# Independent exact moment calculation using the distribution and a recurrence.
for m in range(2,9):
    law = height_law(m)
    mean = sum((Fraction(h)*p for h,p in law.items()), Fraction(0))
    second = sum((Fraction(h*h)*p for h,p in law.items()), Fraction(0))
    prev_mean = sum((transition(m,i)*sum((Fraction(h)*p for h,p in height_law(i).items()), Fraction(0)) for i in range(1,m)), Fraction(0))
    prev_second = sum((transition(m,i)*sum((Fraction(h*h)*p for h,p in height_law(i).items()), Fraction(0)) for i in range(1,m)), Fraction(0))
    check(mean == 1+prev_mean, f'mean recurrence m={m}')
    check(second == 1+2*prev_mean+prev_second, f'second recurrence m={m}')

# Check numeric one-step moments against their proved limiting constants.
for m in [1000,10000,30000]:
    h = sum(1.0/k for k in range(1,m))
    y = log(h)
    raw = [0.0]*4
    for j in range(1,m):
        ell_j = 0.0 if j<3 else log(sum(1.0/k for k in range(1,j))) if j < 10 else None
        # Use precomputed harmonics for the numerical test below.
        break
    hs = [0.0]*(m+1)
    for j in range(1,m+1):
        hs[j] = hs[j-1]+1.0/j
    for j in range(1,m):
        d = y-(log(hs[j-1]) if j>=3 else 0.0)
        w = (1.0/j+1.0/(m-j))/(2*h)
        p = d
        for r in range(4):
            raw[r] += w*p
            p *= d
    for r, v in enumerate(raw,1):
        bound = 10*(1+y**r)/h
        check(abs(v-factorial(r)/2) <= bound, f'finite moment bound n={m},order={r}: {v}')
    print('step_moments',m, 'y',round(y,5),'raw',*[round(v,5) for v in raw])

# Compute exact-from-kernel finite moments with a separate floating recurrence.
import array
N=2000
H=array.array('d',[0.0])*(N+1)
for j in range(1,N+1):H[j]=H[j-1]+1.0/j
A=array.array('d',[0.0])*(N+1)
S=array.array('d',[0.0])*(N+1)
for m in range(2,N+1):
    ma=sa=0.0
    for i in range(1,m):
        w=(1.0/i+1.0/(m-i))/(2.0*H[m-1])
        ma += w*A[i]
        sa += w*S[i]
    A[m]=1.0+ma
    S[m]=1.0+2*ma+sa
for m in [20,100,500,2000]:
    y=log(H[m-1])
    v=S[m]-A[m]**2
    check(v>0, f'nonpositive variance n={m}')
    check(A[m]>2*y, f'unexpected finite mean n={m}')
    print('path_moments',m,'mean',round(A[m],6),'variance',round(v,6),
          'center',round(2*y,6),'asymptotic_variance',round(6*y,6))
print('PASS',checks,'assertions')
