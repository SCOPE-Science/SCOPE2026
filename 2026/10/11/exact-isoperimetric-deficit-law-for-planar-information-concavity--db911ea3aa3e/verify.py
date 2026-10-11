from fractions import Fraction

NVAR = 8  # A, P, r, q, t0, t1, lam, t
ZERO = (0,) * NVAR

class Poly:
    def __init__(self, terms=None):
        self.d = {m: Fraction(c) for m, c in (terms or {}).items() if c}
    @staticmethod
    def const(c):
        return Poly({ZERO: Fraction(c)})
    @staticmethod
    def var(i):
        m = [0] * NVAR
        m[i] = 1
        return Poly({tuple(m): Fraction(1)})
    def __add__(self, other):
        other = aspoly(other)
        d = dict(self.d)
        for m,c in other.d.items():
            d[m] = d.get(m, Fraction(0)) + c
            if not d[m]: del d[m]
        return Poly(d)
    __radd__ = __add__
    def __neg__(self):
        return Poly({m:-c for m,c in self.d.items()})
    def __sub__(self, other): return self + (-aspoly(other))
    def __rsub__(self, other): return aspoly(other) - self
    def __mul__(self, other):
        other = aspoly(other)
        d = {}
        for m,c in self.d.items():
            for n,e in other.d.items():
                mn = tuple(a+b for a,b in zip(m,n))
                d[mn] = d.get(mn, Fraction(0)) + c*e
        return Poly({m:c for m,c in d.items() if c})
    __rmul__ = __mul__
    def __pow__(self, k):
        assert isinstance(k,int) and k>=0
        out = Poly.const(1); base = self
        while k:
            if k & 1: out = out*base
            base = base*base; k >>= 1
        return out
    def diff(self, i):
        d={}
        for m,c in self.d.items():
            if m[i]:
                mm=list(m); p=mm[i]; mm[i]-=1
                d[tuple(mm)] = d.get(tuple(mm),Fraction(0)) + c*p
        return Poly(d)
    def is_zero(self): return not self.d

def aspoly(x):
    return x if isinstance(x, Poly) else Poly.const(x)

A,P,r,q,t0,t1,lam,t = [Poly.var(i) for i in range(NVAR)]
one = Poly.const(1)

def area(x):
    return A*(one-x)**2 + r*P*x*(one-x) + q*r**2*x**2

def per(x):
    return P*(one-x) + 2*q*r*x

tl = (one-lam)*t0 + lam*t1
Delta = P**2 - 4*q*A

# Clear the three positive perimeter denominators in the exact Jensen identity.
finite = (area(tl)*per(t0)*per(t1)
          - (one-lam)*area(t0)*per(t1)*per(tl)
          - lam*area(t1)*per(t0)*per(tl)
          - q*r**2*Delta*lam*(one-lam)*(t1-t0)**2)
assert finite.is_zero(), f"finite identity failed with {len(finite.d)} residual monomials"

# Clear the cubic denominator in I''(t) = -2*q*r^2*Delta/per(t)^3.
At, Pt = area(t), per(t)
At1, At2 = At.diff(7), At.diff(7).diff(7)
Pt1 = Pt.diff(7)
curvature_num = At2*Pt**2 - 2*(At1*Pt - At*Pt1)*Pt1 + 2*q*r**2*Delta
assert curvature_num.is_zero(), f"curvature identity failed with {len(curvature_num.d)} residual monomials"

print('VERIFY_OK')
print('finite_jensen_identity_residual_monomials=0')
print('second_derivative_identity_residual_monomials=0')
