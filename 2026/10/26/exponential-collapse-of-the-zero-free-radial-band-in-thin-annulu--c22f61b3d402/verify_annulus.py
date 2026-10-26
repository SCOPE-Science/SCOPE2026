"""Finite high-precision checks for a thin-annulus Bergman-kernel asymptotic."""
import mpmath as mp

mp.mp.dps = 100


def direct_h(L, v):
    q = mp.exp(-L)
    x = mp.exp(-L * v)
    f = lambda z: z / (1 + z)**2
    return 1/L - mp.nsum(lambda j: f(x * q**j) + f(q**(j+1)/x), [0, mp.inf])


def dual_h(L, v):
    return -4*mp.pi**2/L**2 * mp.nsum(
        lambda k: k*mp.cos(2*mp.pi*k*v)/mp.sinh(2*mp.pi**2*k/L), [1, mp.inf])


max_duality_error = mp.mpf('0')
ratios = []
for Lstr in ['3', '2.2', '1.8', '1.4', '1', '0.8', '0.6']:
    L = mp.mpf(Lstr)
    vc = mp.mpf('0.25')
    diff = abs(direct_h(L, vc) - dual_h(L, vc))
    max_duality_error = max(max_duality_error, diff)
    assert diff < mp.mpf('1e-75')
    left, right = mp.mpf('0.20'), vc
    assert dual_h(L, left) < 0 < dual_h(L, right)
    for _ in range(270):
        mid = (left + right)/2
        if dual_h(L, mid) < 0:
            left = mid
        else:
            right = mid
    v = (left + right)/2
    x = mp.exp(-L*v)
    r = mp.exp(-L/2)
    gap = x-r/x
    predicted = 2*L/mp.pi * mp.exp(-L/4-2*mp.pi**2/L)
    ratio = gap/predicted
    assert mp.mpf('0.999') < ratio < mp.mpf('1.001')
    ratios.append((Lstr, mp.nstr(ratio, 18)))

print('Direct-series versus Poisson-series maximum error:', mp.nstr(max_duality_error, 6))
for Lstr, ratio in ratios:
    print('L=', Lstr, ' exact_width/predicted_width=', ratio)
print('All finite consistency checks passed.')
