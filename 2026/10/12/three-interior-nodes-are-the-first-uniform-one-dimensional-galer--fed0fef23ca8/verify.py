from fractions import Fraction as F
from decimal import Decimal, getcontext

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def inv(A):
    A=[row[:] + [F(int(i==j)) for j in range(len(A))] for i,row in enumerate(A)]
    n=len(A)
    for c in range(n):
        p=next(r for r in range(c,n) if A[r][c])
        A[c],A[p]=A[p],A[c]
        q=A[c][c]
        A[c]=[x/q for x in A[c]]
        for r in range(n):
            if r==c: continue
            q=A[r][c]
            if q:
                A[r]=[A[r][j]-q*A[c][j] for j in range(2*n)]
    return [row[n:] for row in A]

def TK(n):
    T=[[F(4 if i==j else 1 if abs(i-j)==1 else 0) for j in range(n)] for i in range(n)]
    K=[[F(2 if i==j else -1 if abs(i-j)==1 else 0) for j in range(n)] for i in range(n)]
    return T,K

def Hhat(n):
    T,K=TK(n)
    return [[F(6)*x for x in row] for row in matmul(inv(T),K)]

assert Hhat(1)==[[F(3)]]
assert Hhat(2)==[[F(18,5),F(-12,5)],[F(-12,5),F(18,5)]]
H3=Hhat(3)
assert H3==[
    [F(51,14),F(-18,7),F(9,14)],
    [F(-18,7),F(30,7),F(-18,7)],
    [F(9,14),F(-18,7),F(51,14)],
]

class Q2:
    def __init__(self,a=0,b=0):
        self.a=F(a); self.b=F(b)
    def __add__(self,o):
        o=o if isinstance(o,Q2) else Q2(o)
        return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self+(- (o if isinstance(o,Q2) else Q2(o)))
    def __rsub__(self,o): return Q2(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,Q2) else Q2(o)
        return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __eq__(self,o):
        o=o if isinstance(o,Q2) else Q2(o)
        return self.a==o.a and self.b==o.b
    def __repr__(self): return f"Q2({self.a},{self.b})"

s=Q2(0,1)
half=Q2(F(1,2))
rs2half=Q2(0,F(1,2))  # sqrt(2)/2 = 1/sqrt(2)
vecs=[
    [half,rs2half,half],
    [rs2half,Q2(0),-rs2half],
    [half,-rs2half,half],
]
lams=[
    Q2(F(30,7),F(-18,7)),
    Q2(3),
    Q2(F(30,7),F(18,7)),
]
for v,lam in zip(vecs,lams):
    Hv=[]
    for i in range(3):
        Hv.append(sum(Q2(H3[i][j])*v[j] for j in range(3)))
    assert all(Hv[i]==lam*v[i] for i in range(3))

# Orthonormality.
for i in range(3):
    for j in range(3):
        dot=sum(vecs[i][k]*vecs[j][k] for k in range(3))
        assert dot==Q2(1 if i==j else 0)

getcontext().prec=70
sqrt2=Decimal(2).sqrt()
lam1=(Decimal(30)-Decimal(18)*sqrt2)/Decimal(7)
lam3=(Decimal(30)+Decimal(18)*sqrt2)/Decimal(7)
p=Decimal(3)-lam1
q=lam3-Decimal(3)
assert p>0 and q>p

def g(t):
    t=Decimal(t)
    return (p*t).exp()+(-q*t).exp()-Decimal(2)

lo=Decimal("0.21281177692")
hi=Decimal("0.21281177693")
assert g(lo)<0<g(hi)

def corner(t):
    t=Decimal(t)
    return ((-lam1*t).exp()-Decimal(2)*(-Decimal(3)*t).exp()+(-lam3*t).exp())/Decimal(4)

def nearest(t):
    t=Decimal(t)
    return sqrt2/Decimal(4)*(((-lam1*t).exp())-((-lam3*t).exp()))

assert corner(Decimal("0.1"))<0
assert corner(Decimal("0.3"))>0
assert nearest(Decimal("0.0001"))>0
assert nearest(Decimal("1"))>0

# N=2 off-diagonal formula is positive for positive tau.
def off2(t):
    t=Decimal(t)
    return (((-Decimal(6)*t/Decimal(5)).exp())-((-Decimal(6)*t).exp()))/Decimal(2)

assert off2(Decimal("0.0001"))>0
assert off2(Decimal("1"))>0

print("VERIFY_OK")
