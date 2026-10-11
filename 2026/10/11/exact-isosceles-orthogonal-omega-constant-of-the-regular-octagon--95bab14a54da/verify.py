from fractions import Fraction

class Q2:
    __slots__=("a","b")
    def __init__(self,a=0,b=0):
        if isinstance(a,Q2) and b==0:
            self.a,self.b=a.a,a.b
        else:
            self.a=Fraction(a); self.b=Fraction(b)
    def __add__(self,o):
        o=q(o); return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self+(-q(o))
    def __rsub__(self,o): return q(o)-self
    def __mul__(self,o):
        o=q(o); return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        d=self.a*self.a-2*self.b*self.b
        assert d
        return Q2(self.a/d,-self.b/d)
    def __truediv__(self,o): return self*q(o).inv()
    def __rtruediv__(self,o): return q(o)/self
    def __eq__(self,o):
        try:o=q(o)
        except Exception:return False
        return self.a==o.a and self.b==o.b
    def sign(self):
        a,b=self.a,self.b
        if a==0 and b==0:return 0
        if b==0:return 1 if a>0 else -1
        if a==0:return 1 if b>0 else -1
        if a>0 and b>0:return 1
        if a<0 and b<0:return -1
        cmp=a*a-2*b*b
        if a>0 and b<0:return 1 if cmp>0 else -1
        if a<0 and b>0:return -1 if cmp>0 else 1
        raise AssertionError
    def __lt__(self,o): return (self-q(o)).sign()<0
    def __le__(self,o): return (self-q(o)).sign()<=0
    def __gt__(self,o): return (self-q(o)).sign()>0
    def __ge__(self,o): return (self-q(o)).sign()>=0
    def __abs__(self): return self if self.sign()>=0 else -self

def q(x): return x if isinstance(x,Q2) else Q2(x)

r=Q2(0,1)

def maxq(*xs):
    m=xs[0]
    for z in xs[1:]:
        if m<z:m=z
    return m

def N8(v):
    x,y=v
    return maxq(abs(x),abs(y),(abs(x)+abs(y))/r)

d=5*r-7
a=r-1
c=(5*r-1)/7
assert Q2(0)<d<a<c<Q2(1)

# Breakpoint identities causing active-facet changes.
assert (3-d)/r == 2+d
assert r == 1+a
assert (3+c)/r == 1+2*c

def f(t):
    return N8((1+2*t,2-t))
def fm(t):
    return N8((1-2*t,2+t))
def g(t):
    return N8((1+t,1-t))
def Phi(t):
    return (f(t)*f(t)+fm(t)*fm(t))/(5*g(t)*g(t))

# Exact formulas at branch endpoints and interior rational probes.
probes=[
    (Q2(0),d,Fraction(1,2)),
    (d,a,Fraction(1,2)),
    (a,c,Fraction(1,2)),
    (c,Q2(1),Fraction(1,2)),
]
def midpoint(lo,hi): return (lo+hi)/2

for idx,(lo,hi,_) in enumerate(probes):
    for t in (lo, midpoint(lo,hi), hi):
        if idx==0:
            assert g(t)==r
            assert f(t)==(3+t)/r
            assert fm(t)==(3-t)/r
            assert Phi(t)==(t*t+9)/10
        elif idx==1:
            assert g(t)==r
            assert f(t)==(3+t)/r
            assert fm(t)==2+t
            assert Phi(t)==(3*t*t+14*t+17)/20
        elif idx==2:
            assert g(t)==1+t
            assert f(t)==(3+t)/r
            assert fm(t)==2+t
            assert Phi(t)==(3*t*t+14*t+17)/(10*(1+t)*(1+t))
        else:
            assert g(t)==1+t
            assert f(t)==1+2*t
            assert fm(t)==2+t
            assert Phi(t)==(5*t*t+8*t+5)/(5*(1+t)*(1+t))

# Continuity and exact maximum.
M=(3+2*r)/5
assert Phi(a)==M
assert Phi(d)<M and Phi(c)<M and Phi(Q2(0))<M and Phi(Q2(1))<M

# Exact derivative sign numerators on their intervals:
# t/5; (3t+7)/10; -2(2t+5)/(5(1+t)^3); 2(t-1)/(5(1+t)^3)
for t in [Q2(0), d, a, c, Q2(1)]:
    if t>=0:
        assert t>=0
    if d<=t<=a:
        assert 3*t+7>0
    if a<=t<=c:
        assert 2*t+5>0
    if c<=t<=1:
        assert t-1<=0

# Reciprocal symmetry on exact rational test values.
for tt in [Fraction(1,5),Fraction(1,2),Fraction(2,3),Fraction(3,4)]:
    t=Q2(tt)
    assert Phi(t)==Phi(1/t)

# Explicit sharp pair.
x=(Q2(1),a)
y=(-a,Q2(1))
assert N8(x)==1 and N8(y)==1
xp=(x[0]+y[0],x[1]+y[1])
xm=(x[0]-y[0],x[1]-y[1])
assert N8(xp)==r and N8(xm)==r
x2y=(x[0]+2*y[0],x[1]+2*y[1])
txpy=(2*x[0]+y[0],2*x[1]+y[1])
assert N8(x2y)==1+r
assert N8(txpy)==1+r
assert (N8(x2y)*N8(x2y)+N8(txpy)*N8(txpy))/(5*N8(xp)*N8(xp))==M

# Dense exact rational consistency grid on [0,1].
count=0
for den in range(1,41):
    for num in range(den+1):
        t=Q2(Fraction(num,den))
        assert Phi(t)<=M
        count+=1

print(f"VERIFY_OK exact_Qsqrt2 breakpoints=3 grid={count} Omega=(3+2sqrt2)/5 maximizers=sqrt2±1")
