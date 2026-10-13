import mpmath as mp

mp.mp.dps = 80
a0 = mp.pi/2

def survival(x, alpha, theta):
    u = mp.e**(-(x**alpha))
    return 1 - mp.sinh(a0*(1-u)**theta)/mp.sinh(a0)

def density(x, alpha, theta):
    u = mp.e**(-(x**alpha))
    return (
        a0*alpha*theta/mp.sinh(a0)
        * x**(alpha-1)
        * u
        * (1-u)**(theta-1)
        * mp.cosh(a0*(1-u)**theta)
    )

def C(theta):
    return a0*theta*mp.coth(a0)

# Tail, density, and hazard equivalents on all three alpha regimes.
tests = [
    (mp.mpf("0.5"), mp.mpf("0.7"), mp.mpf("2500")),
    (mp.mpf("1.0"), mp.mpf("2.0"), mp.mpf("45")),
    (mp.mpf("2.0"), mp.mpf("3.0"), mp.mpf("7")),
]
for alpha, theta, x in tests:
    s = survival(x,alpha,theta)
    f = density(x,alpha,theta)
    base = mp.e**(-(x**alpha))
    sr = s/(C(theta)*base)
    fr = f/(C(theta)*alpha*x**(alpha-1)*base)
    hr = (f/s)/(alpha*x**(alpha-1))
    assert abs(sr-1) < mp.mpf("5e-8"), (alpha,theta,sr)
    assert abs(fr-1) < mp.mpf("5e-8"), (alpha,theta,fr)
    assert abs(hr-1) < mp.mpf("5e-8"), (alpha,theta,hr)

# Long-tail ratio for alpha<1.
alpha=mp.mpf("0.5")
theta=mp.mpf("1.3")
y=mp.mpf("2")
r1=survival(mp.mpf("10000")+y,alpha,theta)/survival(mp.mpf("10000"),alpha,theta)
assert abs(r1-1) < mp.mpf("0.02")

# Terminal hazard directions.
h_sub=density(mp.mpf("2500"),mp.mpf("0.5"),1)/survival(mp.mpf("2500"),mp.mpf("0.5"),1)
h_crit=density(mp.mpf("45"),1,1)/survival(mp.mpf("45"),1,1)
h_super=density(mp.mpf("7"),2,1)/survival(mp.mpf("7"),2,1)
assert h_sub < mp.mpf("0.02")
assert abs(h_crit-1) < mp.mpf("1e-8")
assert h_super > 10

print("VERIFY_OK")
print("tail_constant_theta_1", mp.nstr(C(1),30))
print("hazards", mp.nstr(h_sub,20), mp.nstr(h_crit,20), mp.nstr(h_super,20))
