import mpmath as mp
mp.mp.dps = 80

def A(x, v, theta):
    x=mp.mpf(x); v=mp.mpf(v); theta=mp.mpf(theta)
    return mp.e**(theta*x**v-1/x)

def cdf(x,v,theta):
    a=A(x,v,theta)
    return -mp.expm1(-a)

def density(x,v,theta):
    x=mp.mpf(x); v=mp.mpf(v); theta=mp.mpf(theta)
    a=A(x,v,theta)
    fac=v*theta*x**(v-1)+x**(-2)
    return fac*a*mp.e**(-a)

def hazard(x,v,theta):
    x=mp.mpf(x); v=mp.mpf(v); theta=mp.mpf(theta)
    return (v*theta*x**(v-1)+x**(-2))*A(x,v,theta)

# theta = 0 is defective with total finite-line mass 1-e^-1.
mass0 = 1-mp.e**(-1)
assert abs(cdf(mp.mpf("1e12"), 2, 0)-mass0) < mp.mpf("2e-12")
assert mass0 < 1

# Negative theta: explicit density sign threshold.
for v,theta in [(mp.mpf("1"),mp.mpf("-1")),(mp.mpf("0.5"),mp.mpf("-0.8")),(mp.mpf("2"),mp.mpf("-0.2"))]:
    xc=mp.power(-1/(v*theta), 1/(v+1))
    assert density(xc*mp.mpf("0.9"),v,theta) > 0
    assert abs(density(xc,v,theta)) < mp.mpf("1e-70")
    assert density(xc*mp.mpf("1.1"),v,theta) < 0
    assert cdf(mp.mpf("1e6"),v,theta) < mp.mpf("1e-20")

g1=cdf(1,1,-1)
g10=cdf(10,1,-1)
f10=density(10,1,-1)
assert abs(g1-mp.mpf("0.12657698150688335701096765133746179")) < mp.mpf("1e-18")
assert abs(g10-mp.mpf("0.00004107871147192566483189848744139")) < mp.mpf("1e-19")
assert abs(f10-mp.mpf("-0.0000406670890528032")) < mp.mpf("1e-19")
assert g10 < g1 and f10 < 0

# Positive theta: proper monotonic CDF samples and endpoint hazard pattern.
for v,theta in [(mp.mpf("0.5"),mp.mpf("0.8")),(mp.mpf("1.5"),mp.mpf("2.0")),(1,mp.mpf("0.1"))]:
    xs=[mp.mpf("0.01"),mp.mpf("0.1"),mp.mpf("0.5"),1]
    vals=[cdf(x,v,theta) for x in xs]
    assert all(vals[i] < vals[i+1] for i in range(len(vals)-1))
    assert all(density(x,v,theta)>0 for x in xs)
    assert hazard(mp.mpf("0.01"),v,theta) < mp.mpf("1e-20")
    assert hazard(100,v,theta) > hazard(1,v,theta)

print("VERIFY_OK")
print("theta0_mass", mp.nstr(mass0, 30))
print("negative_G_1", mp.nstr(g1, 30))
print("negative_G_10", mp.nstr(g10, 30))
print("negative_density_10", mp.nstr(f10, 30))
for v,theta in [(mp.mpf("0.5"),mp.mpf("0.8")),(mp.mpf("1.5"),mp.mpf("2.0"))]:
    print("positive_h_0.01", mp.nstr(v,8), mp.nstr(theta,8), mp.nstr(hazard(mp.mpf("0.01"),v,theta),25))
    print("positive_h_100", mp.nstr(v,8), mp.nstr(theta,8), mp.nstr(hazard(100,v,theta),25))
