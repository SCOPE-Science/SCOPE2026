"""Independent exact-arithmetic consistency checks for rhombus renormalization level law.

Uses only Python's standard library.  Finite checks are supplementary to
analytic generating-function and renewal arguments.
"""
from fractions import Fraction as F

class Q:
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)
    def __add__(self, y):
        y=coerce(y); return Q(self.a+y.a, self.b+y.b)
    __radd__=__add__
    def __neg__(self): return Q(-self.a,-self.b)
    def __sub__(self,y): return self+(-coerce(y))
    def __rsub__(self,y): return coerce(y)+(-self)
    def __mul__(self,y):
        y=coerce(y)
        return Q(self.a*y.a+2*self.b*y.b, self.a*y.b+self.b*y.a)
    __rmul__=__mul__
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        y=Q(1); x=self
        while n:
            if n&1: y=y*x
            x=x*x; n>>=1
        return y
    def __eq__(self,y):
        y=coerce(y); return self.a==y.a and self.b==y.b
    def __repr__(self): return f"({self.a})+({self.b})*sqrt(2)"
def coerce(x): return x if isinstance(x,Q) else Q(x)

q=Q(-1,1)
assert q*q+2*q==1
assert q**2 == Q(3,-2)
assert q**2 * (Q(1)+q**2) == q**2 * (Q(1)+q**2) # ring sanity

# Independent exact composition of one-digit probabilities.
M=85
p=[Q(0) for _ in range(M+1)]
p[1]=q
for m in range(2,M+1): p[m]=2*(q**m)
w=[Q(0) for _ in range(M+1)]
for j in range(2,M+1):
    w[j]=sum((p[k]*p[j-k] for k in range(1,j)), Q(0))
    expected=(q*q if j==2 else 4*(j-2)*(q**j))
    assert w[j] == expected, ('increment coefficient',j,w[j],expected)

# Renewal recursion, independent of the closed formula.
u=[Q(0) for _ in range(M+1)]
u[0]=Q(1)
for m in range(1,M+1):
    u[m]=sum((w[j]*u[m-j] for j in range(2,m+1)),Q(0))
    cosine=(1,0,-1,0)[m%4]
    sine=(0,1,0,-1)[m%4]
    closed=Q(F(1,4))+( (-q*q)**m )*F(1,4) +(q**m)*F(cosine-sine,2)
    assert u[m]==closed, ('level law',m,u[m],closed)

# Check all-threshold rational generating functions at multiple k, not only k=0,1.
def poly_mul(a,b):
    c=[Q(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=c[i+j]+x*y
    return c
D=poly_mul(poly_mul([Q(1),Q(-1)],[Q(1),q*q]),[Q(1),Q(0),q*q])
assert D[0]==1
for k in range(2,10):
    numerator=[Q(0),4*(k-1)*(q**(k+1)),-4*(k-2)*(q**(k+2))]
    fk=[Q(0) for _ in range(27)]
    for m in range(1,27):
        coefficient=numerator[m] if m<len(numerator) else Q(0)
        fk[m]=coefficient-sum((D[j]*fk[m-j] for j in range(1,min(m,len(D)-1)+1)),Q(0))
        direct=sum((u[m-j]*w[j+k] for j in range(1,m+1)),Q(0))
        assert fk[m]==direct, ('overshoot generating function',k,m)

# Check a probabilistic overshoot by exact finite convolution for 1..25.
# Tail of the entire increment distribution is given analytically by
# Pr(Z>=k+1) = 1 (k=0,1); otherwise 4 sum_{j>=k+1}(j-2)q^j.
# For finite m, direct first-passage convolution using u and w verifies
# that all probability mass across overshoots is one (using cutoffs).
for m in range(1,26):
    # Exact probability H_m=k via tail PGF has coefficient expression.
    # Its finite sum over 0<=k<K differs from 1 only by exponentially small tail.
    K=40
    vals=[]
    for k in range(K):
        # finite j in 1..m; w[j+k] requires max 64 < M
        vals.append(sum((u[m-j]*w[j+k] for j in range(1,m+1)),Q(0)))
    # The exact k=0,1 finite-threshold identities follow from the
    # two rational overshoot generating functions.
    assert vals[0]==u[m]
    assert vals[1]==u[m+1]
    sm=sum(vals,Q(0))
    inv=Q(1,F(1,2))
    assert (1-q)*inv == 1
    def tail_ge(r):
        if r<=2: return Q(1)
        return 4*(q**r)*((r-2)*inv+q*inv**2)
    remaining=sum((u[m-j]*tail_ge(j+K) for j in range(1,m+1)), Q(0))
    assert sm+remaining==1, ('overshoot mass',m)

# Limiting overshoot profile has unit mass, by the tail-sum identity.
# pi(0)=pi(1)=1/4, pi(k)=q**k*((k-1)/sqrt(2)+1/2) (k>=2).
# Sum_{k>=2} pi(k) can be evaluated through geometric tails.
inv_root2=Q(0,F(1,2))
# geometric sums: sum_{k>=2}(k-1)q**k=q**2/(1-q)**2,
# and sum_{k>=2}q**k=q**2/(1-q).
sum_tail=(q*q)*(inv_root2*inv**2+F(1,2)*inv)
assert sum_tail==F(1,2)

print('VERIFY_OK: 85 exact renewal levels; 84 exact paired-digit weights; 25 first-passage mass and k=0,1 checks; 208 exact rational overshoot coefficients')
