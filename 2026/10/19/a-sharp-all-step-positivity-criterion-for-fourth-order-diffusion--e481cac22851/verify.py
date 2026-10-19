"""Exact-arithmetic checks for the three-Laplacian-eigenvalue Padé positivity theorem.
Independent rational matrix identities; no floating-point spectral decisions.
"""
from fractions import Fraction as F
from itertools import combinations, product

def zero(n):
    return [[F(0) for _ in range(n)] for _ in range(n)]
def eye(n):
    x=zero(n)
    for i in range(n):x[i][i]=1
    return x
def mul(A,B):
    n=len(A);m=len(B[0]);k=len(B)
    return [[sum((A[i][t]*B[t][j] for t in range(k)),F(0)) for j in range(m)] for i in range(n)]
def add(A,B,c=1):
    return [[A[i][j]+c*B[i][j] for j in range(len(A))] for i in range(len(A))]
def scale(A,c):
    return [[v*c for v in r] for r in A]
def lap(n,edges):
    L=zero(n)
    for u,v,w in edges:
        w=F(w); assert w>0 and u!=v
        L[u][u]+=w;L[v][v]+=w;L[u][v]-=w;L[v][u]-=w
    return L
def inverse(A):
    n=len(A);M=[A[i][:]+eye(n)[i] for i in range(n)]
    for col in range(n):
        piv=next(j for j in range(col,n) if M[j][col])
        M[piv],M[col]=M[col],M[piv]
        q=M[col][col];M[col]=[x/q for x in M[col]]
        for row in range(n):
            if row==col:continue
            q=M[row][col]
            if q:M[row]=[M[row][j]-q*M[col][j] for j in range(2*n)]
    return [r[n:] for r in M]
def petersen():
    v=list(combinations(range(5),2));return len(v),[(i,j,1) for i in range(10) for j in range(i+1,10) if not(set(v[i])&set(v[j]))]
def triangular(m):
    v=list(combinations(range(m),2));return len(v),[(i,j,1) for i in range(len(v)) for j in range(i+1,len(v)) if len(set(v[i])&set(v[j]))==1]
def rook(m):
    v=list(product(range(m),repeat=2));return len(v),[(i,j,1) for i in range(len(v)) for j in range(i+1,len(v)) if v[i][0]==v[j][0] or v[i][1]==v[j][1]]
def paley(q):
    residues={k*k%q for k in range(1,q)};return q,[(i,j,1) for i in range(q) for j in range(i+1,q) if (i-j)%q in residues]
def cycle(n):return n,[(i,(i+1)%n,1) for i in range(n)]
def bipartite(p,q):return p+q,[(i,p+j,1) for i in range(p) for j in range(q)]
def star(n,w):return n,[(0,j,w) for j in range(1,n)]
def triangle(a,b,c):return 3,[(0,1,a),(0,2,b),(1,2,c)]
def srg_parameters(n,edges):
    W=zero(n)
    for i,j,w in edges:
        assert w==1
        W[i][j]=W[j][i]=1
    degrees=[sum(r) for r in W];assert len(set(degrees))==1
    k=degrees[0];l=[];mu=[]
    for i in range(n):
        for j in range(i+1,n):
            z=sum((W[i][t]*W[t][j] for t in range(n)),F(0))
            (l if W[i][j] else mu).append(z)
    assert l and mu and len(set(l))==len(set(mu))==1
    return int(k),int(l[0]),int(mu[0])

CASES=[]
for name,fn,args in [('Petersen',petersen,()),('Triangular5',triangular,(5,)),('Triangular6',triangular,(6,)),('Triangular7',triangular,(7,)),('Rook3',rook,(3,)),('Rook4',rook,(4,)),('Paley5',paley,(5,)),('Paley13',paley,(13,)),('Cycle5',cycle,(5,)),('K3,3',bipartite,(3,3))]:
    n,edges=fn(*args)
    k,la,mu=srg_parameters(n,edges)
    s=F(2*k-la+mu);p=F(n*mu)
    CASES.append((name,n,edges,s,p))
for n,w in [(4,F(1)),(5,F(3,2)),(7,F(2,3))]:
    N,e=star(n,w);CASES.append(('Star'+str(n),N,e,F(n+1)*w,F(n)*w*w))
for a,b,c in [(5,1,1),(1,2,7),(2,3,5),(3,4,4)]:
    N,e=triangle(a,b,c);CASES.append(('Triangle'+str((a,b,c)),N,e,F(2*(a+b+c)),F(3*(a*b+a*c+b*c))))
# All the following cases satisfy exactly the quadratic Laplacian spectral identity.
count=0
for name,n,edges,s,p in CASES:
    L=lap(n,edges);L2=mul(L,L);I=eye(n)
    for i in range(n):
        for j in range(n):
            residual=L2[i][j]-s*L[i][j]+p*(I[i][j]-F(1,n))
            assert residual==0,(name,i,j,residual)
            count+=1
    assert s*s>4*p>0
    for h in [F(0),F(1,25),F(1,4),F(1),F(2),F(3),F(4),F(10),F(100)]:
        Q=add(add(scale(I,12),scale(L,6*h)),scale(L2,h*h))
        R=add(add(scale(I,12),scale(L,-6*h)),scale(L2,h*h))
        den=144+72*s*h+12*(s*s+p)*h*h+6*p*s*h**3+p*p*h**4
        assert den>0
        T=zero(n)
        maxw=max(F(w) for _,_,w in edges)
        for i in range(n):
            for j in range(n):
                if i==j:continue
                w=-L[i][j]
                f=12*w+6*h*p/F(n)+h*h*p*(s/F(n)-w)
                T[i][j]=12*h*f/den
                assert (T[i][j]>=0)==(f>=0 or h==0)
                count+=2
            T[i][i]=1-sum(T[i][j] for j in range(n) if j!=i)
            assert T[i][i]>0
            assert sum(T[i],F(0))==1
            count+=2
        # Independent check by multiplication, not spectral decomposition.
        prod=mul(Q,T)
        for i in range(n):
            for j in range(n):
                assert prod[i][j]==R[i][j],(name,h,i,j,prod[i][j]-R[i][j]);count+=1
        if n<=10 and h in (F(1,4),F(1),F(4)):
            Ti=mul(inverse(Q),R)
            for i in range(n):
                for j in range(n):
                    assert T[i][j]==Ti[i][j];count+=1
        # Sign of the numerically exact worst edge agrees with the global cut.
        fmax=12*maxw+6*h*p/F(n)+h*h*p*(s/F(n)-maxw)
        if h>0:
            assert (min(T[i][j] for i in range(n) for j in range(n) if i!=j)>=0)==(fmax>=0)
            count+=1
    if name in ('Petersen','Triangular7','Rook4','Paley13','Triangular6','Star5','Triangle(5, 1, 1)'):
        print(name,'n',n,'s',s,'p',p,'critical edge weight',s/F(n),'max edge',max(F(w) for _,_,w in edges))
print('VERIFY_OK',count,'exact rational identities/inequalities',len(CASES),'weighted graph instances')
