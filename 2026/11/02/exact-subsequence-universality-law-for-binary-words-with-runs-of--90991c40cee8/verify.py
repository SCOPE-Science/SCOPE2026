#!/usr/bin/env python3
"""Independently reproduce finite coefficients and greedy-arch counts.

Only standard-library modules are needed.  Finite tests corroborate the
mathematical proof; they do not replace the all-length argument.
"""
from collections import Counter
from itertools import product
from math import comb, sqrt, isclose

N_MAX = 16


def admissible(bits):
    return all(not (bits[i] == bits[i+1] == bits[i+2])
               for i in range(len(bits)-2))


def greedy_arches(bits):
    mask = 0
    completed = 0
    for b in bits:
        mask |= (1 << b)
        if mask == 3:
            completed += 1
            mask = 0
    return completed


def exact_poly_coefficient(k, j):
    # Coefficient of z^j in (2+z)^k.
    if not (0 <= j <= k):
        return 0
    return comb(k, j) * 2 ** (k-j)


def formula(n, k):
    if k == 0:
        return {0: 1, 1: 2, 2: 2}.get(n, 0)
    j = n - 2*k
    return (exact_poly_coefficient(k, j)
            + 2*exact_poly_coefficient(k, j-1)
            + 2*exact_poly_coefficient(k, j-2)
            + exact_poly_coefficient(k-1, j-1))


def states_distribution(n_max):
    # Direct 3-state transfer, independent from closed-form coefficient code.
    # State keys: pending run length 1 / 2, or just closed an arch.
    p, q, e = Counter(), Counter(), Counter()
    out = [{0: 1}]
    for n in range(1, n_max+1):
        new_p, new_q, new_e = Counter(), Counter(), Counter()
        if n == 1:
            new_p[0] = 2
        for k, v in p.items():
            new_q[k] += v
            new_e[k+1] += v
        for k, v in q.items():
            new_e[k+1] += v
        for k, v in e.items():
            new_p[k] += v
            new_q[k] += v
        p, q, e = new_p, new_q, new_e
        sums = Counter(p)
        sums.update(q)
        sums.update(e)
        out.append(dict(sums))
    return out


def is_subsequence(needle, haystack):
    j = 0
    for x in haystack:
        if j < len(needle) and needle[j] == x:
            j += 1
    return j == len(needle)


def direct_index(bits):
    # Slow, definition-level check independent of the arch characterization.
    k = 0
    while k + 1 <= len(bits):
        if all(is_subsequence(t, bits) for t in product((0, 1), repeat=k+1)):
            k += 1
        else:
            return k
    return k


def main():
    trans = states_distribution(N_MAX)
    for n in range(N_MAX+1):
        expected = {k: v for k in range(n//2+1)
                    if (v := formula(n, k)) > 0}
        assert expected == trans[n], ("state/formula", n, expected, trans[n])
        observed = Counter()
        for bits in product((0, 1), repeat=n):
            if not admissible(bits):
                continue
            k = greedy_arches(bits)
            observed[k] += 1
            if n <= 12:
                assert k == direct_index(bits), ("universality", bits, k)
        assert dict(observed) == expected, ("direct", n, observed, expected)
        total = sum(expected.values())
        if n == 0:
            assert total == 1
        else:
            f0, f1 = 0, 1
            for _ in range(n+1):
                f0, f1 = f1, f0+f1
            assert total == 2*f0, ("Fibonacci", n, total, f0)
        print(f"n={n:2d} total={total:5d} histogram={dict(sorted(observed.items()))}")
    rho = (sqrt(5)-1)/2
    p2, p3 = 2*rho**2, rho**3
    mu = 2*p2+3*p3
    variance = p2*p3/mu**3
    assert isclose(p2+p3, 1.0, abs_tol=1e-13)
    assert isclose(mu, sqrt(5), abs_tol=1e-13)
    assert isclose(variance, 1 - 11*sqrt(5)/25, abs_tol=1e-13)
    print("analytic constants:", 1/mu, variance)
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
