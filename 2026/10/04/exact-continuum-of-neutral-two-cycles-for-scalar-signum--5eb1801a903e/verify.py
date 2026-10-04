from fractions import Fraction

def sgn(x):
    return 0 if x == 0 else (1 if x > 0 else -1)

def step(x, m, a, delta, beta):
    m1 = beta*m + (1-beta)*a*x
    x1 = x - delta*sgn(m1)
    return x1, m1

for beta in (Fraction(1,5), Fraction(1,2), Fraction(9,10)):
    a = Fraction(7,3)
    delta = Fraction(5,4)
    lo = beta*delta/(1+beta)
    hi = delta/(1+beta)
    for theta in (Fraction(1,5), Fraction(1,2), Fraction(4,5)):
        u = lo + theta*(hi-lo)
        m0 = a*(u-delta/(1+beta))
        x1, m1 = step(u,m0,a,delta,beta)
        x2, m2 = step(x1,m1,a,delta,beta)
        assert m0 < 0 < m1
        assert x1 == u-delta
        assert x2 == u and m2 == m0

beta = Fraction(3,4)
a = Fraction(2)
delta = Fraction(3)
for u in (beta*delta/(1+beta), delta/(1+beta)):
    m0 = a*(u-delta/(1+beta))
    x1,m1 = step(u,m0,a,delta,beta)
    x2,m2 = step(x1,m1,a,delta,beta)
    assert not (x2 == u and m2 == m0 and x1 != u)

for bnum in range(1,100):
    beta = Fraction(bnum,100)
    a = Fraction(11,7)
    delta = Fraction(13,10)
    lo = beta*delta/(1+beta)
    hi = delta/(1+beta)
    for j in range(1,20):
        u = lo + Fraction(j,20)*(hi-lo)
        m0 = a*(u-delta/(1+beta))
        x1,m1 = step(u,m0,a,delta,beta)
        x2,m2 = step(x1,m1,a,delta,beta)
        assert x2 == u and m2 == m0
        midpoint = u-delta/Fraction(2)
        bound = delta*(1-beta)/(2*(1+beta))
        assert abs(midpoint) < bound

beta = Fraction(4,5)
a = Fraction(3,2)
delta = Fraction(7,5)
lo = beta*delta/(1+beta)
hi = delta/(1+beta)
u = (lo+hi)/2
mstar = a*(u-delta/(1+beta))
eps = Fraction(1,1000)
m = mstar + eps
x1,m1 = step(u,m,a,delta,beta)
x2,m2 = step(x1,m1,a,delta,beta)
assert x2 == u
assert m2-mstar == beta*beta*eps

print("verification passed")
