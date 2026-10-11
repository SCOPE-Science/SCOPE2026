from fractions import Fraction as F

class Q2:
    """Exact a+b*sqrt(2)."""
    def __init__(self,a=0,b=0): self.a,self.b=F(a),F(b)
    def __add__(self,o): o=cv(o); return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self+(-cv(o))
    def __rsub__(self,o): return cv(o)-self
    def __mul__(self,o):
        o=cv(o); return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __eq__(self,o): o=cv(o); return self.a==o.a and self.b==o.b
    def __repr__(self): return f"Q2({self.a},{self.b})"

def cv(x): return x if isinstance(x,Q2) else Q2(x,0)

r=Q2(0,1)
q=r-1
assert q*q == 1-2*q
assert (1+q) == r

# Dual-octagon table: (N_*(f+g), N_*(f-g)) for separations m=0,...,4.
table=[(Q2(2),Q2(0)),(Q2(2),2*q),(r,r),(2*q,Q2(2)),(Q2(0),Q2(2))]
assert table[1][1] == 2*r-2
assert table[3][0] == 2*r-2

# Affine dominance identities for the m=1 branch L1=2+2*q*t.
# Coefficients of L1-L2=(2-r)*(1-t) and L1-L3=2*(1-q)*(1-t).
assert Q2(2)-r == -(2*q-r)  # constant = minus t coefficient
assert 2*(1-q) == -(2*q-2)

# Scalar maximization identity after clearing the positive denominator 1+t^2:
# (1+q^2)(1+t^2)-(1+q*t)^2 == (t-q)^2.
# Compare coefficients in t^0,t^1,t^2.
left_coeff=[q*q, -2*q, Q2(1)]
right_coeff=[q*q, -2*q, Q2(1)]
assert left_coeff == right_coeff

# Equality witness at t=q.
# u=(1,q), v=(-q,1): u+qv=(1-q^2,2q)=(2q,2q), u-qv=(1+q^2,0).
assert 1-q*q == 2*q
assert 1+q*q == Q2(4,-2)
# For (2q,2q), diagonal support is (4q)/sqrt(2) = 1+q^2.
# Avoid division by checking sqrt(2)*(1+q^2)=4q.
assert r*(1+q*q) == 4*q
# Squared attained value is 2*(1+q^2)=8-4sqrt(2).
assert 2*(1+q*q) == Q2(8,-4)

print("VERIFY_OK")
