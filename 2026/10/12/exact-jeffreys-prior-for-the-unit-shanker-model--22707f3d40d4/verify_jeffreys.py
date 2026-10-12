import mpmath as mp

mp.mp.dps = 60

def density(t, a):
    return a*a/(a*a+1) * (a+t) * mp.e**(-a*t)

def info_closed(a):
    a = mp.mpf(a)
    return (
        2*(3*a*a+1)/(a*a*(a*a+1)**2)
        + a*a/(a*a+1) * mp.e**(a*a) * mp.e1(a*a)
    )

def info_integral(a):
    a = mp.mpf(a)
    elementary = 2/a**2 + 2*(1-a*a)/(a*a+1)**2
    extra = mp.quad(lambda t: density(t,a)/(a+t)**2, [0, mp.inf])
    return elementary + extra

for a in (mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf("1"), mp.mpf("5")):
    c = info_closed(a)
    q = info_integral(a)
    assert abs(c-q) < mp.mpf("1e-45") * max(1, abs(c))

small = mp.mpf("1e-5") * mp.sqrt(info_closed(mp.mpf("1e-5")))
large = mp.mpf("100") * mp.sqrt(info_closed(mp.mpf("100")))
assert abs(small-mp.sqrt(2)) < mp.mpf("1e-7")
assert abs(large-1) < mp.mpf("3e-4")

# A finite interior check confirms that alpha*sqrt(I(alpha)) is not constant.
mid = mp.sqrt(info_closed(1))
assert abs(mid-small) > mp.mpf("0.05")
assert abs(mid-large) > mp.mpf("0.05")

print("VERIFY_OK")
