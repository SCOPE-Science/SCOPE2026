from fractions import Fraction
from math import factorial

class I:
    def __init__(self, lo, hi=None):
        if hi is None: hi = lo
        self.lo, self.hi = Fraction(lo), Fraction(hi)
        assert self.lo <= self.hi
    def __add__(self, other):
        other = asI(other); return I(self.lo + other.lo, self.hi + other.hi)
    __radd__ = __add__
    def __neg__(self): return I(-self.hi, -self.lo)
    def __sub__(self, other): return self + (-asI(other))
    def __rsub__(self, other): return asI(other) - self
    def __mul__(self, other):
        other = asI(other)
        vals = [self.lo*other.lo, self.lo*other.hi, self.hi*other.lo, self.hi*other.hi]
        return I(min(vals), max(vals))
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = asI(other)
        assert not (other.lo <= 0 <= other.hi)
        return self * I(1/other.hi, 1/other.lo)
    def __rtruediv__(self, other): return asI(other) / self

def asI(x): return x if isinstance(x, I) else I(x)

def alt_sin_bounds(x, even_index=8):
    assert 0 < x < 1 and even_index % 2 == 0
    def partial(N):
        s = Fraction(0)
        for n in range(N+1):
            s += (-1 if n % 2 else 1) * x**(2*n+1) / factorial(2*n+1)
        return s
    return I(partial(even_index+1), partial(even_index))

def alt_cos_bounds(x, even_index=8):
    assert 0 < x < 1 and even_index % 2 == 0
    def partial(N):
        s = Fraction(0)
        for n in range(N+1):
            s += (-1 if n % 2 else 1) * x**(2*n) / factorial(2*n)
        return s
    return I(partial(even_index+1), partial(even_index))

def alt_atan_bounds(x, even_index):
    assert 0 < x < 1 and even_index % 2 == 0
    def partial(N):
        s = Fraction(0)
        for n in range(N+1):
            s += (-1 if n % 2 else 1) * x**(2*n+1) / (2*n+1)
        return s
    return I(partial(even_index+1), partial(even_index))

m0 = Fraction(15,16)
m = I(m0)
S = alt_sin_bounds(m0)
C = alt_cos_bounds(m0)
half = I(Fraction(1,2))

k = C*C/(2*S*S)
q = 2*S/(m + S*C)
sin2 = 2*S*C
cos2 = 1 - 2*S*S
sin3 = S*(3 - 4*S*S)
sin4 = 4*S*C*(1 - 2*S*S)
Iaa = 2*m - sin2
Iab = 2*m*C - Fraction(7,2)*S + half*sin3
Ibb = -half*m*cos2 + Fraction(1,4)*m + Fraction(1,4)*sin2 - Fraction(1,16)*sin4
const = m/2 + sin2/4
C2 = Iaa + q*Iab + q*q*Ibb
C1 = 2*k*Iaa + k*q*Iab
C0 = k*k*Iaa + const
B = 1 - q*C
assert B.lo > 0

eps_star = (half-k)/B
assert eps_star.lo > Fraction(7,10) and eps_star.hi < Fraction(71,100)

# On 0 <= epsilon <= eps_star, r(theta) lies between the center and endpoint values.
r_center_at_star = k + eps_star*(1-q)
r_end_at_star = k + eps_star*(1-q*C)
assert r_center_at_star.lo > Fraction(17,100)
assert r_end_at_star.lo <= Fraction(1,2) <= r_end_at_star.hi

# Area is C0 + C1*epsilon + C2*epsilon^2.  Since C2<0, its derivative decreases.
assert C2.hi < 0
d_at_star = C1 + 2*C2*eps_star
assert d_at_star.lo > Fraction(16,1000)

area_star = C0 + C1*eps_star + C2*eps_star*eps_star
assert area_star.lo > Fraction(78718,100000)
assert area_star.hi < Fraction(78719,100000)

# Source parameter epsilon=13/20.
eps_source = I(Fraction(13,20))
area_source = C0 + C1*eps_source + C2*eps_source*eps_source
assert area_star.lo - area_source.hi > Fraction(96,100000)

# Machin formula: pi/4 = 4 atan(1/5) - atan(1/239), bounded by alternating series.
a5 = alt_atan_bounds(Fraction(1,5), 6)
a239 = alt_atan_bounds(Fraction(1,239), 2)
pi4 = 4*a5 - a239
assert area_star.lo > pi4.hi

print('VERIFY_OK')
print('epsilon_star_interval', float(eps_star.lo), float(eps_star.hi))
print('area_star_interval', float(area_star.lo), float(area_star.hi))
print('source_area_interval', float(area_source.lo), float(area_source.hi))
print('gain_lower', float(area_star.lo-area_source.hi))
print('derivative_at_endpoint_lower', float(d_at_star.lo))
print('r_center_endpoint_interval', float(r_center_at_star.lo), float(r_center_at_star.hi))
