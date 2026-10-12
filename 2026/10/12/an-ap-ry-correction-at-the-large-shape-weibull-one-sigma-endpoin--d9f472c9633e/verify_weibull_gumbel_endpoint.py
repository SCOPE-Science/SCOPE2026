import mpmath as mp

mp.mp.dps = 80

gamma_e = mp.euler
zeta3 = mp.zeta(3)
a = mp.pi / mp.sqrt(6)
u_minus = mp.e ** (-gamma_e - a)
u_plus = mp.e ** (-gamma_e + a)
C_inf = mp.e ** (-u_minus) - mp.e ** (-u_plus)
A = (zeta3 / a) * (u_minus * mp.e ** (-u_minus) + u_plus * mp.e ** (-u_plus))


def central_mass(k):
    k = mp.mpf(k)
    r = 1 / k
    mean = mp.gamma(1 + r)
    sd = mp.sqrt(mp.gamma(1 + 2 * r) - mean * mean)
    lo = mean - sd
    hi = mean + sd
    if lo <= 0:
        lower_tail = mp.mpf('0')
    else:
        lower_tail = mp.e ** (-(lo ** k))
    upper_cdf_tail = mp.e ** (-(hi ** k))
    return lower_tail - upper_cdf_tail


# Reference constants in the theorem.
assert abs(C_inf - mp.mpf('0.72375126751971034068479770553422035')) < mp.mpf('1e-34')
assert abs(A - mp.mpf('0.37546693034735008031194969969760075')) < mp.mpf('1e-34')
assert A > 0

# Direct evaluation of the exact Weibull central probability approaches the
# stated first-order law. These finite calculations are regression checks only.
for k in [50, 100, 200, 500, 1000, 2000]:
    c = central_mass(k)
    first_order = C_inf - A / k
    scaled_second = (c - first_order) * k * k
    assert mp.mpf('0.75') < scaled_second < mp.mpf('0.95')

# The signed first-order coefficient means approach is from below.
for k in [50, 100, 200, 500, 1000, 2000]:
    assert central_mass(k) < C_inf

scaled = 1000 * (C_inf - central_mass(1000))
assert abs(scaled - A) < mp.mpf('0.001')

print(
    'VERIFY_OK '
    f'Cinf={float(C_inf):.15f} '
    f'A={float(A):.15f} '
    f'scaled_k1000={float(scaled):.15f}'
)
