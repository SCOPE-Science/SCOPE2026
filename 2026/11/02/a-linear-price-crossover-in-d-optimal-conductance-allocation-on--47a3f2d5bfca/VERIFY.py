#!/usr/bin/env python3
"""Independent finite checks of the square-torus conductance formulas.

Requires only Python 3 standard library. Finite tests support, but do not
replace, the analytic global optimality and asymptotic arguments.
"""
from math import cos, pi, sin, sqrt, tanh, exp, log, isclose, fsum

CHECKS = 0

def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)

def laplace_eigen(n):
    return [4 * sin(pi*j/n)**2 for j in range(n)]

def price_ratio(n, t):
    e=laplace_eigen(n)
    aa=bb=0.0
    for j,x in enumerate(e):
        for k,y in enumerate(e):
            if j==k==0:
                continue
            den=x+t*y
            aa += x/den
            bb += y/den
    return bb/aa

def optimal_t(n,q):
    lo,hi=-40.0,40.0
    for _ in range(90):
        mid=(lo+hi)/2
        if price_ratio(n, exp(mid))>q:
            lo=mid
        else:
            hi=mid
    return exp((lo+hi)/2)

def phi(z):
    if z<1e-9:
        return 1+z/12-z*z/720
    x=sqrt(z)/2
    return x/tanh(x)

def phi_prime(z):
    if z<1e-6:
        return 1/12-z/360+z*z/10080
    x=sqrt(z)/2
    return (1/tanh(x)-x*(1/(sinh_stable(x)**2)))/(8*x)

def sinh_stable(x):
    return (exp(x)-exp(-x))/2

def H(u, resolution=4096):
    return fsum(phi(u*(4*sin(pi*j/resolution)**2)) for j in range(resolution))/resolution

def Hprime(u, resolution=4096):
    return fsum((4*sin(pi*j/resolution)**2)*phi_prime(u*(4*sin(pi*j/resolution)**2)) for j in range(resolution))/resolution

def find_u(kappa):
    lo,hi=-30.,30.
    for _ in range(90):
        m=(lo+hi)/2
        u=exp(m)
        if H(u)/u>kappa:
            lo=m
        else:
            hi=m
    return exp((lo+hi)/2)

def det_integer(a):
    a=[row[:] for row in a]
    n=len(a)
    prev=1
    for k in range(n-1):
        pivot=a[k][k]
        if not pivot: raise AssertionError('unexpected zero pivot')
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                if num%prev: raise AssertionError('Bareiss division not exact')
                a[i][j]=num//prev
        for i in range(k+1,n):a[i][k]=0
        prev=pivot
    return a[-1][-1]

def torus_tree_count(n, a, b):
    N=n*n
    L=[[0]*N for _ in range(N)]
    for i in range(n):
        for j in range(n):
            x=i*n+j
            for y,w in ((i*n+(j+1)%n,a),(((i+1)%n)*n+j,b)):
                L[x][x]+=w;L[y][y]+=w
                L[x][y]-=w;L[y][x]-=w
    return det_integer([row[:-1] for row in L[:-1]])

def spectral_log_count(n,a,b):
    e=laplace_eigen(n)
    return fsum(log(a*x+b*y) for i,x in enumerate(e) for j,y in enumerate(e) if i or j)-log(n*n)

def main():
    # Full graph Laplacian cofactor against Fourier product.
    for n in (3,4):
        for a,b in ((1,1),(2,3),(5,1)):
            exact=torus_tree_count(n,a,b)
            spectral=exp(spectral_log_count(n,a,b))
            check(abs(spectral/exact-1)<5e-12, f'matrix-tree mismatch n={n}')
    # Unique finite root, reciprocal direction-price relation, budget stationarity.
    for n in (3,4,5,7,12):
        check(abs(optimal_t(n,1)-1)<3e-12, 'isotropic optimum')
        for q in (0.3,1.5,4,30,1000):
            t=optimal_t(n,q)
            check(abs(price_ratio(n,t)/q-1)<2e-11,'root')
            check(abs(t*optimal_t(n,1/q)-1)<3e-10,'reciprocity')
        for t1,t2 in ((0.01,0.1),(0.1,1),(1,10),(10,100)):
            check(price_ratio(n,t1)>price_ratio(n,t2),'price monotonicity')
    # Fixed-size high-price law n*q*t -> 1.
    for n in (3,4,7,12):
        for q in (10000,100000):
            check(abs(n*q*optimal_t(n,q)-1)<0.01, 'high price limit')
    # Lattice resolvent hyperbolic formula, all k>0 summed.
    for n in (3,4,5,8,13):
        e=laplace_eigen(n)
        for t in (0.03,0.4,2.0):
            direct=fsum(t*y/(x+t*y) for i,x in enumerate(e) for k,y in enumerate(e) if i or k)
            alternate=fsum(n*sqrt((t*y)/(4+t*y))/tanh(n*__import__('math').asinh(sqrt(t*y)/2)) for y in e[1:])
            check(abs(direct/alternate-1)<5e-12, 'resolvent identity')
    # Crossover and first finite-size correction at fixed kappa.
    for kappa in (0.5,1.,3.,8.):
        u=find_u(kappa)
        hu=H(u)
        v=u*(hu*hu-1)/(hu-u*Hprime(u))
        check(u>0 and v>0 and abs(hu/u-kappa)<1e-10,'limit root')
        errors=[]
        for n in (40,80,160):
            un=n*n*optimal_t(n,kappa*n)
            errors.append(abs(un-u-v/n))
            check(abs(un-u)<max(0.5,8*u)/n,'double scaling convergence')
        check(errors[2]<errors[0]/7,'first correction improves with size')
    print(f'PASS: {CHECKS} checks; standard-library exact cofactors, resolvents and crossover tests')

if __name__=='__main__':
    main()
