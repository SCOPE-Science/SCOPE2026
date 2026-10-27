#!/usr/bin/env python3
"""Exact independent finite checks for periodic length-two secondary-structure avoidance.

No third-party packages. Symbols 0,1,2,3, with Watson-Crick involution a -> 3-a.
Run: python3 verify_periodic_ssa2.py
"""
from itertools import permutations, product
from collections import Counter
from math import gcd


def rc(edge):
    a, b = edge
    return 3-b, 3-a


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x * y
    while len(c) > 1 and not c[-1]:
        c.pop()
    return tuple(c)


def power(a, k):
    result = (1,)
    while k:
        if k & 1:
            result = mul(result, a)
        a = mul(a, a)
        k >>= 1
    return result


def characteristic(A):
    # Determinant of I-zA, evaluated by the signed-permutation formula.
    accum = [0] * 5
    for perm in permutations(range(4)):
        inversions = sum(perm[i] > perm[j] for i in range(4) for j in range(i+1, 4))
        term = (1,)
        for i, j in enumerate(perm):
            term = mul(term, ((1 if i == j else 0), -A[i][j]))
        for k, v in enumerate(term):
            accum[k] += (-1 if inversions & 1 else 1) * v
    while len(accum) > 1 and not accum[-1]:
        accum.pop()
    assert accum[0] == 1
    return tuple(accum)


def trace_from_det(det, n):
    # Newton's identities: det(I-z A) * sum tr(A^k)z^k = -z det'(I-zA)
    t = [0] * (n+1)
    for i in range(1, n+1):
        t[i] = (-i * det[i] if i < len(det) else 0) - sum(
            det[j] * t[i-j] for j in range(1, min(i-1, len(det)-1)+1)
        )
    return t


pairs = []
for edge in product(range(4), repeat=2):
    if edge == rc(edge) or any(edge in pair for pair in pairs):
        continue
    pairs.append((edge, rc(edge)))
assert pairs == [((0,0),(3,3)), ((0,1),(2,3)), ((0,2),(1,3)),
                 ((1,0),(3,2)), ((1,1),(2,2)), ((2,0),(3,1))]
assert [e for e in product(range(4), repeat=2) if e == rc(e)] == [
    (0,3),(1,2),(2,1),(3,0)]

weights = Counter()
for choice in product((0,1,2), repeat=6):
    A = [[0]*4 for _ in range(4)]
    for selection, (e, f) in zip(choice, pairs):
        if selection == 0:  # delete e, leave f
            A[f[0]][f[1]] = 1
        elif selection == 1:  # delete f, leave e
            A[e[0]][e[1]] = 1
        # Selection 2 deletes both and has inclusion-exclusion sign -1.
    weights[characteristic(A)] += -1 if choice.count(2) & 1 else 1
assert sum(weights.values()) == 1
weights = {k:v for k,v in weights.items() if v}
assert len(weights) == 18

# Constant-first polynomials; the signed exponents multiply determinant factors.
root_factors = {
    (1,-2,-1,1):8,
    (1,-2):-8,
    (1,-1):-6,
    (1,-1,-1):8,
    (1,1):-2,
    (1,-1,1):8,
    (1,-1,0,0,-1):-8,
    (1,0,1):2,
}
# Check product(det^weight) = product(factor^exponent)
# after bringing denominators to the opposite side. Entirely integer exact.
left = (1,)
right = (1,)
for polynomial, e in weights.items():
    if e > 0:
        left = mul(left, power(polynomial, e))
    else:
        right = mul(right, power(polynomial, -e))
for polynomial, e in root_factors.items():
    if e < 0:
        left = mul(left, power(polynomial, -e))
    else:
        right = mul(right, power(polynomial, e))
assert left == right, 'Factorization of signed characteristic-polynomial product failed'

maxn = 45
from_weighted = [0]*(maxn+1)
for pol, weight in weights.items():
    seq = trace_from_det(pol,maxn)
    for n in range(1,maxn+1):
        from_weighted[n] += weight*seq[n]
from_factors = [0]*(maxn+1)
for pol, weight in root_factors.items():
    seq = trace_from_det(pol,maxn)
    for n in range(1,maxn+1):
        from_factors[n] += weight*seq[n]
assert from_weighted == from_factors

initial = [4,12,28,84,244,612,1460,3412,8020,18812,43916,101964,
           235876,543996,1251148,2870100,6568668,15002316]
assert from_factors[1:19] == initial


def direct(word):
    pairs_used = {(word[i],word[(i+1)%len(word)]) for i in range(len(word))}
    return all(rc(edge) not in pairs_used for edge in pairs_used)

for n in range(1,11):
    total = sum(direct(w) for w in product(range(4), repeat=n))
    assert total == from_factors[n], (n,total,from_factors[n])

# Repeated periodic words have the same avoidance property as the primitive period.
# Burnside: fixed words under rotation by j are words with period gcd(n,j).
def totient(d):
    return sum(gcd(d,k)==1 for k in range(1,d+1))
for n in range(1,25):
    v = sum(totient(d)*from_factors[n//d] for d in range(1,n+1) if n%d==0)
    assert v % n == 0

print('PERIODIC_DNA_SSA2_PASS choices=729 nonzero_det_groups=18 '
      'polynomial_identity=exact trace_n=1..45 direct_n=1..10 necklaces_n=1..24')
print('INITIAL_COUNTS=' + ','.join(map(str,initial)))
print('WEIGHTED_DETERMINANTS=' + repr(sorted(weights.items())))
