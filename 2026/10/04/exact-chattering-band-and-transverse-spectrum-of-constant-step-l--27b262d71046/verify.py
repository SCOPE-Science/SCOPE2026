import math, random

def sign(z):
    return 1.0 if z > 0.0 else (-1.0 if z < 0.0 else 0.0)

def step(x, mprev, lam, eta, b1, b2):
    c = b1*mprev + (1.0-b1)*lam*x
    xn = x - eta*sign(c)
    m = b2*mprev + (1.0-b2)*lam*x
    return xn, m, c

def cycle_state(a, lam, eta, b2):
    mA = lam*(a-eta/(1.0+b2))
    mB = lam*(a-b2*eta/(1.0+b2))
    return mA, mB

# Exact family for representative parameters.
for b1,b2 in ((0.0,0.0),(0.2,0.4),(0.5,0.8),(0.9,0.99)):
    assert 2.0*b1 < 1.0+b2
    lo = b1/(1.0+b2)
    hi = 1.0-lo
    for frac in (0.1,0.5,0.9):
        a_frac = lo + frac*(hi-lo)
        for lam in (0.1,1.0,17.0):
            eta = 0.037
            a = a_frac*eta
            mA,mB = cycle_state(a,lam,eta,b2)
            xB,mB2,cA = step(a,mA,lam,eta,b1,b2)
            xA,mA2,cB = step(xB,mB2,lam,eta,b1,b2)
            assert cA > 0.0 and cB < 0.0
            assert abs(xB-(a-eta)) < 1e-14
            assert abs(xA-a) < 1e-14
            assert abs(mB2-mB) < 1e-13
            assert abs(mA2-mA) < 1e-13

# The interval exists exactly under the claimed inequality.
for _ in range(10000):
    b1 = random.random()
    b2 = random.random()
    lo = b1/(1.0+b2)
    hi = 1.0-lo
    assert (lo < hi) == (2.0*b1 < 1.0+b2)

# Transverse two-step contraction.
for b1,b2 in ((0.2,0.7),(0.9,0.99)):
    eta=0.1
    lam=3.0
    lo=b1/(1.0+b2)
    hi=1.0-lo
    a=eta*(lo+hi)/2.0
    mA,_=cycle_state(a,lam,eta,b2)
    for delta in (1e-10,1e-8,1e-6):
        x1,m1,c1=step(a,mA+delta,lam,eta,b1,b2)
        x2,m2,c2=step(x1,m1,lam,eta,b1,b2)
        assert c1 > 0.0 and c2 < 0.0
        assert abs(x2-a) < 1e-14
        ratio=(m2-mA)/delta
        assert abs(ratio-b2*b2) < 2e-7

# Average objective floor.
lam=5.0
eta=0.02
for a_frac in (0.1,0.25,0.5,0.75,0.9):
    a=a_frac*eta
    avg=lam*(a*a+(a-eta)*(a-eta))/4.0
    closed=lam*(a-eta/2.0)**2/2.0 + lam*eta*eta/8.0
    assert abs(avg-closed) < 1e-18
    assert avg >= lam*eta*eta/8.0 - 1e-18

# Published default coefficients.
b1=0.9
b2=0.99
lo=b1/(1.0+b2)
hi=1.0-lo
assert abs(lo-0.4522613065326633) < 1e-15
assert abs(hi-0.5477386934673367) < 1e-15
assert lo < 0.5 < hi
assert abs(b2*b2-0.9801) < 1e-15

print("verification passed")
