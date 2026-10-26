"""Numerical and exact-rational checks for a graph opinion-equilibrium theorem.

Requires only Python 3 standard library. Mathematical proof is in RESULT.md.
"""
from fractions import Fraction as Q
from math import isfinite
from random import Random

checks = 0

def check(predicate, description):
    global checks
    if not predicate:
        raise AssertionError(description)
    checks += 1

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def matvec(A,x):
    return [dot(row,x) for row in A]

def solve(A, b):
    n = len(b)
    T = [list(map(float,A[i])) + [float(b[i])] for i in range(n)]
    for k in range(n):
        h = max(range(k,n),key=lambda i:abs(T[i][k]))
        T[h], T[k] = T[k], T[h]
        check(abs(T[k][k])>1e-13,'Gaussian elimination pivot')
        p=T[k][k]
        for i in range(k+1,n):
            f=T[i][k]/p
            for j in range(k+1,n+1):T[i][j]-=f*T[k][j]
            T[i][k]=0.0
    x=[0.0]*n
    for i in range(n-1,-1,-1):
        x[i]=(T[i][n]-sum(T[i][j]*x[j] for j in range(i+1,n)))/T[i][i]
    return x

def laplacian(n,edges):
    L=[[0.0]*n for _ in range(n)]
    for i,j,w in edges:
        L[i][i]+=w;L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
    return L

def equilibrium(L,sigma,u,p,k,start=None):
    x=[v**(1/p) for v in u] if start is None else list(start)
    n=len(x)
    for step in range(90):
        Lx=matvec(L,x)
        F=[k*Lx[i]-sigma[i]*x[i]*(u[i]-x[i]**p) for i in range(n)]
        if max(map(abs,F))<1e-10:return x
        H=[[k*L[i][j] for j in range(n)] for i in range(n)]
        for i in range(n):H[i][i]+=sigma[i]*((p+1)*x[i]**p-u[i])
        d=solve(H,[-v for v in F]); alpha=1.0
        while alpha>1e-10:
            y=[x[i]+alpha*d[i] for i in range(n)]
            if min(y)<=0:
                alpha*=0.5;continue
            Fy=[k*matvec(L,y)[i]-sigma[i]*y[i]*(u[i]-y[i]**p) for i in range(n)]
            if max(map(abs,Fy))<max(map(abs,F))*(1-0.1*alpha)+1e-12:break
            alpha*=0.5
        x=y
    raise AssertionError('Newton convergence')

def energy(L,x):return 0.5*dot(x,matvec(L,x))

def slope(L,x,sigma,u,p,k):
    Lx=matvec(L,x);H=[[k*L[i][j] for j in range(len(x))] for i in range(len(x))]
    for i in range(len(x)):H[i][i]+=sigma[i]*((p+1)*x[i]**p-u[i])
    z=solve(H,Lx)
    return -dot(Lx,z)

# Exact-rational nontrivial equilibrium and exact susceptibility.
x=[Q(2),Q(3)];u=[Q(3,2),Q(10,3)];L=[[Q(1),Q(-1)],[Q(-1),Q(1)]]
f=[x[i]*(u[i]-x[i]) for i in range(2)]
check(matvec(L,x)==f,'rational equilibrium')
H=[[Q(7,2),Q(-1)],[Q(-1),Q(11,3)]]
check(matvec(H,[Q(16,71),Q(-15,71)])==[Q(1),Q(-1)],'exact implicit derivative')
check(energy(L,x)==Q(1,2),'exact graph disagreement')
check(dot([Q(16,71),Q(-15,71)],matvec(L,x))==-Q(31,71),'exact slope')
c=Q(29,12);coef=c*c*(u[1]-u[0])**2/Q(8)
check(coef==Q(101761,41472),'exact resistance prefactor')

rng=Random(7317)
scenarios=0
for n in (2,3,4,5,6):
    for trial in range(7):
        edges=[(i-1,i,0.3+2*rng.random()) for i in range(1,n)]
        for i in range(n):
            for j in range(i+2,n):
                if rng.random()<0.23:edges.append((i,j,0.3+1.2*rng.random()))
        Lt=laplacian(n,edges)
        sig=[0.5+2*rng.random() for _ in range(n)]
        uu=[0.8+3*rng.random() for _ in range(n)]
        p=[1,1.5,2][trial%3]
        ks=[0.002,0.03,0.4,3,20,150,1500]
        Es=[]; xx=None
        for k in ks:
            xx=equilibrium(Lt,sig,uu,p,k,start=xx)
            val=energy(Lt,xx);der=slope(Lt,xx,sig,uu,p,k)
            Es.append(val)
            check(isfinite(val) and isfinite(der) and der<-1e-14,'strict dissipation slope')
            F=[k*matvec(Lt,xx)[i]-sig[i]*xx[i]*(uu[i]-xx[i]**p) for i in range(n)]
            check(max(map(abs,F))<1e-8,'equilibrium residual')
        check(all(Es[i]>Es[i+1] for i in range(len(Es)-1)),'global strict decrease')
        dd=[v**(1/p) for v in uu]
        E0=energy(Lt,dd)
        check(abs(Es[0]-E0)<0.10*max(1,E0),'small coupling approach')
        c0=(sum(sig[i]*uu[i] for i in range(n))/sum(sig))**(1/p)
        ff=[c0*sig[i]*(uu[i]-c0**p) for i in range(n)]
        # Laplacian pseudoinverse action from grounding by a rank-one correction.
        K=[[Lt[i][j]+1/n for j in range(n)] for i in range(n)]
        z=solve(K,ff)
        target=dot(ff,z)/2
        ratio=ks[-1]*ks[-1]*Es[-1]/target
        check(abs(ratio-1)<0.08,'large coupling resistance coefficient')
        scenarios+=1

print('PASS:',checks,'checks on',scenarios,'connected weighted-graph scenarios')
