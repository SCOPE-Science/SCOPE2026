from fractions import Fraction as F

class Q2:
    __slots__ = ('a','b')
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
        if a==0:
            return (b>0)-(b<0)
        if b==0:
            return (a>0)-(a<0)
        if a>0 and b>0: return 1
        if a<0 and b<0: return -1
        aa=a*a; bb=2*b*b
        if aa==bb: return 0
        if a>0 and b<0: return 1 if aa>bb else -1
        return 1 if bb>aa else -1
    def __lt__(self,o): return (self-q(o)).sign()<0
    def __le__(self,o): return (self-q(o)).sign()<=0
    def __eq__(self,o):
        o=q(o); return self.a==o.a and self.b==o.b
    def __abs__(self): return self if self.sign()>=0 else -self
    def __repr__(self): return f'Q2({self.a},{self.b})'

def q(x): return x if isinstance(x,Q2) else Q2(x,0)

def vmax(*xs):
    m=xs[0]
    for x in xs[1:]:
        if m<x: m=x
    return m

rt2=Q2(0,1)
a=rt2-1
r=Q2(0,F(1,2))
L=Q2(1,F(1,2))
verts=[
    (Q2(1),a),(a,Q2(1)),(-a,Q2(1)),(Q2(-1),a),
    (Q2(-1),-a),(-a,Q2(-1)),(a,Q2(-1)),(Q2(1),-a)
]

def scale(v,c): return (v[0]*c,v[1]*c)
def add(u,v): return (u[0]+v[0],u[1]+v[1])
def sub(u,v): return (u[0]-v[0],u[1]-v[1])
def norm(v):
    x,y=abs(v[0]),abs(v[1])
    diag=(x+y)*Q2(0,F(1,2))
    return vmax(x,y,diag)

def gamma(s):
    s=F(s)
    # reduce modulo 8
    k0=s.numerator//s.denominator
    m=k0//8
    s=s-8*m
    k=s.numerator//s.denominator
    u=s-k
    p=verts[k%8]; w=verts[(k+1)%8]
    return add(scale(p,1-u),scale(w,u))

def D(s,g): return norm(sub(gamma(F(s)+F(g)),gamma(s)))

# Unit vertices.
for v in verts: assert norm(v)==1

# Sharp triple.
u=a*F(1,2)
x=(r,r); y=(u,Q2(-1)); z=(Q2(-1),u)
assert norm(x)==norm(y)==norm(z)==1
assert norm(sub(x,y))==L
assert norm(sub(x,z))==L
assert norm(sub(y,z))==L

# Four convexity-cell vertex tables.
cells=[
    [(F(0),F(0)),(F(0),F(1)),(F(1),F(0))],
    [(F(0),F(1)),(F(0),F(2)),(F(1),F(0)),(F(1),F(1))],
    [(F(0),F(2)),(F(0),F(5,2)),(F(1,2),F(5,2)),(F(1),F(1)),(F(1),F(2))],
    [(F(1,2),F(5,2)),(F(1),F(2)),(F(1),F(5,2))]
]
expected=[2*a,rt2,L,L]
for cell,e in zip(cells,expected):
    vals=[D(u0,g0) for u0,g0 in cell]
    m=vals[0]
    for v in vals[1:]:
        if m<v: m=v
    assert m==e,(cell,vals,m,e)

# Supplementary exact short-gap grid.
short_checks=0
for den in range(1,25):
    for iu in range(den+1):
        U=F(iu,den)
        for ig in range(0,5*den//2+1):
            G=F(ig,den)
            if G<=F(5,2):
                assert D(U,G)<=L,(U,G,D(U,G))
                short_checks+=1

# Exact strict-gap criterion on a rational grid away from boundaries.
strict_checks=0
for den in range(10,51):
    for iu in range(den):
        U=F(iu,den)
        if U==F(1,2): continue
        for ih in range(1,(den+1)//2):
            H=F(ih,den)
            if not (0<H<F(1,2)): continue
            val=D(U,F(5,2)+H)
            pred=(U<F(1,2)) or (U>F(1,2) and U+H>1)
            assert (val>L)==pred,(U,H,val,pred)
            strict_checks+=1

# Exact inequality L < sqrt(3) without adjoining sqrt(3): L^2 < 3.
assert L*L < 3

print(f'VERIFY_OK cells=4 short_gap_checks={short_checks} strict_gap_checks={strict_checks} JT=1+1/sqrt2')
