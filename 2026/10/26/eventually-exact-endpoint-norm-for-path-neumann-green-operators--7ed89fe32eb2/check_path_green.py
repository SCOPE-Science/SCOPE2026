"""Independent finite rational checks for the path Neumann Green identities.
The checker does not certify infinite-dimensional or eventual assertions."""
from fractions import Fraction as Q
from math import isqrt, sqrt

def green(n,i,j):
    s=lambda k:k*k+(1-n)*k+n*(n-1)//2
    return -Q(abs(i-j),2)+Q(s(i)+s(j),2*n)-Q(n*n-1,6*n)

def continuum(x,y):
    return -abs(x-y)/2+(x*x-x+y*y-y)/2+Q(1,3)

checks=0
for n in range(2,81):
    rows=[]
    for i in range(n):
        row=[green(n,i,j) for j in range(n)]
        assert sum(row)==0; checks+=1
        for j in range(n):
            x,y=Q(2*i+1,2*n),Q(2*j+1,2*n)
            assert row[j]/n == continuum(x,y)-Q(1,12*n*n);checks+=1
            assert row[j]==green(n,j,i);checks+=1
            lg=(row[j]-row[j-1] if j==n-1 else 0)
        rows.append(row)
    for i in range(n):
        for j in range(n):
            lap=(rows[0][j]-rows[1][j]) if i==0 else ((rows[n-1][j]-rows[n-2][j]) if i==n-1 else 2*rows[i][j]-rows[i-1][j]-rows[i+1][j])
            assert lap == (1 if i==j else 0)-Q(1,n);checks+=1
    norms=[sum(map(abs,row)) for row in rows]
    assert norms==norms[::-1];checks+=1
    assert norms[0]>=max(norms);checks+=1  # finite examples only
    # Fully exact endpoint-sum formula and sign index by rational inequality.
    positive=[j for j in range(n) if rows[0][j]>=0]
    assert positive==list(range(len(positive))); checks+=1
    m=len(positive)-1
    rhs=Q((m+1)*(m*(m-3*n+2)+2*n*n-3*n+1),3*n)
    assert norms[0]==rhs;checks+=1
    assert abs(float(norms[0])-2*n*n/(9*sqrt(3)))<1.025;checks+=1
    for k in range(min(6,n)):
        if k>0 and n>40:
            assert abs(float(norms[0]-norms[k])-k*(k+1)/sqrt(3))<3;checks+=1
print('PASS',checks,'exact-rational/equality assertions and bounded numerical checks')
