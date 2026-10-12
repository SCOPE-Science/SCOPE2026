import mpmath as mp

mp.mp.dps = 70

def G(x, shape):
    x = mp.mpf(x); shape = mp.mpf(shape)
    return mp.gammainc(shape, 0, x) / mp.gamma(shape)

def cdf(t, sigma, alpha, q):
    t=mp.mpf(t); sigma=mp.mpf(sigma); alpha=mp.mpf(alpha); q=mp.mpf(q)
    a=alpha/2
    return G(t/(2*sigma),a) - (2*sigma/t)**q * mp.gamma(a+q)/mp.gamma(a) * G(t/(2*sigma),a+q)

def density(t, sigma, alpha, q):
    t=mp.mpf(t); sigma=mp.mpf(sigma); alpha=mp.mpf(alpha); q=mp.mpf(q)
    a=alpha/2
    return q*(2*sigma)**q * mp.gamma(a+q)/mp.gamma(a) * t**(-q-1) * G(t/(2*sigma),a+q)

def survival_correct(t, sigma, alpha, q):
    t=mp.mpf(t); sigma=mp.mpf(sigma); alpha=mp.mpf(alpha); q=mp.mpf(q)
    a=alpha/2
    term=(2*sigma/t)**q * mp.gamma(a+q)/mp.gamma(a) * G(t/(2*sigma),a+q)
    return 1-G(t/(2*sigma),a)+term

def survival_printed(t, sigma, alpha, q):
    t=mp.mpf(t); sigma=mp.mpf(sigma); alpha=mp.mpf(alpha); q=mp.mpf(q)
    a=alpha/2
    term=(2*sigma/t)**q * mp.gamma(a+q)/mp.gamma(a) * G(t/(2*sigma),a+q)
    return 1-G(t/(2*sigma),a)-term

def hazard_correct(t,sigma,alpha,q):
    return density(t,sigma,alpha,q)/survival_correct(t,sigma,alpha,q)

def hazard_printed(t,sigma,alpha,q):
    return density(t,sigma,alpha,q)/survival_printed(t,sigma,alpha,q)

# Algebraic/numerical consistency of the published CDF, density, and corrected survival.
tests = [
    (mp.mpf("0.3"),mp.mpf("0.7"),mp.mpf("1.2"),mp.mpf("0.8")),
    (mp.mpf("2"),mp.mpf("1"),mp.mpf("3"),mp.mpf("1")),
    (mp.mpf("5"),mp.mpf("2"),mp.mpf("4.5"),mp.mpf("3")),
    (mp.mpf("12"),mp.mpf("0.4"),mp.mpf("6"),mp.mpf("5")),
]
for t,sigma,alpha,q in tests:
    assert abs((1-cdf(t,sigma,alpha,q))-survival_correct(t,sigma,alpha,q)) < mp.mpf("1e-60")
    fd = mp.diff(lambda u: cdf(u,sigma,alpha,q), t)
    assert abs(fd-density(t,sigma,alpha,q)) < mp.mpf("1e-50")
    assert survival_correct(t,sigma,alpha,q) > 0
    assert density(t,sigma,alpha,q) > 0

# Table 1 reproduction for sigma=1, alpha=3.
expected = {
    1:[mp.mpf("0.362"),mp.mpf("0.296"),mp.mpf("0.249")],
    5:[mp.mpf("0.096"),mp.mpf("0.050"),mp.mpf("0.027")],
    10:[mp.mpf("0.067"),mp.mpf("0.031"),mp.mpf("0.014")],
}
for q,row in expected.items():
    vals=[survival_correct(t,1,3,q) for t in [8,10,12]]
    for v,e in zip(vals,row):
        assert abs(v-e) < mp.mpf("0.0006")

# Decisive source example.
sp8 = survival_printed(8,1,3,1)
sc8 = survival_correct(8,1,3,1)
hp8 = hazard_printed(8,1,3,1)
hc8 = hazard_correct(8,1,3,1)
assert abs(sc8-mp.mpf("0.36242334534758550076")) < mp.mpf("1e-19")
assert abs(sp8-mp.mpf("-0.270399933969123")) < mp.mpf("1e-15")
assert abs(hc8-mp.mpf("0.109130538816041")) < mp.mpf("1e-15")
assert abs(hp8-mp.mpf("-0.146270209377384")) < mp.mpf("1e-15")

root = mp.findroot(lambda t: survival_printed(t,1,3,1), (3,4))
assert abs(root-mp.mpf("3.48777992428690682196")) < mp.mpf("1e-19")
assert hazard_printed(20,1,3,1) < 0
assert hazard_correct(20,1,3,1) > 0

# Tail laws.
for sigma,alpha,q in [(1,3,1),(1,3,5),(mp.mpf("0.7"),mp.mpf("2.4"),mp.mpf("2.2"))]:
    a=mp.mpf(alpha)/2
    C=(2*mp.mpf(sigma))**mp.mpf(q)*mp.gamma(a+mp.mpf(q))/mp.gamma(a)
    t=mp.mpf("1e5")
    assert abs((t**q)*survival_correct(t,sigma,alpha,q)/C-1) < mp.mpf("1e-12")
    assert abs(t*hazard_correct(t,sigma,alpha,q)/q-1) < mp.mpf("1e-12")

print("VERIFY_OK")
print("S_correct_8", mp.nstr(sc8, 35))
print("S_printed_8", mp.nstr(sp8, 35))
print("h_correct_8", mp.nstr(hc8, 35))
print("h_printed_8", mp.nstr(hp8, 35))
print("printed_survival_zero", mp.nstr(root, 35))
