#!/usr/bin/env python3
"""Exact-polynomial and finite-dimensional checks of a Laguerre Hankel spectral formula.

Requires only Python 3 standard library. Numerical checks illustrate, and do not prove,
the uniform-in-order spectral assertion established in RESULT.md.
"""
from fractions import Fraction as F
from math import comb, factorial, sin, pi, sqrt, cos

checks=0

def check(flag, description):
    global checks
    checks += 1
    if not flag:
        raise AssertionError(description)

def lag_coeff(j, a):
    if a>j: return F(0)
    return F((-1)**a*comb(j,a)*2**a, factorial(a))

# Polynomial kernel expansion, performed with exact rational arithmetic.
for n in range(21):
    for a in range(n+1):
        for b in range(n+1):
            lhs=F(0) if a+b>n else F((-1)**(a+b)*comb(n,a+b)*2**(a+b),factorial(a)*factorial(b))
            rhs=sum((lag_coeff(j,a)*lag_coeff(n-j,b) for j in range(n+1)),F(0))
            if n>0:
                rhs-=sum((lag_coeff(j,a)*lag_coeff(n-1-j,b) for j in range(n)),F(0))
            check(lhs==rhs, f'Laguerre addition coefficient n={n}, a={a}, b={b}')

for m in range(1,81):
    # A_m=R_m(I-S_m)/2, with its rows defined without numeric packages.
    def mult(v):
        return [0.5*(v[m-1-i]-(v[m-2-i] if m-2-i>=0 else 0.0)) for i in range(m)]
    vals=[]
    vecs=[]
    for k in range(1,m+1):
        theta=(2*k-1)*pi/(2*m+1)
        lam=(-1)**(k-1)*sin(theta/2)
        v=[2/sqrt(2*m+1)*sin((j+1)*theta) for j in range(m)]
        w=mult(v)
        check(max(abs(w[j]-lam*v[j]) for j in range(m)) < 5e-12, f'eigen-residual m={m}, k={k}')
        check(abs(sum(x*x for x in v)-1)<5e-12, f'eigenvector norm m={m}, k={k}')
        vals.append(lam)
        vecs.append(v)
    check(abs(sum(vals)-((-1)**(m-1))/2)<1e-11, f'trace m={m}')
    check(abs(sum(lam*lam for lam in vals)-(2*m-1)/4)<1e-11, f'S2 m={m}')
    check(abs(max(abs(v) for v in vals)-cos(pi/(2*m+1)))<1e-11, f'op norm m={m}')
    check(abs(min(abs(v) for v in vals)-sin(pi/(4*m+2)))<1e-11, f'min singular m={m}')
    check(abs(sum((1 if v>0 else -1) for v in vals)-(m%2))<1e-11, f'inertia m={m}')
    for k in range(m):
        for j in range(k):
            check(abs(sum(a*b for a,b in zip(vecs[k],vecs[j]))) < 1e-11, f'orthogonality m={m},k={k},j={j}')

# A second, exact rational determinant calculation for small orders.
def determinant_rational(matrix):
    n=len(matrix)
    a=[[F(x) for x in row] for row in matrix]
    d=F(1)
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        if pivot is None:return F(0)
        if pivot!=j:
            a[j],a[pivot]=a[pivot],a[j]
            d=-d
        x=a[j][j]
        d*=x
        for i in range(j+1,n):
            z=a[i][j]/x
            for c in range(j+1,n): a[i][c]-=z*a[j][c]
            a[i][j]=F(0)
    return d
for m in range(1,14):
    M=[[F(int(i+j==m-1)-int(i+j==m-2),2) for j in range(m)] for i in range(m)]
    check(determinant_rational(M)==F((-1)**(m*(m-1)//2),2**m),f'exact determinant m={m}')
# The generalized Laguerre addition identity is an exact, separate check.
def lag1_coeff(j,a):
    if a>j:return F(0)
    return F((-1)**a*comb(j+1,a+1)*2**a,factorial(a))
for n in range(20):
    for a in range(n+1):
        for b in range(n+1):
            lhs=F(0) if a+b>n else F((-1)**(a+b)*comb(n+1,a+b+1)*2**(a+b),factorial(a)*factorial(b))
            rhs=sum((lag_coeff(j,a)*lag_coeff(n-j,b) for j in range(n+1)),F(0))
            check(lhs==rhs, f'associated Laguerre identity n={n}, a={a}, b={b}')

# Rational-parameter Gram matrix and inverse determinant normalization.
for tau in [F(0), F(1,3), F(1), F(3,2), F(2)]:
    for m in range(1,15):
        M=[[F(int(i+j==m-1)-tau*int(i+j==m-2),2) for j in range(m)] for i in range(m)]
        check(all(M[i][j]==M[j][i] for i in range(m) for j in range(m)),f'symmetry tau={tau}, m={m}')
        check(determinant_rational(M)==F((-1)**(m*(m-1)//2),2**m),f'invertible tau={tau}, m={m}')
        T=[[sum(4*M[i][r]*M[r][j] for r in range(m)) for j in range(m)] for i in range(m)]
        for i in range(m):
            for j in range(m):
                expected=(F(1)+tau*tau if i==j and i<m-1 else (F(1) if i==j else (-tau if abs(i-j)==1 else F(0))))
                check(T[i][j]==expected,f'Jacobi square tau={tau},m={m},i={i},j={j}')

# Sturm counts give an independent finite-dimensional smallest-singular check.
def smallest_tridiag(tau,m):
    def negative_pivots(lam):
        count=0
        last=1+tau*tau-lam if m>1 else 1-lam
        if last<0:count+=1
        if abs(last)<1e-17:last=-1e-17
        for i in range(1,m):
            a=(1+tau*tau if i<m-1 else 1)-lam
            last=a-tau*tau/last
            if last<0:count+=1
            if abs(last)<1e-17:last=-1e-17
        return count
    low,high=0.0,(1+tau)**2+1
    for _ in range(75):
        mid=(low+high)/2
        if negative_pivots(mid):high=mid
        else:low=mid
    return sqrt(max(0,(low+high)/2))/2
for tau in (0.25,0.5,0.8):
    m=500
    z=smallest_tridiag(tau,m)
    check(abs(z-(1-tau)/2)<0.01,f'subcritical numerical endpoint tau={tau}')
for m in (5,10,20,60):
    z=smallest_tridiag(1.0,m)
    check(abs(z-sin(pi/(4*m+2)))<3e-7,f'critical numerical endpoint m={m}')
for tau in (1.4,2.0):
    for m in (5,7,9,11):
        z=smallest_tridiag(tau,m)
        pred=(tau*tau-1)*tau**(-m-1)/2
        check(abs(z/pred-1)<0.20, f'supercritical asymptotic check tau={tau},m={m}')

print('PASS',checks,'checks; exact Laguerre identities, Jacobi square, determinant and finite spectral checks')
