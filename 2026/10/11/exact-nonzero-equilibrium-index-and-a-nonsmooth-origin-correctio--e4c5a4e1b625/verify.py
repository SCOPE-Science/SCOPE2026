from fractions import Fraction
from math import sqrt

class Qs:
    # a + b*sqrt(13)
    def __init__(self,a=0,b=0):
        self.a=Fraction(a); self.b=Fraction(b)
    def __add__(self,o):
        o=o if isinstance(o,Qs) else Qs(o); return Qs(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Qs(-self.a,-self.b)
    def __sub__(self,o): return self+(- (o if isinstance(o,Qs) else Qs(o)))
    def __rsub__(self,o): return Qs(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,Qs) else Qs(o)
        return Qs(self.a*o.a+13*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def val(self): return float(self.a)+float(self.b)*sqrt(13.0)
    def __eq__(self,o):
        o=o if isinstance(o,Qs) else Qs(o); return self.a==o.a and self.b==o.b

b=Fraction(1,25)
c=Fraction(23,25)
r=Qs(Fraction(-1,2),Fraction(3,10))
assert r*r+r == Qs(c)
alpha=r*(2*r+1)
assert alpha == Qs(Fraction(117,50),Fraction(-3,10))
assert alpha.val()>0
assert b>0 and b<1
routh=[1.0,float(b),alpha.val()*float(b-1)/float(b),alpha.val()]
assert [x>0 for x in routh]==[True,True,False,True]
changes=sum((routh[i]>0)!=(routh[i+1]>0) for i in range(3))
assert changes==2
# one-sided derivative of -|x| at zero
h=1e-8
right=(-abs(h)-0.0)/h
left=(-abs(-h)-0.0)/(-h)
assert right < 0 and left > 0 and abs(right+1)<1e-12 and abs(left-1)<1e-12
# numerical roots of t^3+b t^2+alpha t+alpha via a fixed cubic polynomial check
# Reference values are checked by substitution, not used in the proof.
roots=[complex(-0.719935297443999,0),complex(0.339967648721999,1.27760167336743),complex(0.339967648721999,-1.27760167336743)]
a=float(b); al=alpha.val()
for z in roots:
    residual=z**3+a*z**2+al*z+al
    assert abs(residual)<2e-12, residual
print('VERIFY_OK')
