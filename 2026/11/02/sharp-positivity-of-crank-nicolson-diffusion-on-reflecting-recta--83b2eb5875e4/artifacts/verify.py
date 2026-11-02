#!/usr/bin/env python3
"""Reproduce finite-grid Crank--Nicolson positivity and square-grid asymptotics.

Dependencies: Python 3, sympy, mpmath. All finite matrix calculations below
use exact rational arithmetic; asymptotic tests use high-precision quadrature.
"""
from itertools import product
import mpmath as mp
import sympy as sp

mp.mp.dps = 55
CHECKS = 0

def check(v, msg):
    global CHECKS
    if not v:
        raise AssertionError(msg)
    CHECKS += 1

def lap_path(n):
    A = sp.zeros(n)
    for i in range(n-1):
        A[i,i] += 1
        A[i+1,i+1] += 1
        A[i,i+1] -= 1
        A[i+1,i] -= 1
    return A

def lap_rect(m,n):
    return sp.kronecker_product(lap_path(m),sp.eye(n)) + sp.kronecker_product(sp.eye(m),lap_path(n))

def centers(m,n):
    return {(i*n+j) for i in range(m) for j in range(n)
            if i in ((m-1)//2,m//2) and j in ((n-1)//2,n//2)}

def finite_root(m,n):
    def w(n):
        i = (n-1)//2
        out=[(mp.mpf(0),mp.mpf(1)/n)]
        for k in range(1,n):
            out.append((2-2*mp.cos(mp.pi*k/n),mp.mpf(2)/n*mp.cos(mp.pi*k*(i+mp.mpf('0.5'))/n)**2))
        return out
    spectrum=[(x+y,wx*wy) for x,wx in w(m) for y,wy in w(n)]
    def g(s):
        return mp.fsum(wt/(1+s*lam) for lam,wt in spectrum)
    lo=mp.mpf(0); hi=mp.mpf(2)
    for k in range(95):
        mid=(lo+hi)/2
        if g(mid)>mp.mpf('.5'):lo=mid
        else:hi=mid
    return (lo+hi)/2

# Independent rational inversions, including all off-diagonals and every
# diagonal return, at a pre-critical and post-critical rational step.
for m,n in [(2,2),(2,3),(3,3),(3,4),(4,4)]:
    N=m*n; L=lap_rect(m,n); I=sp.eye(N)
    check(L==L.T,f'symmetry {m} {n}')
    check(L*sp.ones(N,1)==sp.zeros(N,1),f'zero row sums {m} {n}')
    for s in [sp.Rational(1,4),sp.Rational(1,3),sp.Rational(1,2),sp.Rational(1,1)]:
        R=(I+s*L).inv()
        C=2*R-I
        center=centers(m,n)
        least=min(R[k,k] for k in range(N))
        for k in range(N):
            check(R[k,k]>=least, f'internal consistency {m} {n} {s}')
            if k in center:check(R[k,k]==least,f'center {m} {n} {s}')
            else:check(R[k,k]>least,f'noncentral strictness {m} {n} {s}')
            check(sum(R[k,j] for j in range(N))==1,f'resolvent rows {m} {n}')
            check(sum(C[k,j] for j in range(N))==1,f'CN rows {m} {n}')
            for j in range(N):
                if k!=j:check(C[k,j]>0,f'CN off-diagonal positivity {m} {n} {s}')
        check((min(C[k,k] for k in range(N))>=0)==(least>=sp.Rational(1,2)),f'threshold criterion {m} {n}')

# Independently compare spectral thresholds against direct dense matrix
# entrywise positivity for several finite rectangles.
for m,n in [(2,2),(2,3),(2,5),(3,3),(3,4),(4,4),(4,5),(5,5),(5,6)]:
    t=finite_root(m,n)
    L=mp.matrix([[int(x) for x in row] for row in lap_rect(m,n).tolist()]);N=m*n
    check(t>mp.mpf('0.29'),f'low threshold {m} {n}')
    for mult,positive in [(mp.mpf('0.99'),True),(mp.mpf('1.01'),False)]:
        B=mp.eye(N)+mult*t*L
        R=mp.inverse(B)
        C=2*R-mp.eye(N)
        check((min(C[i,i] for i in range(N))>=0)==positive,f'crossing {m} {n}')
        check(min(C[i,j] for i in range(N) for j in range(N) if i!=j)>0,f'offdiagonal {m} {n}')

# Elliptic lattice Green constant with modulus convention.
def ginf(s):
    return 2/(mp.pi*(1+4*s))*mp.ellipk((4*s/(1+4*s))**2)
s0=mp.findroot(lambda s:ginf(s)-mp.mpf('.5'),(mp.mpf('.28'),mp.mpf('.31')))
check(abs(ginf(s0)-mp.mpf('.5'))<mp.mpf('1e-45'),'elliptic root')
D=-mp.diff(ginf,s0)
xi=mp.acosh(1+1/(2*s0))
c=1/(2*s0*mp.sqrt(2*mp.pi*mp.sinh(xi)))
Aodd=4*c/D
Aeven=4*c*mp.cosh(xi)/D
check(D>0 and Aodd>0 and Aeven>Aodd,'coefficient positivity')

# Validate 2D lattice Green against independent double Fourier integral.
for s in [mp.mpf('.2'),s0,mp.mpf('.4')]:
    # Integrate in one angle explicitly, then one-dimensional quadrature.
    f=lambda theta:1/mp.sqrt((1+4*s-2*s*mp.cos(theta))**2-(2*s)**2)
    g=mp.quad(f,[0,mp.pi])/mp.pi
    check(abs(g-ginf(s))<mp.mpf('1e-40'),f'elliptic Fourier {s}')

# Asymptotic correction, odd and even n. Print ratios as numerical evidence,
# not as substitutes for the analytic Laplace-method proof.
ratios=[]
for n in [5,6,7,8,9,10,11,12,13,14,15,16,17,18]:
    t=finite_root(n,n)
    err=t-s0
    amp=Aodd if n%2 else Aeven
    model=amp*mp.exp(-xi*n)/mp.sqrt(n)
    ratio=err/model
    check(t>s0 and err>0,f'finite above limit {n}')
    check(mp.mpf('.75')<ratio<mp.mpf('1.5'),f'quantitative size {n} ratio={ratio}')
    ratios.append((n,mp.nstr(t,21),mp.nstr(ratio,12)))
for parity in (0,1):
    r=[mp.mpf(x[2]) for x in ratios if x[0]%2==parity]
    check(abs(r[-1]-1)<abs(r[0]-1),f'asymptotic convergence parity {parity}')

print('ALL CHECKS PASS:',CHECKS)
print('lattice critical s0=',mp.nstr(s0,45))
print('physical hκ/Δx²=',mp.nstr(2*s0,44))
print('axis mass xi=',mp.nstr(xi,40))
print('D=',mp.nstr(D,35),'axis prefactor c=',mp.nstr(c,35))
print('A_odd=',mp.nstr(Aodd,40),'A_even=',mp.nstr(Aeven,40))
print('n : root : asymptotic ratio (approaches 1 separately by parity)')
for r in ratios:print(' : '.join(map(str,r)))
