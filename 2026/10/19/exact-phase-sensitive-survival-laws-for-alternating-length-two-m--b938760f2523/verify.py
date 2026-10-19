"""Exact finite-horizon checks for alternating length-two Markov holes.

Requires only Python 3. The proof of the all-alphabet theorem is in RESULT.md;
finite exhaustive checks here do not replace that proof.
"""

from itertools import product
from math import sqrt


def matmul(a, b):
    k = len(a)
    return [[sum(a[i][v] * b[v][j] for v in range(k))
             for j in range(k)] for i in range(k)]


def paths(k, p, q, r, s, steps):
    a = [[int((i, j) != (p, q)) for j in range(k)] for i in range(k)]
    b = [[int((i, j) != (r, s)) for j in range(k)] for i in range(k)]
    m = matmul(a, b)
    v = [1] * k
    out = []
    for _ in range(steps + 1):
        out.append(sum(v))
        v = [sum(v[i] * m[i][j] for i in range(k)) for j in range(k)]
    return out


def recursion(k, d, e, steps):
    t = k * k - 2 + d * e
    delta = (k * d - 1) * (k * e - 1)
    out = [k, k**3 - 2*k + d]
    for m in range(2, steps + 1):
        out.append(t*out[-1] - delta*out[-2])
    return out[:steps + 1]


def brute(k, p, q, r, s, m):
    total = 0
    for digits in product(range(k), repeat=2*m+1):
        if all((digits[j], digits[j+1]) !=
               ((p, q) if j % 2 == 0 else (r, s))
               for j in range(2*m)):
            total += 1
    return total


for k in range(2, 7):
    representatives = {}
    for p, q, r, s in product(range(k), repeat=4):
        d, e = int(q == r), int(p == s)
        representatives.setdefault((d, e), (p, q, r, s))
        assert paths(k, p, q, r, s, 6) == recursion(k, d, e, 6)
    assert set(representatives) == {(0, 0), (0, 1), (1, 0), (1, 1)}
    table = {de: recursion(k, *de, 6) for de in representatives}
    for m in range(2, 7):
        assert table[0, 0][m] < table[0, 1][m]
        assert table[0, 1][m] < table[1, 0][m]
        assert table[1, 0][m] < table[1, 1][m]
    assert table[0, 0][1] == table[0, 1][1]
    assert table[1, 0][1] == table[1, 1][1]
    for de, args in representatives.items():
        for m in range(3 if k <= 3 else 2):
            assert brute(k, *args, m) == recursion(k, *de, m)[m]
    u = k*k-2
    eig0 = (u + sqrt(u*u-4))/2
    eigm = (u + sqrt(u*u+4*(k-1)))/2
    eig1 = (u+1 + sqrt((u+1)**2-4*(k-1)**2))/2
    assert eig0 < eigm < eig1

# Exhaustive independent word enumeration of all 16 binary configurations.
for p, q, r, s in product(range(2), repeat=4):
    de = (int(q == r), int(p == s))
    for m in range(5):
        assert brute(2, p, q, r, s, m) == recursion(2, *de, m)[m]
    if de == (0, 0):
        assert recursion(2, *de, 10) == [2*(m+1) for m in range(11)]

# Starting-phase asymmetry has the exact universal recurrence u_m.
for k in range(2, 10):
    a = recursion(k, 1, 0, 12)
    b = recursion(k, 0, 1, 12)
    diffs = [x-y for x, y in zip(a,b)]
    u = k*k-2
    pred = [0,1]
    for _ in range(2,13):
        pred.append(u*pred[-1]+(k-1)*pred[-2])
    assert diffs == pred

print('VERIFY_OK')
