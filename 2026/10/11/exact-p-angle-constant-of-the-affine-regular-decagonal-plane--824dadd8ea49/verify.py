from fractions import Fraction as F

class Q5:
    """Exact element a+b*sqrt(5), with rational a,b."""
    __slots__=("a","b")
    def __init__(self,a=0,b=0): self.a=F(a); self.b=F(b)
    def __add__(self,o): o=q(o); return Q5(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q5(-self.a,-self.b)
    def __sub__(self,o): return self+(-q(o))
    def __rsub__(self,o): return q(o)-self
    def __mul__(self,o):
        o=q(o)
        return Q5(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=q(o); den=o.a*o.a-5*o.b*o.b
        return Q5((self.a*o.a-5*self.b*o.b)/den,(self.b*o.a-self.a*o.b)/den)
    def __rtruediv__(self,o): return q(o)/self
    def __eq__(self,o): o=q(o); return self.a==o.a and self.b==o.b
    def sign(self):
        if self.b==0: return (self.a>0)-(self.a<0)
        if self.b<0: return -(-self).sign()
        if self.a>=0: return 1
        d=5*self.b*self.b-self.a*self.a
        return (d>0)-(d<0)
    def __lt__(self,o): return (self-q(o)).sign()<0
    def __le__(self,o): return (self-q(o)).sign()<=0
    def __abs__(self): return self if self.sign()>=0 else -self
    def __repr__(self): return f"Q5({self.a},{self.b})"

def q(x): return x if isinstance(x,Q5) else Q5(x)

zero=Q5(0); one=Q5(1)
r=Q5(F(-1,2),F(1,2)); phi=one+r
assert r*r==one-r

V=[
    (one,zero),(zero,one),(-one,phi),(-phi,phi),(-phi,one),
    (-one,zero),(zero,-one),(one,-phi),(phi,-phi),(phi,-one),
]
E=[
    (r,zero),(one,r),(one,one),(r,one),(zero,r),
    (-r,zero),(-one,-r),(-one,-one),(-r,-one),(zero,-r),
]

def dot(f,x): return f[0]*x[0]+f[1]*x[1]
def N(x): return max(abs(dot(f,x)) for f in E[:5])
def Nd(f): return max(abs(dot(f,v)) for v in V)

for v in V: assert N(v)==one
for f in E: assert Nd(f)==one

# Complete cyclic dual table.
f=E[0]
rows=[]
for k in range(6):
    g=E[k]
    plus=(f[0]+r*g[0],f[1]+r*g[1])
    minus=(f[0]-r*g[0],f[1]-r*g[1])
    rows.append((Nd(plus),Nd(minus),Nd(plus)+Nd(minus)))
expected=[
    (phi,r*r,Q5(2)),
    (phi,r,Q5(0,1)),
    (Q5(F(5,2),F(-1,2)),one,Q5(F(7,2),F(-1,2))),
    (one,Q5(F(5,2),F(-1,2)),Q5(F(7,2),F(-1,2))),
    (r,phi,Q5(0,1)),
    (r*r,phi,Q5(2)),
]
assert rows==expected
assert max(s for _,_,s in rows)==3-r

# All ordered signed-facet pairs satisfy the sharp support inequality.
checks=0
for f in E:
    for g in E:
        plus=(f[0]+r*g[0],f[1]+r*g[1])
        minus=(f[0]-r*g[0],f[1]-r*g[1])
        assert Nd(plus)+Nd(minus)<=3-r
        checks+=1
assert checks==100

# Chord-envelope polygon and convex quadratic certificate.
c=(3-r)/(1+r)
P=[(zero,zero),(2*one,zero),(2*one,r),(c,c),(r,2*one),(zero,2*one)]
for A,B in P:
    assert zero<=A<=2 and zero<=B<=2
    assert A+r*B<=3-r
    assert r*A+B<=3-r

def Q(A,B): return A*A+B*B-(r/2)*A*B
for A,B in P: assert Q(A,B)<=4
assert Q(2*one,r)==4 and Q(r,2*one)==4
assert Q(c,c)==Q5(F(321,4),F(-137,4))
assert Q(c,c)<4

# Sharp adjacent-vertex witness.
x=(one,zero); y=(zero,one)
A=N((x[0]+y[0],x[1]+y[1]))
B=N((x[0]-y[0],x[1]-y[1]))
assert A==2 and B==r
cosine=(A*A+B*B-4)/(2*A*B)
assert cosine==r/4

print(
    "VERIFY_OK "
    f"vertices={len(V)} facets={len(E)} facet_pairs={checks} "
    f"envelope_vertices={len(P)} target=(sqrt5-1)/8"
)
