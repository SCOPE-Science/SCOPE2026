"""Exact rational checks for site-clock transport on a periodic lattice.

Run: python3 verify.py
Only the Python standard library is required.
The finite tests corroborate, but do not replace, the all-size proof.
"""
from fractions import Fraction as F
from itertools import combinations


def gaussian(a, b):
    n = len(a)
    a = [list(x) + [y] for x, y in zip(a, b)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        z = a[j][j]
        a[j] = [x / z for x in a[j]]
        for i in range(n):
            if i != j:
                z = a[i][j]
                a[i] = [a[i][k] - z * a[j][k] for k in range(n + 1)]
    return [row[-1] for row in a]


def word(n, m):
    return frozenset(i for i in range(n)
                     if (i + 1) * m // n > i * m // n)


def rates(n, occupied, r0=F(1), epsilon=F(1)):
    return [r0 + (epsilon if j in occupied else 0) for j in range(n)]


def direct_cumulants(r, p):
    n = len(r)
    q = 1 - p
    R = sum(r)
    delta = p - q
    drift = F(n) * delta / R
    mat = [[F(0) for _ in range(n)] for _ in range(n)]
    rhs = [F(0) for _ in range(n)]
    mat[0][0] = F(1)
    for i in range(1, n):
        c = 1 / r[i]
        mat[i][i] -= c
        mat[i][(i + 1) % n] += p * c
        mat[i][(i - 1) % n] += q * c
        rhs[i] = drift - delta * c
    h = gaussian(mat, rhs)
    for i in range(n):
        c = 1 / r[i]
        lhs = c * (p * (h[(i + 1) % n] - h[i]) +
                   q * (h[(i - 1) % n] - h[i]))
        assert lhs == drift - delta * c
    kappa2 = sum(p * (1 + h[(i + 1) % n] - h[i]) ** 2 +
                 q * (-1 + h[(i - 1) % n] - h[i]) ** 2
                 for i in range(n)) / R
    return drift, kappa2


def kernel_cumulant(n, occupied, p, r0=F(1), epsilon=F(1)):
    q = 1 - p
    delta = p - q
    m = len(occupied)
    R = n * r0 + m * epsilon
    if delta == 0:
        return F(n, 1) / R
    if q == 0:
        return F(n*n, 1) * sum(x*x for x in rates(n, occupied, r0, epsilon)) / R**3
    t = q / p
    k = lambda d: (t**d + t**(n-d)) / (delta * (1-t**n))
    a = sum(k((i-j) % n) for i in occupied for j in occupied)
    return F(n, 1)/R + n*n * delta*delta * epsilon*epsilon / R**3 * (a - F(m*m, n*delta*delta))


def rotations(s, n):
    return {frozenset((x + j) % n for x in s) for j in range(n)}


def check():
    direct_cases = 0
    exact_maxima = 0
    endpoint_cases = 0
    for n in range(4, 11):
        for m in range(2, n-1):
            all_sites = [frozenset(s) for s in combinations(range(n), m)]
            balanced = rotations(word(n, m), n)
            clustered = rotations(frozenset(range(m)), n)
            for p in (F(3, 4), F(2, 3)):
                values = {s: kernel_cumulant(n, s, p) for s in all_sites}
                lo, hi = min(values.values()), max(values.values())
                assert {s for s, v in values.items() if v == lo} == balanced
                assert {s for s, v in values.items() if v == hi} == clustered
                assert lo < hi
                exact_maxima += 1
            for p in (F(1, 2), F(1)):
                assert len({kernel_cumulant(n, s, p) for s in all_sites}) == 1
                endpoint_cases += 1
            # Independent direct Markov-generator + Poisson-equation calculation.
            for p in (F(3, 4), F(2, 3), F(1, 2), F(1)):
                for s in (all_sites[0], all_sites[len(all_sites)//2], all_sites[-1]):
                    r = rates(n, s)
                    v, k2 = direct_cumulants(r, p)
                    assert v == n*(2*p-1) / sum(r)
                    assert k2 == kernel_cumulant(n, s, p)
                    direct_cases += 1
    for n in (6, 8, 10):
        s = frozenset((0, n//2))
        a, b = direct_cumulants(rates(n, s), F(3, 4))
        assert a == n*F(1, 2)/(n+2)
        assert b == kernel_cumulant(n, s, F(3, 4))
    print(f'PASS: {direct_cases} independent generator/Poisson comparisons; '
          f'{exact_maxima} complete pairwise extrema enumerations; '
          f'{endpoint_cases} zero-bias/one-way ordering-invariance comparisons.')

if __name__ == '__main__':
    check()
