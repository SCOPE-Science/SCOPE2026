#!/usr/bin/env python3
"""Reproduce exact one-step Rule-22 image counts under cyclic 00 avoidance.

No dependencies beyond the Python standard library. All checks use indexed rings.
"""
from collections import defaultdict

RULE = 22
T = (((1, 0), (0, 0)), ((0, 0), (0, 1)), ((0, 1), (1, 0)))


def rule22_on_ring(x, n):
    y = 0
    for i in range(n):
        a = (x >> ((i - 1) % n)) & 1
        b = (x >> i) & 1
        c = (x >> ((i + 1) % n)) & 1
        if a + b + c == 1:
            y |= 1 << i
    return y


def zero_gaps(y, n):
    zeros = [i for i in range(n) if not (y >> i) & 1]
    if not zeros:
        return []
    return [(zeros[(j + 1) % len(zeros)] - z - 1) % n
            for j, z in enumerate(zeros)]


def avoids_cyclic_00(y, n):
    return all(((y >> i) & 1) or ((y >> ((i + 1) % n)) & 1)
               for i in range(n))


def mat_product(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def predicted_fiber(y, n):
    if not avoids_cyclic_00(y, n):
        raise ValueError("Only cyclic-00-avoiding outputs are covered")
    gaps = zero_gaps(y, n)
    if not gaps:
        return 3 if n % 3 == 0 else 0
    assert all(a >= 1 for a in gaps)
    P = ((1, 0), (0, 1))
    for a in gaps:
        P = mat_product(P, T[a % 3])
    return P[0][0] + P[1][1]


def lucas_trib(nmax):
    t = [3, 1, 1]
    for n in range(3, nmax + 1):
        t.append(t[n - 1] + t[n - 3])
    return t


def exact_count(n, t):
    val = t[n] + (-1 if n % 2 else 1)
    if n % 3 == 0:
        val += 1 - 3 * (2 ** (n // 3 - 1))
    return val


def brute_check(nmax=17):
    t = lucas_trib(max(3, nmax))
    result = []
    for n in range(1, nmax + 1):
        fibers = defaultdict(int)
        for x in range(1 << n):
            fibers[rule22_on_ring(x, n)] += 1
        accepted = 0
        doubled = 0
        for y in range(1 << n):
            if not avoids_cyclic_00(y, n):
                continue
            expected = predicted_fiber(y, n)
            actual = fibers[y]
            if expected != actual:
                raise AssertionError((n, y, expected, actual))
            accepted += (actual > 0)
            doubled += (actual == 2)
        assert accepted == exact_count(n, t), (n, accepted, exact_count(n, t))
        result.append((n, accepted, doubled))
    return result


def check_rational_series(nmax=120):
    # Work entirely in Z[[z]] to test the independently derived rational OGF.
    # B(z)= z(1+3z^2)/(1-z-z^3) -z/(1+z)
    #       -2z^3/(1-z^3) - 3z^6/((1-z^3)(1-2z^3)).
    t = lucas_trib(nmax)
    coeff = [0] * (nmax + 1)
    u = [0] * (nmax + 1)
    for n in range(nmax + 1):
        if n == 0:
            u[n] = 1
        else:
            u[n] = u[n - 1] + (u[n - 3] if n >= 3 else 0)
    # First summand z(1+3z^2)/(1-z-z^3).
    for n in range(1, nmax + 1):
        coeff[n] = u[n - 1] + (3 * u[n - 3] if n >= 3 else 0)
        coeff[n] += (-1) ** n
        if n % 3 == 0:
            m = n // 3
            coeff[n] -= 2 + 3 * (2 ** (m - 1) - 1)
        assert coeff[n] == exact_count(n, t), (n, coeff[n], exact_count(n, t))
    assert coeff[0] == 0


if __name__ == '__main__':
    checks = brute_check()
    check_rational_series()
    print('N,B_n,two_preimage_outputs')
    for row in checks:
        print(*row, sep=',')
    print('VERIFY_OK')
