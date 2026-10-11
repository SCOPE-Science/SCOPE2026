from fractions import Fraction as F
class Q5:
    __slots__=('a','b')
    def __init__(self,a=0,b=0): self.a=F(a); self.b=F(b)
    def __add__(self,o): o=q(o); return Q5(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q5(-self.a,-self.b)
    def __sub__(self,o): return self+(-q(o))
    def __rsub__(self,o): return q(o)-self
    def __mul__(self,o): o=q(o); return Q5(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def sign(self):
        if self.b==0: return (self.a>0)-(self.a<0)
        if self.b<0: return -(-self).sign()
        if self.a>=0: return 1
        d=5*self.b*self.b-self.a*self.a
        return (d>0)-(d<0)
    def __abs__(self): return self if self.sign()>=0 else -self
    def __lt__(self,o): return (self-q(o)).sign()<0
    def __eq__(self,o): o=q(o); return self.a==o.a and self.b==o.b
def q(x): return x if isinstance(x,Q5) else Q5(x,0)
one=Q5(1); zero=Q5(0); r=Q5(F(-1,2),F(1,2)); phi=one+r; r2=r*r
M=Q5(4,-1); m=Q5(F(9,4),F(-1,4)); rho=Q5(F(-27,16),F(9,16)); delta=Q5(F(-19,2),4)
assert r2==one-r and M==3-2*r and m==2-r*F(1,2)
assert rho==one-m*m*F(1,2) and delta==one-M*M*F(1,2)
FCTS=[lambda s,t:s+t,lambda s,t:r*s+t,lambda s,t:r*t,lambda s,t:r*s,lambda s,t:s+r*t]
def N(v):
    vals=[abs(f(v[0],v[1])) for f in FCTS]; out=vals[0]
    for w in vals[1:]:
        if out<w: out=w
    return out
verts=[(one,zero),(zero,one),(-one,phi),(-phi,phi),(-phi,one),(-one,zero),(zero,-one),(one,-phi),(phi,-phi),(phi,-one)]
for v in verts: assert N(v)==one
def R(v): s,t=v; return (-t,s+phi*t)
def S(v): s,t=v; return (t,s)
for i,v in enumerate(verts): assert R(v)==verts[(i+1)%10] and N(S(v))==one
checks=0
for k in range(101):
    u=Q5(F(k,100))
    a=u*r2; x=(a,one-a); y=(2-r+r*a,-r-a); z=(x[0]-y[0],x[1]-y[1])
    assert N(x)==N(y)==N(z)==one
    e1=M-r2*a; e2=phi+r2*a; ex=e1 if e2<e1 else e2
    assert N((x[0]+y[0],x[1]+y[1]))==ex
    assert N(z)==one and N((x[0]-z[0],x[1]-z[1]))==one; checks+=1
    a=r2+u*(r-r2); x=(a,one-a); y=(phi,-a-r); z=(x[0]-y[0],x[1]-y[1])
    assert N(x)==N(y)==N(z)==one and N((x[0]+y[0],x[1]+y[1]))==3*r+(one-2*r)*a; checks+=1
    a=r+u*(one-r); x=(a,one-a); y=(phi,-one-r2*a); z=(x[0]-y[0],x[1]-y[1])
    assert N(x)==N(y)==N(z)==one and N((x[0]+y[0],x[1]+y[1]))==phi+(2-3*r)*a; checks+=1
a=r2*F(1,2); x=(a,one-a); y=(Q5(F(3,2)),-phi*F(1,2)); z=(x[0]-y[0],x[1]-y[1])
assert N(x)==N(y)==N(z)==one and N((x[0]+y[0],x[1]+y[1]))==m
x=(zero,one); y=(2-r,-r); z=(x[0]-y[0],x[1]-y[1])
assert N(x)==N(y)==N(z)==one and N((x[0]+y[0],x[1]+y[1]))==M
assert m < 6*r-2 and 6*r-2 < M
print(f'VERIFY_OK vertices={len(verts)} branch_checks={checks} field=Q(sqrt5) min=(9-sqrt5)/4 max=4-sqrt5')
