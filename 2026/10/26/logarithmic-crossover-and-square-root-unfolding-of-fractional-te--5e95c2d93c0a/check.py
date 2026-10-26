"""Reproduce numerical diagnostics for the fractional-tent Fourier-zero transition.
Run: python check.py (requires mpmath 1.3 or later).
Finite tests are diagnostics, not a substitute for the uniform asymptotic proof.
"""
import mpmath as mp
mp.mp.dps=70


def transform(alpha, t):
    """Exact Fourier integral via the lower incomplete gamma function."""
    z = 1j * mp.mpf(t)
    return 2 * mp.re(mp.exp(z) * mp.gammainc(alpha + 1, 0, z) / z ** (alpha + 1))


def root_shift(alpha, n, lower, upper):
    center = 2 * mp.pi * n
    left, right = mp.mpf(lower), mp.mpf(upper)
    fl = transform(alpha, center + left)
    fr = transform(alpha, center + right)
    assert fl * fr < 0
    for _ in range(105):
        mid = (left + right) / 2
        fm = transform(alpha, center + mid)
        if fl * fm <= 0:
            right, fr = mid, fm
        else:
            left, fl = mid, fm
    return (left + right) / 2


def verify():
    for n in (1, 2, 7):
        eps = mp.mpf('0.0001')
        center = 2 * mp.pi * n
        c = mp.euler + mp.log(center) - mp.ci(center)
        assert c > 0
        predicted = mp.sqrt(2 * eps * c)
        left = root_shift(1-eps, n, -2*predicted, 0)
        right = root_shift(1-eps, n, 0, 2*predicted)
        assert abs(-left / predicted - 1) < mp.mpf('0.02')
        assert abs(right / predicted - 1) < mp.mpf('0.02')
        print('local', n, 'minus', mp.nstr(left, 11), 'plus', mp.nstr(right, 11), 'predicted', mp.nstr(predicted, 11))
    target_lambda = mp.mpf('0.5')
    target_shift = mp.acos(mp.exp(-target_lambda))
    for eps, n in ((mp.mpf('0.1'), 24), (mp.mpf('0.05'), 3505), (mp.mpf('0.025'), 77222800), (mp.mpf('0.02'), 11459600000)):
        center = 2 * mp.pi * n
        lam = eps * mp.log(center)
        left = root_shift(1-eps, n, -mp.pi, 0)
        right = root_shift(1-eps, n, 0, mp.pi)
        assert abs(lam-target_lambda)<mp.mpf('0.002')
        assert abs(left+target_shift)<mp.mpf('0.25')
        assert abs(right-target_shift)<mp.mpf('0.25')
        print('crossover',mp.nstr(eps,5),'n',n,'lambda',mp.nstr(lam,9), 'minus',mp.nstr(left,11),'plus',mp.nstr(right,11), 'limit',mp.nstr(target_shift,11))
    for t in (mp.mpf('1.3'), mp.pi, 2*mp.pi, 17*mp.pi):
        expected = 2*(1-mp.cos(t))/(t*t)
        assert abs(transform(mp.mpf(1),t)-expected)<mp.mpf('1e-48')
    print('triangular-transform identities: 4 passed')
    print('all diagnostic checks passed')

if __name__=='__main__':
    verify()
