#!/usr/bin/env python3
"""Exact diagonal-majorant certificates and independent numerical row tests.

Python standard library only. The rational checks verify finite instances
of algebraic certificates; the infinite-parameter assertion uses the
symbolic identities and proof in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt

checks = 0

def require(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def matrix_product(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def rank_q(a):
    a = [list(row) for row in a]
    n, m = len(a), len(a[0]); rank = 0
    for j in range(m):
        pivot = next((i for i in range(rank, n) if a[i][j]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        f = a[rank][j]
        a[rank] = [v/f for v in a[rank]]
        for i in range(n):
            if i != rank and a[i][j]:
                f = a[i][j]
                a[i] = [v-f*u for v, u in zip(a[i], a[rank])]
        rank += 1
        if rank == n:
            break
    return rank

def certificates(n, t, w):
    m = n-2
    c = F(21,10)
    C = [[(c if i==j else -t*w if {i,j}=={0,n-1} else w)
          for j in range(n)] for i in range(n)]
    for i in range(n):
        require(C[i][i] > sum(abs(C[i][j]) for j in range(n) if j!=i),
                'C must be positive definite by diagonal dominance')
    if 2*t<=m:
        se = w*(m-t); so = w*(m+1)
    else:
        se = w*t; so = w*(m-1+F(m,1)/t)
    q = [C[i][i]+(se if i in (0,n-1) else so) for i in range(n)]
    T = sum(q)
    S = [[(q[i] if i==j else F(0))-C[i][j]
          for j in range(n)] for i in range(n)]
    # Algebraic PSD factorization: S=sum positive multiples of outer products.
    vectors=[]
    if 2*t<=m:
        for j in range(1,n-1):
            z=[F(0)]*n; z[j]=F(2); z[0]=z[-1]=-F(1)
            vectors.append((w/F(2),z))
        for i in range(1,n-1):
            for j in range(i+1,n-1):
                z=[F(0)]*n; z[i]=F(1); z[j]=-F(1)
                vectors.append((w,z))
        z=[F(0)]*n; z[0]=F(1); z[-1]=-F(1)
        vectors.append((w*(F(m,2)-t),z))
    else:
        z=[F(1),*([-F(1)/t]*m),F(1)]
        vectors.append((w*t,z))
        for i in range(1,n-1):
            for j in range(i+1,n-1):
                z=[F(0)]*n; z[i]=F(1); z[j]=-F(1)
                vectors.append((w*(1+F(1)/t),z))
    for coeff,_ in vectors:
        require(coeff>=0,'PSD certificate coefficients')
    generated = [[sum(coeff*z[i]*z[j] for coeff,z in vectors)
                  for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            require(generated[i][j]==S[i][j], 'primal PSD certificate')
    r=min(F(1),F(m,1)/(2*t))
    g=[r]+[F(1)]*m+[r]
    f=[F(1)]+[F(0)]*m+[-F(1)]
    X=[[g[i]*g[j]+(1-r*r)*f[i]*f[j] for j in range(n)] for i in range(n)]
    for i in range(n):
        require(X[i][i]==1, 'dual elliptope diagonal')
    require(0<=r<=1, 'positive Gram coefficient')
    require(sum(C[i][j]*X[j][i] for i in range(n) for j in range(n))==T,
            'exact equality of primal and dual values')
    SX=matrix_product(S,X)
    for row in SX:
        for x in row:
            require(x==0,'complementary slackness')
    require(rank_q(S)==(n-1 if 2*t<m else n-2), 'slack nullity')
    require(all(x>0 for x in q), 'strictly positive primal probabilities')
    return q,T

# Pure-Python numerical check of actual unit-row matrices.
def inverse(a):
    n=len(a); x=[[float(a[i][j]) for j in range(n)]+[float(i==j) for j in range(n)] for i in range(n)]
    for i in range(n):
        k=max(range(i,n),key=lambda k:abs(x[k][i]))
        x[i],x[k]=x[k],x[i]
        v=x[i][i]; assert abs(v)>1e-12
        x[i]=[z/v for z in x[i]]
        for k in range(n):
            if k==i:continue
            v=x[k][i]
            x[k]=[z-v*y for z,y in zip(x[k],x[i])]
    return [row[n:] for row in x]

def cholesky(a):
    n=len(a);l=[[0.]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            v=a[i][j]-sum(l[i][k]*l[j][k] for k in range(j))
            l[i][j]=sqrt(v) if i==j else v/l[j][j]
    return l

def smallest_eigen(a):
    n=len(a); a=[list(row) for row in a]
    for _ in range(40*n*n):
        i,j=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda ij:abs(a[ij[0]][ij[1]]))
        if abs(a[i][j])<1e-12:break
        tau=(a[j][j]-a[i][i])/(2*a[i][j])
        z=(1 if tau>=0 else -1)/(abs(tau)+sqrt(1+tau*tau))
        c=1/sqrt(1+z*z); s=z*c; x=a[i][j]
        a[i][i]-=z*x; a[j][j]+=z*x; a[i][j]=a[j][i]=0.
        for k in range(n):
            if k in (i,j):continue
            ai,aj=a[k][i],a[k][j]
            a[k][i]=a[i][k]=c*ai-s*aj
            a[k][j]=a[j][k]=s*ai+c*aj
    return min(a[i][i] for i in range(n))

def normalized_test(n,t):
    w=1/(100*n*(1+t))
    C=[[1.0 if i==j else -t*w if {i,j}=={0,n-1} else w
        for j in range(n)] for i in range(n)]
    # Fixed-point/Newton correction of diagonal C ensuring diag(C^{-1})=1.
    for _ in range(20):
        G=inverse(C)
        err=max(abs(G[i][i]-1) for i in range(n))
        if err<1e-12:break
        for i in range(n):
            C[i][i]+=(G[i][i]-1)/(G[i][i]*G[i][i])
    G=inverse(C)
    require(max(abs(G[i][i]-1) for i in range(n))<1e-9,'unit row norms')
    B=cholesky(G)
    require(max(abs(sum(z*z for z in B[i])-1) for i in range(n))<1e-9,'actual normalized rows')
    m=n-2
    if 2*t<=m:
        se=w*(m-t);so=w*(m+1)
    else:
        se=w*t;so=w*(m-1+m/t)
    q=[C[i][i]+(se if i in (0,n-1) else so) for i in range(n)]
    T=sum(q);p=[z/T for z in q]
    matrix=[[sum(B[k][i]*p[k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    require(abs(smallest_eigen(matrix)-1/T)<1e-8,'direct normalized Kaczmarz eigenvalue')

if __name__=='__main__':
    count=0
    for n in range(5,19):
        m=n-2
        ts=[F(1,9),F(1,2),F(1),F(3,2),F(m,2)-F(1,10),F(m,2),F(m,2)+F(1,10),F(7),F(13)]
        for t in sorted(set(x for x in ts if x>0)):
            w=F(1,100*n*(1+t))
            certificates(n,t,w);count+=1
    for n in range(5,12):
        for t in (0.3,(n-2)/2,(n-2)/2+1,11.):
            normalized_test(n,t)
    print('PASS: %d exact-rational certificate cases, 28 normalized-system eigenvalue cases, %d assertion checks' % (count,checks))
