"""Exact rational-quadratic certificate for degree-wise rhombicuboctahedral sampling.

Run with Python 3.10 or later. No third-party packages required.
The finite checks are supplemented by the analytic Legendre tail bound in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product

class Q2:
    __slots__=('a','b')
    def __init__(self,a=0,b=0):
        self.a=F(a); self.b=F(b)
    def __add__(self,z):
        z=coerce(z);return Q2(self.a+z.a,self.b+z.b)
    __radd__=__add__
    def __neg__(self):return Q2(-self.a,-self.b)
    def __sub__(self,z):return self+-coerce(z)
    def __rsub__(self,z):return coerce(z)+-self
    def __mul__(self,z):
        z=coerce(z);return Q2(self.a*z.a+2*self.b*z.b,self.a*z.b+self.b*z.a)
    __rmul__=__mul__
    def __truediv__(self,z):
        z=coerce(z); denom=z.a*z.a-2*z.b*z.b
        assert denom
        return Q2((self.a*z.a-2*self.b*z.b)/denom,(self.b*z.a-self.a*z.b)/denom)
    def __eq__(self,z):
        z=coerce(z);return self.a==z.a and self.b==z.b
    def sign(self):
        a,b=self.a,self.b
        if a==0:return (b>0)-(b<0)
        if b==0:return (a>0)-(a<0)
        if a>0 and b>0:return 1
        if a<0 and b<0:return -1
        if a>0:return (a*a>2*b*b)-(a*a<2*b*b)
        return (2*b*b>a*a)-(2*b*b<a*a)
    def __gt__(self,z):return (self-coerce(z)).sign()>0
    def __repr__(self):return f'({self.a})+({self.b})sqrt2'

def coerce(z):return z if isinstance(z,Q2) else Q2(z)

ONE=Q2(1)
theta=(Q2(7,4)/17,Q2(-3,8)/17,Q2(5,-2)/17)
large=Q2(1,1);radius2=Q2(5,2)
vertices=[]
for main in range(3):
    for signs in product((-1,1),repeat=3):
        if signs[0]!=1:continue
        vertices.append([signs[j]*(large if j==main else ONE) for j in range(3)])
assert len(vertices)==12

# Three signed adjacency relations of the twelve antipodal classes.
relations=[]
for parity in (0,1):
    matrices=[[[0]*12 for _ in range(12)] for j in range(3)]
    counts=[0,0,0]
    for i in range(12):
        for j in range(i+1,12):
            dot=sum((vertices[i][h]*vertices[j][h] for h in range(3)),Q2())
            matches=[(z,sgn) for z,v in enumerate(theta) for sgn in (1,-1)
                     if dot==sgn*radius2*v]
            assert len(matches)==1
            z,sgn=matches[0]; counts[z]+=1
            matrices[z][i][j]=matrices[z][j][i]=(sgn if parity else 1)
    assert counts==[24,18,24]
    relations.append(matrices)

# An exact 1+2+3+6 decomposition in each parity.
sectors=[
    [((4,3,4), [[1]*12]),
     ((1,0,-2),[[-1]*4+[1]*4+[0]*4,[-1]*4+[0]*4+[1]*4]),
     ((-1,-2,2),[[1,1,-1,-1,-1,-1,1,1,0,0,0,0],
                    [0,-1,1,0,1,0,-1,0,-1,1,0,0],
                    [1,0,0,-1,-1,0,1,0,0,0,-1,1]])],
    [((0,-1,-4),[[1,-1,-1,1]*3]),
     ((-3,2,2),[[-1,1,1,-1,1,-1,-1,1,0,0,0,0],
                    [-1,1,1,-1,0,0,0,0,1,-1,-1,1]]),
     ((-1,0,-2),[[1,-1,1,-1,-1,1,-1,1,0,0,0,0],
                    [0,-1,1,0,-1,0,-1,0,1,1,0,0],
                    [1,0,0,-1,-1,0,-1,0,0,0,1,1]])]
]
for par in (0,1):
    for multipliers,basis in sectors[par]:
        for v in basis:
            for M,c in zip(relations[par],multipliers):
                assert [sum(M[i][j]*v[j] for j in range(12)) for i in range(12)] == [c*z for z in v]
    # Exact independence of the first six invariant vectors.
    rows=sum((b for _,b in sectors[par]),[])
    def rational_rank(A):
        A=[[F(x) for x in row] for row in A];i=0
        for j in range(len(A[0])):
            idx=next((h for h in range(i,len(A)) if A[h][j]),None)
            if idx is None:continue
            A[i],A[idx]=A[idx],A[i];a=A[i][j]
            for k in range(j,len(A[i])):A[i][k]/=a
            for h in range(len(A)):
                if h==i:continue
                b=A[h][j]
                if b:
                    for k in range(j,len(A[h])):A[h][k]-=b*A[i][k]
            i+=1
            if i==len(A):break
        return i
    assert rational_rank(rows)==6

# The remaining dimension-six invariant sector has two triple eigenvalues.
# Their sum S and sum-of-squares T follow from traces of K and K^2;
# their product is (S^2-T)/2. This avoids floating-point eigensolvers.
def components(k,u,v,w):
    if k%2==0:
        l1=1+4*u+3*v+4*w
        l2=1+u-2*w
        l3=1-u-2*v+2*w
    else:
        l1=1-v-4*w
        l2=1-3*u+2*v+2*w
        l3=1-u-2*w
    S=(12-l1-2*l2-3*l3)/3
    trace2=12+48*u*u+36*v*v+48*w*w
    T=(trace2-l1*l1-2*l2*l2-3*l3*l3)/3
    P=(S*S-T)/2
    return l1,l2,l3,S,P

# Verify the quadratic spectral factor on the six-dimensional orthogonal
# complement as an identity in the three Legendre parameters, not only at
# finitely many harmonic degrees. The ten test triples are unisolvent for
# polynomials of total degree at most two.
def nullspace_rows(A):
    A=[[F(v) for v in row] for row in A]
    n=len(A[0]); pivots=[]; i=0
    for j in range(n):
        idx=next((h for h in range(i,len(A)) if A[h][j]),None)
        if idx is None:continue
        A[i],A[idx]=A[idx],A[i]
        z=A[i][j]
        A[i]=[a/z for a in A[i]]
        for h in range(len(A)):
            if h!=i:
                z=A[h][j]
                if z:A[h]=[a-z*b for a,b in zip(A[h],A[i])]
        pivots.append(j); i+=1
        if i==len(A):break
    free=[j for j in range(n) if j not in pivots]
    return [[(F(1) if j==f else F(0)) if j in free else -A[pivots.index(j)][f]
             for j in range(n)] for f in free]

def mulmat(M,v):
    return [sum((M[i][j]*v[j] for j in range(12)),Q2()) for i in range(12)]

def check_quadratic_identity():
    triples=[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(2,0,0),
             (0,2,0),(0,0,2),(1,1,0),(1,0,1),(0,1,1)]
    for par in (0,1):
        B=sum((basis for _,basis in sectors[par]),[])
        complement=nullspace_rows(B)
        assert len(complement)==6
        for u,v,w in triples:
            l1,l2,l3,S,P=components(0 if par==0 else 1,Q2(u),Q2(v),Q2(w))
            M=relations[par]
            for x0 in complement:
                x=list(map(Q2,x0))
                Kx=[x[i]+u*sum(M[0][i][j]*x[j] for j in range(12))
                      +v*sum(M[1][i][j]*x[j] for j in range(12))
                      +w*sum(M[2][i][j]*x[j] for j in range(12)) for i in range(12)]
                K2x=[Kx[i]+u*sum(M[0][i][j]*Kx[j] for j in range(12))
                       +v*sum(M[1][i][j]*Kx[j] for j in range(12))
                       +w*sum(M[2][i][j]*Kx[j] for j in range(12)) for i in range(12)]
                assert all(K2x[i]-S*Kx[i]+P*x[i]==0 for i in range(12))
check_quadratic_identity()

def roots_above(S,P,c):
    return S-2*c>0 and P-c*S+c*c>0

def roots_below(S,P,c):
    return 2*c-S>0 and c*c-c*S+P>0

def nonnegative_root_count(S,P):
    assert S.sign()>=0 and P.sign()>=0
    if P==0:return 0 if S==0 else 1
    return 2

pminus=[ONE]*3
pcurrent=list(theta)
small_ranks=[1,3,5,7,9,11]
for k in range(200):
    if k==0:pvals=pminus
    elif k==1:pvals=pcurrent
    else:
        pnext=[((2*k-1)*theta[i]*pcurrent[i]-(k-1)*pminus[i])/k for i in range(3)]
        pminus,pcurrent=pcurrent,pnext
        pvals=pnext
    l1,l2,l3,S,P=components(k,*pvals)
    assert all(x.sign()>=0 for x in (l1,l2,l3))
    nr=nonnegative_root_count(S,P)
    rank=(l1.sign()>0)+2*(l2.sign()>0)+3*(l3.sign()>0)+3*nr
    if k<=5: assert rank==small_ranks[k],(k,rank)
    if k==9:
        assert rank==10 and l2==0 and all(x>0 for x in (l1,l3,S,P))
    if k>=6 and k!=9:
        assert rank==12,(k,rank)
    if k>=6 and k not in (9,13,14):
        bound=Q2(F(1,50))
        assert all(x>bound for x in (l1,l2,l3)) and roots_above(S,P,bound),('lower',k)
    if k==13:
        bound=Q2(F(1,300))
        assert all(x>bound for x in (l1,l2,l3)) and roots_above(S,P,bound)
    if k==14:
        assert l1>0 and all(x>l1 for x in (l2,l3)) and roots_above(S,P,l1)
        assert all(l3>x for x in (l1,l2)) and roots_below(S,P,l3)
        assert l3>90000*l1
        print('degree14_min',l1)
        print('degree14_max',l3)
    if k in (5,9,13,14,199):print('degree',k,'rank',rank,'checks_passed')
print('RHOMBICUBOCTAHEDRON_SAMPLING_CERTIFICATE_OK 200 exact degrees')
