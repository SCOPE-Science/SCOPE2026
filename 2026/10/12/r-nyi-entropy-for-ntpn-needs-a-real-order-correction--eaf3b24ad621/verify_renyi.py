import mpmath as mp

mp.mp.dps = 60

def renyi_integral_direct(alpha, lam, gamma):
    C = alpha*alpha*(lam*lam + 1) + 2
    pref = C**(-gamma) * (2*mp.pi)**(-gamma/2) * mp.e**(-gamma*lam*lam/2)
    def integrand(x):
        q = (1-alpha*x)**2 + 1
        return q**gamma * mp.e**(-gamma*x*x/2) * mp.cosh(lam*x)**gamma
    return pref * mp.quad(integrand, [-mp.inf, 0, mp.inf])

def renyi_integral_expectation(alpha, lam, gamma):
    C = alpha*alpha*(lam*lam + 1) + 2
    pref = (
        C**(-gamma)
        * (2*mp.pi)**(-gamma/2)
        * mp.e**(-gamma*lam*lam/2)
        * mp.sqrt(2*mp.pi/gamma)
    )
    def normal_density(x):
        return mp.sqrt(gamma/(2*mp.pi))*mp.e**(-gamma*x*x/2)
    def integrand(x):
        q = (1-alpha*x)**2 + 1
        return normal_density(x) * q**gamma * mp.cosh(lam*x)**gamma
    expectation = mp.quad(integrand, [-mp.inf, 0, mp.inf])
    return pref * expectation

def entropy_from_integral(value, gamma):
    return mp.log(value)/(1-gamma)

alpha = mp.mpf("0.7")
lam = mp.mpf("1.2")
for gamma in (mp.mpf("0.5"), mp.mpf("1.5"), mp.mpf("2.3")):
    a = renyi_integral_direct(alpha, lam, gamma)
    b = renyi_integral_expectation(alpha, lam, gamma)
    assert abs(a-b) < mp.mpf("1e-45")
    assert a > 0

for gamma in (mp.mpf("0.5"), mp.mpf("1.5")):
    value = renyi_integral_direct(mp.mpf("0"), mp.mpf("0"), gamma)
    observed = entropy_from_integral(value, gamma)
    exact = mp.log(2*mp.pi)/2 + mp.log(gamma)/(2*(gamma-1))
    assert abs(observed-exact) < mp.mpf("1e-45")

half = mp.mpf("0.5")
normal_half = mp.log(2*mp.pi)/2 + mp.log(half)/(2*(half-1))
assert abs(normal_half - mp.mpf("1.61208571376461805119756185786")) < mp.mpf("1e-28")

print("VERIFY_OK")
print("normal_H_1_2", mp.nstr(normal_half, 35))
print("example_H_1_2", mp.nstr(entropy_from_integral(renyi_integral_direct(alpha, lam, half), half), 35))
