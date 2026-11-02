#!/usr/bin/env python3
"""Exact finite tests for the semi-Pell mod-eight distribution theorem.

This uses only the Python standard library. Finite tests complement the
symbolic recurrence and transfer-matrix proof in RESULT.md.
"""
from collections import Counter

LIMIT = 1 << 16
f = [0] * LIMIT
f[1] = 1
for n in range(2, LIMIT):
    f[n] = f[n // 2] if n % 2 == 0 else 2 * f[n - 1] + f[n - 2]


def q_bit(m):
    bits = [(m >> j) & 1 for j in range(max(2, m.bit_length() + 1))]
    return (sum(bits[1:]) + sum(a*b for a,b in zip(bits, bits[1:]))) & 1


def predicted_odd(m):
    return (1 + 2*(m&1) + 4*q_bit(m)) % 8


assert all(f[n] & 1 for n in range(1, LIMIT))
for m in range(LIMIT // 2):
    assert f[2*m + 1] % 8 == predicted_odd(m), (m, f[2*m+1])
for n in range(1, LIMIT):
    t = n
    while t % 2 == 0:
        t //= 2
    assert f[n] % 8 == f[t] % 8

T = ((1, 1), (-1, 1))
def mul(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in (0, 1))
                       for j in (0, 1)) for i in (0, 1))
I = ((1,0),(0,1))
T4 = mul(mul(T, T), mul(T, T))
assert T4 == ((-4,0),(0,-4))

def step(v):
    return (v[0] + v[1], -v[0] + v[1])

E = [1,1]
O = [0,1]
e, o = (1,-1), (1,1)
for k in range(2,16):
    E.append(sum(e))
    O.append(sum(o))
    mres = [predicted_odd(m) for m in range(1 << k)]
    assert E[k] == mres.count(1) - mres.count(5)
    assert O[k] == mres.count(3) - mres.count(7)
    if k >= 6:
        assert E[k] == -4*E[k-4] and O[k] == -4*O[k-4]
    e, o = step(e), step(o)

for r in range(1,17):
    counts = Counter(f[n] % 8 for n in range(1,1<<r))
    se, so = sum(E[:r]), sum(O[:r])
    predicted = {
        1: (2**(r-1) + se)//2,
        5: (2**(r-1) - se)//2,
        3: (2**(r-1)-1 + so)//2,
        7: (2**(r-1)-1 - so)//2,
    }
    assert sum(predicted.values()) == (1<<r)-1
    assert all(counts[j]==predicted[j] for j in (1,3,5,7)), (r,counts,predicted)
    if (r-1) % 4 == 0:
        a = (r-1)//4
        assert se == (-4)**a and so == 1-(-4)**a

# Check the rational coefficient formulas by exact polynomial arithmetic.
def coefficients_of_rational(numer, denom, maxdegree):
    result = []
    for i in range(maxdegree):
        s = numer.get(i, 0)
        for j, c in denom.items():
            if 0 < j <= i:
                s -= c*result[i-j]
        result.append(s)
    return result
assert E == coefficients_of_rational({0:1,1:1,3:-2},{0:1,4:4},16)
assert O == coefficients_of_rational({1:1,2:2,3:2},{0:1,4:4},16)

print('VERIFY_OK: recurrence, 32768 odd-index formulae, 65535 odd-part reductions,')
print('16 exact dyadic distributions, transfer identity, rational generating series.')
