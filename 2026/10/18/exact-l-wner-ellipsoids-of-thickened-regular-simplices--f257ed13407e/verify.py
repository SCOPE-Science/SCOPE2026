"""Exact-arithmetic checks for the enclosing ellipsoid of rounded regular simplices.

These are finite checks of identities used in the separate general proof, not
an exhaustive verification of its universal quantifiers.
"""
from fractions import Fraction as Q


def check():
    tests = 0
    support_tests = 0
    for n in range(3, 17):
        for k in range(2, n):
            for t in (Q(1, 2), Q(1, 3), Q(1, 4), Q(1, 5), Q(1, 7)):
                if n * t * t >= k:
                    continue
                s = (k - n * t * t) / ((n - k) * t)
                B = 1 + s * t
                A = B * (1 + s / t)
                assert n * t * (s + t) == k * B
                assert A - B - s * s == s / t
                assert (s + t) ** 2 / A == Q(k, n)
                assert (1 - t * t) / B == Q(n - k, n)
                # Exact scalar normalized covariance: the regular simplex
                # Gram structure averages to I_k/k; a signed basis averages
                # to I_(n-k)/(n-k).
                assert (s + t) ** 2 / (A * k) == Q(1, n)
                assert (1 - t * t) / (B * (n - k)) == Q(1, n)
                # Envelope derivative (partial s, with stationary t) = k/(s+t).
                assert n * t / (2 * B) + k / (2 * (s + t)) == k / (s + t)
                assert n * s / (2 * B) - k * s / (2 * t * (s + t)) == 0
                tests += 1
                for p in (Q(0), Q(1, 7), Q(1, 3), t, Q(2, 3), Q(1)):
                    ell_sq = A * p * p + B * (1 - p * p)
                    convex_sq = (1 + s * p) ** 2
                    assert ell_sq - convex_sq == (s / t) * (p - t) ** 2
                    assert ell_sq >= convex_sq
                    support_tests += 1
    for n in range(3, 17):
        for k in range(2, n):
            t = Q(1, 1)
            # s=0 uses t=sqrt(k/n), not rational generally; all semiaxes
            # reduce exactly to 1 independently of t when s=0.
            s = Q(0)
            assert (1+s*t)*(1+s/t) == 1
            assert 1+s*t == 1
    print(f'VERIFY_OK exact_parameter_pairs={tests} support_factorizations={support_tests} dimensions=3..16')


if __name__ == '__main__':
    check()
