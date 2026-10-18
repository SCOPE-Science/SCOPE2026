"""Independent finite checks for optimal symmetric mixing on clique-cycle joins.

Requires Python 3, NumPy and SciPy. Execute with: python verify.py
"""
import math
import numpy as np
from scipy.optimize import linprog

checks = 0

def close(a, b, eps=3e-8):
    global checks
    assert abs(float(a)-float(b)) <= eps * (1+abs(float(a))+abs(float(b))), (a,b)
    checks += 1

def spectral_data(m):
    delta=2-2*math.cos(2*math.pi/m)
    Delta=2-2*math.cos(2*math.pi*(m//2)/m)
    rho=(Delta-delta)/(Delta+delta)
    tau=m*rho/(1+rho)
    return delta,Delta,rho,tau

def theorem(k,m):
    delta,Delta,rho,tau=spectral_data(m)
    a=min(1/m,(1+rho)/(m+k*(1+rho)))
    b=2*(1-k*a)/(delta+Delta)
    t=rho*(1-k*a)
    c=(1-m*a)/k
    return a,b,c,t,tau

def matrix(k,m,a,b,c):
    N=k+m
    P=np.zeros((N,N))
    for u in range(k):
        for v in range(k):
            if u!=v: P[u,v]=c
        for v in range(m):P[u,k+v]=P[k+v,u]=a
    for v in range(m):
        P[k+v,k+(v-1)%m]=b
        P[k+v,k+(v+1)%m]=b
    for v in range(N):P[v,v]=1-sum(P[v,:])
    return P

def lp_opt(k,m):
    ds=[2-2*math.cos(2*math.pi*j/m) for j in range(1,m)]
    vecs=[(k+m,0,0),(m,0,k)]+[(k,d,0) for d in ds]
    A=[];Y=[]
    for v in vecs:
        A.append([*v,-1]);Y.append(1)
        A.append([-q for q in v]+[-1]);Y.append(-1)
    A.extend(([m,0,k-1,0],[k,2,0,0]));Y.extend((1,1))
    res=linprog([0,0,0,1],A_ub=A,b_ub=Y,bounds=[(0,None)]*4,method='highs')
    assert res.success, res.message
    return res.x

for m in range(4,41):
    d,D,r,tau=spectral_data(m)
    assert 0<d<D and d+D>4-1e-12
    checks+=1
    for k in range(2,12):
        a,b,c,t,T=theorem(k,m)
        assert a>0 and b>0 and c>=-1e-12
        assert m*a+(k-1)*c<=1+1e-12
        assert k*a+2*b<1+1e-12
        checks+=3
        close(max(abs(1-(k+m)*a),abs(1-k*a-d*b),abs(1-k*a-D*b)),t)
        close(1-m*a-k*c,0)
        close(t,lp_opt(k,m)[3])
        N=k+m
        if N<=29:
            P=matrix(k,m,a,b,c)
            assert np.min(P)>-2e-12
            close(float(np.max(np.abs(P.sum(axis=1)-1))),0)
            vals=np.linalg.eigvalsh(P)
            close(np.max(np.abs(vals[:-1])),t)
            close(vals[-1],1)
        cmin=max(0,(1-m*a-t)/k)
        cmax=min((1-m*a+t)/k,(1-m*a)/(k-1))
        assert -1e-9<=cmin<=cmax+1e-9
        checks+=1
        if k<=tau+1e-10:
            close(a,1/m)
            close(cmax,0)
        if tau+1e-10<k<=2*tau+1e-10:
            close(cmin,0)
        if k>2*tau+1e-10:
            assert cmin>0
            checks+=1

# Direct exact algebraic checks at cycle orders with rational cosines.
from fractions import Fraction as F
for m,d,D in [(4,F(2),F(4)),(6,F(1),F(4))]:
    rho=(D-d)/(D+d)
    tau=F(m)*rho/(1+rho)
    for k in range(2,22):
        a=min(F(1,m),(1+rho)/(m+k*(1+rho)))
        b=2*(1-k*a)/(d+D)
        c=(1-m*a)/k
        t=rho*(1-k*a)
        modes=[1-(k+m)*a,1-m*a-k*c,1-k*a-d*b,1-k*a-D*b]
        assert max(map(abs,modes))==t
        assert m*a+(k-1)*c<=1 and k*a+2*b<=1
        checks+=2

# Independent vertex-level SDP form is not required for the analytical theorem.
# The LP checks independently optimize all dihedral-invariant edge classes.
print('VERIFY_OK',checks,'checks')
