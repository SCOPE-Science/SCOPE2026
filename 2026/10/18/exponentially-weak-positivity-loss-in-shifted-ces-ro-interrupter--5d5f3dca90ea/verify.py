"""Reproducibility checks for a negative auxiliary-defect eigenvalue.

Run: python verify.py. Requires mpmath>=1.3,<2.
The continuum statements are proved analytically in RESULT.md.
"""
from fractions import Fraction
import mpmath as mp


def column(j, eps):
    r = Fraction(1, 1) / (Fraction(j + 2) - eps)
    return tuple([r] * (j + 1) + [r - 1])


def gram(i, j, eps):
    x, y = column(i, eps), column(j, eps)
    return sum((x[k] if k < len(x) else 0) * (y[k] if k < len(y) else 0)
               for k in range(max(len(x), len(y))))


def exact_tests():
    count = 0
    for eps in (Fraction(1, 5), Fraction(1, 3), Fraction(2, 3), Fraction(9, 10)):
        for i in range(18):
            for j in range(18):
                ri = Fraction(1, 1) / (Fraction(i + 2) - eps)
                rj = Fraction(1, 1) / (Fraction(j + 2) - eps)
                expected = (1 - ri if i == j else 0) + eps * ri * rj
                assert gram(i, j, eps) == expected
                count += 1
    return count


def finite_detection_size(eps, b):
    """First initial-coordinate compression with a negative direction."""
    def test(n):
        return eps * (mp.digamma(n + b) - mp.digamma(b)) > 1
    lo, hi = 0, 1
    while not test(hi):
        lo, hi = hi, 2 * hi
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if test(mid):
            hi = mid
        else:
            lo = mid
    assert not test(hi - 1) and test(hi)
    return hi


def spectral_tests():
    mp.mp.dps = 85
    target = mp.exp(mp.euler - 1)
    records = []
    for eps_str in ('0.3', '0.2', '0.1', '0.05', '0.02'):
        eps = mp.mpf(eps_str)
        b = 2 - eps
        def f(h):
            return eps * (mp.digamma(b + mp.exp(h)) - mp.digamma(b)) - 1
        lo, hi = mp.mpf('-20'), mp.mpf(1) / eps + 5
        assert f(lo) < 0 and f(hi) > 0
        for _ in range(325):
            mid = (lo + hi) / 2
            if f(mid) > 0:
                hi = mid
            else:
                lo = mid
        h = (lo + hi) / 2
        delta = mp.exp(-h)
        residual = abs(f(h))
        assert residual < mp.mpf('1e-50')
        scaled = mp.exp(1 / eps) * delta
        c_sq_over_delta = delta / mp.polygamma(1, b + 1 / delta)
        N = finite_detection_size(eps, b)
        records.append((eps_str, mp.nstr(delta, 15), mp.nstr(scaled, 15),
                        mp.nstr(c_sq_over_delta, 12), str(N), mp.nstr(N * delta, 12)))
    assert abs(mp.mpf(records[-1][2]) - target) < mp.mpf('0.02')
    assert abs(mp.mpf(records[-1][3]) - 1) < mp.mpf('1e-10')
    assert abs(mp.mpf(records[-1][5]) - 1) < mp.mpf('1e-10')
    return mp.nstr(target, 15), records


if __name__ == '__main__':
    print('Exact rational Gram identities:', exact_tests())
    target, records = spectral_tests()
    print('Predicted limiting prefactor:', target)
    for entry in records:
        print('eps, delta, exp(1/eps)*delta, c^2/delta, N*, N*delta:', *entry)
    print('All checks passed.')
