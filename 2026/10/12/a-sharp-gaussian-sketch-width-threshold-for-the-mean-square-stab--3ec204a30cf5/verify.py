"""Exact arithmetic checks for one-step squared-entry and sketch-row pivoting.

No external dependencies; analytic Gaussian invariance is established in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def trans(A):
    return [list(x) for x in zip(*A)]

def gram_norm_rows(A):
    return [sum(x*x for x in row) for row in A]

def residual(A,i,j):
    p=A[i][j]
    assert p
    return [[A[s][t]-A[s][j]*A[i][t]/p for t in range(2)] for s in range(2)]

def one(A,h):
    assert A==[[F(1),h],[h,F(1)]]
    det=F(1)-h*h
    total=2+2*h*h
    assert det>0
    for p in [1,2,3,4,6]:
        empirical=F(0)
        for i,j in product(range(2),repeat=2):
            R=residual(A,i,j)
            nonzero=[R[s][t] for s,t in product(range(2),repeat=2) if R[s][t]]
            assert len(nonzero)==1
            magnitude=abs(nonzero[0])
            empirical+=A[i][j]**2/total*(magnitude/(1-h))**p
        expected=(1+h)**p*(1+h**(2-p))/(1+h*h)
        assert empirical==expected,(h,p,empirical,expected)
    assert (1+h)/(1-h)<=2

def row_weight_symmetry(A,Omega):
    # Gaussian Omega and row-exchanged J Omega have the same law;
    # certify pointwise pairwise normalization for arbitrary nonzero test matrices.
    Y=mm(A,Omega)
    swapped=mm(A,list(reversed(Omega)))
    v=gram_norm_rows(Y)
    w=gram_norm_rows(swapped)
    assert sum(v)>0
    assert sum(v)==sum(w)
    assert (v[0],v[1])==(w[1],w[0])
    assert v[0]/sum(v)+w[0]/sum(w)==1

count=0
for k in range(3,104):
    h=F(1,k)
    A=[[F(1),h],[h,F(1)]]
    one(A,h)
    count+=1
for b in [1,2,3,5,9]:
    for h in [F(1,3),F(1,8),F(2,11),F(1,100)]:
        A=[[F(1),h],[h,F(1)]]
        for seed in range(1,19):
            O=[[F((seed+3*k+1)%(k+5)-2,k+3) for k in range(b)],
               [F((2*seed+2*k+3)%(k+7)-3,k+4) for k in range(b)]]
            row_weight_symmetry(A,O)
            count+=1
print('VERIFY_OK moment_families=101 Gaussian_exchange_test_cases=',count-101)

# Independent midpoint quadratures of the exact beta-ratio integrals.
from math import sin, cos, pi, log, sqrt

def midpoint(fn,n=80000):
    return sum(fn((i+.5)/n) for i in range(n))/n

for e in [0.07,0.1,0.2,0.4,0.7,0.9]:
    t=e*e
    # b=1: U=sin^2(theta), theta uniform [0,pi/2].
    s1=midpoint(lambda v:(t*sin(pi*v/2)**2)/(t*sin(pi*v/2)**2+cos(pi*v/2)**2),50000)
    exact1=e/(1+e)
    assert abs(s1-exact1)<1e-9,(e,s1,exact1)
    # b=2: U uniform on [0,1].
    s2=midpoint(lambda u:t*u/(1+(t-1)*u),50000)
    exact2=t*(t-1-log(t))/(t-1)**2
    assert abs(s2-exact2)<1e-8,(e,s2,exact2)
    mse1=1+(1/t-1)*exact1
    mse2=1+(1/t-1)*exact2
    assert abs(mse1-1/e)<1e-12
    assert abs(mse2-(-log(t))/(1-t))<1e-12
print('VERIFY_OK beta_integrals=12 exact_mean_square_identities=12')
