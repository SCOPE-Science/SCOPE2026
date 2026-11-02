"""Numerical reproduction checks for a two-rate Brownian resetting FPT law.

Usage: python verify.py
Dependency: mpmath >= 1.2 (only for high-precision arithmetic).
The checks verify finite instances and asymptotic identities; they are not
substitutes for the analytical proof in RESULT.md.
"""
from mpmath import mp

mp.dps = 70
checks = 0


def assert_close(x, y, atol='1e-47', rtol='1e-44'):
    global checks
    x, y = mp.mpf(x), mp.mpf(y)
    assert abs(x - y) <= mp.mpf(atol) + mp.mpf(rtol) * max(abs(x), abs(y))
    checks += 1


def h(x, ell=1):
    return mp.expm1(ell * mp.sqrt(x)) / x


def hprime(x, ell=1):
    z = ell * mp.sqrt(x)
    return (1 + mp.exp(z) * (z / 2 - 1)) / x**2


def hsecond(x, ell=1):
    z = ell * mp.sqrt(x)
    return (mp.exp(z) * (z * z - 5 * z + 8) - 8) / (4 * x**3)


def exact(r, eta, nu, ell=1):
    """Closed spectral formula, stable against huge fast-mode exponentials."""
    r, eta, nu, ell = map(mp.mpf, (r, eta, nu, ell))
    assert r > eta > 0 and nu > 0
    w = mp.sqrt(nu * nu / 4 + eta * eta)
    low, high = r + nu / 2 - w, r + nu / 2 + w
    c2, q2 = (1 + nu / (2 * w)) / 2, (1 - nu / (2 * w)) / 2
    L, H = h(low, ell), h(high, ell)
    return (nu * L * H + c2 * L + q2 * H) / (1 + nu * (q2 * L + c2 * H))


def backward_ode(r, eta, nu, ell=1):
    """Independent two-component backward-boundary linear-system calculation.

    The environmental basis is (symmetric,antisymmetric), and resetting in a
    given phase preserves the environmental state. The solution at the reset
    point solves (I-G Lambda) v = G 1 with G=B^-1(I-exp(-ell sqrt B)).
    """
    r, eta, nu, ell = map(mp.mpf, (r, eta, nu, ell))
    B = mp.matrix([[r, eta], [eta, r + nu]])
    Lambda = mp.matrix([[r, eta], [eta, r]])
    w = mp.sqrt(nu * nu / 4 + eta * eta)
    low, high = r + nu / 2 - w, r + nu / 2 + w
    Id = mp.eye(2)
    Plow = (high * Id - B) / (high - low)
    Phigh = Id - Plow
    K = Plow * (1 - mp.exp(-ell * mp.sqrt(low))) / low
    K += Phigh * (1 - mp.exp(-ell * mp.sqrt(high))) / high
    v = mp.inverse(Id - K * Lambda) * (K * mp.matrix([mp.sqrt(2), 0]))
    return v[0] / mp.sqrt(2)


for ell in [mp.mpf('0.5'), mp.mpf('1'), mp.mpf('2')]:
    zstar = mp.findroot(lambda z: mp.exp(z) * (z - 2) + 2, (mp.mpf('1.4'), mp.mpf('1.8')))
    star = (zstar / ell)**2
    assert_close(hprime(star, ell), 0)
    for v in [mp.mpf('.1'), mp.mpf('.7'), mp.mpf('2'), star, star * 2]:
        assert_close(hprime(v, ell), mp.diff(lambda x: h(x, ell), v, 1))
        assert_close(hsecond(v, ell), mp.diff(lambda x: h(x, ell), v, 2))
        assert hsecond(v, ell) > 0
        checks += 1
    for ratio in [mp.mpf('.2'), mp.mpf('.5'), mp.mpf('.8')]:
        eta = star * ratio
        for nu in [mp.mpf('.15'), mp.mpf('1'), mp.mpf('5'), mp.mpf('30')]:
            assert_close(exact(star, eta, nu, ell), backward_ode(star, eta, nu, ell))
        # At the Poisson optimum the first nonzero correction is positive.
        alpha2 = eta**2 * h(star, ell) + eta**4 * hsecond(star, ell) / 2
        cstar = h(star, ell) / hsecond(star, ell) + eta**2 / 2
        for nu in [mp.mpf('100000'), mp.mpf('300000'), mp.mpf('1000000')]:
            raw = exact(star, eta, nu, ell) - h(star, ell)
            assert raw > 0
            checks += 1
            # Scaled remainder is O(1/nu), with generous finite-n bound.
            assert abs(nu**2 * raw / alpha2 - 1) < mp.mpf('10') / nu
            checks += 1
            for off, sign in [(-mp.mpf('15'), 1), (mp.mpf('15'), -1)]:
                r = star + (cstar + off) / nu
                if r <= eta:  # skip outside required positive-rate domain
                    continue
                delta = exact(r, eta, nu, ell) - h(r, ell)
                assert sign * delta > 0
                checks += 1
                # Limit at fixed critical-window displacement.
                lim = -eta**2 * hsecond(star, ell) * off
                assert abs(nu**2 * delta / lim - 1) < mp.mpf('1500') / nu, (ell,eta,nu,off,nu**2 * delta / lim)
                checks += 1
        # Slow switching gives a strict convexity excess over the same mean.
        quench = (h(star - eta, ell) + h(star + eta, ell)) / 2
        assert quench > h(star, ell)
        checks += 1
        assert abs(exact(star, eta, mp.mpf('1e-9'), ell) - quench) < mp.mpf('1e-6')
        checks += 1
        for factor, expected in [(mp.mpf('.7'), 1), (mp.mpf('1.3'), -1)]:
            r = star * factor
            if r <= eta:
                continue
            nu = mp.mpf('4000')
            delta = exact(r, eta, nu, ell) - h(r, ell)
            assert delta * expected > 0
            checks += 1
            first = -eta**2 * hprime(r, ell) / nu
            second = (eta**2 * h(r, ell) + eta**4 * hsecond(r, ell) / 2) / nu**2
            assert abs((delta - first - second) / first) < mp.mpf('4e-5')
            checks += 1

print('PASS:', checks, 'bounded high-precision checks')
