from fractions import Fraction as F
from itertools import product
from math import factorial

def det(A):
    n=len(A)
    if n==1: return A[0][0]
    return sum(((-1)**j)*A[0][j]*det([row[:j]+row[j+1:] for row in A[1:]]) for j in range(n))

def check(n,m=30):
    c=F(m*m-1,m*m+1); s=F(2*m,m*m+1)
    V = {}
    for i in range(n):
        for sign in (-1,1):
            p=[F(0)]*n;p[i]+=sign*c;p[(i+1)%n]+=s
            V[i,sign]=p
    # Every sign-selected simplex is an exposed facet; opposite vertices lie strictly inside its plane.
    min_slack=None
    for signs in product((-1,1),repeat=n):
        A=[V[i,signs[i]] for i in range(n)]
        detA=det(A)
        assert detA
        normal=[]
        for j in range(n):
            B=[row[:] for row in A]
            for k in range(n):B[k][j]=F(1)
            normal.append(det(B)/detA)
        assert all(sum(A[i][j]*normal[j] for j in range(n))==1 for i in range(n))
        for i in range(n):
            val=sum(V[i,-signs[i]][j]*normal[j] for j in range(n))
            assert val<1,(n,m,signs,i,val)
            slack=1-val
            min_slack=slack if min_slack is None or slack<min_slack else min_slack
    assert c>2*s
    # Here W=cI. Exact equality for the nonlinear deficit; D is the Procrustes loss.
    D=4*n*(1-c)
    peak=F(2**n,factorial(n))
    volume=peak*c**n
    assert peak-volume==peak*(1-(1-D/F(4*n))**n)
    return (n,str(c),str(s),str(D),str(volume),str(min_slack))
for n in range(2,7):
 print(check(n))
