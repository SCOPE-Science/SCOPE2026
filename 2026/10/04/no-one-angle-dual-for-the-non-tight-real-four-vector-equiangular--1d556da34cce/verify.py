from fractions import Fraction as F
from itertools import product, permutations

class R:
    __slots__=('a','b')
    def __init__(self,a=0,b=0): self.a=F(a); self.b=F(b)
    def __add__(self,o): o=C(o); return R(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return R(-self.a,-self.b)
    def __sub__(self,o): return self+(-C(o))
    def __rsub__(self,o): return C(o)-self
    def __mul__(self,o):
        o=C(o); return R(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        d=self.a*self.a-5*self.b*self.b
        assert d != 0
        return R(self.a/d,-self.b/d)
    def __truediv__(self,o): return self*C(o).inv()
    def __eq__(self,o): o=C(o); return self.a==o.a and self.b==o.b
    def __bool__(self): return self.a!=0 or self.b!=0
    def __repr__(self): return f'({self.a})+({self.b})*sqrt5'

def C(x): return x if isinstance(x,R) else R(x)
Z=R(0); O=R(1); S=R(0,1)

def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Z) for j in range(len(B[0]))] for i in range(len(A))]
def mt(A): return [list(x) for x in zip(*A)]
def madd(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def eye(n): return [[O if i==j else Z for j in range(n)] for i in range(n)]
def det(A):
    A=[row[:] for row in A]; n=len(A); out=O
    for c in range(n):
        p=next((r for r in range(c,n) if A[r][c]),None)
        if p is None: return Z
        if p!=c: A[c],A[p]=A[p],A[c]; out=-out
        piv=A[c][c]; out=out*piv
        for r in range(c+1,n):
            if A[r][c]:
                q=A[r][c]/piv
                for j in range(c,n): A[r][j]=A[r][j]-q*A[c][j]
    return out

def rref_solve(A,b,nvar):
    M=[A[i][:]+[b[i]] for i in range(len(A))]
    r=0; piv=[]
    for c in range(nvar):
        p=next((i for i in range(r,len(M)) if M[i][c]),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        q=M[r][c]
        M[r]=[x/q for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]:
                q=M[i][c]; M[i]=[M[i][j]-q*M[r][j] for j in range(nvar+1)]
        piv.append(c); r+=1
    for row in M:
        if all(not row[c] for c in range(nvar)) and row[nvar]: return None
    assert len(piv)==nvar
    x=[Z]*nvar
    for i,c in enumerate(piv): x[c]=M[i][nvar]
    return x

def mat_eq(A,B): return all(A[i][j]==B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def scale(A,c): return [[c*x for x in row] for row in A]

# Canonical mixed switching class.
Q=[[R(0),R(1),R(1),R(1)],
   [R(1),R(0),R(1),R(-1)],
   [R(1),R(1),R(0),R(-1)],
   [R(1),R(-1),R(-1),R(0)]]
G=madd(eye(4),scale(Q,S/R(5))) # 1/sqrt(5)=sqrt(5)/5
z=[R(-1), (S-R(1))/R(2), (S-R(1))/R(2), R(1)]
# Exact Moore-Penrose inverse of G (verified below algebraically).
K=[[R(F(3,4),F(-3,20)), R(0,F(1,20)), R(0,F(1,20)), R(F(1,2),F(-1,10))],
   [R(0,F(1,20)), R(F(3,4),F(3,20)), R(F(-1,2),F(-1,10)), R(0,F(-1,20))],
   [R(0,F(1,20)), R(F(-1,2),F(-1,10)), R(F(3,4),F(3,20)), R(0,F(-1,20))],
   [R(F(1,2),F(-1,10)), R(0,F(-1,20)), R(0,F(-1,20)), R(F(3,4),F(-3,20))]]
assert mat_eq(mm(mm(G,K),G),G)
assert mat_eq(mm(mm(K,G),K),K)
assert mat_eq(mm(G,K),mm(K,G))
assert all(sum((G[i][j]*z[j] for j in range(4)),Z)==Z for i in range(4))

# Classification of switched 4x4 real signature matrices: +++, ---, and six mixed.
def traces_int(Qi,k):
    A=[[R(int(x)) for x in row] for row in Qi]
    P=eye(4)
    for _ in range(k): P=mm(P,A)
    return sum((P[i][i] for i in range(4)),Z)
def charpoly_coeffs(Qi):
    # Newton identities for x^4+c1 x^3+c2 x^2+c3 x+c4.
    p=[None]+[traces_int(Qi,k) for k in range(1,5)]
    c=[O]
    for k in range(1,5):
        sm=p[k]
        for i in range(1,k): sm=sm+c[i]*p[k-i]
        c.append(-sm/R(k))
    return c[1:]
classes={}
for a,b,c in product([1,-1],repeat=3):
    Qi=[[0,1,1,1],[1,0,a,b],[1,a,0,c],[1,b,c,0]]
    coeff=charpoly_coeffs(Qi)
    key=tuple((x.a,x.b) for x in coeff)
    classes.setdefault(key,[]).append((a,b,c))
assert sorted(map(len,classes.values()))==[1,1,6]
# Expected polynomials: (x-3)(x+1)^3; (x+3)(x-1)^3; (x^2-1)(x^2-5).
expected={
    ((F(0),F(0)),(F(-6),F(0)),(F(-8),F(0)),(F(-3),F(0))),
    ((F(0),F(0)),(F(-6),F(0)),(F(8),F(0)),(F(-3),F(0))),
    ((F(0),F(0)),(F(-6),F(0)),(F(0),F(0)),(F(5),F(0)))
}
assert set(classes)==expected
# The six mixed normalized signatures form one signed-permutation orbit.
def canon_norm(Qi):
    # switch so first row is positive
    d=[1]+[Qi[0][j] for j in range(1,4)]
    return tuple(tuple(d[i]*Qi[i][j]*d[j] for j in range(4)) for i in range(4))
def permute(Qi,p): return [[Qi[p[i]][p[j]] for j in range(4)] for i in range(4)]
Qc=[[int(x.a) for x in row] for row in Q]
orb=set()
for p in permutations(range(4)):
    orb.add(canon_norm(permute(Qc,p)))
mixed=set()
for a,b,c in product([1,-1],repeat=3):
    if (a,b,c) not in [(1,1,1),(-1,-1,-1)]:
        mixed.add(tuple(tuple(x for x in row) for row in [[0,1,1,1],[1,0,a,b],[1,a,0,c],[1,b,c,0]]))
assert mixed.issubset(orb) and len(mixed)==6

# A one-angle dual U would have Gram H=U^T U with rank <=3 and GHG=G.
# Every symmetric generalized inverse has H=K+z a^T+a z^T.  Fix the
# first off-diagonal sign and enumerate the 32 relative sign patterns.
edges=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
consistent=[]
for bits in product([1,-1],repeat=5):
    eps=(1,)+bits
    A=[]; rhs=[]
    for e,(i,j) in enumerate(edges):
        row=[Z for _ in range(5)]
        row[j]=row[j]+z[i]
        row[i]=row[i]+z[j]
        row[4]=row[4]-R(eps[e]) # beta coefficient
        A.append(row); rhs.append(-K[i][j])
    sol=rref_solve(A,rhs,5)
    if sol is None: continue
    av=sol[:4]; beta=sol[4]
    H=[[K[i][j]+z[i]*av[j]+av[i]*z[j] for j in range(4)] for i in range(4)]
    # All six off diagonals have one modulus/sign pattern, and generalized-inverse identity holds.
    assert all(H[i][j]==beta*R(eps[e]) for e,(i,j) in enumerate(edges))
    assert mat_eq(mm(mm(G,H),G),G)
    d=det(H)
    assert d != Z  # impossible for a Gram matrix of four vectors in R^3
    consistent.append((''.join('+' if x==1 else '-' for x in eps),beta,d))
assert len(consistent)==12
print('VERIFY_OK signature_classes=1,1,6 one_angle_patterns=32 inconsistent=20 full_rank_candidates=12')
for word,beta,d in consistent:
    print(word,'beta=',beta,'det=',d)
