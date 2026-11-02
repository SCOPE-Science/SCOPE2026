"""Self-contained exact checks for priced spanning-tree allocation on balanced multipartite graphs."""
from fractions import Fraction as F
from math import comb, sqrt
import random

def tree_formula(r,m,x,y):
    a=(r-1)*(m-1); b=r-2
    return F((r-1)**(m-1)*m**(r*m-2))*x**m*(x+(r-2)*y)**a*(x+(r-1)*y)**b

def determinant(mat):
    n=len(mat)
    a=[[F(v) for v in row] for row in mat]
    out=F(1)
    for j in range(n):
        k=next((i for i in range(j,n) if a[i][j]),None)
        if k is None: return F(0)
        if j!=k: a[j],a[k]=a[k],a[j];out=-out
        pivot=a[j][j];out*=pivot
        for i in range(j+1,n):
            if a[i][j]:
                z=a[i][j]/pivot
                for l in range(j+1,n): a[i][l]-=z*a[j][l]
                a[i][j]=F(0)
    return out

def tree_minor(r,m,x,y):
    n=r*m; a=[[F(0) for j in range(n-1)] for i in range(n-1)]
    for i in range(n):
      for j in range(i+1,n):
        ci=i//m;cj=j//m
        if ci==cj:continue
        w=x if (ci==0 or cj==0) else y
        if i<n-1:a[i][i]+=w
        if j<n-1:a[j][j]+=w
        if i<n-1 and j<n-1:a[i][j]-=w;a[j][i]-=w
    return determinant(a)

def polynomial_coefs(r,m,P,Q):
    C=2*P*m*(r-1)-Q*(r*m-1)
    L=2*P*(r-1)*(m*(r-1)-1)-Q*(m*(r*r-2)-2*r+3)
    A=Q*m*(r-2)*(r-1)
    return C,L,A

def directional_log_derivative(r,m,P,Q,t):
    # Numerator differentiated with cost normalization, scaled by positive factors
    a=(r-1)*(m-1);b=r-2; n=r*m-1
    return (a*(r-2)/(1+(r-2)*t)+b*(r-1)/(1+(r-1)*t)-n*(r-2)*Q/(2*P+(r-2)*Q*t))

checks=0
for r in range(3,7):
    for m in range(2,6):
        if r*m>16: continue
        for x,y in [(F(1),F(1)),(F(2,3),F(1,4)),(F(3,2),F(0))]:
            actual=tree_minor(r,m,x,y)
            predicted=tree_formula(r,m,x,y)
            assert actual==predicted,(r,m,x,y,actual,predicted)
            checks+=1

from fractions import Fraction as F
for r in range(3,10):
    for m in range(2,9):
      for P in (F(1),F(2,3),F(7,5)):
       for Q in (F(1,3),F(1),F(11,6),F(10)):
        C,L,A=polynomial_coefs(r,m,P,Q)
        boundary= F(2*m*(r-1),r*m-1)
        assert (C>0)==(Q/P<boundary)
        assert (C==0)==(Q/P==boundary)
        assert A>0
        for t in (F(0),F(1,7),F(1,2),F(1),F(7,3),F(11)):
            v=directional_log_derivative(r,m,P,Q,t)
            pol=C+L*t-A*t*t
            assert (v>0)==(pol>0),(r,m,P,Q,t,v,pol)
            assert (v<0)==(pol<0)
            checks+=2
        if C>0:
            root=(float(L)+sqrt(float(L*L+4*A*C)))/(2*float(A))
            assert root>0 and abs(float(C+L*F(root)-A*F(root)**2))<1e-5*(abs(float(C))+abs(float(L))*root+abs(float(A))*root**2)
            checks+=1
        else:
            assert directional_log_derivative(r,m,P,Q,F(0))<=0
            checks+=1


# Independent off-orbit perturbations, with exact rational determinants.
def independent_tree(r,m,weighted_edges):
    n=r*m; a=[[F(0) for _ in range(n-1)] for _ in range(n-1)]
    for u,v,w in weighted_edges:
        if u<n-1:a[u][u]+=w
        if v<n-1:a[v][v]+=w
        if u<n-1 and v<n-1:a[u][v]-=w;a[v][u]-=w
    return determinant(a)

rng=random.Random(47)
for r,m,P,Q in [(3,2,F(1),F(1)),(3,2,F(1),F(2)),(4,2,F(1),F(1)),(4,2,F(1),F(2))]:
    edges=[(u,v) for u in range(r*m) for v in range(u+1,r*m) if u//m!=v//m]
    prices=[P if u//m==0 or v//m==0 else Q for u,v in edges]
    cstar=F(1) if P==Q else F(0)
    bud=sum(pr*(F(1) if u//m==0 or v//m==0 else cstar) for (u,v),pr in zip(edges,prices))
    target=tree_formula(r,m,F(1),cstar)
    assert independent_tree(r,m,[(u,v,F(1) if u//m==0 or v//m==0 else cstar) for u,v in edges])==target
    checks+=1
    for k in range(30):
        vals=[F(rng.randrange(1,11),rng.randrange(1,7)) for _ in edges]
        z=bud/sum(v*pr for v,pr in zip(vals,prices))
        value=independent_tree(r,m,[(u,v,z*weight) for (u,v),weight in zip(edges,vals)])
        assert 0<value<target,(r,m,P,Q,k,value,target)
        checks+=1

print('PASS',checks,'exact determinant, derivative, threshold, root, and unrestricted asymmetric tests')

