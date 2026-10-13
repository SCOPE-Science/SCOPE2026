#!/usr/bin/env python3
"""Exact symbolic and independent numerical checks of synchronized sampling on P3 square."""
import sympy as S
x, a, b = S.symbols('x a b', real=True)
A = S.Matrix([[0,1,0],[1,0,1],[0,1,0]])
I = S.eye(3)
assert A**3 == 2*A
# Use cos(sqrt(2)t)=x and sin(sqrt(2)t)^2=1-x^2.
# Imaginary A term has only off-diagonal support, so real and imaginary parts do not interfere.
R = I + (x-1)*A**2/2
C = (1-x**2)*A.applyfunc(lambda z: z**2)/2
B = R.multiply_elementwise(R) + C
B_expected = S.Matrix([
 [(1+x)**2/4,(1-x**2)/2,(1-x)**2/4],
 [(1-x**2)/2,x**2,(1-x**2)/2],
 [(1-x)**2/4,(1-x**2)/2,(1+x)**2/4]])
assert (B-B_expected).applyfunc(S.simplify) == S.zeros(3)
assert (B*S.ones(3,1)-S.ones(3,1)).applyfunc(S.simplify) == S.zeros(3,1)
Q = S.kronecker_product(B,B)
reflect = S.eye(3); reflect[0,0]=0;reflect[2,2]=0;reflect[0,2]=1;reflect[2,0]=1
assert (B.subs(x,-x) - B*reflect).applyfunc(S.simplify) == S.zeros(3)
assert (Q.subs(x,-x) - Q*S.kronecker_product(reflect,reflect)).applyfunc(S.simplify) == S.zeros(9)
# A symmetric law has E[x]=E[x^3]=0 and E[x^2]=a, E[x^4]=b.
def expectation(z):
    return S.expand(sum(coeff * {0:1,1:0,2:a,3:0,4:b}[power[0]]
        for power,coeff in S.Poly(S.expand(z),x).terms()))
M = Q.applyfunc(expectation)
F = S.factor(sum((z-S.Rational(1,9))**2 for z in M))
F_expected = (81*b*b-108*a*b+18*b+124*a*a-60*a+9)/16
assert S.simplify(F-F_expected)==0
assert S.simplify(S.diff(F,b)-9*(9*b-6*a+1)/8)==0
H=S.factor(F.subs(b,a*a))
H_expected=(81*a**4-108*a**3+142*a*a-60*a+9)/16
assert S.simplify(H-H_expected)==0
G=81*a**3-81*a**2+71*a-15
assert S.simplify(S.diff(H,a)-G/4)==0
assert S.simplify(S.diff(G,a)-(243*(a-S.Rational(1,3))**2+44))==0
assert G.subs(a,0)<0 and G.subs(a,1)>0
lo,hi=S.Rational(2731289,10000000),S.Rational(2731291,10000000)
assert G.subs(a,lo)<0 and G.subs(a,hi)>0
assert S.simplify(H.subs(a,S.Rational(1,3))-S.Rational(1,9))==0
rho = S.N(S.nroots(G, maxsteps=100)[0],35)
# Do not assume numerical root ordering: choose the real member.
roots=S.nroots(G,n=35,maxsteps=100)
rho=[S.re(z) for z in roots if abs(float(S.im(z)))<1e-20][0]
delta=S.N(H.subs(a,rho),20)
assert 0.09<float(delta)<0.10
# Real-time two-atom witness, independent matrix exponential from the original 9x9 graph.
import numpy as np
from scipy.linalg import expm
An=np.array(A,dtype=float)
A9=np.kron(An,np.eye(3))+np.kron(np.eye(3),An)
r=float(rho)
angles=[np.arccos(np.sqrt(r)), np.pi-np.arccos(np.sqrt(r))]
times=[u/np.sqrt(2) for u in angles]
empirical=sum(np.abs(expm(1j*t*A9))**2/2 for t in times)
assert abs(float(np.sum((empirical-1/9)**2))-float(delta))<1e-12
exact_avg=np.array(M.subs({a:r,b:r*r}).evalf(),float)
assert np.max(np.abs(empirical-exact_avg))<1e-12
print('VERIFY_OK single_path_entries=9 product_entries=81 symmetric_quartic=True unique_cubic_root=True two_atom_exponential_entries=81 rho=%.15f delta=%.15f'%(r,float(delta)))
