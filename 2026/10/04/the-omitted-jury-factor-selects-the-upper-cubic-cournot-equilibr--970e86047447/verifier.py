from fractions import Fraction as F

D=70

class S:
    __slots__=("a","b")
    def __init__(self,a=0,b=0): self.a=F(a); self.b=F(b)
    def __add__(self,o):
        o=o if isinstance(o,S) else S(o)
        return S(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return S(-self.a,-self.b)
    def __sub__(self,o): return self+(- (o if isinstance(o,S) else S(o)))
    def __rsub__(self,o): return S(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,S) else S(o)
        return S(self.a*o.a+D*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def sign(self):
        a,b=self.a,self.b
        if b==0: return (a>0)-(a<0)
        if a==0: return (b>0)-(b<0)
        if a>0 and b>0: return 1
        if a<0 and b<0: return -1
        left=a*a; right=D*b*b
        if a>0 and b<0: return (left>right)-(left<right)
        if a<0 and b>0: return (right>left)-(right<left)
        raise AssertionError
    def __eq__(self,o):
        o=o if isinstance(o,S) else S(o)
        return self.a==o.a and self.b==o.b
    def __repr__(self): return f"S({self.a},{self.b})"

def pos(x): return (x if isinstance(x,S) else S(x)).sign()>0
def neg(x): return (x if isinstance(x,S) else S(x)).sign()<0

a=F(7,5); c=F(2,5); d=F(1,2); mu=F(1)
c1=F(1); c2=F(-2); c3=F(3,2); c4=F(0)
k=F(1,100); m=F(1)
s=d*(mu-1)
B=4*(1+c2)-s*s
q1=S(F(1,2))
q=S(F(1,3),F(-1,30))
qplus=S(F(1,3),F(1,30))

# Source cubic-cost restrictions and positive marginal cost certificate.
assert c1>0 and c2<=0 and c4>=0 and c2*c2<=3*c1*c3
assert (2*c2)*(2*c2)-4*(3*c1)*c3 == F(-2)

# Both equilibrium roots are positive, and q1 is the source equilibrium value.
assert pos(q) and pos(qplus)
assert q1 == S((a-c+s*F(0))/2)  # s=0, independent of q here

def P(x): return 6*c1*x*x+B*x-(2*(a-c3)+s*(a-c))
assert P(q)==0 and P(qplus)==0

def Pprime(x): return 12*c1*x+B
assert neg(Pprime(q)) and pos(Pprime(qplus))

# Proposition 2 retained conditions and omitted Jury condition.
cond40=2*q1+2*(1+c2)*q+6*c1*q*q-12*k*c1*q1*q*q-k*B*q1*q
cond41=k*k*B*q1*q-4*k*(q1+(1+c2)*q+3*c1*q*q)+12*k*k*c1*q1*q*q+4
jury2=k*k*q1*q*Pprime(q)
eig2=1-2*k*q*((1+c2)+3*c1*q)
assert cond40 == S(F(731,500),F(-33,500))
assert cond41 == S(F(595607,150000),F(199,150000))
assert jury2 == S(F(7,150000),F(-1,150000))
assert eig2 == S(F(1493,1500),F(1,1500))
assert pos(cond40) and pos(cond41) and neg(jury2) and pos(eig2-1)

# Proposition 3 retained conditions at m=1 and its omitted Jury condition.
cond48=2*(1+m)*(q1+(1+c2)*q+3*c1*q*q)-12*k*c1*q1*q*q-k*B*q1*q
cond49=k*k*B*q1*q-4*k*(1+m)*(q1+(1+c2)*q+3*c1*q*q)+12*k*k*c1*q1*q*q+4*(1+m)*(1+m)
jury2m=S(k*k)*q1*q*Pprime(q)*F(1,(1+m)*(1+m))
eig2m=1-2*F(k,1+m)*q*((1+c2)+3*c1*q)
assert cond48 == S(F(4393,1500),F(-199,1500))
assert cond49 == S(F(797069,50000),F(133,50000))
assert jury2m == S(F(7,600000),F(-1,600000))
assert eig2m == S(F(2993,3000),F(1,3000))
assert pos(cond48) and pos(cond49) and neg(jury2m) and pos(eig2m-1)

print("VERIFY_OK")
