from fractions import Fraction as F

class Q2:
    """Exact a + b*sqrt(2)."""
    def __init__(self,a=0,b=0): self.a,self.b=F(a),F(b)
    def __add__(self,o): o=co(o); return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self+(-co(o))
    def __rsub__(self,o): return co(o)-self
    def __mul__(self,o):
        o=co(o); return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        d=self.a*self.a-2*self.b*self.b
        if d==0: raise ZeroDivisionError
        return Q2(self.a/d,-self.b/d)
    def __truediv__(self,o): return self*co(o).inv()
    def __eq__(self,o): o=co(o); return self.a==o.a and self.b==o.b
    def sign(self):
        a,b=self.a,self.b
        if b==0: return (a>0)-(a<0)
        if a==0: return (b>0)-(b<0)
        if a>0 and b>0: return 1
        if a<0 and b<0: return -1
        if a<0<b:
            return 1 if 2*b*b>a*a else -1
        if b<0<a:
            return 1 if a*a>2*b*b else -1
        raise AssertionError
    def __repr__(self): return f"{self.a}+({self.b})sqrt2"

def co(x): return x if isinstance(x,Q2) else Q2(x,0)

s=Q2(0,1)
q=s-1
M=2*s-1
half=F(1,2)
inv_s=s*half

# Candidate and tangent-edge witness identities.
assert M == 1 + 2*q
lam=2*q
x1,x2=q,Q2(1)
y1,y2=inv_s,-inv_s
z1,z2=x1+lam*y1,x2+lam*y2
assert z1==1 and z2==q
# N(z)=1 because |z1|=1 and both coordinates are nonnegative with z1+z2=sqrt(2).
assert z1+z2==s

# Vertex branch 1: derivative of the intersection quotient is positive,
# and its endpoint u=q has lambda=1 and value sqrt(2).
d1=4*(-4+3*s)
assert d1.sign()>0
u=q
c=(1-u)/s
lam1=(1-q)/(1-c)
assert lam1==1
assert (1+lam1)/(q+lam1)==s

# Vertex branch 2: derivative is positive.  At u=1/sqrt(2),
# lambda=2q, denominator=1, and the quotient is M.
d2=2*(s-1)
assert d2.sign()>0
u=inv_s
v=s-u
lam2=s/(1+u)
assert lam2==2*q
assert q+v*lam2==1
assert (1+lam2)/(q+v*lam2)==M

# The Hilbert endpoint sqrt(2) is strictly below the octagonal maximum.
assert (M-s).sign()>0
print("VERIFY_OK")
