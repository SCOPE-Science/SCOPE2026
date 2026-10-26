#!/usr/bin/env python3
"""Independent finite-matrix and asymptotic checks for a directed Gaussian Langevin chain.
All calculations use Python's standard library. Finite tests support but do not replace the proof.
"""
import math

D = 1.3

def cov(n, i, j, k, diffusion=D):
    """Zero-based stationary covariance from a closed binomial sum."""
    if i > j:
        i, j = j, i
    gap = j - i
    # Stable recursion: a_m = Bin(2m+gap,m)/(2k)^(2m+gap)
    term = math.exp(-gap * math.log(2*k))
    total = term
    for m in range(1, n - j):
        term *= ((2*m+gap)*(2*m+gap-1)/(m*(m+gap))) / (4*k*k)
        total += term
    return diffusion*total/k

def lim_cov(s, zeta, gap, diffusion=D):
    L = 1-s
    h = abs(gap)
    if zeta == 0:
        return diffusion*(2*math.sqrt(L/math.pi)*math.exp(-h*h/(4*L))
            - h*math.erfc(h/(2*math.sqrt(L))))
    # Substitution t=y^2 removes the square-root singularity.
    n=4000
    b=math.sqrt(L)
    def f(j):
        y=b*j/n
        if y==0.0:
            return 1.0 if h==0 else 0.0
        return math.exp(-h*h/(4*y*y)-2*zeta*y*y)
    total=f(0)+f(n)
    for j in range(1,n):
        total += (4 if j%2 else 2)*f(j)
    return (2*diffusion/math.sqrt(math.pi))*(b/n)/3*total

checks=0
max_resid=0
for n in [2,3,5,8,12]:
    for k in [0.8,1.0,1.5]:
        C=[[cov(n,i,j,k) for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                resid= -2*k*C[i][j]
                if i+1<n: resid+=C[i+1][j]
                if j+1<n: resid+=C[i][j+1]
                if i==j: resid+=2*D
                max_resid=max(max_resid,abs(resid))
                assert abs(resid) < 1e-8*(1+abs(C[i][j])), (n,k,i,j,resid)
                checks+=1

max_err=0
for n in [400,1600,6400]:
    for s in [0.25,0.65]:
        for zeta in [-0.6,0,1.4]:
            k=1+zeta/n
            for u,v in [(0.,0.),(0.,0.8),(-0.45,1.2)]:
                i=math.floor(s*n+u*math.sqrt(n))
                j=math.floor(s*n+v*math.sqrt(n))
                a=cov(n,i,j,k)/math.sqrt(n)
                target=lim_cov(s,zeta,u-v)
                err=abs(a-target)
                max_err=max(max_err,err)
                assert err < .11, (n,s,zeta,u,v,a,target,err)
                checks+=1

for k in [1.2,1.5,2.0]:
    for n in [100,1000]:
        a=cov(n,0,0,k)
        target=D/math.sqrt(k*k-1)
        assert abs(a-target)<.01, (k,n,a,target)
        checks+=1

for k in [.75,.9]:
    for n in [150,300]:
        # Use ratio to avoid numerical overflow at much larger n.
        a=cov(n,0,0,k)
        target=D*k**(1-2*n)/((1-k*k)*math.sqrt(math.pi*n))
        assert abs(a/target-1)<.05, (k,n,a/target)
        checks+=1

for n in [500,2000,8000]:
    a=cov(n,0,0,1.0)/math.sqrt(n)
    target=2*D/math.sqrt(math.pi)
    assert abs(a-target)<.05, (n,a,target)
    checks+=1

print('PASS',checks,'checks; maximum finite-matrix residual',max_resid,
      '; maximum absolute mesoscopic covariance discrepancy',max_err)
