import mpmath as mp

mp.mp.dps = 70

def source_m0(n, r, lam, k):
    n = int(n)
    return ((-1)**n)/mp.pi * (r*lam)**n/mp.factorial(n) * mp.gamma(mp.mpf(n)/k + 1) / (mp.mpf('0.5')**(mp.mpf(n)/k + 1))

def moment_integral(r, lam, k):
    assert k == 1
    f = lambda z: z**(r*lam-mp.mpf('0.5')) * (1-z)**(-mp.mpf('0.5')) / mp.pi
    return mp.quad(f, [0, mp.mpf('0.25'), mp.mpf('0.5'), mp.mpf('0.75'), mp.mpf('0.9'), mp.mpf('0.99'), mp.mpf('0.999'), 1])

# Transparent k=lambda=r=1 counterexample.
r = lam = k = mp.mpf(1)
true_mu = moment_integral(r,lam,k)
closed = mp.gamma(r*lam + mp.mpf('0.5'))/(mp.sqrt(mp.pi)*mp.gamma(r*lam+1))
assert abs(true_mu-mp.mpf('0.5')) < mp.mpf('1e-35')
assert abs(true_mu-closed) < mp.mpf('1e-35')

for n in range(8):
    exact = (mp.mpf(2)/mp.pi) * ((-2)**n)
    assert abs(source_m0(n,r,lam,k)-exact) < mp.mpf('1e-60')

# For k<1, the m=0 terms rapidly violate the term test.
k2 = mp.mpf('0.5')
vals = [abs(source_m0(n,1,1,k2)) for n in range(7)]
assert all(vals[j+1] > vals[j] for j in range(1,6))
assert vals[-1] > mp.mpf('1e9')

# Positive Tonelli-valid m-series at k=1.
def central_binom_coeff(m):
    return mp.binomial(2*m,m)/(mp.mpf(4)**m)

def corrected_k1_partial(M, r=mp.mpf(1), lam=mp.mpf(1)):
    return mp.fsum(central_binom_coeff(m)/(m+mp.mpf('0.5')+r*lam) for m in range(M+1))/mp.pi

# The positive series converges slowly (tail ~ m^-3/2), so compare a large partial sum with a rigorous-scale tolerance.
p200000 = corrected_k1_partial(200000)
assert abs(p200000-mp.mpf('0.5')) < mp.mpf('0.001')

print('VERIFY_OK')
print('true_mean_k1_lam1', mp.nstr(true_mu,40))
print('closed_mean_k1_lam1', mp.nstr(closed,40))
print('source_m0_terms', ' '.join(mp.nstr(source_m0(n,1,1,1),16) for n in range(6)))
print('k_half_m0_abs_n6', mp.nstr(vals[-1],30))
print('corrected_positive_partial_200000', mp.nstr(p200000,30))
