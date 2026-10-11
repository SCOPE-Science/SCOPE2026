from fractions import Fraction as F

class Q5:
    """Exact a+b*sqrt(5), a,b rational."""
    __slots__=("a","b")
    def __init__(self,a=0,b=0):
        self.a=F(a); self.b=F(b)
    def __add__(self,o):
        o=asq(o); return Q5(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q5(-self.a,-self.b)
    def __sub__(self,o): return self+(-asq(o))
    def __rsub__(self,o): return asq(o)-self
    def __mul__(self,o):
        o=asq(o)
        return Q5(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def sign(self):
        a,b=self.a,self.b
        if b==0: return (a>0)-(a<0)
        if b<0: return -Q5(-a,-b).sign()
        if a>=0: return 1
        d=5*b*b-a*a
        return (d>0)-(d<0)
    def __abs__(self): return self if self.sign()>=0 else -self
    def __lt__(self,o): return (self-asq(o)).sign()<0
    def __le__(self,o): return (self-asq(o)).sign()<=0
    def __eq__(self,o):
        o=asq(o); return self.a==o.a and self.b==o.b
    def __repr__(self): return f"Q5({self.a},{self.b})"

def asq(x): return x if isinstance(x,Q5) else Q5(x,0)

one=Q5(1)
r=Q5(F(-1,2),F(1,2))
phi=Q5(F(1,2),F(1,2))
c=Q5(F(-1,4),F(3,4))
assert r*phi==one
assert r*r==one-r
assert 2*r+phi==2*c

FCTS=[
    lambda s,t:s+t,
    lambda s,t:r*s+t,
    lambda s,t:r*t,
    lambda s,t:r*s,
    lambda s,t:s+r*t,
]
def N(v):
    vals=[abs(f(v[0],v[1])) for f in FCTS]
    m=vals[0]
    for q in vals[1:]:
        if m<q: m=q
    return m

verts=[
    (one,Q5(0)),
    (Q5(0),one),
    (-one,phi),
    (-phi,phi),
    (-phi,one),
    (-one,Q5(0)),
    (Q5(0),-one),
    (one,-phi),
    (phi,-phi),
    (phi,-one),
]
for v in verts:
    assert N(v)==one

def R(v):
    s,t=v
    return (-t,s+phi*t)
def S(v):
    s,t=v
    return (t,s)

for i,v in enumerate(verts):
    assert R(v)==verts[(i+1)%10]
    assert S(v) in verts
    assert N(R(v))==N(v)
    assert N(S(v))==N(v)

edge_checks=0
vertex_checks=0
for k in range(101):
    q=F(k,100)
    a=Q5(q)
    x=(a,one-a)
    y=(phi,-phi)
    A=N((x[0]+y[0],x[1]+y[1]))
    B=N((x[0]-y[0],x[1]-y[1]))
    assert A==2*r+r*r*a
    assert B==phi-r*r*a
    assert A+B==2*c
    edge_checks+=1

    th=Q5(q)
    x=(one,Q5(0))
    y=(one+r*th,-phi)
    A=N((x[0]+y[0],x[1]+y[1]))
    B=N((x[0]-y[0],x[1]-y[1]))
    assert A==2*r+r*r*th
    assert B==phi-r*r*th
    assert A+B==2*c
    # Vertex Birkhoff condition: active values straddle zero.
    e0=y[0]+y[1]
    e4=y[0]+r*y[1]
    assert e0.sign()<=0 and e4.sign()>=0
    vertex_checks+=1

half=Q5(F(1,2))
x=(half,half)
y=(phi,-phi)
assert N(x)==N(y)==one
assert (x[0]+x[1])==one
assert (y[0]+y[1])==Q5(0)
assert N((x[0]+y[0],x[1]+y[1]))==c
assert N((x[0]-y[0],x[1]-y[1]))==c

print(
    "VERIFY_OK "
    f"vertices={len(verts)} edge_checks={edge_checks} "
    f"vertex_checks={vertex_checks} "
    "field=Q(sqrt5) chord_sum=(3sqrt5-1)/2"
)
