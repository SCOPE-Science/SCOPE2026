#!/usr/bin/env python3
"""Exact algebraic verification of a 3-site weighted diffusion Padé identity."""
import itertools
from fractions import Fraction
import sympy as sp

h,a,b,c=sp.symbols('h a b c',real=True)
s=a+b+c
tau=a*b+a*c+b*c
L=sp.Matrix([[a+b,-a,-b],[-a,a+c,-c],[-b,-c,b+c]])
I=sp.eye(3)
D=48+48*s*h+(16*s*s+12*tau)*h*h+12*s*tau*h**3+3*tau*tau*h**4
U=-48*h-48*s*h*h+(12*tau-16*s*s)*h**3
V=24*h*h+8*s*h**3
M=D*I+U*L+V*L*L
N=12*I-6*h*L+h*h*L*L
B=12*I+6*h*L+h*h*L*L
assert (L**3-2*s*L*L+3*tau*L).applyfunc(sp.expand)==sp.zeros(3)
assert (M*B-D*N).applyfunc(lambda x:sp.factor(x))==sp.zeros(3)
for (i,j,w) in [(0,1,a),(0,2,b),(1,2,c)]:
    q=12*w+6*tau*h+tau*(2*s-3*w)*h*h
    assert sp.factor(M[i,j]-4*h*q)==0
J=sp.ones(3,3)
G=(2*s*(I-J/3)-L)/(3*tau)
assert (L*G-(I-J/3)).applyfunc(sp.simplify)==sp.zeros(3)
for i,j,w in [(0,1,a),(0,2,b),(1,2,c)]:
    assert sp.factor(G[i,j]-(3*w-2*s)/(9*tau))==0

# Independent rational matrix inversions (without using the polynomial remainder).
weights=[sp.Rational(0),sp.Rational(1,3),sp.Rational(1),sp.Rational(3),sp.Rational(7)]
steps=[sp.Rational(0),sp.Rational(1,10),sp.Rational(1,2),sp.Rational(1),sp.Rational(2),sp.Rational(10)]
ntrip=nmat=0
for wa,wb,wc in itertools.product(weights,repeat=3):
    st=wa*wb+wa*wc+wb*wc
    if st<=0: continue
    ntrip+=1
    lv=L.subs({a:wa,b:wb,c:wc})
    for hv in steps:
        nmat+=1
        di=12*I+6*hv*lv+hv*hv*lv*lv
        ni=12*I-6*hv*lv+hv*hv*lv*lv
        direct=ni*di.inv()
        expected=M.subs({a:wa,b:wb,c:wc,h:hv})/D.subs({a:wa,b:wb,c:wc,h:hv})
        assert direct==expected
        assert direct*sp.ones(3,1)==sp.ones(3,1)
        assert direct==direct.T
        assert all(direct[i,i]>0 for i in range(3))
        sr=wa+wb+wc
        for i,j,w in [(0,1,wa),(0,2,wb),(1,2,wc)]:
            q=12*w+6*st*hv+st*(2*sr-3*w)*hv*hv
            assert (direct[i,j]>=0)==(q>=0) if hv>0 else direct[i,j]==0

# Boundary examples: a 3-site weighted path is unconditional at ratio 2,
# but the same path with ratio 3 has a finite positivity horizon.
z=sp.symbols('z',nonnegative=True)
assert sp.expand((z-3)**2+3-(z*z-6*z+12))==0
assert sp.expand((z*z+6*z+12)-(z*z-6*z+12)-12*z)==0
q_path=12*3+6*3*h+3*(2*4-3*3)*h*h
assert sp.factor(q_path+3*(h*h-6*h-12))==0
# With weights 3,1,0, the unique critical transition vanishes at h=3+sqrt(21);
# the other two off-diagonal entries remain positive.
for hv,sgn in [(sp.Rational(7),1),(3+sp.sqrt(21),0),(sp.Rational(8),-1)]:
    mat=(12*I-6*hv*L.subs({a:3,b:1,c:0})+hv**2*(L.subs({a:3,b:1,c:0})**2))*(12*I+6*hv*L.subs({a:3,b:1,c:0})+hv**2*(L.subs({a:3,b:1,c:0})**2)).inv()
    assert sp.sign(mat[0,1])==sgn
    assert mat[0,2]>0 and mat[1,2]>0
print(f'VERIFY_OK: matrix quotient identity; Green-kernel identity; {ntrip} connected weight triples, {nmat} exact rational Padé matrices, {9*nmat} matrix-entry checks; sharp weighted-path transition')
