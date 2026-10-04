from fractions import Fraction as F
from decimal import Decimal, getcontext

class Qs:
    """u + v*sqrt(230), with exact rational coefficients."""
    __slots__ = ("u", "v")
    def __init__(self, u=0, v=0):
        self.u = F(u)
        self.v = F(v)
    def __add__(self, o):
        o = o if isinstance(o, Qs) else Qs(o)
        return Qs(self.u + o.u, self.v + o.v)
    __radd__ = __add__
    def __neg__(self): return Qs(-self.u, -self.v)
    def __sub__(self, o): return self + (- (o if isinstance(o, Qs) else Qs(o)))
    def __rsub__(self, o): return Qs(o) - self
    def __mul__(self, o):
        o = o if isinstance(o, Qs) else Qs(o)
        return Qs(self.u*o.u + F(230)*self.v*o.v,
                  self.u*o.v + self.v*o.u)
    __rmul__ = __mul__
    def __truediv__(self, q):
        if isinstance(q, Qs):
            den = q.u*q.u - F(230)*q.v*q.v
            return self * Qs(q.u/den, -q.v/den)
        return Qs(self.u/F(q), self.v/F(q))
    def __pow__(self, n):
        if n == 0: return Qs(1)
        if n == 1: return self
        if n == 2: return self*self
        raise ValueError('small nonnegative powers only')
    def __eq__(self, o):
        o = o if isinstance(o, Qs) else Qs(o)
        return self.u == o.u and self.v == o.v
    def dec(self, prec=50):
        getcontext().prec = prec
        su = Decimal(self.u.numerator) / Decimal(self.u.denominator)
        sv = Decimal(self.v.numerator) / Decimal(self.v.denominator)
        return su + sv * Decimal(230).sqrt()

xH = Qs(F(10,197), F(-3,197))
assert F(197)*xH**2 - F(20)*xH - F(10) == 0

cH = xH**2 - xH/F(5)
expected_cH = Qs(F(1776,38809), F(291,194045))
assert cH == expected_cH

A = Qs(1) + F(3,10)*xH**2
C = xH*(F(2)*xH - F(1,5))
assert A/F(10) - C == 0

# Positive large branch: H(x)=1/10+x/5-197*x^2/100.
def Hq(x):
    x = F(x)
    return F(1,10) + x/F(5) - F(197,100)*x*x

assert Hq(F(1,10)) == F(1003,10000)
assert Hq(F(1,5)) == F(153,2500)
assert Hq(F(1,10)) > 0 and Hq(F(1,5)) > 0

v = cH.dec(60)
lo = Decimal('0.06850593165728568')
hi = Decimal('0.06850593165728570')
assert lo < v < hi

print('x_H =', xH.dec(30))
print('c_H =', v)
print('A_H =', A.dec(30))
print('VERIFY_OK')
