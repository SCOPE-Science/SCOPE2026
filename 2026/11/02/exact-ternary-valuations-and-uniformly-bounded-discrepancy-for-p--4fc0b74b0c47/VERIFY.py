#!/usr/bin/env python3
"""Exact-arithmetic finite checks for a 3-adic valuation theorem on Perrin numbers.
The infinite proof is algebraic and independent of these finite tests.
"""
from fractions import Fraction

def matmul(a, b, modulus=None):
    c = tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)) for i in range(3))
    return c if modulus is None else tuple(tuple(x % modulus for x in row) for row in c)

def matpow(a, k, modulus=None):
    result = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    while k:
        if k & 1:
            result = matmul(result, a, modulus)
        a = matmul(a, a, modulus)
        k >>= 1
    return result

def trace(a):
    return sum(a[i][i] for i in range(3))

def order3(a):
    if a == 0:
        return 10**9
    j = 0
    while a % 3 == 0:
        a //= 3
        j += 1
    return j

M = ((0, 0, 1), (1, 0, 1), (0, 1, 0))
B = matpow(M, 13)
assert B == ((7, 9, 12), (12, 16, 21), (9, 12, 16))
A = tuple(tuple((B[i][j] - int(i == j)) // 3 for j in range(3)) for i in range(3))
assert A == ((2, 3, 4), (4, 5, 7), (3, 4, 5))
base = [trace(matpow(M, r)) for r in range(13)]
assert base == [3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17, 22, 29]
slopes = {r: trace(matmul(matpow(M, r), A)) for r in (1, 3, 9)}
assert slopes == {1: 17, 3: 29, 9: 158}

# Lift the unique root in each of the three isometric congruence classes.
depth = 15
roots = {}
for r in (1, 3, 9):
    m = 0
    for j in range(1, depth + 1):
        modulus = 3 ** (j + 1)
        choices = [m + digit * 3**(j-1) for digit in range(3)]
        matches = [x for x in choices if trace(matpow(M, 13*x+r, modulus)) % modulus == 0]
        assert len(matches) == 1, (r, j, matches)
        m = matches[0]
    roots[r] = m
assert roots[1] == 0
assert roots[3] % 6561 == 4477
assert roots[9] % 6561 == 2107

LIMIT = 120000
modulus = 3**17
seq = [3, 0, 2]
for n in range(3, LIMIT):
    seq.append((seq[n-2] + seq[n-3]) % modulus)
counts = [0] * 17
for n in range(2, LIMIT):
    r = n % 13
    m = n // 13
    if r not in (0, 1, 3, 9):
        expected = 0
    elif r == 0:
        expected = 1
    else:
        expected = 1 + order3(m-roots[r])
    actual = order3(seq[n])
    assert expected == actual, (n, expected, actual)
    assert actual < len(counts)
    counts[actual] += 1
    # Check a uniform discrepancy bound for every initial cutoff N=n+1.
    N = n+1
    for t in range(12):
        p = Fraction(9,13) if t == 0 else (Fraction(3,13) if t == 1 else Fraction(6,13*3**t))
        assert abs(Fraction(counts[t])-p*N) <= 9, (N,t,counts[t],p)
print('VERIFY_OK', 'matrix=13', 'slopes=3', 'hensel_roots=3', 'lift_depth=15', 'recurrence_indices='+str(LIMIT-2), 'discrepancy_cutoffs='+str(LIMIT-2), 'root_mod_6561='+str((roots[3]%6561,roots[9]%6561)))
