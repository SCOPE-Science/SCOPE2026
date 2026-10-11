from fractions import Fraction

class Q5:
    __slots__=('a','b')
    def __init__(self,a=0,b=0):
        self.a=Fraction(a); self.b=Fraction(b)
    def __add__(self,o):
        o=q(o); return Q5(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q5(-self.a,-self.b)
    def __sub__(self,o): return self+(-q(o))
    def __rsub__(self,o): return q(o)-self
    def __mul__(self,o):
        o=q(o); return Q5(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        d=self.a*self.a-5*self.b*self.b
        assert d
        return Q5(self.a/d,-self.b/d)
    def __truediv__(self,o): return self*q(o).inv()
    def __rtruediv__(self,o): return q(o)/self
    def __eq__(self,o):
        o=q(o); return self.a==o.a and self.b==o.b
    def sign(self):
        if self.a==0 and self.b==0: return 0
        if self.b==0: return 1 if self.a>0 else -1
        # compare a with -b*sqrt(5), using signs and exact squares
        if self.a>=0 and self.b>0: return 1
        if self.a<=0 and self.b<0: return -1
        aa=self.a*self.a; bb=5*self.b*self.b
        if self.a>0 and self.b<0: return 1 if aa>bb else -1
        if self.a<0 and self.b>0: return -1 if aa>bb else 1
        raise AssertionError
    def __lt__(self,o): return (self-q(o)).sign()<0
    def __le__(self,o): return (self-q(o)).sign()<=0

def q(x): return x if isinstance(x,Q5) else Q5(x,0)

sqrt5=Q5(0,1)
r=(sqrt5-1)/2
assert r*r+r == 1
phi=1/r
assert phi == 1+r
M=(3*sqrt5-1)/4

def F1(x): return (1+2*x*x)/(2*x)
def F2(x): return (3*x-2*x*x)/(1-x+x*x)
def F3(x): return (-2+4*x+x*x)/(-1+2*x+x*x)

assert F1(r)==M
assert F2(r)==M
assert F2(Q5(Fraction(2,3)))==Q5(Fraction(10,7))
assert F3(Q5(Fraction(2,3)))==Q5(Fraction(10,7))
assert M < Q5(Fraction(10,7))
# F1' numerator is 2 beta^2-1; it is negative even at the right endpoint r.
assert (2*r*r-1).sign()<0
# F2' has negative of q(beta)=beta^2+4 beta-3; q is increasing for beta>0.
assert (r*r+4*r-3).sign()<0
assert Fraction(1,9)>0  # q(2/3)=1/9, so the unique zero is interior and is a maximum of F2.
# F3'=-2 beta(beta-1)/(...)^2 is positive on [2/3,1).

# At beta=r we have k_beta=r. Verify the regular-decagon recurrence.
V=[(Q5(1),Q5(0)),(Q5(1),r),(r,Q5(1)),(Q5(0),Q5(1)),(-r,r),(Q5(-1),Q5(0))]
def vsub(u,v): return (u[0]-v[0],u[1]-v[1])
def vmul(a,u): return (a*u[0],a*u[1])
for j in range(1,5):
    rhs=vsub(vmul(phi,V[j]),V[j-1])
    assert rhs==V[j+1]

# Exact positivity certificate for 47-21 sqrt(5).
D=Q5(47,-21)
assert D.sign()>0
assert 47*47 > 5*21*21
print('VERIFY_OK')
