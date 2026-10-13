from fractions import Fraction
import math

def direct_round(x, b1, b2, t1, t2):
    # Normalize a=1 and eta=1. Each client reaches its local minimizer
    # after its first gradient step and then has zero gradient.
    grads1 = [x-b1] + [Fraction(0,1)]*(t1-1)
    grads2 = [x-b2] + [Fraction(0,1)]*(t2-1)
    d1 = sum(grads1, Fraction(0,1)) / t1
    d2 = sum(grads2, Fraction(0,1)) / t2
    tau_eff = Fraction(t1+t2, 2)
    return x - tau_eff * (d1+d2) / 2

def closed_round(x, b1, b2, t1, t2):
    M = -Fraction((t1-t2)**2, 4*t1*t2)
    xf = Fraction(t2*b1+t1*b2, t1+t2)
    return xf + M*(x-xf)

# Direct source-form reconstruction equals the closed map.
for t1 in range(1, 15):
    for t2 in range(1, 15):
        for x in (Fraction(-7,3), Fraction(0,1), Fraction(11,5)):
            for b1,b2 in ((Fraction(-1,1),Fraction(1,1)),
                          (Fraction(2,3),Fraction(-5,4))):
                assert direct_round(x,b1,b2,t1,t2) == closed_round(x,b1,b2,t1,t2)

# Exact integer stability classification agrees with the continuous threshold.
lo = 3.0 - 2.0*math.sqrt(2.0)
hi = 3.0 + 2.0*math.sqrt(2.0)
for t1 in range(1, 100):
    for t2 in range(1, 100):
        M = -Fraction((t1-t2)**2, 4*t1*t2)
        q = t2/t1
        stable_exact = abs(M) < 1
        stable_ratio = lo < q < hi
        assert stable_exact == stable_ratio

# First 1:m unstable pair.
assert all(abs(Fraction((1-m)**2,4*m)) < 1 for m in range(1,6))
assert abs(Fraction((1-6)**2,4*6)) > 1

# Exact 1:6 witness with shifted local minima.
t1,t2 = 1,6
b1,b2 = Fraction(-1,1), Fraction(1,1)
M = -Fraction((t1-t2)**2,4*t1*t2)
xf = Fraction(t2*b1+t1*b2,t1+t2)
xglobal = Fraction(b1+b2,2)
assert M == Fraction(-25,24)
assert xf == Fraction(-5,7)
assert xglobal == 0

# Relative error expands by exactly 25/24 every round and alternates.
x = Fraction(0,1)
for _ in range(8):
    e = x-xf
    xn = direct_round(x,b1,b2,t1,t2)
    en = xn-xf
    assert en == M*e
    x = xn

# A stable imbalanced case still has a displaced fixed point.
t1,t2 = 1,5
M = -Fraction((t1-t2)**2,4*t1*t2)
xf = Fraction(t2*b1+t1*b2,t1+t2)
assert M == Fraction(-4,5)
assert xf == Fraction(-2,3)
assert abs(M) < 1
assert xf != xglobal

print("verification passed")
