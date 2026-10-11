from fractions import Fraction as F

class Q2:
    __slots__ = ("a","b")
    def __init__(self,a=0,b=0):
        self.a=F(a); self.b=F(b)
    def __add__(self,o):
        o=q(o); return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self+(-q(o))
    def __rsub__(self,o): return q(o)-self
    def __mul__(self,o):
        o=q(o)
        return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def sign(self):
        if self.b==0:
            return (self.a>0)-(self.a<0)
        if self.b<0:
            return -(-self).sign()
        if self.a>=0:
            return 1
        z=2*self.b*self.b-self.a*self.a
        return (z>0)-(z<0)
    def __abs__(self): return self if self.sign()>=0 else -self
    def __lt__(self,o): return (self-q(o)).sign()<0
    def __eq__(self,o):
        o=q(o); return self.a==o.a and self.b==o.b
    def __truediv__(self,o):
        o=q(o)
        den=o.a*o.a-2*o.b*o.b
        return Q2(
            (self.a*o.a-2*self.b*o.b)/den,
            (self.b*o.a-self.a*o.b)/den
        )

def q(x): return x if isinstance(x,Q2) else Q2(x)

s=Q2(0,1)
one=Q2(1)
r=s-one
d=2-s

V=[
    (one,r),(r,one),(-r,one),(-one,r),
    (-one,-r),(-r,-one),(r,-one),(one,-r)
]

def edge(j,t):
    t=q(t); v=V[j]; w=V[(j+1)%8]
    return (
        v[0]+t*(w[0]-v[0]),
        v[1]+t*(w[1]-v[1])
    )

def N(z):
    A=abs(z[0]); B=abs(z[1]); C=(A+B)/s
    out=A
    if out<B: out=B
    if out<C: out=C
    return out

def add(u,v): return (u[0]+v[0],u[1]+v[1])
def sub(u,v): return (u[0]-v[0],u[1]-v[1])
def R(u): return (-u[1],u[0])

for A in [F(0),F(1),F(7,19)]:
    x=edge(0,A)
    assert edge(2,A)==R(x)
    y=edge(6,A)
    rx=R(x)
    assert y==(-rx[0],-rx[1])

checks=0
for j in range(8):
    for A in range(21):
        for B in range(21):
            av=F(A,20); bv=F(B,20)
            x=edge(0,av); y=edge(j,bv)
            f=N(add(x,y))-N(sub(x,y))
            sg=f.sign()
            if j==0:
                assert sg>0
            elif j==1:
                assert sg==(0 if (A==0 and B==20) else 1)
            elif j==2:
                assert sg==((A>B)-(A<B))
            elif j==3:
                assert sg==(0 if (A==20 and B==0) else -1)
            elif j==4:
                assert sg<0
            elif j==5:
                assert sg==(0 if (A==0 and B==20) else -1)
            elif j==6:
                assert sg==((B>A)-(B<A))
            elif j==7:
                assert sg==(0 if (A==20 and B==0) else 1)
            checks+=1

for A in range(21):
    x=edge(0,F(A,20))
    y=R(x)
    assert N(add(x,y))==s
    assert N(sub(x,y))==s

print(
    "VERIFY_OK "
    f"edge_classes=8 exact_grid_checks={checks} "
    "classification=y=+-R(x) common_chord=sqrt2"
)
