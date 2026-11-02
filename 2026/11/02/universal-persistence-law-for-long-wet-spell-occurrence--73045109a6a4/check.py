#!/usr/bin/env python3
"""Pure-standard-library checks for wet-spell spectral optimization.

The analytic proof in RESULT.md, not these finite checks, establishes all-length assertions.
Run: python3 check.py
"""
from fractions import Fraction
from itertools import product
from math import exp, log, sqrt, expm1

count = 0

def test(condition, detail=''):
    global count
    if not condition:
        raise AssertionError(detail)
    count += 1

def close(a, b, tolerance=3e-9):
    test(abs(a-b) <= tolerance*(1+abs(a)+abs(b)), f'{a}, {b}')

def transition(k,q):
    M=[[0 for _ in range(k)] for _ in range(k)]
    M[0][0]=q; M[0][1]=1-q
    for j in range(1,k):
        M[j][0]=1-q
        if j<k-1:M[j][j+1]=q
    return M

def probability_dp(n,k,q):
    masses=[Fraction(0) for _ in range(k)]
    masses[0]=masses[1]=Fraction(1,2)
    M=transition(k,q)
    for _ in range(n-1):
        nxt=[Fraction(0) for _ in range(k)]
        for i in range(k):
            for j in range(k):nxt[j]+=masses[i]*M[i][j]
        masses=nxt
    return sum(masses)

def probability_direct(n,k,q):
    p=Fraction(0)
    for s in product((0,1),repeat=n):
        if any(all(s[t+j]==1 for j in range(k)) for t in range(n-k+1)):
            continue
        mass=Fraction(1,2)
        for t in range(1,n):
            mass*=q if s[t]==s[t-1] else 1-q
        p+=mass
    return p

def determinant(A):
    # Fraction Gaussian elimination with row pivoting.
    n=len(A);B=[[Fraction(a) for a in row] for row in A]
    product=Fraction(1)
    for j in range(n):
        pivot=next((i for i in range(j,n) if B[i][j]),None)
        if pivot is None:return Fraction(0)
        if pivot!=j:
            B[j],B[pivot]=B[pivot],B[j];product=-product
        u=B[j][j];product*=u
        for i in range(j+1,n):
            if B[i][j]:
                z=B[i][j]/u
                for h in range(j+1,n):B[i][h]-=z*B[j][h]
                B[i][j]=0
    return product

def characteristic(k,q,L):
    M=transition(k,q)
    return determinant([[(L if i==j else Fraction(0))-M[i][j] for j in range(k)] for i in range(k)])

def formula(k,q,L):
    m=k-1
    return L**m*(L-q)-(1-q)**2*sum(q**j*L**(m-1-j) for j in range(m))

def residual(m,r):
    # Transformed optimizer equation, no cancellation even for m large.
    if r<=0:return -m
    if r>=1:return m
    v=-expm1(m*log(r))
    S=v/(1-r)
    return 2*r*S/(1+sqrt(v))-m

def optimum(m):
    lo=0.0;hi=1.0
    for _ in range(110):
        r=(lo+hi)/2
        if residual(m,r)>0:hi=r
        else:lo=r
    r=(lo+hi)/2
    h=r+(1-r)/sqrt(-expm1(m*log(r)))
    return r, r/h, 1/h

def eigenvalue_pf(M,steps=6000):
    k=len(M)
    v=[1.0]*k
    eigen=1.0
    for _ in range(steps):
        w=[sum(M[i][j]*v[j] for j in range(k)) for i in range(k)]
        eigen=max(w)
        nxt=[w[i]/eigen for i in range(k)]
        if max(abs(v[i]-nxt[i]) for i in range(k))<1e-14:
            return eigen
        v=nxt
    raise RuntimeError('Power iteration did not converge; not evidence of impossibility')

# Independent exact enumeration of trajectories and Markov recursion.
for k in range(2,6):
    for n in range(k,11):
        for q in (Fraction(1,7),Fraction(2,5),Fraction(1,2),Fraction(4,5)):
            test(probability_dp(n,k,q)==probability_direct(n,k,q),f'enumeration {k,n,q}')

# Exact characteristic-polynomial checks at rational argument values.
for k in range(2,7):
    for q in (Fraction(1,7),Fraction(2,5),Fraction(3,4)):
        for L in (Fraction(1,4),Fraction(2,3),Fraction(9,8)):
            test(characteristic(k,q,L)==formula(k,q,L),f'characteristic {k,q,L}')

# Global maximizer checked numerically against a spectral radius computed
# independently via Perron power iteration. The proof is analytic.
for k in range(2,21):
    r,q,l=optimum(k-1)
    close(residual(k-1,r),0,2e-8)
    close(eigenvalue_pf(transition(k,q)),l,2e-9)
    for p in (.05,.13,.25,.4,.5,.65,.8,.92,.97):
        test(eigenvalue_pf(transition(k,p))>=l-1e-9,f'nonoptimal case {k,p}')

# Checks the two known calibration cases and new k=3 value.
close(optimum(1)[1],3/5)
close(optimum(1)[2],4/5)
close(optimum(2)[1],0.7395349543396587)

# Independently solve the scalar asymptotic equation.
lo=.001;hi=2.0
for _ in range(100):
    c=(lo+hi)/2
    g=2*(-expm1(-c))/(1+sqrt(-expm1(-c)))-c
    if g>0:lo=c
    else:hi=c
c=(lo+hi)/2
s=sqrt(-expm1(-c))
a=c/s;b=c*(1/s-1)
for m in (100,200,500,1000,2000):
    r,q,l=optimum(m)
    test(abs(m*(1-q)-a)<3/m+.0001,f'asymptotic q {m}')
    test(abs(m*(1-l)-b)<3/m+.0001,f'asymptotic L {m}')
print('UNIVERSAL_C',format(c,'.14f'))
print('ASYMPTOTIC_Q_CONSTANT',format(a,'.14f'))
print('ASYMPTOTIC_EIGEN_CONSTANT',format(b,'.14f'))
print('K3',*[format(v,'.14f') for v in optimum(2)])
print('VERIFY_OK assertions=',count)
