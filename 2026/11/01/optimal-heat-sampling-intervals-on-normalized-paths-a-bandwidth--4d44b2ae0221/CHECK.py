#!/usr/bin/env python3
"""Supplemental numerical checks for the normalized-path heat sampling theorem.

Only Python's standard library is needed. These checks are finite regression
checks and do not replace the general determinant and continuum-limit proofs.
"""
import math

COUNT = 0


def require(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(message)


def path_rates(N, m):
    return [1.0-math.cos(math.pi*j/(N-1)) for j in range(m)]


def eig(N, j, k):
    M = N-1
    d = 1 if j in (0, M) else 2
    if k == 0:
        return math.sqrt(d/(2*M))
    if k == M:
        return ((-1)**j)*math.sqrt(d/(2*M))
    return math.sqrt(d/M)*math.cos(math.pi*k*j/M)


def determinant(A):
    A = [list(row) for row in A]
    n = len(A)
    sign = 1.0
    ans = 1.0
    for k in range(n):
        pivot = max(range(k,n), key=lambda r:abs(A[r][k]))
        if abs(A[pivot][k]) < 1.e-250:
            return 0.0
        if pivot != k:
            A[pivot], A[k] = A[k], A[pivot]
            sign = -sign
        x = A[k][k]
        ans *= x
        for i in range(k+1,n):
            scale = A[i][k]/x
            for c in range(k+1,n):
                A[i][c] -= scale*A[k][c]
    return ans*sign


def root_scaled(N, m):
    r = path_rates(N,m)
    L = r[-1]
    r = [x/L for x in r]
    pairs = [(r[i],r[j]-r[i]) for i in range(m) for j in range(i+1,m)]
    def deriv(s):
        return sum(-a + (1/s if s*d<1.e-7 else d/math.expm1(s*d))
                   for a,d in pairs)
    lo = 1.e-9
    hi = 1.0
    while deriv(hi) > 0:
        hi *= 2
    for _ in range(65):
        mid = (lo+hi)/2
        if deriv(mid) > 0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2, deriv


def continuum_root(theta, steps=180):
    # Midpoint quadrature on the square, restricted to i<j.  The diagonal
    # has zero area; here the discrete double midpoint measure converges.
    if theta == 0:
        r = lambda x: x*x
    else:
        denom = 1-math.cos(math.pi*theta)
        r = lambda x: (1-math.cos(math.pi*theta*x))/denom
    # Product-midpoint rule after the triangular map
    # (u,w) -> (u, u+(1-u)w), Jacobian 1-u.
    pairs = []
    for i in range(steps):
        u=(i+.5)/steps
        v0=r(u)
        for j in range(steps):
            v=u+(1-u)*(j+.5)/steps
            pairs.append((1-u, v0, r(v)-v0))
    def fun(s):
        return sum(w*(-v + (1/s if s*d<1.e-7 else d/math.expm1(s*d)))
                   for w,v,d in pairs)
    lo, hi=0.1, 10.0
    for _ in range(48):
        x=(lo+hi)/2
        if fun(x) > 0:lo=x
        else:hi=x
    return (lo+hi)/2


def verify():
    for N in range(3,15):
        M=N-1
        ds=[1 if j in (0,M) else 2 for j in range(N)]
        for k in range(N):
            v=[eig(N,j,k) for j in range(N)]
            lam=1-math.cos(math.pi*k/M)
            for j in range(N):
                weighted_sum=sum(v[z]/math.sqrt(ds[j]*ds[z])
                                 for z in (j-1,j+1) if 0 <= z < N)
                require(abs((v[j]-weighted_sum)-lam*v[j])<3.e-12,
                        'eigenvalue equation')
            for l in range(N):
                dot=sum(v[j]*eig(N,j,l) for j in range(N))
                require(abs(dot-(1.0 if k==l else 0.0))<3.e-12,
                        'orthonormality')
        for m in range(2,min(N,7)+1):
            rates=path_rates(N,m)
            L=rates[-1]
            for c in (0.6, 1.1):
                t=c/L
                q=[math.exp(-t*v) for v in rates]
                A=[[eig(N,0,j)*q[j]**ell for j in range(m)]
                   for ell in range(m)]
                lhs=abs(determinant(A))
                rhs=math.prod(abs(eig(N,0,j)) for j in range(m))
                rhs*=math.prod(abs(q[j]-q[i]) for i in range(m)
                               for j in range(i+1,m))
                require(abs(lhs-rhs)<5.e-9*max(rhs,1.e-14),
                        'spectral Vandermonde determinant')
            if m>=3:
                root,deriv=root_scaled(N,m)
                require(deriv(root*0.99)>0 and deriv(root*1.01)<0,
                        'strict unique peak')
    for theta,answer in [(0,3.50135659780167),
                         (0.5,3.15495966176148),
                         (1.0,2.19180873992866)]:
        require(abs(continuum_root(theta)-answer)<2.e-3,
                'continuum integral benchmark')
    a=0.905947727416320
    f=lambda a:-1+1/math.expm1(a)+3/math.expm1(3*a)+4/math.expm1(4*a)
    require(abs(f(a)) < 1.e-10, 'three-mode limiting root')
    print('VERIFY_OK',COUNT,'supplementary_assertions')


if __name__ == '__main__':
    verify()
