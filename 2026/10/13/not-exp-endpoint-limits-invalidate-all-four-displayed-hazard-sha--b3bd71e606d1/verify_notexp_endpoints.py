import mpmath as mp

mp.mp.dps = 90

def v(y,theta):
    return 1-mp.e**(-theta*y)

def cdf(y,alpha,gamma,theta):
    vv=v(y,theta)
    return (((1+alpha)*vv)/(alpha+vv))**gamma

def pdf(y,alpha,gamma,theta):
    vv=v(y,theta)
    return alpha*gamma*theta*(1+alpha)**gamma*mp.e**(-theta*y)*vv**(gamma-1)/(alpha+vv)**(gamma+1)

def hazard(y,alpha,gamma,theta):
    return pdf(y,alpha,gamma,theta)/(1-cdf(y,alpha,gamma,theta))

def small_asym(y,alpha,gamma,theta):
    C=((1+alpha)*theta/alpha)**gamma
    return gamma*C*y**(gamma-1)

# PDF is derivative of CDF.
for a,g,t,y in [
    (mp.mpf("0.1"),mp.mpf("0.1"),mp.mpf("0.1"),mp.mpf("0.7")),
    (mp.mpf("2.8"),mp.mpf("4.5"),mp.mpf("1.5"),mp.mpf("0.9")),
    (mp.mpf("1.5"),mp.mpf("2.8"),mp.mpf("1.5"),mp.mpf("0.4")),
]:
    d=mp.diff(lambda z: cdf(z,a,g,t),y)
    assert abs(d-pdf(y,a,g,t)) < mp.mpf("1e-65")

# Small-time asymptotic on both sides of gamma=1.
for a,g,t in [
    (mp.mpf("0.1"),mp.mpf("0.1"),mp.mpf("0.1")),
    (mp.mpf("2.5"),mp.mpf("0.9"),mp.mpf("3.2")),
    (mp.mpf("1.2"),mp.mpf("1"),mp.mpf("0.7")),
    (mp.mpf("1.5"),mp.mpf("2.8"),mp.mpf("1.5")),
    (mp.mpf("2.8"),mp.mpf("4.5"),mp.mpf("1.5")),
]:
    y=mp.mpf("1e-60")/t
    ratio=hazard(y,a,g,t)/small_asym(y,a,g,t)
    assert abs(ratio-1) < mp.mpf("2e-6")

# Large-time hazard limit for all four source examples.
examples=[
    ("IHR",mp.mpf("0.1"),mp.mpf("0.1"),mp.mpf("0.1")),
    ("DHR",mp.mpf("2.8"),mp.mpf("4.5"),mp.mpf("1.5")),
    ("BTS",mp.mpf("1.5"),mp.mpf("2.8"),mp.mpf("1.5")),
    ("UBTS",mp.mpf("2.5"),mp.mpf("0.9"),mp.mpf("3.2")),
]
for name,a,g,t in examples:
    y=mp.mpf("80")/t
    rat=hazard(y,a,g,t)/t
    assert abs(rat-1) < mp.mpf("1e-25")

# Endpoint order contradicts the first two global labels.
a,g,t=mp.mpf("0.1"),mp.mpf("0.1"),mp.mpf("0.1")
assert hazard(mp.mpf("1e-10"),a,g,t) > 100*t
a,g,t=mp.mpf("2.8"),mp.mpf("4.5"),mp.mpf("1.5")
assert hazard(mp.mpf("1e-6"),a,g,t) < mp.mpf("1e-10")*t

print("VERIFY_OK")
for name,a,g,t in examples:
    ysmall=mp.mpf("1e-10")/t
    ylarge=mp.mpf("50")/t
    print(name,
          "h_small",mp.nstr(hazard(ysmall,a,g,t),25),
          "h_large",mp.nstr(hazard(ylarge,a,g,t),25),
          "theta",mp.nstr(t,12))
