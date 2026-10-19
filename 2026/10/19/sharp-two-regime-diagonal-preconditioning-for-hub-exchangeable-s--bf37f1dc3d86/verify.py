"""Independent finite checks for a two-coupling Stieltjes preconditioner.

Requirements: Python 3.10+ and NumPy. This verifies numerical consequences
and specific exact examples; general optimality is proved analytically.
"""
from fractions import Fraction as F
from math import sqrt
import random
import numpy as np

CHECKS = 0

def check(statement, detail=''):
    global CHECKS
    CHECKS += 1
    if not statement:
        raise AssertionError(f'check {CHECKS}: {detail}')

def parameters(m, a, b):
    d = 1-(m-1)*b
    check(m >= 3 and a > 0 and b > 0 and d > m*a*a)
    threshold = m*b*b/d
    x = max(d, b*(1+b)/(b+a*a))
    if a*a >= threshold:
        k = (d+a*sqrt(m*d))/(d-a*sqrt(m*d))
    else:
        k = (1+b)*(b+a*a)/(b*(d-m*a*a))
    return d, x, k

def matrix(m,a,b):
    A = np.eye(m+1, dtype=float)
    A[0,1:] = -a; A[1:,0] = -a
    A[1:,1:] -= b*(np.ones((m,m))-np.eye(m))
    return A

def condition(A, scale):
    e=np.linalg.eigvalsh(scale[:,None]*A*scale[None,:])
    return float(e[-1]/e[0]), e

# Exact fractional, nontrivial six-dimensional instance.
m=5; a=F(1,4); b=F(1,8); u=F(3,4)
d=1-(m-1)*b
check(d==F(1,2))
check(u==b*(1+b)/(b+a*a))
check(u+d==F(9,8)+F(1,8))
check(u*(d-m*a*a)==F(9,8)*F(1,8))
check(F(1,1)+b==F(9,8))
check((F(9,8))/(F(1,8))==9)

rng=random.Random(1729)
for m in range(3,12):
    for ib in range(1,8):
        b=ib/(12*(m-1))
        d=1-(m-1)*b
        for ia in range(1,8):
            a=sqrt(d/m)*(ia/9)
            d,u,k=parameters(m,a,b)
            A=matrix(m,a,b)
            eigA=np.linalg.eigvalsh(A)
            check(eigA[0]>0)
            scale=np.ones(m+1);scale[0]=sqrt(u)
            calc,eig=condition(A,scale)
            check(abs(calc-k)<1e-10*max(1,k), f'closed formula m={m}, a={a}, b={b}')
            block=np.array([[u,-sqrt(m*u)*a],[-sqrt(m*u)*a,d]])
            reduced=np.sort(np.r_[np.linalg.eigvalsh(block),np.full(m-1,1+b)])
            check(np.max(np.abs(eig-reduced))<1e-10)
            cross=b*(1+b)/(b+a*a)
            check(abs(u-max(d,cross))<1e-12)
            check((a*a >= m*b*b/d)==(u==d) or abs(u-d)<1e-12)
            for factor in (.5,.75,.9,.95,1.05,1.1,1.25,1.5,2):
                v=u*factor
                s=np.ones(m+1);s[0]=sqrt(v)
                trial,_=condition(A,s)
                check(trial>=k-1e-9*max(1,k), f'symmetric deviation at {m,a,b,factor}')
            for _ in range(4):
                scales=np.exp(np.array([rng.uniform(-.5,.5) for _ in range(m+1)]))
                trial,_=condition(A,scales)
                check(trial>=k-1e-9*max(1,k),'asymmetric competitor')

# Equality at the exact regime boundary for a rational sample m=3,b=1/10.
m=3;b=F(1,10);d=1-(m-1)*b
asq=m*b*b/d
check(asq==F(3,80))
check(b*(1+b)/(b+asq)==d)
# Jacobi optimal exactly on the homogeneous line a=b.
for m in range(3,30):
    b=1/(4*m); a=b
    d,u,k=parameters(m,a,b)
    check(abs(u-1)<1e-12)
    check(abs(k-(1+b)/(1-m*b))<1e-11)

print(f'PASS {CHECKS} checks')
