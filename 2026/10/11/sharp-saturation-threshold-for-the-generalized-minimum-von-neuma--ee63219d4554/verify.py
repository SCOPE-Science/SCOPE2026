from fractions import Fraction as F

class Q2:
    __slots__=("a","b")
    def __init__(self,a=0,b=0):
        self.a=F(a); self.b=F(b)
    def __add__(self,o):
        o=q(o); return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self+(-q(o))
    def __rsub__(self,o): return q(o)-self
    def __mul__(self,o):
        o=q(o); return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def sign(self):
        a,b=self.a,self.b
        if a==0 and b==0: return 0
        if a>=0 and b>=0: return 1
        if a<=0 and b<=0: return -1
        if a>0 and b<0:
            return 1 if a*a>2*b*b else -1
        if a<0 and b>0:
            return 1 if 2*b*b>a*a else -1
        raise AssertionError
    def __lt__(self,o): return (self-q(o)).sign()<0
    def __le__(self,o): return (self-q(o)).sign()<=0
    def __eq__(self,o):
        o=q(o); return self.a==o.a and self.b==o.b
    def __abs__(self): return self if self.sign()>=0 else -self
    def __repr__(self): return f"Q2({self.a},{self.b})"

def q(x): return x if isinstance(x,Q2) else Q2(x,0)

rt2=Q2(0,1)
r=rt2-1
half=F(1,2)
invrt2=Q2(0,half)

verts=[
    (Q2(1), r), (r,Q2(1)), (-r,Q2(1)), (Q2(-1),r),
    (Q2(-1),-r), (-r,Q2(-1)), (r,Q2(-1)), (Q2(1),-r)
]

facets=[
    (Q2(1),Q2(0)), (Q2(-1),Q2(0)),
    (Q2(0),Q2(1)), (Q2(0),Q2(-1)),
    (invrt2,invrt2), (-invrt2,-invrt2),
    (invrt2,-invrt2), (-invrt2,invrt2)
]

def dot(f,v): return f[0]*v[0]+f[1]*v[1]
def sub(u,v): return (u[0]-v[0],u[1]-v[1])
def add(u,v): return (u[0]+v[0],u[1]+v[1])
def scale(c,v): return (q(c)*v[0],q(c)*v[1])
def norm(v):
    s,t=v
    vals=[abs(s),abs(t),abs((s+t)*invrt2),abs((s-t)*invrt2)]
    m=vals[0]
    for x in vals[1:]:
        if m<x: m=x
    return m

# Every listed vertex is on the unit sphere and each facet has exactly two vertices.
assert all(norm(v)==1 for v in verts)
FV=[]
for f in facets:
    ids=[i for i,v in enumerate(verts) if dot(f,v)==1]
    assert len(ids)==2
    FV.append(ids)

# Opposite facet lookup.
opp=[]
for i,f in enumerate(facets):
    target=(-f[0],-f[1])
    j=facets.index(target)
    opp.append(j)

sqrt2_cert_count=0
incident_distinct=0
for i,f in enumerate(facets):
    for j,g in enumerate(facets):
        common=set(FV[i]) & set(FV[j])
        if not common:
            continue
        ys=[verts[k] for k in FV[j]]
        zs=[verts[k] for k in FV[opp[i]]]
        if i==j:
            # f(y-z)=2 on the whole product.
            for y in ys:
                for z in zs:
                    assert dot(f,sub(y,z))==2
            continue

        incident_distinct += 1
        # Find a signed facet h giving h(y-z)>=sqrt(2) at every endpoint pair.
        witnesses=[]
        for h in facets:
            vals=[dot(h,sub(y,z)) for y in ys for z in zs]
            if all(rt2<=v for v in vals):
                witnesses.append((h,vals))
        assert witnesses, (i,j)
        sqrt2_cert_count += 1

assert incident_distinct==16
assert sqrt2_cert_count==16

# Equality triple.
x=(Q2(1),r)
y=(r,Q2(1))
z=(Q2(-1),r)
assert norm(x)==norm(y)==norm(z)==1
assert norm(sub(x,z))==2
assert norm(add(x,y))==2
assert norm(sub(y,z))==rt2

# Strict endpoint approximation y_e=(1-e)y:
# for 0<e<1/2 the three candidate dominant bounds are all < sqrt(2),
# and N(x+y_e) tends to 2 as e -> 0.
e=F(1,10)
ye=scale(F(9,10),y)
assert norm(sub(ye,z)) < rt2
assert norm(add(x,ye)) < 2
# Exact convergence is immediate from linear dependence on e; verify a smaller e is closer.
e2=F(1,100)
ye2=scale(F(99,100),y)
assert norm(sub(ye2,z)) < rt2
assert norm(add(x,ye)) < norm(add(x,ye2)) < 2

print("VERIFY_OK facets=8 vertices=8 incident_distinct=16 threshold=sqrt2")
