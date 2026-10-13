import mpmath as mp

mp.mp.dps = 70

def source_term(i, j):
    # Source Eq. (3.2) at r=tau=eta=kappa=phi=1.
    return mp.e * ((-1)**i) * (mp.mpf(i)**j) / mp.factorial(i)

# Exact row obstruction.
for j in range(0, 40):
    assert abs(source_term(1, j) + mp.e) < mp.mpf("1e-60")

# Equal rectangular truncations, for reproducibility only.
def rectangular(N):
    return mp.fsum(source_term(i,j) for i in range(N+1) for j in range(N+1))

vals = [rectangular(N) for N in range(1, 16)]
assert abs(vals[-1]) > mp.mpf("1e6")

# True all-one mean: direct integral versus incomplete gamma.
f = lambda x: mp.e * mp.e**(-mp.e**x - x)
quad = mp.quad(f, [0, 1, 2, 4, 8])
exact = mp.e * mp.gammainc(-1, 1, mp.inf)
assert abs(quad-exact) < mp.mpf("1e-45")

# Equal-shape identity at a second interior parameter point.
p = mp.mpf("2")
tau = mp.mpf("1.3")
kappa = mp.mpf("0.8")
r = p
c = (kappa/tau)**p

orig = r*mp.e*mp.quad(
    lambda x: x**(r-1) * mp.e**(-mp.e**((tau*x)**p) - (kappa*x)**p),
    [0, mp.mpf("0.5"), 1, 2, 4]
)
trans = (r*mp.e)/(p*tau**r) * mp.quad(
    lambda z: (mp.log(z)**(r/p-1)) * z**(-c-1) * mp.e**(-z),
    [1, 2, 5, 20, mp.inf]
)
closed = mp.e * tau**(-p) * mp.gammainc(-c, 1, mp.inf)
assert abs(orig-trans) < mp.mpf("1e-40")
assert abs(trans-closed) < mp.mpf("1e-55")

print("VERIFY_OK")
print("true_mean_all_one", mp.nstr(exact, 40))
print("rectangular_N15", mp.nstr(vals[-1], 30))
print("equal_shape_check", mp.nstr(closed, 40))
