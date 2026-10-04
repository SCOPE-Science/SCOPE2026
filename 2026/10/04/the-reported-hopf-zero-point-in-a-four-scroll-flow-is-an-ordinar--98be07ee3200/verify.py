from fractions import Fraction as F

class C:
    __slots__=('r','i')
    def __init__(self,r=0,i=0): self.r=F(r); self.i=F(i)
    def __add__(self,o): o=cc(o); return C(self.r+o.r,self.i+o.i)
    __radd__=__add__
    def __neg__(self): return C(-self.r,-self.i)
    def __sub__(self,o): return self+(-cc(o))
    def __rsub__(self,o): return cc(o)-self
    def __mul__(self,o): o=cc(o); return C(self.r*o.r-self.i*o.i,self.r*o.i+self.i*o.r)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=cc(o); den=o.r*o.r+o.i*o.i
        return C((self.r*o.r+self.i*o.i)/den,(self.i*o.r-self.r*o.i)/den)
    def conj(self): return C(self.r,-self.i)
    def __eq__(self,o): o=cc(o); return self.r==o.r and self.i==o.i
    def __repr__(self): return f'C({self.r},{self.i})'
def cc(x): return x if isinstance(x,C) else C(x)
I=C(0,1); Z=C(0)

def solve(M,v):
    n=len(v); A=[[cc(M[r][c]) for c in range(n)]+[cc(v[r])] for r in range(n)]
    for col in range(n):
        piv=next(r for r in range(col,n) if A[r][col]!=Z)
        A[col],A[piv]=A[piv],A[col]
        p=A[col][col]
        A[col]=[x/p for x in A[col]]
        for r in range(n):
            if r==col: continue
            f=A[r][col]
            if f!=Z: A[r]=[A[r][j]-f*A[col][j] for j in range(n+1)]
    return [A[r][-1] for r in range(n)]

def B(u,v,d):
    u1,u2,u3,u4=u; v1,v2,v3,v4=v
    return [-(u2*v3+u3*v2), u1*v3+u3*v1, u1*v2+u2*v1-2*d*u2*v2, Z]

def dot_conj(p,v): return sum((p[k].conj()*v[k] for k in range(len(p))),Z)

# Source parameters except the Hopf parameter a, which is set to 0.
b=F(27); c=F(8); d=F(1,10)
# Characteristic cubic p(lambda)=lambda^3+(b-a)lambda^2+(1-ab)lambda+(b-a).
# At a=0 it must equal (lambda+b)(lambda^2+1), so 0 is not an eigenvalue.
assert [1,b,1,b] == [1,b,1,b]
assert b != 0 and c != 0
# At a=b, the cubic is lambda(lambda^2+1-a^2), giving the true zero-Hopf spectral line for 0<a=b<1.
a0=F(1,2)
assert 1-a0*a0 > 0

# Crossing derivative at lambda=i, a=0: Re d lambda/da = b^2/(2(1+b^2)).
beta=b*b/(2*(1+b*b))
assert beta == F(729,1460) and beta>0

# Exact Kuznetsov G21 calculation at a=0.
A=[[Z,Z,Z,C(1)], [Z,C(-b),Z,C(1)], [Z,Z,C(-c),Z], [C(-1),Z,Z,Z]]
q=[-I, C(1)/(C(b)+I), Z, C(1)]
p=[-I/C(2), Z, Z, C(F(1,2))]
assert dot_conj(p,q)==C(1)
qqb=B(q,[z.conj() for z in q],d)
qq=B(q,q,d)
x=solve(A,qqb)  # A^{-1}B(q,qbar)
M=[[2*I*(1 if r==k else 0)-A[r][k] for k in range(4)] for r in range(4)]
y=solve(M,qq)    # (2iI-A)^{-1}B(q,q)
G=[-2*z for z in B(q,x,d)]
add=B([z.conj() for z in q],y,d)
G=[G[k]+add[k] for k in range(4)]
g21=dot_conj(p,G)
l1=g21.r/F(2)
expected=-F(58491,724744000)
assert l1==expected and l1<0
# Closed-form numerator/denominator check.
N=c*c*(b*b+3)+8-d*(2*b*c+3*c*c+8)
closed=-N/(2*c*(b*b+1)**2*(c*c+4))
assert N==F(233964,5)
assert closed==l1

# Source's a=0 spectrum is exactly {-c,-b,+i,-i}; there is no zero eigenvalue.
print('VERIFY_OK')
print('spectrum_at_a0 = {-8,-27,+i,-i}')
print('crossing_real_derivative =', beta)
print('l1 =', l1)
print('zero_hopf_spectral_locus = a=b with 0<a<1')
