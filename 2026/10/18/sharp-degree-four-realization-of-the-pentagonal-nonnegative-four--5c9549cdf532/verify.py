#!/usr/bin/env python3
"""Exact algebraic checks for a positive-definite pentagon interpolation theorem.

SymPy checks the explicit identities; the universal inequalities and copositivity
argument are proved in the accompanying mathematical text.
"""
import sympy as s

x, delta = s.symbols('x delta', real=True)
rt = s.sqrt(5)
phi = (1 + rt) / 2
eta = (rt - 1) / 2
c1 = (rt - 1) / 4      # cos(2 pi / 5)
c2 = -(rt + 1) / 4     # cos(4 pi / 5)

N = 5 * phi + 8*x + 2*(8*x**4 - 8*x**2 + 1)
Q = x**2 - phi*x + (1+3*rt)/8
assert s.simplify(N-16*(x+phi/2)**2*Q) == 0
assert s.simplify(phi**2-4*(1+3*rt)/8) == 1-rt
F = N / (5*(phi+2))
for val, expected in [(1,1),(c1,eta),(c2,0)]:
    assert s.simplify(F.subs(x,val)-expected) == 0

P2 = ((x-c2)/(1-c2))**2
assert s.simplify(P2.subs(x,1)-1) == 0
assert s.simplify(P2.subs(x,c2)) == 0
assert s.simplify(P2.subs(x,c1)-eta**2) == 0
assert s.simplify(eta**2 - (3-rt)/2) == 0
assert (eta**2).evalf() < s.S.Half
assert s.simplify(phi*eta-1)==0

# Harmonic Fourier coefficients for F and for L(t)=1+cos(2t).
cf = {0:phi/(phi+2), 1:4/(5*(phi+2)), -1:4/(5*(phi+2)),
      4:1/(5*(phi+2)), -4:1/(5*(phi+2))}
assert s.simplify(sum(cf.values())-1)==0
assert all(v.evalf()>0 for v in cf.values())

# The sampled Gram and the copositive Horn witness H=J-2A(C5).
def Fvalue(d):
    return [s.S.One, eta, s.S.Zero][min(d%5,5-d%5)]
def Lvalue(d):
    return [s.S(2), 1+c2, 1+c1][min(d%5,5-d%5)]
G=s.Matrix(5,5,lambda i,j:Fvalue(i-j))
LL=s.Matrix(5,5,lambda i,j:Lvalue(i-j))
H=s.Matrix(5,5,lambda i,j: -1 if (i-j)%5 in (1,4) else 1)
assert s.simplify(sum(H[i,j]*G[i,j] for i in range(5) for j in range(5)) - 5*(2-rt))==0
assert s.simplify(sum(H[i,j]*LL[i,j] for i in range(5) for j in range(5)) - 5*(2+rt))==0
assert s.simplify((rt-2)/(rt+2) - (9-4*rt))==0
assert s.simplify(F.subs(x,0))>0  # F nonzero at the zeros of L

# For delta=1/100, all five sampled Fourier residues are represented by
# strictly positive coefficients; the Horn witness is strictly negative.
d=s.Rational(1,100)
KG=(G+d*LL)/(1+2*d)
assert all(complex(s.N(v)).real > 1e-12 and abs(complex(s.N(v)).imag) < 1e-12 for v in KG.eigenvals().keys())
assert s.N(sum(H[i,j]*KG[i,j] for i in range(5) for j in range(5))) < 0
print('VERIFY_OK exact cyclotomic factorization, five-point samples, Fourier weights, sharp cubic threshold, and Horn separation')
print('q_degree_le_3=',s.simplify(eta**2),'q_degree_4=',eta)
print('strict_example_delta=',d,'Horn=',s.simplify(sum(H[i,j]*KG[i,j] for i in range(5) for j in range(5))))
