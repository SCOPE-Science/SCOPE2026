#!/usr/bin/env python3
from fractions import Fraction
from math import sqrt

class Quad:
    """Exact a + b*sqrt(d) with rational a,b and fixed squarefree-like d."""
    __slots__ = ("a","b","d")
    def __init__(self,a=0,b=0,d=0):
        self.a=Fraction(a); self.b=Fraction(b); self.d=int(d)
    def _coerce(self,o):
        if isinstance(o, Quad):
            if self.d == 0: return Quad(self.a, self.b, o.d), o
            if o.d == 0: return self, Quad(o.a, o.b, self.d)
            assert self.d == o.d
            return self,o
        return self, Quad(o,0,self.d)
    def __add__(self,o):
        x,y=self._coerce(o); return Quad(x.a+y.a,x.b+y.b,x.d)
    __radd__=__add__
    def __neg__(self): return Quad(-self.a,-self.b,self.d)
    def __sub__(self,o): return self+(-o if isinstance(o,Quad) else -Fraction(o))
    def __rsub__(self,o): return (-self)+o
    def __mul__(self,o):
        x,y=self._coerce(o)
        return Quad(x.a*y.a+x.b*y.b*x.d, x.a*y.b+x.b*y.a, x.d)
    __rmul__=__mul__
    def __truediv__(self,o):
        x,y=self._coerce(o)
        den=y.a*y.a-y.b*y.b*x.d
        assert den != 0
        return Quad((x.a*y.a-x.b*y.b*x.d)/den,
                    (x.b*y.a-x.a*y.b)/den,x.d)
    def __rtruediv__(self,o):
        return Quad(o,0,self.d)/self
    def __pow__(self,n):
        assert n >= 0
        out=Quad(1,0,self.d); base=self
        while n:
            if n&1: out=out*base
            base=base*base; n//=2
        return out
    def __eq__(self,o):
        x,y=self._coerce(o); return x.a==y.a and x.b==y.b
    def approx(self): return float(self.a)+float(self.b)*sqrt(self.d)
    def __repr__(self): return f"Quad({self.a},{self.b},sqrt({self.d}))"

def F(m, x):
    n = 6
    num = x*x/Fraction(m) - Fraction(8,7)*x + Fraction(m+1,7)
    den = 6*(x*x/Fraction(m) + (1-x)*(1-x)/Fraction(n-m) - Fraction(1,7))
    return num/den

# derivative numerator from exact quadratic numerator/denominator coefficients
def poly_mul(p,q):
    out=[Fraction(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j]+=a*b
    return out
def poly_sub(p,q):
    n=max(len(p),len(q)); out=[Fraction(0)]*n
    for i in range(n):
        out[i]=(p[i] if i<len(p) else 0)-(q[i] if i<len(q) else 0)
    while len(out)>1 and out[-1]==0: out.pop()
    return out
def derivative(p):
    return [Fraction(i)*p[i] for i in range(1,len(p))]
def deriv_num(m):
    # ascending coefficient order
    N=[Fraction(m+1,7), -Fraction(8,7), Fraction(1,m)]
    r=6-m
    # 6*(s^2/m +(1-2s+s^2)/r -1/7)
    D=[6*(Fraction(1,r)-Fraction(1,7)),
       6*(-Fraction(2,r)),
       6*(Fraction(1,m)+Fraction(1,r))]
    return poly_sub(poly_mul(derivative(N),D), poly_mul(N,derivative(D)))

expected = {
    1: (70,6),
    2: (105,18),
    3: (140,36),
    4: (175,60),
    5: (210,90),
}
# Each derivative numerator is a positive rational multiple of
# 119*s^2 - B*s + C.
for m,(B,C) in expected.items():
    p=deriv_num(m)
    target=[Fraction(C),-Fraction(B),Fraction(119)]
    scale=p[2]/target[2]
    assert scale>0
    assert p == [scale*z for z in target]

crit = {
    1: (Quad(Fraction(5,17), Fraction(-1,119),511),
        Quad(Fraction(1,2),Fraction(1,42),511)),
    2: (Quad(Fraction(15,34),Fraction(-3,238),273),
        Quad(Fraction(5,12),Fraction(1,28),273)),
    3: (Quad(Fraction(10,17),Fraction(-2,119),154),
        Quad(Fraction(1,3),Fraction(1,21),154)),
    4: (Quad(Fraction(25,34),Fraction(-1,238),2065),
        Quad(Fraction(1,4),Fraction(1,84),2065)),
}
for m,(x,M) in crit.items():
    B,C=expected[m]
    assert 119*x*x-B*x+C == 0
    assert F(m,x) == M
    xa=x.approx()
    assert 0 < xa < m/7
    # The derivative is positive at zero and negative at the right endpoint,
    # so this smaller root is the unique chamber maximum.
    p0=C
    pend=119*Fraction(m,7)**2-B*Fraction(m,7)+C
    assert p0>0 and pend<0

# m=5 derivative stays positive: its quadratic decreases on [0,5/7]
# and is still positive at the right endpoint.
assert 238*Fraction(5,7)-210 < 0
assert 119*Fraction(5,7)**2-210*Fraction(5,7)+90 == Fraction(5,7)
assert F(5,Fraction(5,7)) == Fraction(7,12)

M1=crit[1][1]; M2=crit[2][1]
# M1 > 1 because sqrt(511)>21.
assert 511 > 21**2
# M1 > M2: 7 + 2*sqrt(511) > 3*sqrt(273).
# Squaring reduces this to 28*sqrt(511)>364, i.e. sqrt(511)>13.
assert 511 > 13**2
# Remaining chamber maxima are below 1.
assert 154 < 14**2
assert 2065 < 63**2
assert Fraction(7,12) < 1

# Equality coordinate and ratio.
t=crit[1][0]
b=(1-t)/5
ratio=t/b
target_ratio=Quad(Fraction(29,11),Fraction(-1,11),511)
assert ratio == target_ratio
assert 0 < t.approx() < 1/7 < b.approx()

# Final volume ratio is 12*M1 = 6 + 2*sqrt(511)/7.
final=12*M1
target_final=Quad(6,Fraction(2,7),511)
assert final == target_final
assert abs(final.approx()-12.45865974597561) < 1e-12

print("VERIFY_OK regular six-simplex reflection maximum")
