"""Exact finite certificate for the least odd squarefree 2-near-perfect integer.
Requires Python 3 and no external dependencies.
"""
from fractions import Fraction
from itertools import combinations
from math import isqrt, prod

BOUND = 39585

def primes_upto(n):
    return [k for k in range(3, n+1, 2) if all(k % d for d in range(3, isqrt(k)+1, 2))]

def proper_divisors_from_primes(primes):
    ds = [1]
    for p in primes:
        ds += [p*d for d in ds]
    ds.remove(prod(primes))
    return sorted(ds)

def witnesses(primes):
    n = prod(primes)
    d = prod(p+1 for p in primes) - 2*n
    if d <= 0:
        return d, []
    ds = proper_divisors_from_primes(primes)
    S = set(ds)
    return d, [(x, d-x) for x in ds if x < d-x and d-x in S]

def ratio(primes):
    return prod((Fraction(p+1,p) for p in primes), start=Fraction(1,1))

# The first five prime factors are at least 3,5,7,11,13. The first six
# distinct odd primes have product 255255 > BOUND, excluding support >=6.
assert 3*5*7*11*13*17 > BOUND
assert ratio((3,5,7,11)) < 2
assert ratio((5,7,11,13,17)) < 2
assert ratio((3,7,11,13,17)) < 2
assert ratio((3,5,11,13,17)) < 2
assert ratio((3,5,7,23,29)) < 2

expected = [(15015, 2226), (19635, 2202), (21945, 2190),
            (23205, 1974), (25935, 1890), (26565, 2166),
            (31395, 1722), (33495, 2130), (33915, 1290),
            (35805, 2118), (36465, -354), (39585, 1470)]
rows = []
for ps in combinations(primes_upto(53), 5):
    n = prod(ps)
    if n > BOUND:
        continue
    d, pairs = witnesses(ps)
    rows.append((n, d, ps, pairs))
rows.sort()
assert [(n,d) for n,d,ps,pairs in rows] == expected, rows
assert all(not pairs for n,d,ps,pairs in rows if n < BOUND)
assert rows[-1][2] == (3,5,7,13,29)
assert rows[-1][3] == [(105,1365),(455,1015)]
assert prod(p+1 for p in (3,5,7,13,29)) == 80640
assert 2*BOUND + 105+1365 == 80640

# Independent full bounded scan via trial-factorization, avoiding a prime-list
# representation of candidate five-tuples.
def factors_squarefree(n):
    result = []
    r = n
    for p in range(3, isqrt(r)+2, 2):
        if r%p == 0:
            r//=p
            if r%p == 0:
                return None
            result.append(p)
            while r%p == 0:
                return None
    if r>1: result.append(r)
    return result

seen = []
for n in range(3, BOUND+1, 2):
    ps=factors_squarefree(n)
    if ps and len(ps)==5:
        d,pairs=witnesses(ps)
        seen.append((n,d))
        if n<BOUND: assert not pairs, (n,pairs)
assert seen==expected, seen
print('VERIFY_OK odd_squarefree_five_support=' + str(len(rows)) +
      ' independent_scan=' + str(len(seen)) +
      ' first=' + str(BOUND) + ' sigma=80640 omitted_pairs=2')
