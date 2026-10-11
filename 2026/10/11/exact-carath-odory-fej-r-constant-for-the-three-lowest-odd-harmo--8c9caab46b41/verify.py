from fractions import Fraction as F
import math

class Q2:
    __slots__=('a','b')
    def __init__(self,a=0,b=0): self.a=F(a); self.b=F(b)
    def __add__(self,o): o=q(o); return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self+(-q(o))
    def __rsub__(self,o): return q(o)-self
    def __mul__(self,o):
        o=q(o); return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __eq__(self,o): o=q(o); return self.a==o.a and self.b==o.b
    def val(self): return float(self.a)+float(self.b)*math.sqrt(2)
    def __repr__(self): return f'({self.a})+({self.b})sqrt2'
def q(x): return x if isinstance(x,Q2) else Q2(x,0)

def padd(p,r):
    n=max(len(p),len(r)); out=[Q2() for _ in range(n)]
    for i in range(n): out[i]=(p[i] if i<len(p) else Q2())+(r[i] if i<len(r) else Q2())
    return trim(out)
def pscale(p,s): return trim([c*s for c in p])
def pmul(p,r):
    out=[Q2() for _ in range(len(p)+len(r)-1)]
    for i,a in enumerate(p):
        for j,b in enumerate(r): out[i+j]=out[i+j]+a*b
    return trim(out)
def trim(p):
    while len(p)>1 and p[-1]==0: p.pop()
    return p

s=Q2(0,1); r=Q2(0,F(1,2))
a=Q2(F(1,2),F(1,2))
b=Q2(F(1,4),F(-3,8))
c=Q2(F(1,4),F(-1,8))
# Q=a*T1+b*T3+c*T5
T1=[Q2(),Q2(1)]
T3=[Q2(),Q2(-3),Q2(),Q2(4)]
T5=[Q2(),Q2(5),Q2(),Q2(-20),Q2(),Q2(16)]
Q=padd(padd(pscale(T1,a),pscale(T3,b)),pscale(T5,c))
one=[Q2(1)]
L=padd(one,pscale(Q,-1))
K=Q2(4,-2)
f1=[Q2(1),Q2(-1)]                         # 1-x
f2=pmul([ -r, Q2(1)],[-r,Q2(1)])           # (x-r)^2
f3=[Q2(1,F(1,2)), Q2(1,1), Q2(1)]          # x^2+(1+s)x+1+s/2
R=pscale(pmul(pmul(f1,f2),f3),K)
assert L==R,(L,R)
# contact equations Q(0 angle)=1; Q(pi/4)=1; derivative=0
assert a+b+c==1
assert r*(a-b-c)==1
assert a+3*b-5*c==0
# coefficient optimum
assert a==Q2(F(1,2),F(1,2))
# discriminant of f3 is -1
D=Q2(1,1)*Q2(1,1)-4*Q2(1,F(1,2))
assert D==-1,D
# dense numerical corroboration
av,bv,cv=a.val(),b.val(),c.val(); worst=0.0
for j in range(20001):
    th=math.pi*j/20000
    v=av*math.cos(th)+bv*math.cos(3*th)+cv*math.cos(5*th)
    worst=max(worst,abs(v))
assert worst <= 1+2e-12,worst
print(f'VERIFY_OK exact_factorization=1 contacts=3 discriminant=-1 grid=20001 max_abs={worst:.15f}')
