import mpmath as mp

mp.mp.dps = 80

def C(alpha):
    a = mp.mpf(alpha)
    return (
        155*mp.pi**6*a*a
        - 98*mp.pi**4*(a*a-1)
        + 35*mp.pi**2*(3*a*a-4)
        + 630
    )/105

def poly(x, alpha):
    a = mp.mpf(alpha)
    return ((1-a*x)**2 + 1) * ((x*x-1)**2 + 2)

def dens(x, alpha):
    return poly(x, alpha)/C(alpha) * mp.e**(-x)/(1+mp.e**(-x))**2

def tail_degree(alpha):
    return 4 if mp.mpf(alpha) == 0 else 6

def tail_constant(alpha):
    a = mp.mpf(alpha)
    return (mp.mpf(2) if a == 0 else a*a)/C(a)

# Normalization and finite interior MGF checks.
for a in [mp.mpf("-2"), mp.mpf("-0.5"), mp.mpf("0"), mp.mpf("0.5"), mp.mpf("3")]:
    mass = mp.quad(lambda x: dens(x,a), [-mp.inf, -8, 0, 8, mp.inf])
    assert abs(mass-1) < mp.mpf("1e-45")
    for t in [mp.mpf("-0.5"), mp.mpf("0"), mp.mpf("0.5")]:
        val = mp.quad(lambda x: mp.e**(t*x)*dens(x,a), [-mp.inf, -8, 0, 8, mp.inf])
        assert mp.isfinite(val) and val > 0

# Pointwise density tail constants.
for a in [mp.mpf("-2"), mp.mpf("-0.5"), mp.mpf("0"), mp.mpf("0.5"), mp.mpf("3")]:
    m = tail_degree(a)
    A = tail_constant(a)
    x = mp.mpf("250")
    rr = dens(x,a)/(A*x**m*mp.e**(-x))
    lr = dens(-x,a)/(A*x**m*mp.e**(-x))
    assert abs(rr-1) < mp.mpf("0.03")
    assert abs(lr-1) < mp.mpf("0.03")

# Survival balance and hazard limits by direct quadrature.
for a in [mp.mpf("-0.5"), mp.mpf("0"), mp.mpf("2")]:
    x = mp.mpf("220")
    sf = mp.quad(lambda z: dens(z,a), [x, x+20, x+80, mp.inf])
    lf = mp.quad(lambda z: dens(z,a), [-mp.inf, -x-80, -x-20, -x])
    assert abs(sf/lf-1) < mp.mpf("0.08")
    h = dens(x,a)/sf
    rh = dens(-x,a)/lf
    assert abs(h-1) < mp.mpf("0.04")
    assert abs(rh-1) < mp.mpf("0.04")

# Boundary MGF mechanism: at t=1 on the right and t=-1 on the left,
# the exponential damping disappears and the integrand is asymptotic
# to a positive polynomial.
for a in [mp.mpf("-0.5"), mp.mpf("0"), mp.mpf("2")]:
    m = tail_degree(a)
    A = tail_constant(a)
    x = mp.mpf("250")
    right_boundary_ratio = mp.e**x * dens(x,a)/(A*x**m)
    left_boundary_ratio = mp.e**x * dens(-x,a)/(A*x**m)
    assert abs(right_boundary_ratio-1) < mp.mpf("0.03")
    assert abs(left_boundary_ratio-1) < mp.mpf("0.03")

print("VERIFY_OK")
for a in [mp.mpf("-0.5"), mp.mpf("0"), mp.mpf("2")]:
    m = tail_degree(a)
    A = tail_constant(a)
    x = mp.mpf("220")
    sf = mp.quad(lambda z: dens(z,a), [x, x+20, x+80, mp.inf])
    lf = mp.quad(lambda z: dens(z,a), [-mp.inf, -x-80, -x-20, -x])
    print(
        "alpha", mp.nstr(a,8),
        "tail_balance", mp.nstr(sf/lf,20),
        "right_hazard", mp.nstr(dens(x,a)/sf,20),
        "left_reversed_hazard", mp.nstr(dens(-x,a)/lf,20)
    )
