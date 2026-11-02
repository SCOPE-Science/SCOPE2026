"""Deterministic finite numerical checks of nonlinear active-gas stationary formulas.

Python 3 standard library only. This supports, but does not prove, the all-flux theorem.
"""
import math

M, alpha, rho_m, u = 4.0, 1.0, 8.0, 1.0 / 8.0
J = rho_m * u
r = 1.0
L = math.sqrt(r * (r + alpha))
b = (u / L) * math.log(M * L / (2.0 * J))
assert b > 0


def simpson(fn, lo, hi, n=4000):
    assert n % 2 == 0
    h = (hi - lo) / n
    ans = fn(lo) + fn(hi)
    for k in range(1, n):
        ans += (4 if k % 2 else 2) * fn(lo + h * k)
    return h * ans / 3


def root(fn, lo, hi, n=100):
    assert fn(lo) <= 0 <= fn(hi)
    for _ in range(n):
        mid = (lo + hi) / 2
        if fn(mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


for p in (1, 2, 3, 4, 7):
    def flux(z):
        return z * (1 - (z / rho_m) ** p)

    def derivative(z):
        return 1 - (p + 1) * (z / rho_m) ** p

    peak = rho_m / (p + 1) ** (1.0 / p)
    peak_flux = flux(peak)
    rb = root(lambda z: flux(z) - J, 0, peak)
    assert abs(flux(rb) - J) < 3e-14

    # Evaluate phase branch current, gas mass, liquid mass via distinct quadratures.
    gas_half = simpson(lambda z: derivative(z) / L, 0, rb)
    liquid_half = simpson(lambda x: rho_m * math.exp(L * (b - x) / u), 0, b)
    assert abs(2 * (gas_half + liquid_half) - M) < 3e-10
    assert abs(gas_half - J / L) < 3e-12

    # Distance inversion and original stationary ODE at four positive distances.
    def distance(y):
        return (math.log(rb / y) - (p + 1) *
                (rb ** p - y ** p) / (p * rho_m ** p)) / L

    for d in (0.02, 0.2, 0.7, 1.5):
        z = root(lambda y: d - distance(y), 1e-12, rb)
        assert abs(distance(z) - d) < 1e-10
        expected_drho_dx = -L * z / derivative(z)
        step = 1e-5
        z_2 = root(lambda y: d + step - distance(y), 1e-12, rb)
        z_1 = root(lambda y: d - step - distance(y), 1e-12, rb)
        assert abs((z_2 - z_1) / (2 * step) - expected_drho_dx) < 2e-5

    pure_gas = M * L / 2 <= peak_flux
    if p == 1:
        assert not pure_gas
    if p == 2:
        assert pure_gas
    if pure_gas:
        rho0 = root(lambda z: flux(z) - M * L / 2, 0, peak)
        assert abs(flux(rho0) - M * L / 2) < 5e-14

    print(f'p={p} fmax={peak_flux:.6f} gas_only={pure_gas} '
          f'interface={rb:.6f} droplet_width={b:.9f}')

Lstar = 2 * math.e * J / M
bstar = u * math.log(M * Lstar / (2 * J)) / Lstar
assert abs(bstar - M / (2 * math.e * rho_m)) < 1e-13
assert abs(2 * J / (M * Lstar) - 1 / math.e) < 1e-13
assert 2 < math.e < 16 / (3 * math.sqrt(3))
print('Optimal width',format(bstar,'.14g'),'; liquid fraction',format(1-1/math.e,'.14g'))
print('All finite checks passed.')
