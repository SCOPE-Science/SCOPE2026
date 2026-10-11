from fractions import Fraction as F

class Q3:
    __slots__=("a","b")
    def __init__(self,a=0,b=0): self.a=F(a); self.b=F(b)
    def __add__(self,o): o=q(o); return Q3(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q3(-self.a,-self.b)
    def __sub__(self,o): return self+(-q(o))
    def __rsub__(self,o): return q(o)-self
    def __mul__(self,o):
        o=q(o)
        return Q3(self.a*o.a+3*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        d=self.a*self.a-3*self.b*self.b
        return Q3(self.a/d,-self.b/d)
    def __truediv__(self,o): return self*q(o).inv()
    def __rtruediv__(self,o): return q(o)/self
    def __eq__(self,o):
        o=q(o); return self.a==o.a and self.b==o.b
    def sign(self):
        if self.a==0: return (self.b>0)-(self.b<0)
        if self.b==0: return (self.a>0)-(self.a<0)
        if self.a>0 and self.b>0: return 1
        if self.a<0 and self.b<0: return -1
        c=self.a*self.a-3*self.b*self.b
        if c==0: return 0
        if self.a>0: return 1 if c>0 else -1
        return -1 if c>0 else 1
    def __lt__(self,o): return (self-q(o)).sign()<0
    def __le__(self,o): return (self-q(o)).sign()<=0
    def __abs__(self): return self if self.sign()>=0 else -self

def q(x): return x if isinstance(x,Q3) else Q3(x,0)
R=Q3(0,1)

def add(u,v): return tuple(a+b for a,b in zip(u,v))
def sub(u,v): return tuple(a-b for a,b in zip(u,v))
def scale(c,u): return tuple(q(c)*a for a in u)
def dot(f,z): return f[0]*z[0]+f[1]*z[1]
def det(u,v): return u[0]*v[1]-u[1]*v[0]

def solve_adjacent(f,g):
    d=det(f,g)
    return ((g[1]-f[1])/d,(f[0]-g[0])/d)

E=[
    (q(1),q(0)),
    (R/2,q(1)/2),
    (q(1)/2,R/2),
    (q(0),q(1)),
    (-q(1)/2,R/2),
    (-R/2,q(1)/2),
]
E=E+[(-a,-b) for a,b in E]

def N(z): return max(dot(f,z) for f in E)

V=[]
for i in range(12):
    v=solve_adjacent(E[i],E[(i+1)%12])
    assert N(v)==1
    V.append(v)
assert len(V)==12

def dual_norm(h): return max(abs(dot(h,v)) for v in V)

for f in E:
    for g in E:
        assert dual_norm(add(f,scale(R,g)))+dual_norm(sub(f,scale(R,g)))<=4
        assert dual_norm(add(scale(R,f),g))+dual_norm(sub(scale(R,f),g))<=4

expected=[
    (q(1)+R,R-q(1)),
    (q(1)+R,q(1)),
    (q(2)*R-q(1),q(5)-q(2)*R),
    (q(2),q(2)),
    (q(5)-q(2)*R,q(2)*R-q(1)),
    (q(1),q(1)+R),
    (R-q(1),q(1)+R),
]
for k,(u0,v0) in enumerate(expected):
    f,g=E[0],E[k]
    assert dual_norm(add(f,scale(R,g)))==u0
    assert dual_norm(sub(f,scale(R,g)))==v0

T=q(2)-R
P=[
    (q(0),q(0)),
    (q(2),q(0)),
    (q(2),q(2)*T),
    (q(2)*(R-q(1)),q(2)*(R-q(1))),
    (q(2)*T,q(2)),
    (q(0),q(2)),
]

def Q(A,B): return A*A+B*B-T*A*B
for A,B in P:
    assert Q(A,B)<=4

x=(q(1),T)
y=(-q(1),T)
assert N(x)==1 and N(y)==1
A=N(add(x,y)); B=N(sub(x,y))
assert A==q(2)*T and B==2
cosine=(A*A+B*B-q(4))/(q(2)*A*B)
assert cosine==T/2

print("VERIFY_OK")
