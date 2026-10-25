#!/usr/bin/env python3
"""Independent exact-rational checks for affine skeleton projections (stdlib only)."""
from fractions import Fraction as F
from itertools import combinations
from math import comb, exp

COUNTER=0

def test(condition, description):
    global COUNTER
    if not condition:
        raise AssertionError(description)
    COUNTER += 1

def B(n,s):
    return F((n-1)*(s+1),2*n-s-1)

def threshold(n,s):
    return F(s-1,(n-1)*(s+1))

def closed(n,s):
    return 2*B(n,s)*(1-threshold(n,s))**s-1

def invert(matrix):
    n=len(matrix)
    a=[list(row)+[F(int(i==j)) for j in range(n)] for i,row in enumerate(matrix)]
    for j in range(n):
        k=next(k for k in range(j,n) if a[k][j])
        a[j],a[k]=a[k],a[j]
        q=a[j][j]
        a[j]=[v/q for v in a[j]]
        for i in range(n):
            if i==j:continue
            q=a[i][j]
            a[i]=[a[i][k]-q*a[j][k] for k in range(2*n)]
    return [row[n:] for row in a]

def gram(n,s):
    # basis = 1,t_0,...,t_{n-2}; exact face-mixture moments
    g=[[F(1) for _ in range(n)] for __ in range(n)]
    for i in range(1,n):
        g[0][i]=g[i][0]=F(1,n)
    for i in range(1,n):
        for j in range(1,n):
            g[i][j] = F(2,n*(s+1)) if i==j else F(s-1,n*(n-1)*(s+1))
    return g

def kernel_independent(n,s,x,y):
    inv=invert(gram(n,s))
    vx=[F(1)]+list(x[:n-1])
    vy=[F(1)]+list(y[:n-1])
    return sum(vx[i]*inv[i][j]*vy[j] for i in range(n) for j in range(n))

def beta_integral(n,s):
    # Independently integrate the negative part of K(vertex,y) against
    # atom at zero + beta density via polynomial expansion.
    b=B(n,s)-1
    if s==1: return F(1)
    u=threshold(n,s)
    gamma=n*B(n,s)
    i=sum(F((-1)**j*comb(s-2,j))*(b*u**(j+1)/F(j+1)-gamma*u**(j+2)/F(j+2)) for j in range(s-1))
    neg=(1-F(s,n))*b+F(s,n)*(s-1)*i
    return 1+2*neg

def check():
    for n in range(3,12):
        for s in range(1,n+1):
            test(beta_integral(n,s)==closed(n,s),f'integral n={n} s={s}')
            g=gram(n,s);inv=invert(g)
            test(all(sum(g[i][k]*inv[k][j] for k in range(n))==int(i==j) for i in range(n) for j in range(n)),f'Gram n={n} s={s}')
            for i in range(n):
                x=[F(int(k==i)) for k in range(n)]
                for j in range(n):
                    y=[F(int(k==j)) for k in range(n)]
                    direct=kernel_independent(n,s,x,y) if n<=5 else sum(([F(1)]+x[:n-1])[k]*inv[k][h]*([F(1)]+y[:n-1])[h] for k in range(n) for h in range(n))
                    spectral=1+n*B(n,s)*(F(int(i==j))-F(1,n))
                    test(direct==spectral, f'kernel at vertices n={n} s={s} i={i} j={j}')
            test(closed(n,s)>=1,f'norm >=1 n={n} s={s}')
        test(closed(n,1)==1,f'vertex interpolation n={n}')
        test(closed(n,n)==2*(n+1)*F(n,n+1)**n-1,f'full simplex n={n}')
    # fixed-s large-n and extensive s/n regimes; tests only, not proofs.
    for s in [2,3,4,6,10]:
        n=10000
        test(abs(float(closed(n,s))-s)<.1,f'fixed s limit s={s}')
    for p,q in [(1,4),(1,2),(3,4),(1,1)]:
        n=10000;s=n*p//q
        predicted=2*(p/q)*exp(-p/q)/(2-p/q)
        test(abs(float(closed(n,s))/n-predicted)<.001,f'extensive limit {p}/{q}')
    print('PASS',COUNTER,'exact-rational and asymptotic-consistency assertions')

if __name__=='__main__':check()
