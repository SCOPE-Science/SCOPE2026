#!/usr/bin/env python3
"""Reproducible finite numerical checks for single-circle Bergman polynomial sampling."""
import math
import cmath
import random

# Only Python standard library; finite numerical diagonal checks and complex
# Gram eigenvalue comparisons via Jacobi diagonalization.

def ww(alpha, n):
    v=1.0
    for k in range(1,n+1):v*=1.0+(alpha+1)/k
    return v

def gram(alpha,n,t,angles,weights):
    total=sum(weights); w=[ww(alpha,k) for k in range(n+1)]
    return [[math.sqrt(w[k]*w[l])*t**((k+l)/2)*sum(weights[j]*cmath.exp(1j*(k-l)*angles[j]) for j in range(len(angles)))/total
             for l in range(n+1)] for k in range(n+1)]

def hermitian_eigenvalues(a):
    # Cholesky-free Jacobi rotations via numpy if present, otherwise use
    # a self-contained real 2m-dimensional Hermitian embedding.
    n=len(a)
    B=[[0.0]*(2*n) for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            z=a[i][j]
            B[i][j]=z.real;B[i][j+n]=-z.imag
            B[i+n][j]=z.imag;B[i+n][j+n]=z.real
    size=2*n
    for _ in range(15*size*size):
        p=q=0; best=0.0
        for i in range(size):
            for j in range(i+1,size):
                if abs(B[i][j])>best:best=abs(B[i][j]);p=i;q=j
        if best<1e-10:break
        v=B[p][q];tau=(B[q][q]-B[p][p])/(2*v)
        u=math.copysign(1.,tau)/(abs(tau)+math.sqrt(1+tau*tau)) if tau else 1.
        c=1/math.sqrt(1+u*u);s=u*c
        pp=B[p][p];qq=B[q][q]
        B[p][p]=pp-u*v;B[q][q]=qq+u*v;B[p][q]=B[q][p]=0.
        for i in range(size):
            if i==p or i==q:continue
            x=B[i][p];y=B[i][q]
            B[i][p]=B[p][i]=c*x-s*y
            B[i][q]=B[q][i]=s*x+c*y
    return sorted(B[i][i] for i in range(size))[::2]

def main():
    count=0
    rng=random.Random(2607)
    for alpha in [-.75,-.5,0,.25,.5,1,2,4]:
        for n in range(2,12):
            wN=ww(alpha,n);t=wN**(-1/n)
            d=[ww(alpha,k)*t**k for k in range(n+1)]
            K=max(d)
            assert abs(d[0]-1)<1e-12 and abs(d[-1]-1)<1e-12 and min(d)>1-1e-12
            assert all(d[k]>1 for k in range(1,n))
            count+=3
            for m in [n+1,2*n+3]:
                angles=[2*math.pi*j/m for j in range(m)]
                G=gram(alpha,n,t,angles,[1]*m)
                assert max(abs(G[k][l]-(d[k] if k==l else 0)) for k in range(n+1) for l in range(n+1))<1e-10
                count+=1
            for z in [.65,.8,.92,1.1,1.18,1.4]:
                s=t*z
                if s<=0 or s>=1:continue
                seq=[ww(alpha,k)*s**k for k in range(n+1)]
                assert max(seq)/min(seq)>K+1e-11
                count+=1
            if n<=6:
                angles=[2*math.pi*(j+rng.random()*.1)/ (n+1) for j in range(n+1)]
                wt=[1+rng.random() for _ in angles]
                vals=hermitian_eigenvalues(gram(alpha,n,t,angles,wt))
                assert vals[-1]/vals[0]>K-1e-8
                count+=1
                # The equality case is unique at equal weights and polygon nodes.
                vals2=hermitian_eigenvalues(gram(alpha,n,t,[2*math.pi*j/(n+1) for j in range(n+1)],[1]*(n+1)))
                assert abs(vals2[-1]/vals2[0]-K)<1e-8
                count+=1
    for alpha in [-.5,0,.5,2]:
        a=alpha+1
        for n in [3000,10000,30000]:
            logw=math.lgamma(n+alpha+2)-math.lgamma(alpha+2)-math.lgamma(n+1)
            tlog=-logw/n
            km=max(0,min(n,int(a/math.expm1(-tlog)-1)))
            km=max(range(max(0,km-2),min(n,km+3)+1),key=lambda k:math.lgamma(k+alpha+2)-math.lgamma(alpha+2)-math.lgamma(k+1)+k*tlog)
            K=math.exp(math.lgamma(km+alpha+2)-math.lgamma(alpha+2)-math.lgamma(km+1)+km*tlog)
            asym=(1/math.e)**a*(n/math.log(n))**a/math.gamma(a+1)
            assert .75<K/asym<1.5,(alpha,n,K/asym)
            count+=1
    print('FINITE_CHECKS_OK',count)

if __name__=='__main__': main()
