from fractions import Fraction as F

class Q2:
    __slots__ = ("a", "b")
    def __init__(self, a=0, b=0):
        self.a = a if isinstance(a, F) else F(a)
        self.b = b if isinstance(b, F) else F(b)
    def __add__(self, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return Q2(self.a + o.a, self.b + o.b)
    __radd__ = __add__
    def __neg__(self): return Q2(-self.a, -self.b)
    def __sub__(self, o): return self + (- (o if isinstance(o, Q2) else Q2(o)))
    def __rsub__(self, o): return Q2(o) - self
    def __mul__(self, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return Q2(self.a*o.a + 2*self.b*o.b, self.a*o.b + self.b*o.a)
    __rmul__ = __mul__
    def inv(self):
        d = self.a*self.a - 2*self.b*self.b
        if d == 0: raise ZeroDivisionError
        return Q2(self.a/d, -self.b/d)
    def __truediv__(self, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return self * o.inv()
    def __pow__(self, n):
        if n < 0: return (self.inv()) ** (-n)
        r, x = Q2(1), self
        while n:
            if n & 1: r = r*x
            x = x*x
            n //= 2
        return r
    def __eq__(self, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return self.a == o.a and self.b == o.b
    def __repr__(self): return f"Q2({self.a},{self.b})"

p_plus = [Q2(F(3,8), F(1,4)), Q2(F(1,4)), Q2(F(3,8), -F(1,4))]
p_minus = [p_plus[2], p_plus[1], p_plus[0]]
beta = [Q2(1), Q2(F(1,2)), Q2(0)]

def projective_update(p):
    mu = sum((p[i]*beta[i] for i in range(3)), Q2(0))
    f = [(mu-beta[i])**4 for i in range(3)]
    z = sum((p[i]*f[i] for i in range(3)), Q2(0))
    return [p[i]*f[i]/z for i in range(3)], mu, z

u1, mu1, z1 = projective_update(p_plus)
u2, mu2, z2 = projective_update(p_minus)
assert sum(p_plus, Q2(0)) == Q2(1)
assert sum(p_minus, Q2(0)) == Q2(1)
assert mu1 == Q2(F(1,2), F(1,4))
assert mu2 == Q2(F(1,2), -F(1,4))
assert u1 == p_minus
assert u2 == p_plus
assert z1 == Q2(F(1,64)) and z2 == Q2(F(1,64))
# Exact positivity of the smaller extreme weight:
assert F(3,8)*F(3,8) > 2*F(1,4)*F(1,4)
# The general two-cycle radial factor and the known (3,2,1) witness.
def Q_factor(m,h):
    return h**4 / (2*m*m-h*h)**2
assert Q_factor(F(2),F(1)) == F(1,49)
# Condition-number expression agrees at kappa=3.
kappa=F(3)
assert (kappa-1)**4/(kappa*kappa+6*kappa+1)**2 == F(1,49)
print("VERIFY_OK")
