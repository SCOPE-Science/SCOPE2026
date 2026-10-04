from fractions import Fraction as F
from decimal import Decimal, getcontext

DIGITS = 40

def root_frac_bounds(x, n=2, digits=DIGITS):
    """Exact decimal-grid enclosure of the positive n-th root of a positive Fraction."""
    scale = 10 ** digits
    target = x.numerator * scale ** n
    den = x.denominator
    lo, hi = 0, 1
    while hi ** n * den <= target:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid ** n * den <= target:
            lo = mid
        else:
            hi = mid
    lower, upper = F(lo, scale), F(lo + 1, scale)
    assert lower ** n <= x <= upper ** n
    return lower, upper

class I:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = F(lo if hi is None else hi)
        assert self.lo <= self.hi
    def __add__(self, other):
        other = as_i(other); return I(self.lo + other.lo, self.hi + other.hi)
    __radd__ = __add__
    def __sub__(self, other):
        other = as_i(other); return I(self.lo - other.hi, self.hi - other.lo)
    def __rsub__(self, other):
        return as_i(other).__sub__(self)
    def __mul__(self, other):
        other = as_i(other)
        vals = [self.lo*other.lo, self.lo*other.hi, self.hi*other.lo, self.hi*other.hi]
        return I(min(vals), max(vals))
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = as_i(other)
        assert other.lo > 0
        return self * I(1/other.hi, 1/other.lo)
    def sqrt(self):
        assert self.lo >= 0
        lo = root_frac_bounds(self.lo, 2)[0]
        hi = root_frac_bounds(self.hi, 2)[1]
        return I(lo, hi)
    def pow_21_10(self):
        assert self.lo >= 0
        lo = root_frac_bounds(self.lo ** 21, 10)[0]
        hi = root_frac_bounds(self.hi ** 21, 10)[1]
        return I(lo, hi)

def as_i(x):
    return x if isinstance(x, I) else I(x)

def shown(x):
    getcontext().prec = 30
    return str(Decimal(x.numerator) / Decimal(x.denominator))

# Explicit counterexample.
h = F(1, 100)
eps = F(3, 2000)
q = (1 - eps) / (1 + eps)
H, E, Q = I(h), I(eps), I(q)
e1 = E * (I(1) + H*H/F(4)).sqrt()
e2 = I(1-eps)/(2*(1+eps)) * I(4*eps*eps + (1-eps)**2*h*h).sqrt()
e3 = I(1-eps)/(2*(1+eps)) * I(4*eps*eps + (1+eps)**2*h*h).sqrt()
r = (I(1+h) - I(1+h*h).sqrt()) / 2
mn = Q * H
ln = ((I(1)-Q)*(I(1)-Q) + H*H/F(4)).sqrt()
lm = ((I(1)-Q)*(I(1)-Q) + (Q*H-H/F(2))*(Q*H-H/F(2))).sqrt()
area = E * I(1-eps) * H / I((1+eps)**2)
rq = area / ((mn + ln + lm)/2)
defect = e1.pow_21_10() + e2.pow_21_10() + e3.pow_21_10() - 2*r.pow_21_10() - (2*rq).pow_21_10()
print("finite_defect_interval", shown(defect.lo), shown(defect.hi))
assert defect.hi < 0

# Normalized h -> 0+ limit for eps=(3/20)h.
c = F(3, 20)
m = I(F(109, 400)).sqrt()  # sqrt(109)/20
t = I(3) / (I(5) + I(34).sqrt())
limit_defect = I(c).pow_21_10() + 2*m.pow_21_10() - 2*I(F(1,2)).pow_21_10() - t.pow_21_10()
print("limit_defect_interval", shown(limit_defect.lo), shown(limit_defect.hi))
assert limit_defect.hi < 0
print("CERTIFIED_NEGATIVE")
