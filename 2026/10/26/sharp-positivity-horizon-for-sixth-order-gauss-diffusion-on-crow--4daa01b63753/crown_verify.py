"""Exact certificate and finite matrix checks for the 3-stage Gauss heat step on crown graphs.
Python 3 standard library only. Run: python crown_verify.py
The coefficient-positivity verification is an identity in two indeterminates,
not a finite parameter scan. Numerical eigenvalue tests are not used.
"""
from fractions import Fraction as F
from collections import defaultdict

def add(*arr):
    out=defaultdict(int)
    for a in arr:
        for k,v in a.items():out[k]+=v
    return {k:v for k,v in out.items() if v}
def mul(a,b):
    out=defaultdict(int)
    for (i,j),x in a.items():
        for (k,l),y in b.items():out[(i+k,j+l)]+=x*y
    return {k:v for k,v in out.items() if v}
def neg(a):return {k:-v for k,v in a.items()}
def scale(a,k):return {ij:k*v for ij,v in a.items()}
def power(a,k):
    out={(0,0):1}
    for _ in range(k):out=mul(out,a)
    return out
I={(0,0):1};U={(1,0):1};H={(0,1):1}
n=add(U,scale(I,2)); nm2=U; nm1=add(U,I)
a=mul(n,H);b=mul(nm2,H);c=scale(mul(nm1,H),2)
def P(z):return add(scale(I,120),scale(z,-60),scale(power(z,2),12),neg(power(z,3)))
def Q(z):return add(scale(I,120),scale(z,60),scale(power(z,2),12),power(z,3))
pa,pb,pc=P(a),P(b),P(c);qa,qb,qc=Q(a),Q(b),Q(c)
D=mul(mul(qa,qb),qc)
terms=[D,mul(pc,mul(qa,qb)),mul(pa,mul(qb,qc)),mul(pb,mul(qa,qc))]
within=add(terms[0],terms[1],neg(terms[2]),neg(terms[3]))
matched=add(terms[0],neg(terms[1]),mul(nm1,add(terms[2],neg(terms[3]))))
cross=add(terms[0],neg(terms[1]),neg(terms[2]),terms[3])
for label,C,lowest in [('within',within,2),('matched',matched,3),('cross',cross,1)]:
    assert C and all(v>0 for v in C.values()),(label,[(ij,x) for ij,x in C.items() if x<=0])
    assert min(j for i,j in C)==lowest
    assert all(i>=0 and j>=lowest for (i,j) in C)
    print('SYMBOLIC_CERTIFICATE',label,'positive_monomials',len(C),'time_orders',lowest,'through',max(j for i,j in C))

def rat(z):return F(120-60*z+12*z*z-z**3,120+60*z+12*z*z+z**3)
def prod(A,B):
    n=len(A);return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def inverse(A):
    n=len(A);W=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        k=next(i for i in range(j,n) if W[i][j]);W[k],W[j]=W[j],W[k]
        z=W[j][j];W[j]=[a/z for a in W[j]]
        for i in range(n):
            if i!=j:
                z=W[i][j];W[i]=[a-z*b for a,b in zip(W[i],W[j])]
    return [row[n:] for row in W]
def laplacian(n):
    m=2*n;A=[[F(0) for j in range(m)] for i in range(m)]
    for i in range(n):
        for j in range(n):
            if i!=j:A[i][n+j]=A[n+j][i]=-1
    for i in range(m):A[i][i]=n-1
    return A
def step(L,t):
    m=len(L);Z=[[F(i==j) for j in range(m)] for i in range(m)]
    X=[[t*x for x in row] for row in L];Y=prod(X,X);V=prod(X,Y)
    P=[[120*Z[i][j]-60*X[i][j]+12*Y[i][j]-V[i][j] for j in range(m)] for i in range(m)]
    Q=[[120*Z[i][j]+60*X[i][j]+12*Y[i][j]+V[i][j] for j in range(m)] for i in range(m)]
    return prod(inverse(Q),P)
def formula(n,t):
    x=rat(n*t);y=rat((n-2)*t);z=rat((2*n-2)*t)
    diag=(1+z+(n-1)*(x+y))/F(2*n)
    within=(1+z-x-y)/F(2*n)
    matched=(1-z+(n-1)*(x-y))/F(2*n)
    cross=(1-z-x+y)/F(2*n)
    m=2*n
    return [[diag if i==j else within if (i<n)==(j<n) else matched if (i%n)==(j%n) else cross for j in range(m)] for i in range(m)]
checks=0
for n in range(3,9):
    L=laplacian(n)
    for t in [F(0),F(1,12),F(1,3),F(1),F(3),F(10)]:
        T=step(L,t);A=formula(n,t)
        assert T==A,(n,t,'formula')
        assert all(sum(row)==1 for row in T)
        if t:assert all(T[i][j]>0 for i in range(2*n) for j in range(2*n) if i!=j)
        checks+=1
print('MATRIX_CHECKS',checks,'exact complete rational matrices')

def Rf(z):return (120-60*z+12*z*z-z**3)/(120+60*z+12*z*z+z**3)
def horizon(n):
    def diag(h):return (1+Rf((2*n-2)*h)+(n-1)*(Rf(n*h)+Rf((n-2)*h)))/(2*n)
    lo,hi=0.,1.
    while diag(hi)>0:hi*=2
    for _ in range(65):
        md=(lo+hi)/2
        if diag(md)>0:lo=md
        else:hi=md
    assert diag(lo)>-1e-14 and diag(hi)<1e-14
    return (lo+hi)/2
for n in (3,4,5,6,8,10,20,50,200):print('HORIZON',n,format(horizon(n),'.13f'))
print('OK')
