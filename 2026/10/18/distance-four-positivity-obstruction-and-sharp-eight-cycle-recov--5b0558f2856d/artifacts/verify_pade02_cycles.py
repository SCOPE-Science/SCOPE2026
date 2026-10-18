#!/usr/bin/env python3
"""Reproduce exact cycle positivity certificates for the [0/2] Pade heat step.

Requires SymPy >= 1.11; all principal certificates use rational polynomial algebra.
"""
import sympy as s

h=s.symbols('h', positive=True)

def lap_cycle(n):
    assert n>=3
    L=s.zeros(n)
    for i in range(n):
        L[i,i]=2
        L[i,(i+1)%n]=-1
        L[i,(i-1)%n]=-1
    return L

def step(n):
    L=lap_cycle(n)
    M=s.eye(n)+h*L+s.Rational(1,2)*h**2*L**2
    return M.inv()

def positive_coeffs(expr):
    nu,de=s.fraction(s.cancel(expr))
    a=s.Poly(nu,h); b=s.Poly(de,h)
    # A rational function with common numerator/denominator sign taken at h=1.
    if b.eval(1)<0: a=-a; b=-b
    return all(c>=0 for c in a.all_coeffs()) and all(c>=0 for c in b.all_coeffs()) and a.eval(1)>0 and b.eval(1)>0

count=0
for n in range(3,9):
    L=lap_cycle(n)
    T=step(n)
    assert s.simplify((s.eye(n)+h*L+(h*h/2)*L*L)*T-s.eye(n))==s.zeros(n)
    assert s.simplify(T*s.ones(n,1)-s.ones(n,1))==s.zeros(n,1)
    count+=2
    for i in range(n):
        for j in range(n):
            assert s.cancel(T[i,j]-T[0,(j-i)%n])==0
            count+=1
    for d in range(n//2+1):
        expr=s.factor(T[0,d]); sym=s.factor(T[0,(n-d)%n])
        assert s.cancel(expr-sym)==0
        count+=1
        if n<=7 or d<4:
            assert positive_coeffs(expr), (n,d,expr)
            count+=1
    if n==8:
        num=4*h**4+22*h**3+17*h**2-1
        denom=2*(2*h*h+2*h+1)*(8*h*h+4*h+1)*(h**4+4*h**3+8*h*h+4*h+1)
        assert s.cancel(T[0,4]-h**4*num/denom)==0
        assert s.diff(num,h)==16*h**3+66*h*h+34*h
        count+=2
        r=s.nroots(num)
        pos=[s.re(z) for z in r if abs(float(s.im(z)))<1e-12 and float(s.re(z))>0]
        assert len(pos)==1
        assert abs(float(pos[0])-0.21375796584462)<1e-11
        count+=2
    print('C_%d row distance kernels verified, n=%d'% (n,n//2+1))

z=s.symbols('z')
r=s.series(1/(1-z+z*z/2),z,0,6).removeO()
assert s.simplify(r-(1+z+z*z/2-z**4/4-z**5/4))==0
count+=1
# Distance-four obstructing coefficient on a path graph.
N=8
A=s.zeros(N)
for i in range(N-1): A[i,i+1]=A[i+1,i]=1
D=s.diag(*[sum(A[i,j] for j in range(N)) for i in range(N)])
L=D-A
assert (L**4)[0,4]==(A**4)[0,4]==1
assert all((L**k)[0,4]==0 for k in range(4))
count+=2
print('VERIFIED exact symbolic assertions:',count)
print('For every C_3,...,C_7 entry strictly positive at h>0; C_8 unique sharp root.')
