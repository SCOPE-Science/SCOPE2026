"""Supplementary finite tests for cross-products of Gaussian Fock weighted compositions.

Requires Python 3 and numpy. Numerical truncation is not a proof of any
infinite-dimensional statement; consult RESULT.md for the analytical proof.
"""
import math
import numpy as np


def coefficients(a, b, u, h=1.0, dimension=58):
    """Top-left monomial matrix of h exp(uz) f(az+b) in e_n=z^n/sqrt(n!)."""
    output = np.zeros((dimension, dimension), dtype=np.complex128)
    for n in range(dimension):
        for m in range(dimension):
            value = 0j
            for k in range(min(m, n) + 1):
                if (b == 0 and n > k) or (u == 0 and m > k):
                    continue
                value += (math.comb(n, k) * a ** k * b ** (n-k)
                          * u ** (m-k) / math.factorial(m-k))
            output[m, n] = h * value * math.exp(0.5 *
                (math.lgamma(m+1) - math.lgamma(n+1)))
    return output


def data(a, b, u, h=1.0):
    v = (u.conjugate() + a.conjugate() * b) / (1 - abs(a)**2)
    w = -b - a*v
    nrm = abs(h) * math.exp((abs(b)**2 + (1-abs(a)**2)*abs(v)**2)/2)
    return v, w, nrm


def expected(left, right):
    a, b, u, h = left
    c, d, x, g = right
    vl, wl, nl = data(a, b, u, h)
    vr, wr, nr = data(c, d, x, g)
    kappa = (1-abs(a)**2)*(1-abs(c)**2)/(1-abs(a*c)**2)
    r = abs(a*c)
    return (nl*nr*math.exp(-kappa*abs(wl-wr)**2/2),
            nl*nr*math.exp(-kappa*abs(vl-vr)**2/2), r)


def assert_close(actual, predicted, rel_tol=1e-8):
    assert abs(actual-predicted) <= rel_tol * max(1, abs(predicted)), (actual, predicted)


CASES = [
    ((.4+.15j, -.2+.3j, .12+.2j, 1), (.5-.2j, .3+.1j, .2-.1j, 1)),
    ((.6+0j, .2+.1j, .1+.3j, 1), (.3+0j, .4j, .2+0j, 1)),
    ((.3+0j, .5+0j, 0j, 1), (.3+0j, -.5+0j, 0j, 1)),
    ((0j, .2+0j, .14+0j, 1), (.5+0j, .1+0j, 0j, 1)),
    ((.45+.1j, -.1+.2j, .18-.03j, .7+.2j), (.35-.15j, .1-.2j, .05+.17j, -.7j)),
]


def run():
    assertions = 0
    for left, right in CASES:
        a, b, u, h = left
        c, d, x, g = right
        A = coefficients(a, b, u, h)
        B = coefficients(c, d, x, g)
        expected_left, expected_right, r = expected(left, right)
        for product, target in ((A @ B.conj().T, expected_left),
                                (A.conj().T @ B, expected_right)):
            actual = np.linalg.svd(product, compute_uv=False)
            for k in range(5):
                assert_close(actual[k], target*r**k, 2e-7)
                assertions += 1
        _, _, n1 = data(a, b, u, h)
        _, _, n2 = data(c, d, x, g)
        assert_close(np.linalg.svd(A, compute_uv=False)[0], n1, 2e-7)
        assert_close(np.linalg.svd(B, compute_uv=False)[0], n2, 2e-7)
        assertions += 2
    # Equal-slope, unit-normalized example with reversible order preference.
    a = .5+0j
    t = 2+0j
    first = (a, 0j, 0j, 1.)
    second_left = (a, -a*t, t.conjugate(), math.exp(-abs(t)**2/2))
    second_right = (a, -t, a*t.conjugate(), math.exp(-abs(t)**2/2))
    kappa = (1-abs(a)**2)/(1+abs(a)**2)
    direct, reverse, _ = expected(first, second_left)
    assert_close(direct, 1.)
    assert_close(reverse, math.exp(-kappa*abs(t)**2/2))
    assertions += 2
    direct, reverse, _ = expected(first, second_right)
    assert_close(reverse, 1.)
    assert_close(direct, math.exp(-kappa*abs(t)**2/2))
    assertions += 2
    print(f"PASS: {assertions} finite numerical assertions; every tested cross-product agrees with its first five predicted singular values.")


if __name__ == '__main__':
    run()
