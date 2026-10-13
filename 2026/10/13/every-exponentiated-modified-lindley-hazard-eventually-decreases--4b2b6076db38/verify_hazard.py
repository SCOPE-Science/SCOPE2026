import mpmath as mp
mp.mp.dps = 100

def baseline_survival(x, theta):
    u = theta*x
    return mp.e**(-u)*(1 + u*mp.e**(-u)/(1+theta))

def baseline_density(x, theta):
    u = theta*x
    return theta*mp.e**(-u)*(1 + (2*u-1)*mp.e**(-u)/(1+theta))

def hazard(x, theta, alpha):
    s = baseline_survival(x, theta)
    f = baseline_density(x, theta)
    ls = mp.log1p(-s)
    den = -mp.expm1(alpha*ls)
    return alpha*f*mp.e**((alpha-1)*ls)/den

def d_ratio_du(u, theta, alpha):
    return mp.diff(lambda z: hazard(z/theta,theta,alpha)/theta, u)

for theta,alpha in [
    (mp.mpf("0.5"),mp.mpf("0.7")),
    (mp.mpf("0.5"),mp.mpf("5.0")),
    (mp.mpf("2.0"),mp.mpf("1.0")),
    (mp.mpf("2.0"),mp.mpf("10.0")),
]:
    u = mp.mpf("20")
    a = 1/(1+theta)
    exact = hazard(u/theta,theta,alpha)/theta
    deriv = d_ratio_du(u,theta,alpha)
    approx = 1 + (a*(u-1)-(alpha-1)/2)*mp.e**(-u)
    dapprox = (a*(2-u)+(alpha-1)/2)*mp.e**(-u)
    scale = u*u*mp.e**(-2*u)
    assert abs(exact-approx) < 2*scale
    assert abs(deriv-dapprox) < 2*scale

for theta,alpha in [
    (mp.mpf("0.4"),mp.mpf("1.0")),
    (mp.mpf("0.4"),mp.mpf("1.5")),
    (mp.mpf("1.5"),mp.mpf("2.0")),
    (mp.mpf("3.0"),mp.mpf("6.0")),
]:
    x0 = mp.mpf("1e-6")/theta
    xt = mp.mpf("30")/theta
    hp0 = mp.diff(lambda z: hazard(z,theta,alpha), x0)
    hpt = mp.diff(lambda z: hazard(z,theta,alpha), xt)
    assert hp0 > 0
    assert hpt < 0
    assert hazard(xt,theta,alpha) > theta

print("VERIFY_OK")
