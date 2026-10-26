"""Standalone checks for sharp wheel-graph Green norms and lattice-phase asymptotics.
Only standard-library Python is required. Analytical proof is in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt, log, cos, pi


def inverse(M):
    n=len(M)
    a=[[F(M[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        k=next(i for i in range(j,n) if a[i][j])
        a[j],a[k]=a[k],a[j]
        v=a[j][j]
        a[j]=[x/v for x in a[j]]
        for i in range(n):
            if i==j: continue
            v=a[i][j]
            if v: a[i]=[x-v*y for x,y in zip(a[i],a[j])]
    return [r[n:] for r in a]


def laplacian(m):
    N=m+1
    L=[[F(0) for _ in range(N)] for _ in range(N)]
    edges={(min(i,(i+1)%m),max(i,(i+1)%m)) for i in range(m)}
    edges.update((i,m) for i in range(m))
    for i,j in edges:
        L[i][j]=L[j][i]=F(-1)
        L[i][i]+=1
        L[j][j]+=1
    return L


def rational_green(m):
    L=laplacian(m); N=m+1
    H=inverse([[L[i][j]+F(1,N) for j in range(N)] for i in range(N)])
    return [[H[i][j]-F(1,N) for j in range(N)] for i in range(N)]


def exact_row_formula(m):
    A=[[F(3 if i==j else 0)-F(j in {(i-1)%m,(i+1)%m}) for j in range(m)] for i in range(m)]
    Ainv=inverse(A)
    c=F(m+2,(m+1)**2)
    return F(2)*sum(max(F(0),Ainv[0][d]-c) for d in range(m)), Ainv


def analytic_formula(m):
    q=(3-sqrt(5))/2
    c=(m+2)/(m+1)**2
    B=[(q**d+q**(m-d))/(sqrt(5)*(1-q**m)) for d in range(m)]
    return 2*sum(max(0,x-c) for x in B)


def asymptotic(m):
    q=(3-sqrt(5))/2; a=-log(q)
    T=log(m/sqrt(5))/a
    u=T-int(T)
    phi=2-4*u+4*q**(1-u)/(1-q)
    return 2-(4*T+phi)/m

checks=0
for m in range(3,18):
    G=rational_green(m)
    e,A=exact_row_formula(m)
    hub=F(2*m,(m+1)**2)
    assert all(sum(r)==0 for r in G)
    assert all(G[i][j]==G[j][i] for i in range(m+1) for j in range(m+1))
    for i in range(m):
        for j in range(m):
            assert G[i][j]==A[i][j]-F(m+2,(m+1)**2)
            checks+=1
        assert G[i][m]==-F(1,(m+1)**2)
        checks+=1
    assert G[m][m]==F(m,(m+1)**2)
    row_norms=[sum(abs(x) for x in row) for row in G]
    assert all(v==e for v in row_norms[:m])
    assert row_norms[m]==hub and e>=hub
    assert abs(float(e)-analytic_formula(m))<1e-11
    checks+=5
for m in range(18,300):
    q=(3-sqrt(5))/2
    c=(m+2)/(m+1)**2
    an=analytic_formula(m)
    # Independent diagonalization of 3I - shift - inverse shift.
    if m<=65:
        row=[sum(cos(2*pi*j*d/m)/(3-2*cos(2*pi*j/m)) for j in range(m))/m for d in range(m)]
        numeric=2*sum(max(0,v-c) for v in row)
        assert abs(numeric-an)<3e-12
        checks+=1
    if m>=25:
        # Error is O(m^-2), so m^2 times the error remains bounded.
        assert m*m*abs(an-asymptotic(m))<10
        checks+=1
for m in [100,200,500,1000,2000,5000,10000,50000]:
    an=analytic_formula(m)
    assert m*m*abs(an-asymptotic(m))<10
    checks+=1
print('PASS',checks,'exact-entry and independent numerical/asymptotic checks')
print('m=3,5,10,50,500 norms:',[(m,round(analytic_formula(m),12)) for m in [3,5,10,50,500]])
