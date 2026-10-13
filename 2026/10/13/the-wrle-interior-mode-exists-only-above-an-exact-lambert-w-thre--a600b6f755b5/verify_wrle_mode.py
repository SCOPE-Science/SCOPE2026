import mpmath as mp

mp.mp.dps = 70

def density(theta, alpha, beta):
    a = mp.mpf(alpha); b = mp.mpf(beta); th = mp.mpf(theta)
    x = 2*mp.pi*a*b
    C = a*a*b / ((1+a)*(1-mp.e**(-x)))
    K = 2*mp.pi*b*mp.e**(-x)/(1-mp.e**(-x))
    return C*mp.e**(-a*b*th)*(1+b*th+K)

def sign_factor(theta, alpha, beta):
    a = mp.mpf(alpha); b = mp.mpf(beta); th = mp.mpf(theta)
    x = 2*mp.pi*a*b
    K = 2*mp.pi*b*mp.e**(-x)/(1-mp.e**(-x))
    return 1-a*(1+b*th+K)

def derivative(theta, alpha, beta):
    a = mp.mpf(alpha); b = mp.mpf(beta); th = mp.mpf(theta)
    x = 2*mp.pi*a*b
    pref = a*a*b*b*mp.e**(-a*b*th)/((1+a)*(1-mp.e**(-x)))
    return pref*sign_factor(th,a,b)

def theta0(alpha,beta):
    a=mp.mpf(alpha); b=mp.mpf(beta)
    x=2*mp.pi*a*b
    return (1-a)/(a*b)-2*mp.pi/(mp.e**x-1)

def xcrit(alpha):
    a=mp.mpf(alpha)
    assert 0<a<1
    c=1-a
    return -mp.lambertw(-c*mp.e**(-c),-1)-c

def betacrit(alpha):
    a=mp.mpf(alpha)
    return xcrit(a)/(2*mp.pi*a)

# Normalization and analytic derivative.
for a,b in [(mp.mpf("0.5"),mp.mpf("0.2")),
            (mp.mpf("0.5"),mp.mpf("0.5")),
            (mp.mpf("2"),mp.mpf("1")),
            (mp.mpf("0.1"),mp.mpf("2"))]:
    mass = mp.quad(lambda t: density(t,a,b), [0,2*mp.pi])
    assert abs(mass-1) < mp.mpf("1e-55")
    for th in [mp.mpf("0.1"), mp.mpf("1.3"), mp.mpf("5.8")]:
        num = mp.diff(lambda z: density(z,a,b), th)
        ana = derivative(th,a,b)
        assert abs(num-ana) < mp.mpf("1e-55")

# Sharp root and Lambert-W formula.
a = mp.mpf("0.5")
xc = xcrit(a)
bc = betacrit(a)
assert abs((1-a)*(mp.e**xc-1)-xc) < mp.mpf("1e-60")
assert abs(bc-mp.mpf("0.3999344750155586220714446513914644")) < mp.mpf("1e-34")

# Below threshold: decreasing.
b = mp.mpf("0.2")
assert b < bc
assert theta0(a,b) < 0
for j in range(401):
    th = 2*mp.pi*j/401
    assert derivative(th,a,b) < 0

# Above threshold: exactly one sign change at theta0.
b = mp.mpf("0.5")
t0 = theta0(a,b)
assert 0 < t0 < 2*mp.pi
assert derivative(t0/2,a,b) > 0
assert abs(derivative(t0,a,b)) < mp.mpf("1e-60")
assert derivative((t0+2*mp.pi)/2,a,b) < 0
assert abs(t0-mp.mpf("0.35107660300878218416517852439316")) < mp.mpf("1e-31")

# Source-displayed alpha=2, beta=1: stationary point lies outside support.
a2=mp.mpf("2"); b2=mp.mpf("1")
t02=theta0(a2,b2)
assert t02 < 0
assert abs(t02-mp.mpf("-0.50002191169466721830953191642627")) < mp.mpf("1e-31")
for j in range(401):
    th = 2*mp.pi*j/401
    assert derivative(th,a2,b2) < 0

# Positive stationary points are inside the support over representative alpha values.
for a in [mp.mpf("0.1"),mp.mpf("0.3"),mp.mpf("0.7"),mp.mpf("0.9")]:
    bc=betacrit(a)
    for factor in [mp.mpf("1.01"),mp.mpf("2"),mp.mpf("10")]:
        t=theta0(a,bc*factor)
        assert 0<t<2*mp.pi

print("VERIFY_OK")
print("beta_c_alpha_half", mp.nstr(betacrit(mp.mpf("0.5")), 40))
print("theta0_alpha_half_beta_point2", mp.nstr(theta0(mp.mpf("0.5"),mp.mpf("0.2")), 40))
print("theta0_alpha_half_beta_point5", mp.nstr(theta0(mp.mpf("0.5"),mp.mpf("0.5")), 40))
print("theta0_alpha2_beta1", mp.nstr(theta0(mp.mpf("2"),mp.mpf("1")), 40))
