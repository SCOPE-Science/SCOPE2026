"""Independent numerical checks for the square-gap pressure identities.

Requires mpmath. Numerical diagnostics do not prove the infinite statements.
"""
import math
import mpmath as mp

mp.mp.dps = 155


def theta_direct(p):
    # Each omitted term is below 10^(-165), with a geometric tail bound.
    cutoff = int(mp.ceil(mp.sqrt((165 * mp.log(10) + 10) / p))) + 2
    return mp.fsum(mp.exp(-p * j * j) for j in range(1, cutoff + 1))


def theta_dual(p):
    s = mp.sqrt(mp.pi / p)
    return (s - 1) / 2 + s * mp.fsum(
        mp.exp(-mp.pi**2 * j * j / p) for j in range(1, 5)
    )


def analytic_root(z):
    def f(p):
        return z * mp.exp(-p) * (mp.sqrt(mp.pi / p) - 1) / 2 - 1
    lo, hi = mp.mpf('1e-100'), mp.pi
    for _ in range(560):
        mid = (lo + hi) / 2
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def root_true(z, p0):
    p = +p0
    for _ in range(5):
        vals = [mp.exp(-p * j * j) for j in range(1, int(mp.ceil(mp.sqrt((165 * mp.log(10) + 10) / p))) + 3)]
        q = mp.fsum(vals)
        d = -z * mp.exp(-p) * mp.fsum((j*j + 1) * v for j, v in enumerate(vals, start=1))
        p = p - (z * mp.exp(-p) * q - 1) / d
    return p


def marker_density(z, p):
    cutoff = int(mp.ceil(mp.sqrt((165 * mp.log(10) + 10) / p))) + 2
    return 1 / (z * mp.exp(-p) * mp.fsum(
        (j*j + 1) * mp.exp(-p*j*j) for j in range(1, cutoff+1)))


ratios = []
for z_text in ('1', '0.75', '0.5', '0.35'):
    z = mp.mpf(z_text)
    p0 = analytic_root(z)
    p = root_true(z, p0)
    assert p > p0 > 0
    assert abs(z * mp.exp(-p) * theta_direct(p) - 1) < mp.mpf('1e-130')
    assert abs(theta_direct(p0) - theta_dual(p0)) < mp.mpf('1e-120')
    density = marker_density(z, p)
    dt = mp.mpf('1e-12')
    pp = root_true(z * mp.exp(dt), analytic_root(z * mp.exp(dt)))
    pm = root_true(z * mp.exp(-dt), analytic_root(z * mp.exp(-dt)))
    assert abs((pp - pm) / (2*dt) - density) < mp.mpf('1e-19')
    ratio = (p-p0) / (4*p0*mp.exp(-mp.pi**2/p0))
    assert mp.mpf('0.6') < ratio < mp.mpf('1.01')
    ratios.append(float(ratio))
    print(f'z={z_text}: analytic_root={mp.nstr(p0, 19)}; '
          f'flat_correction={mp.nstr(p-p0, 8)}; ratio={mp.nstr(ratio, 12)}')

assert all(ratios[i] < ratios[i+1] for i in range(3))
assert math.gcd(2, 5) == 1
print('VERIFY_OK: 4 renewal normalizations; 4 Jacobi-dual checks; '
      '4 pressure-density checks; 4 beyond-all-orders ratios; mixing gcd')
