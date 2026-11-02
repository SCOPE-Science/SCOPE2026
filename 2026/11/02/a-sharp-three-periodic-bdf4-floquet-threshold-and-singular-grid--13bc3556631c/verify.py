#!/usr/bin/env python3
"""Exact symbolic checks for a three-periodic variable-coefficient BDF4 theorem.

Requires Python 3 and SymPy. All identities in the proof are polynomial/rational
identities; the floating-point comparisons below are supplementary only.
"""
import sympy as sp

R = sp.symbols('R', positive=True)
s = sp.symbols('s', positive=True)


def bdf4_matrix(h):
    x = [sp.Integer(0)]
    for h_j in h:
        x.append(x[-1] - h_j)
    # Derivative weights for the degree-four Lagrange interpolant.
    a = [sum(1/(x[0]-x[j]) for j in range(1, 5))]
    for j in range(1, 5):
        numerator = sp.prod(-x[k] for k in range(1, 5) if k != j)
        denominator = sp.prod(x[j]-x[k] for k in range(5) if k != j)
        a.append(numerator/denominator)
    u = [sp.cancel(sum(a[j+1:])/a[0]) for j in range(1, 4)]
    return sp.Matrix([[*u], [1,0,0], [0,1,0]])


def three_steps(pattern):
    return [bdf4_matrix([pattern[(i-j) % 3] for j in range(4)]) for i in range(3)]


def invariant_formulas(A):
    a0, a1, a2 = A
    u0,v0,w0 = a0[0,0],a0[0,1],a0[0,2]
    u1,v1,w1 = a1[0,0],a1[0,1],a1[0,2]
    u2,v2,w2 = a2[0,0],a2[0,1],a2[0,2]
    trace = u0*u1*u2+u0*v2+u1*v0+u2*v1+w0+w1+w2
    second = u0*v2*w1+u1*v0*w2+u2*v1*w0-v0*v1*v2+w0*w1+w0*w2+w1*w2
    det = w0*w1*w2
    return trace,second,det

# The finite-ratio theorem at (1,R,3).
A=three_steps([1,R,sp.Integer(3)])
tr,e2,det=invariant_formulas(A)
D=(5*R**2+53*R+136)*(R**3+23*R**2+145*R+267)*(7*R**3+37*R**2+52*R+16)
U=23*R**8+569*R**7+5833*R**6+32661*R**5+112864*R**4+264082*R**3+443584*R**2+497504*R+267072
V=3*R**8+57*R**7+490*R**6+2558*R**5+8743*R**4+19753*R**3+31676*R**2+39280*R+27648
W=12*R*(R+1)*(R+3)*(R+4)**3
P=R**7-38*R**6-1120*R**5-10170*R**4-42193*R**3-81856*R**2-60496*R-3104
for label,delta in [('trace',tr+2*U/D),('second',e2-V/D),('det',det-W/D)]:
    assert sp.cancel(delta)==0, label
assert sp.expand(D-2*U+V+W+8*(R+3)*P)==0

# Four strict Jury expressions other than the sign-changing one.
Q1=sp.Poly(D-W,R)
Q2=sp.Poly(D+2*U+V-W,R)
Q3=sp.Poly(sp.expand(D*D-D*V-2*U*W-W*W),R)
for label, p in [('D-W',Q1),('p(1)',Q2),('Schur remainder',Q3)]:
    assert all(t>0 for t in p.all_coeffs()), label
assert sp.Poly(P,R).all_coeffs()[0]>0
assert all(t<0 for t in sp.Poly(P,R).all_coeffs()[1:])
assert P.subs(R,59)<0<P.subs(R,60)
root=sp.nsolve(P,sp.Rational(597,10),prec=40)
assert sp.Rational(59)<root<sp.Rational(60)

# General singular limit as R tends to infinity, for each fixed s>0.
A=three_steps([1,R,s])
limits=[
    (A[0][0,0], 0, 1/(s*(s+2))),
    (A[0][0,1], 3, -4*(s+1)**2/(s+2)),
    (A[0][0,2], 2, (s+1)**2/(s+2)),
    (A[1][0,0], -2, 4/(7*(s+1))),
    (A[1][0,1], -2, -4/(7*s*(s+1))),
    (A[1][0,2], 0, sp.Rational(1,7)),
    (A[2][0,0], 2, 6*s**2),
    (A[2][0,1], 0, -s**2/(s+1)),
    (A[2][0,2], 0, s/(s+1)),
]
for expression, power, expected in limits:
    obtained=sp.limit(expression*R**power,R,sp.oo)
    assert sp.cancel(obtained-expected)==0,(expression,power,obtained,expected)

# Substitution into exact algebraic invariant formulas for companion triples.
u0=1/(s*(s+2)); v0=0; w0=0
u1=4/(7*(s+1)); v1=-4/(7*s*(s+1)); w1=sp.Rational(1,7)
u2=6*s**2; v2=-s**2/(s+1); w2=s/(s+1)
trace_limit=u0*u1*u2+u0*v2+u2*v1+w1+w2
second_limit=u0*v2*w1+w1*w2
assert sp.factor(trace_limit+2*(8*s-1)/(7*(s+2)))==0
assert sp.factor(second_limit-s/(7*(s+2)))==0
assert sp.factor(1-2*(8*s-1)/(7*(s+2))+s/(7*(s+2))-8*(2-s)/(7*(s+2)))==0

# Independently compare direct monodromy entries and eigenvalues for sample ratios.
for t in [sp.Rational(1,100),sp.Rational(1,2),sp.Integer(1),sp.Integer(10),sp.Integer(59),sp.Integer(60),sp.Integer(100)]:
    Fmat=three_steps([1,t,3]); T=Fmat[2]*Fmat[1]*Fmat[0]
    got=sp.Poly(T.charpoly().as_expr(),T.charpoly().gen)
    expected=sp.Poly(sp.Symbol('z')**3+2*U.subs(R,t)/D.subs(R,t)*sp.Symbol('z')**2+V.subs(R,t)/D.subs(R,t)*sp.Symbol('z')-W.subs(R,t)/D.subs(R,t),sp.Symbol('z'))
    assert [sp.cancel(a-b)==0 for a,b in zip(got.all_coeffs(),expected.all_coeffs())]==[True]*4

print('EXACT_VERIFIED: coefficient identities, all positivity certificates, unique threshold, asymptotic limit, sampled direct monodromy')
print('critical_ratio:',root)
print('degree_schur_remainder:',Q3.degree())
