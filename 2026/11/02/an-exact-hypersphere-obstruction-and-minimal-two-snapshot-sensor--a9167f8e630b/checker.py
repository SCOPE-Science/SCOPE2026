"""Independent finite checks for exact Gaussian-puff sensor-geometry theorem.

Run: python3 checker.py
Requires only Python standard library.
"""
from fractions import Fraction as F
from itertools import combinations
from math import exp, log, pi, sqrt, isclose
from random import Random


def determinant(M):
    M = [[F(x) for x in row] for row in M]
    n = len(M)
    d = F(1)
    for k in range(n):
        h = next((i for i in range(k,n) if M[i][k]),None)
        if h is None: return F(0)
        if h != k:
            M[k],M[h] = M[h],M[k]
            d = -d
        p = M[k][k]
        d *= p
        for i in range(k+1,n):
            fac = M[i][k]/p
            for j in range(k+1,n):M[i][j] -= fac*M[k][j]
            M[i][k] = 0
    return d


def geo_row(s):
    x,y=s
    return [1,x,y,x*x+y*y]


def solve(M,y):
    A = [[float(x) for x in row]+[float(v)] for row,v in zip(M,y)]
    n=len(A)
    for k in range(n):
        j=max(range(k,n),key=lambda i:abs(A[i][k]))
        assert abs(A[j][k])>1e-12
        A[k],A[j]=A[j],A[k]
        v=A[k][k]
        for m in range(k,n+1):A[k][m]/=v
        for i in range(n):
            if i==k: continue
            v=A[i][k]
            for m in range(k,n+1):A[i][m]-=v*A[k][m]
    return [A[k][-1] for k in range(n)]


def log_c(s,t,z,k,q,t0):
    w=k*(t-t0)
    return log(q/(4*pi*w))-((s[0]-z[0])**2+(s[1]-z[1])**2)/(4*w)


S = [(0,0),(2,0),(0,2),(1,3)]
H = [geo_row(s) for s in S]
assert determinant(H) != 0

# Structural test: exactly circumcircle points have rank deficiency.
C=[(0,0),(2,0),(0,2),(2,2)]
assert determinant([geo_row(s) for s in C])==0
checks=2

# Circle-inversion identity is checked with exact rational arithmetic,
# independent of the exponential evaluation.
O=(F(1),F(1))
R2=F(2)
z=(F(2),F(1))
v=(z[0]-O[0],z[1]-O[1])
alpha=R2/(v[0]*v[0]+v[1]*v[1])
z2=(O[0]+alpha*v[0],O[1]+alpha*v[1])
assert alpha==2 and z2==(3,1)
for s in C:
    sq=lambda a:(F(s[0])-a[0])**2+(F(s[1])-a[1])**2
    assert sq(z2)==alpha*sq(z)
    checks+=1
for t in [F(1,10),F(1,3),F(1),F(3),F(7)]:
    for s in C:
        original=log_c(s,float(t),z,1.,1.,0.)
        alternate=log_c(s,float(t),z2,2.,2.,0.)
        assert isclose(original,alternate,abs_tol=1e-12)
        checks+=1
# The fourth off-circle sensor separates the two identical three-site traces.
assert abs(log_c(S[3],1.,z,1.,1.,0.)-log_c(S[3],1.,z2,2.,2.,0.))>0.1
checks+=1

# Full two-snapshot inversion, including unknown launch time and mass.
rng=Random(861020)
for _ in range(1200):
    zz=(rng.uniform(-1.2,2.4),rng.uniform(-1.2,2.4))
    k=rng.uniform(0.2,3)
    q=rng.uniform(0.3,7)
    t0=rng.uniform(-2,0.3)
    t1=1.
    t2=rng.uniform(2.,5.)
    obs1=[log_c(s,t1,zz,k,q,t0) for s in S]
    obs2=[log_c(s,t2,zz,k,q,t0) for s in S]
    A1,b1,b2,c1=solve(H,obs1)
    A2,b21,b22,c2=solve(H,obs2)
    w1=-1/(4*c1)
    w2=-1/(4*c2)
    khat=(w2-w1)/(t2-t1)
    t0hat=t1-w1/khat
    zhat=(-b1/(2*c1),-b2/(2*c1))
    qhat=4*pi*w1*exp(A1+(zhat[0]**2+zhat[1]**2)/(4*w1))
    for actual,estimate in [(k,khat),(q,qhat),(t0,t0hat),(zz[0],zhat[0]),(zz[1],zhat[1])]:
        assert isclose(actual,estimate,rel_tol=3e-10,abs_tol=3e-10),(actual,estimate)
        checks+=1

# Three collinear sensors cannot distinguish mirror-image source points.
L=[(-1,0),(0,0),(2,0)]
for s in L:
    for t in [1.,2.,3.5]:
        assert isclose(log_c(s,t,(0.3,1.7),0.6,3.,-0.2),log_c(s,t,(0.3,-1.7),0.6,3.,-0.2),abs_tol=1e-14)
        checks+=1
print(f"PASS: {checks} assertions of structural, exact and numerical identities")
print(f"off-circle design determinant: {determinant(H)}")
