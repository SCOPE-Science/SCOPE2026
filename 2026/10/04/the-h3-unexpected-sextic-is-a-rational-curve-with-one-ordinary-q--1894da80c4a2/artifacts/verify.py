from fractions import Fraction
from math import comb, gcd

class K:
    __slots__ = ("a","b")
    def __init__(self,a=0,b=0): self.a,self.b=Fraction(a),Fraction(b)
    def __add__(self,o): o=co(o); return K(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return K(-self.a,-self.b)
    def __sub__(self,o): return self+(-co(o))
    def __rsub__(self,o): return co(o)-self
    def __mul__(self,o):
        o=co(o); return K(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        d=self.a*self.a-5*self.b*self.b
        assert d
        return K(self.a/d,-self.b/d)
    def __truediv__(self,o): return self*co(o).inv()
    def __rtruediv__(self,o): return co(o)/self
    def __eq__(self,o): o=co(o); return self.a==o.a and self.b==o.b
    def __bool__(self): return bool(self.a or self.b)
    def __repr__(self): return f"K({self.a},{self.b})"
def co(x): return x if isinstance(x,K) else K(x)
s=K(0,1)

def pw(x,n):
    r=K(1)
    for _ in range(n): r=r*x
    return r

pts=[
(K(0),K(0),K(1)),(K(1),K(0),K(1)),(K(1),K(0),K(-1)),(K(0),K(1),K(1)),(K(0),K(1),K(-1)),
(K(0),K(1),K(2)+s),(K(0),K(1),K(-2)-s),(K(1),K(0),K(-2)-s),(K(1),K(0),K(2)+s),
(K(1),K(-1),K(0)),(K(1),K(1),K(0)),
(s+3,-(2*s+4),3*s+7),(2*s+4,-(s+3),-(3*s+7)),(2*s+4,-(s+3),3*s+7),(s+3,-(2*s+4),-(3*s+7))]
mons=[(i,j,6-i-j) for i in range(7) for j in range(7-i)]
rows=[]
for X,Y,Z in pts:
    rows.append([pw(X,i)*pw(Y,j)*pw(Z,k) for i,j,k in mons])
for a in range(5):
    for b in range(5-a):
        rows.append([K(comb(i,a)*3**(i-a)*comb(j,b)*5**(j-b)) if a<=i and b<=j else K() for i,j,k in mons])

def rref(A):
    A=[r[:] for r in A]; m,n=len(A),len(A[0]); piv=[]; rr=0
    for c in range(n):
        p=next((i for i in range(rr,m) if A[i][c]),None)
        if p is None: continue
        A[rr],A[p]=A[p],A[rr]
        q=A[rr][c].inv(); A[rr]=[x*q for x in A[rr]]
        for i in range(m):
            if i!=rr and A[i][c]:
                f=A[i][c]; A[i]=[A[i][j]-f*A[rr][j] for j in range(n)]
        piv.append(c); rr+=1
    return A,piv
R,piv=rref(rows)
assert len(piv)==27
free=[c for c in range(28) if c not in piv]
assert free==[27]
v=[K() for _ in range(28)]; v[27]=K(1)
for rr,c in enumerate(piv): v[c]=-R[rr][27]
# Scale so the x^6 coefficient is 3125.
v=[x*3125 for x in v]

# All interpolation equations vanish.
for row in rows:
    assert sum((row[j]*v[j] for j in range(28)),K())==K()

# Expand after x=3+u, y=5+v, z=1 into homogeneous local pieces.
local={}
for coeff,(i,j,k) in zip(v,mons):
    for a in range(i+1):
        for b in range(j+1):
            q=coeff*comb(i,a)*3**(i-a)*comb(j,b)*5**(j-b)
            local[(a,b)]=local.get((a,b),K())+q
for (a,b),q in local.items():
    if a+b<5: assert q==K()
A=[local.get((a,5-a),K()) for a in range(6)]
B=[local.get((a,6-a),K()) for a in range(7)]
expected_A=[K(-1545),K(11700,-645),K(-33600,3300),K(45600,-6300),K(-29100,5475),K(6975,-1920)]
expected_B=[K(-405),K(2860,-81),K(-6900,280),K(5120,-160),K(4180,-280),K(-7980,241),K(3125)]
assert A==expected_A and B==expected_B

def trim(p):
    while len(p)>1 and not p[-1]: p.pop()
    return p

def divmodp(a,b):
    a=trim(a[:]); b=trim(b[:]); q=[K() for _ in range(max(1,len(a)-len(b)+1))]
    while len(a)>=len(b) and any(a):
        d=len(a)-len(b); c=a[-1]/b[-1]; q[d]=c
        for i in range(len(b)): a[d+i]=a[d+i]-c*b[i]
        trim(a)
    return trim(q),trim(a)

def monic(p):
    p=trim(p[:]); return [x/p[-1] for x in p]

def gcdp(a,b):
    a,b=trim(a[:]),trim(b[:])
    while any(b):
        _,r=divmodp(a,b); a,b=b,r
    return monic(a)

def deriv(p): return [p[i]*i for i in range(1,len(p))] or [K()]

# v=1 dehomogenizations. Nonzero top u-coefficients exclude a factor v.
gAB=gcdp(A,B)
gsq=gcdp(A,deriv(A))
assert len(gAB)==1 and gAB[0]==K(1)
assert len(gsq)==1 and gsq[0]==K(1)
assert A[-1] and B[-1]
print("rank=27")
print("gcd(A5,B6)=1")
print("gcd(A5,dA5)=1")
print("VERIFY_OK")
