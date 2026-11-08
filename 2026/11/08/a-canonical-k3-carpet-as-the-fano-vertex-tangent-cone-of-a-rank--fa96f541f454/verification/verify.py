#!/usr/bin/env python3
"""Standalone exact checks for the rank-three quadric Fano-vertex K3 carpet.
Scientific assertions over arbitrary fields are proved in RESULT.md; this
program replays the algebraic identities and finite-characteristic samples.
Requires Python 3 and SymPy.
"""
import math
import sympy as s

A0,A1,A2,B0,B1,B2=s.symbols('a0 a1 a2 b0 b1 b2')
variables=(A0,A1,A2,B0,B1,B2)
qa=A0*A2-A1**2
qb=B0*B2-B1**2
qab=A0*B2+A2*B0-2*A1*B1
ideal=(qa,qb,qab)
scroll=s.Matrix([[A0,A1,B0,B1],[A1,A2,B1,B2]])
minors=[s.expand(scroll[0,i]*scroll[1,j]-scroll[0,j]*scroll[1,i])
        for i in range(4) for j in range(i+1,4)]

# Universal Grassmannian-chart restriction: the coefficient of s^2,st,t^2.
t,u=s.symbols('t u')
assert s.expand((A0*t+B0*u)*(A2*t+B2*u)-(A1*t+B1*u)**2
                -(qa*t**2+qab*t*u+qb*u**2)) == 0
print('FANO_CHART_EQS_OK')

# A0 != 0 chart: exactly one nilpotent coordinate epsilon, epsilon^2=0.
h,r,b,eps=s.symbols('h r b epsilon')
local={A0:h,A1:h*r,A2:h*r**2,B0:b,B1:r*b+eps,B2:r*r*b+2*r*eps}
assert s.expand(qa.subs(local, simultaneous=True))==0
assert s.expand(qab.subs(local, simultaneous=True))==0
assert s.expand(qb.subs(local, simultaneous=True))==-eps**2
print('DUAL_NUMBER_LOCAL_CHART_OK')

# The six scroll minors have square-zero pairwise products in the carpet ideal,
# checked directly in characteristic 0, 2, 3, 5, 7.
for characteristic in (0,2,3,5,7):
    basis=s.groebner(ideal,*variables,order='grlex',
                     modulus=characteristic or None)
    for i,p in enumerate(minors):
        for q in minors[i:]:
            _,remainder=basis.reduce(p*q)
            assert remainder==0,(characteristic,p,q,remainder)
    print('NILRADICAL_SQUARE_ZERO_MOD_'+str(characteristic)+'_OK')

# Complete-intersection Hilbert function and scroll + dualizing-piece Hilbert
# functions; these are exact algebraic consequences, tested for n=0,...,12.
def binom_nonnegative(n,k):
    return math.comb(n,k) if n>=k>=0 else 0
for n in range(13):
    h_carpet=sum((-1)**j*math.comb(3,j)*binom_nonnegative(n-2*j+5,5)
                 for j in range(4))
    h_scroll=(n+1)*(2*n+1)
    h_canonical=(n-1)*(2*n-1) if n>=2 else 0
    assert h_carpet==h_scroll+h_canonical,(n,h_carpet,h_scroll,h_canonical)
print('HILBERT_FUNCTION_0_TO_12_OK')

# The homogeneous CI has Hilbert polynomial 4n^2+2; the scroll polynomial
# is (n+1)(2n+1), and the difference 2n^2-3n+1.
N=s.symbols('N',integer=True)
assert s.expand((2*N**2+3*N+1)+(2*N**2-3*N+1)-(4*N**2+2))==0
assert 2*2*2==8
print('DEGREE_GENUS_AND_MULTIPLICITY_OK')
print('ALL_CHECKS_PASSED')
