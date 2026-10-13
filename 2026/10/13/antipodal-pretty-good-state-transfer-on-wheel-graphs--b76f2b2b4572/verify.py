#!/usr/bin/env python3
"""Reproduce finite algebra and phase consistency checks for the wheel-transfer theorem.

The all-orders conclusions in RESULT.md follow from the proof, not these tests.
Only Python's standard library is used.
"""
import cmath
import math


def matrix_action(n, v):
    """Adjacency of K1 join C_n, hub indexed n."""
    out = [v[(j - 1) % n] + v[(j + 1) % n] + v[n] for j in range(n)]
    out.append(sum(v[:n]))
    return out


def residual(n, v, eigenvalue):
    out = matrix_action(n, v)
    return max(abs(out[j] - eigenvalue * v[j]) for j in range(n + 1))


def wheel_phase_error_squared(n, j):
    """Exact spectral-basis formula evaluated in floating point at time 2*pi*j."""
    root = math.sqrt(n + 1)
    plus, minus = 1 + root, 1 - root
    weight_plus = (1 + 1 / root) / 2
    weight_minus = 1 - weight_plus
    def dist_sq(x, target=1):
        return abs(cmath.exp(2j * math.pi * j * x) - target) ** 2
    error = weight_plus * dist_sq(plus) + weight_minus * dist_sq(minus)
    error += sum(dist_sq(2 * math.cos(2 * math.pi * k / n), (-1) ** k)
                 for k in range(1, n))
    return error / n


def check():
    count = 0
    for n in range(4, 49, 2):
        root = math.sqrt(n + 1)
        for k in range(1, n):
            w = cmath.exp(2j * math.pi * k / n)
            v = [w ** ell for ell in range(n)] + [0j]
            lam = 2 * math.cos(2 * math.pi * k / n)
            assert residual(n, v, lam) < 1e-10
            count += 1
        for lam in (1 + root, 1 - root):
            v = [1.0 for _ in range(n)] + [lam - 2]
            assert residual(n, v, lam) < 1e-10
            count += 1
        # Exact absence/phase-obstruction bookkeeping for all three cases.
        if n % 4 == 2:
            k = 1 + n // 2
            assert k % 2 == 0
            assert (n // 2) % 2 == 1
        elif n % 8 == 4:
            assert (n // 4) % 2 == 1 and (n // 2) % 2 == 0
        elif n & (n - 1):
            odd_primes = [p for p in range(3, n + 1, 2)
                          if n % p == 0 and all(p % d for d in range(3, math.isqrt(p) + 1, 2))]
            assert odd_primes
            p = odd_primes[0]
            q = n // p
            assert q % 2 == 0
            for k in (1, 2):
                ids = [k + a * q for a in range(p)]
                assert all(1 <= idx < n and idx % 2 == k % 2 for idx in ids)
                zeta = cmath.exp(2j * math.pi / n)
                assert abs(sum(zeta ** idx + zeta ** (-idx) for idx in ids)) < 1e-9
    # The small power-of-two exceptional case, and first irrational hub split.
    best = {}
    for n, bound in ((8, 3000), (16, 180000)):
        j, val = min(((j, wheel_phase_error_squared(n, j))
                      for j in range(1, bound + 1)), key=lambda t: t[1])
        best[n] = (j, math.sqrt(val))
    assert best[8][1] < 0.025
    assert best[16][1] < 0.21
    # Cyclotomic difference-basis check via the explicit unique powers
    # in X^(m-1) * (a0+sum a_k(X^k+X^-k)); all degrees < n/2.
    for exponent in range(3, 11):
        n = 1 << exponent
        m = n // 4
        centers = [{m - 1}, *[{m - 1 - k, m - 1 + k} for k in range(1, m)]]
        assert all(0 <= e < n // 2 for support in centers for e in support)
        assert len(set().union(*centers)) == sum(len(support) for support in centers)
    print('VERIFY_OK Fourier_eigenmodes=%d phase_witness_n8=%s phase_witness_n16=%s '
          'power_two_cyclotomic_supports=8' % (count, best[8], best[16]))


if __name__ == '__main__':
    check()
