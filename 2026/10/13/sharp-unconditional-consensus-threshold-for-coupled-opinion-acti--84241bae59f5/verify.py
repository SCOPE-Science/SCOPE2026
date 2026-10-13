"""Reproducibility checks for an opinion--action consensus barrier.

Requires only the Python standard library. Finite tests support, but do not
replace, the all-network mathematical proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
import random


def matrix(n, phi, masks):
    """One-step state matrix on (opinion, action) for prescribed neighbor sets."""
    q = F(1) - phi
    z = [[F(0) for _ in range(2*n)] for __ in range(2*n)]
    for i in range(n):
        neighbors = [j for j in range(n) if j != i and masks[i][j]]
        k = len(neighbors)
        z[i][i] = F(1, k+1)
        for j in neighbors:
            z[i][n+j] += F(1, k+1)
        for j in range(2*n):
            z[n+i][j] += phi*z[i][j]
        for j in range(n):
            z[n+i][n+j] += q/F(n)
    return z


def multiply(a,b):
    n=len(a)
    return [[sum((a[i][k]*b[k][j] for k in range(n)),F(0))
             for j in range(n)] for i in range(n)]


def masks_for(n):
    edge=[(i,j) for i in range(n) for j in range(n) if i!=j]
    for bits in product((0,1),repeat=len(edge)):
        v=[[False]*n for _ in range(n)]
        for (i,j),k in zip(edge,bits): v[i][j]=bool(k)
        yield v


phi=F(2,5)
for n in (2,3):
    allm=list(masks_for(n))
    eta=min(phi,1-phi)/n
    for mask in allm:
        p=matrix(n,phi,mask)
        assert all(sum(row)==1 for row in p)
        assert all(x>=0 for row in p for x in row)
        assert all(x>=eta for row in p for x in row if x>0)
        for mask2 in allm:
            q=matrix(n,phi,mask2)
            r=multiply(q,p)
            assert all(r[i][j]>=eta*eta for i in range(n,2*n) for j in range(2*n))
    full=[[i!=j for j in range(n)] for i in range(n)]
    b=multiply(matrix(n,phi,full),matrix(n,phi,full))
    assert all(v>=eta*eta for row in b for v in row)

# Rational fixed-point obstruction below the sharp threshold and its
# exact disappearance at equality.
threshold=(1+phi)/2
x=[F(0),F(1)]
y=[(1-phi)/2,(1+phi)/2]
assert threshold==F(7,10)
assert y[1]-x[0]==threshold and x[1]-y[0]==threshold
for eps,active in ((F(69,100),False),(threshold,True)):
    ns=[[j for j in range(2) if j!=i and abs(x[i]-y[j])<=eps]
        for i in range(2)]
    assert bool(ns[0])==active and bool(ns[1])==active
    newx=[(x[i]+sum((y[j] for j in ns[i]),F(0)))/(len(ns[i])+1)
          for i in range(2)]
    newy=[phi*newx[i]+(1-phi)*sum(y,F(0))/2 for i in range(2)]
    if not active: assert newx==x and newy==y
    else: assert newx!=x


def evolve(x,y,phi,eps,steps):
    n=len(x)
    for _ in range(steps):
        xx=[]
        for i in range(n):
            ns=[j for j in range(n) if j!=i and abs(x[i]-y[j])<=eps]
            xx.append((x[i]+sum(y[j] for j in ns))/(len(ns)+1))
        avg=sum(y)/n
        yy=[phi*xx[i]+(1-phi)*avg for i in range(n)]
        x,y=xx,yy
    return max(x+y)-min(x+y)

rng=random.Random(260406140)
for n in (2,3,5,10):
    for test in range(25):
        x=[rng.random() for _ in range(n)]
        y=[rng.random() for _ in range(n)]
        assert evolve(x,y,float(phi),float(threshold),150)<1e-9
print('VERIFY_OK: rational two-step action mixing, sharp two-agent obstruction, 100 dynamical checks')
