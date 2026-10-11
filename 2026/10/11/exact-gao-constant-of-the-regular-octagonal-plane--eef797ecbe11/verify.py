from fractions import Fraction as F

class Q2:
    """Exact a+b*sqrt(2)."""
    def __init__(self,a=0,b=0): self.a=F(a); self.b=F(b)
    def __add__(self,o): o=coerce(o); return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self+(-coerce(o))
    def __rsub__(self,o): return coerce(o)-self
    def __mul__(self,o):
        o=coerce(o); return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=coerce(o); den=o.a*o.a-2*o.b*o.b
        return Q2((self.a*o.a-2*self.b*o.b)/den,(self.b*o.a-self.a*o.b)/den)
    def __rtruediv__(self,o): return coerce(o)/self
    def __eq__(self,o): o=coerce(o); return self.a==o.a and self.b==o.b
    def __repr__(self): return f"Q2({self.a},{self.b})"

def coerce(x): return x if isinstance(x,Q2) else Q2(x,0)

r=Q2(0,1)
a=r-1
d2=1+a*a
assert d2==Q2(4,-2)
candidate=1/d2
assert candidate==Q2(F(1,2),F(1,4))  # (2+sqrt(2))/4

inv_sqrt2=r/2
n_plus=1+inv_sqrt2
n_minus=inv_sqrt2
objective=(n_plus*n_plus+n_minus*n_minus)/4
assert objective==candidate

# Unit checks for x=(1,0), y=(1/sqrt(2),1/sqrt(2)).
# For y the l1/sqrt(2) branch equals 1 exactly.
assert (inv_sqrt2+inv_sqrt2)/r==1
# Active branches for x+y and x-y reduce to the stated values.
assert (1+inv_sqrt2+inv_sqrt2)/r==n_plus
assert (1-inv_sqrt2+inv_sqrt2)/r==n_minus

# Closest published equality criterion: on [0,1/2], max(phi/phi2)
# is attained only at t=0 or t=1/2; max(phi2/phi) occurs at
# t=1-1/sqrt(2). Neither maximizing t1 satisfies
# (1-t1)(1-t2)=1/2.
t2=1-inv_sqrt2
assert (1-0)*(1-t2)!=F(1,2)
assert (1-F(1,2))*(1-t2)!=F(1,2)

print('VERIFY_OK')
