from fractions import Fraction as F

class Q5:
    __slots__=('a','b')
    def __init__(self,a=0,b=0): self.a=F(a); self.b=F(b)
    def __add__(self,o):
        o=o if isinstance(o,Q5) else Q5(o); return Q5(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q5(-self.a,-self.b)
    def __sub__(self,o): return self+(- (o if isinstance(o,Q5) else Q5(o)))
    def __rsub__(self,o): return Q5(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,Q5) else Q5(o)
        return Q5(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=o if isinstance(o,Q5) else Q5(o)
        d=o.a*o.a-5*o.b*o.b
        return Q5((self.a*o.a-5*self.b*o.b)/d,(self.b*o.a-self.a*o.b)/d)
    def __eq__(self,o):
        o=o if isinstance(o,Q5) else Q5(o); return self.a==o.a and self.b==o.b
    def positive(self):
        if self.b==0: return self.a>0
        if self.a<=0 and self.b<=0: return False
        if self.a>=0 and self.b>=0: return self.a>0 or self.b>0
        if self.a>0 and self.b<0: return self.a*self.a > 5*self.b*self.b
        return 5*self.b*self.b > self.a*self.a
    def __repr__(self): return f'Q5({self.a},{self.b})'

Z=Q5
sqrt5=Z(0,1)
r=(Z(1)+sqrt5)/4
s=(sqrt5-Z(1))/4
A=(Z(5)+3*sqrt5)/10
B=(Z(15)-11*sqrt5)/50
C=(Z(5)-2*sqrt5)/25
assert A*(r+s)==Z(1)+s
assert Z(1)-A-B-C==Z(0)

def padd(p,q):
    n=max(len(p),len(q)); out=[Z(0) for _ in range(n)]
    for i,v in enumerate(p): out[i]=out[i]+v
    for i,v in enumerate(q): out[i]=out[i]+v
    return out
def pmul(p,q):
    out=[Z(0) for _ in range(len(p)+len(q)-1)]
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j]=out[i+j]+a*b
    return out
def pscale(p,c): return [v*c for v in p]

def ppow(p,n):
    out=[Z(1)]
    for _ in range(n): out=pmul(out,p)
    return out

# T = 1 + A*x + B*T3 + C*T7
T3=[Z(0),Z(-3),Z(0),Z(4)]
T7=[Z(0),Z(-7),Z(0),Z(56),Z(0),Z(-112),Z(0),Z(64)]
T=padd([Z(1),A],padd(pscale(T3,B),pscale(T7,C)))
R=[(Z(25)+5*sqrt5)/32, -(Z(1)+sqrt5/2), (Z(7)+7*sqrt5)/8, -(Z(3)+sqrt5)/2, Z(1)]
K=Z(64,F(-128,25))  # 64/5 - 128 sqrt(5)/25 corrected next line
K=Z(F(64,5),F(-128,25))
rhs=pscale(pmul(pmul([Z(1),Z(1)],ppow([r,Z(1)],2)),R),K)
assert len(T)==len(rhs) and all(a==b for a,b in zip(T,rhs))

# Degree-five Bernstein coefficients of R(2y-1), from exact power-to-Bernstein conversion.
q=[
 (Z(165)+65*sqrt5)/32,
 (Z(21)+17*sqrt5)/32,
 (Z(113)-3*sqrt5)/160,
 (Z(145)-3*sqrt5)/160,
 (Z(9)+21*sqrt5)/160,
 (Z(5)+sqrt5)/32,
]
assert all(v.positive() for v in q)

# Reconstruct Bernstein polynomial and compare with R(2y-1).
from math import comb
bern=[Z(0) for _ in range(6)]
for k,qk in enumerate(q):
    # qk * C(5,k) y^k (1-y)^(5-k)
    for j in range(5-k+1):
        bern[k+j]=bern[k+j] + qk*comb(5,k)*comb(5-k,j)*((-1)**j)
# Substitute x=2y-1 in R exactly.
sub=[Z(-1),Z(2)]
power=[Z(1)]
Ry=[Z(0)]
for coeff in R:
    Ry=padd(Ry,pscale(power,coeff)); power=pmul(power,sub)
Ry += [Z(0)]*(6-len(Ry))
assert all(a==b for a,b in zip(bern,Ry))

T3p=Z(F(3,2),F(3,2))
T7p=Z(F(-7,2),F(-7,2))
assert T3p-T7p==Z(5,5)
assert A+B*T3p+C*T7p==Z(0)
assert (T3p-T7p).positive()
print('VERIFY_OK exact_upper=1 factorization=1 bernstein_positive=6 uniqueness=1')
