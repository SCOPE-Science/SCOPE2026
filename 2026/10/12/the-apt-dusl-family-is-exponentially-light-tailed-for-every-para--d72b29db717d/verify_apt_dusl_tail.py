import mpmath as mp

mp.mp.dps = 90

def c_alpha(alpha):
    alpha = mp.mpf(alpha)
    if alpha == 1:
        return mp.mpf(1)
    return alpha*mp.log(alpha)/(alpha-1)

def lindley_survival(x, xi):
    return (1 + xi*x/(1+xi))*mp.e**(-xi*x)

def lindley_density(x, xi):
    return xi**2/(1+xi)*(1+x)*mp.e**(-xi*x)

def dus_cdf(x, xi):
    s = lindley_survival(x, xi)
    return (mp.e**(1-s)-1)/(mp.e-1)

def apt_survival(x, xi, alpha):
    H = dus_cdf(x, xi)
    alpha = mp.mpf(alpha)
    if alpha == 1:
        return 1-H
    return (alpha-alpha**H)/(alpha-1)

def apt_density(x, xi, alpha):
    s = lindley_survival(x, xi)
    G = 1-s
    H = (mp.e**G-1)/(mp.e-1)
    h_dus = lindley_density(x, xi)*mp.e**G/(mp.e-1)
    alpha = mp.mpf(alpha)
    if alpha == 1:
        return h_dus
    return mp.log(alpha)/(alpha-1)*h_dus*alpha**H

def tail_constant(alpha, xi):
    return c_alpha(alpha)*mp.e/(mp.e-1)*xi/(1+xi)

tests = [
    (mp.mpf("0.4"), mp.mpf("0.7")),
    (mp.mpf("1"), mp.mpf("1.3")),
    (mp.mpf("3.5"), mp.mpf("0.9")),
    (mp.mpf("2"), mp.mpf("2")),
]

for alpha, xi in tests:
    K = tail_constant(alpha, xi)
    # Large-x tail ratios.
    x = mp.mpf("160")/xi
    sr = apt_survival(x,xi,alpha)/(K*x*mp.e**(-xi*x))
    dr = apt_density(x,xi,alpha)/(xi*K*x*mp.e**(-xi*x))
    hz = apt_density(x,xi,alpha)/apt_survival(x,xi,alpha)
    assert abs(sr-1) < mp.mpf("0.03")
    assert abs(dr-1) < mp.mpf("0.03")
    assert abs(hz/xi-1) < mp.mpf("0.03")

    # At the MGF boundary, the density integrand is asymptotically linear.
    br = mp.e**(xi*x)*apt_density(x,xi,alpha)/(xi*K*x)
    assert abs(br-1) < mp.mpf("0.03")

# Below the boundary the density integrand decays exponentially.
alpha = mp.mpf("2.5")
xi = mp.mpf("1.2")
t = mp.mpf("0.7")
v1 = mp.e**(t*50)*apt_density(mp.mpf("50"),xi,alpha)
v2 = mp.e**(t*80)*apt_density(mp.mpf("80"),xi,alpha)
assert v2 < v1

print("VERIFY_OK")
for alpha, xi in tests:
    K = tail_constant(alpha,xi)
    x = mp.mpf("160")/xi
    print("alpha", mp.nstr(alpha,8), "xi", mp.nstr(xi,8),
          "survival_ratio", mp.nstr(apt_survival(x,xi,alpha)/(K*x*mp.e**(-xi*x)),20),
          "density_ratio", mp.nstr(apt_density(x,xi,alpha)/(xi*K*x*mp.e**(-xi*x)),20),
          "hazard_over_xi", mp.nstr((apt_density(x,xi,alpha)/apt_survival(x,xi,alpha))/xi,20))
