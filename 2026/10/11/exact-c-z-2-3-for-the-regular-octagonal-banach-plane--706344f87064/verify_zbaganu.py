from fractions import Fraction as F
from itertools import combinations

class Q2:
    __slots__=("a","b")
    def __init__(self,a=0,b=0):
        self.a = a if isinstance(a,F) else F(a)
        self.b = b if isinstance(b,F) else F(b)
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
        assert d != 0
        return Q2(self.a/d,-self.b/d)
    def __truediv__(self,o): return self*q(o).inv()
    def __rtruediv__(self,o): return q(o)/self
    def __eq__(self,o):
        o=q(o); return self.a==o.a and self.b==o.b
    def sign(self):
        a,b=self.a,self.b
        if a==0:
            return (b>0)-(b<0)
        if b==0:
            return (a>0)-(a<0)
        if a>0 and b>0: return 1
        if a<0 and b<0: return -1
        cmp=a*a-2*b*b
        if cmp==0: return 0
        if a>0 and b<0: return 1 if cmp>0 else -1
        if a<0 and b>0: return -1 if cmp>0 else 1
        raise AssertionError
    def __lt__(self,o): return (self-q(o)).sign()<0
    def __le__(self,o): return (self-q(o)).sign()<=0
    def __repr__(self): return f"Q2({self.a},{self.b})"

def q(x): return x if isinstance(x,Q2) else Q2(x)
R=Q2(0,1)
ZERO=Q2(0); ONE=Q2(1)

def mat_add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mat_scale(c,A): return [[q(c)*x for x in row] for row in A]
def outer(u,v): return [[u[i]*v[j] for j in range(len(v))] for i in range(len(u))]
def transpose(A): return list(map(list,zip(*A)))
def det(A):
    n=len(A)
    if n==0: return ONE
    if n==1: return A[0][0]
    out=ZERO
    for j in range(n):
        minor=[row[:j]+row[j+1:] for row in A[1:]]
        out += ((-1)**j)*A[0][j]*det(minor)
    return out

def principal_minors_nonnegative(A):
    n=len(A)
    for k in range(1,n+1):
        for I in combinations(range(n),k):
            M=[[A[i][j] for j in I] for i in I]
            d=det(M)
            assert d.sign()>=0, (I,d)

def dot(u,v): return sum((u[i]*v[i] for i in range(len(u))),ZERO)

def proj(v): return outer(v,v)

# Eight norming functionals for N(s,t)=max(|s|,|t|,(|s|+|t|)/sqrt(2)).
S=[
 [ONE,ZERO], [ONE/R,ONE/R], [ZERO,ONE], [-ONE/R,ONE/R],
 [-ONE,ZERO], [-ONE/R,-ONE/R], [ZERO,-ONE], [ONE/R,-ONE/R]
]
P=[proj(S[i]) for i in range(4)]

def combo(terms):
    A=[[ZERO,ZERO],[ZERO,ZERO]]
    total=ZERO
    for w,M in terms:
        assert q(w).sign()>=0
        total += q(w)
        A=mat_add(A,mat_scale(w,M))
    assert total==ONE
    return A

theta=(Q2(81)-Q2(36)*R)/Q2(49)
assert ZERO <= theta <= ONE
C0=Q2(3)+Q2(149)*R/Q2(48)
K=Q2(6)/Q2(13)+Q2(149)*R/Q2(312)
assert Q2(2)*C0/Q2(13)==K

certs={
 0:(combo([(ONE,P[0])]), combo([(ONE,P[0])])),
 1:(combo([(ONE-theta,P[0]),(theta,P[1])]), combo([(ONE,P[3])])),
 2:(combo([(Q2(F(1,4)),P[2]),(Q2(F(3,4)),P[1])]),
    combo([(Q2(F(1,4)),P[0]),(Q2(F(3,4)),P[3])])),
 3:(combo([(ONE,P[2])]), combo([(theta,P[0]),(ONE-theta,P[3])])),
 4:(combo([(ONE,P[0])]), combo([(ONE,P[0])])),
}

# For each relative support angle k*pi/4, certify
# C0*(x^T Gx x + y^T Gy y) - (c.(2x+3y))*(d.(3x-2y)) >= 0.
c=S[0]
for k in range(5):
    d=S[k]
    ell=[Q2(2)*c[0],Q2(2)*c[1],Q2(3)*c[0],Q2(3)*c[1]]
    emm=[Q2(3)*d[0],Q2(3)*d[1],-Q2(2)*d[0],-Q2(2)*d[1]]
    Sym=mat_scale(Q2(F(1,2)),mat_add(outer(ell,emm),outer(emm,ell)))
    Gx,Gy=certs[k]
    D=[[ZERO for _ in range(4)] for _ in range(4)]
    for i in range(2):
        for j in range(2):
            D[i][j]=Gx[i][j]; D[i+2][j+2]=Gy[i][j]
    M=mat_add(mat_scale(C0,D),mat_scale(-ONE,Sym))
    principal_minors_nonnegative(M)

# Exact equality witness.
a=R-ONE
z=Q2(6)/(Q2(9)+Q2(4)*R)
w=(Q2(9)-Q2(4)*R-Q2(6)*z)/Q2(12)
x=[-a,-ONE]
y=[-z,-w]

def norm(v):
    vals=[dot(s,v) for s in S]
    return max(vals)

def vecadd(a,b,ca=ONE,cb=ONE): return [ca*a[i]+cb*b[i] for i in range(2)]
Nx=norm(x); Ny=norm(y)
A=vecadd(x,y,Q2(2),Q2(3))
B=vecadd(x,y,Q2(3),-Q2(2))
NA=norm(A); NB=norm(B)
assert Nx==ONE and Ny==z
assert ZERO < w < a*z
value=Q2(2)*NA*NB/(Q2(13)*(Nx*Nx+Ny*Ny))
assert value==K

print("VERIFY_OK")
print("K=(144+149*sqrt(2))/312")
print("support_classes=5")
print("principal_minors_checked=75")
