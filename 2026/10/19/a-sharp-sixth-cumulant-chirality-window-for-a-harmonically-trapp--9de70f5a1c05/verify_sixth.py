#!/usr/bin/env python3
"""Exact stationary sixth-cumulant and phase-threshold checks for a chiral active particle.

Run: python verify_sixth.py
Requires: Python 3, sympy.
"""
import sympy as s
b, x, w = s.symbols('b x w', real=True)
I = s.I
H1=(b+1)**2+x
H2=(b+2)**2+x
H3=(b+3)**2+x
J3=(3*b+1)**2+x
J5=(5*b+1)**2+x

Q=(b*x**4
 +(36*b**3+29*b**2+b)*x**3
 +(294*b**5+727*b**4+533*b**3+153*b**2+285*b+216)*x**2
 +(484*b**7+3863*b**6+10439*b**5+8958*b**4-6038*b**3-14997*b**2-8453*b-1392)*x
 +(225*b**9+3165*b**8+18739*b**7+60773*b**6+117845*b**5+140183*b**4+100985*b**3+41711*b**2+8734*b+696))

# Fourier-generator moment hierarchy, computed at the algebraic complex variable w.
M={(0,0):s.S.One}
def at(n,j):
    return M.get((n,j),s.S.Zero)
for n in range(1,7):
    for j in range(-n,n+1,2):
        if j<0: continue
        val=s.cancel(s.Rational(n,2)*(at(n-1,j-1)+at(n-1,j+1))/(n*b+j*j-I*j*w))
        M[n,j]=val
        if j>0:M[n,-j]=s.conjugate(val)
    # for every n all allowed modes are generated, all forbidden are zero

def real_expr(expr):
    return s.cancel(s.together(s.expand_complex(expr)).subs(w**2,x))

m2,m4,m6=(real_expr(M[n,0]) for n in (2,4,6))
k6=s.cancel(m6-15*m4*m2+30*m2**3)
expected=5*Q/(4*b*H1**3*H2*H3*J3*J5)
assert s.cancel(k6-expected)==0, 'Exact sixth cumulant algebra'
assert s.cancel(m2-(b+1)/(2*b*H1))==0, 'Second moment'
Q0=s.factor(Q.subs(b,0))
assert s.expand(Q0-24*(9*x*x-58*x+29))==0
roots0=((29-2*s.sqrt(145))/9,(29+2*s.sqrt(145))/9)
assert all(s.simplify(Q0.subs(x,z))==0 for z in roots0)

# Convex in nonnegative x: all coefficients of Q_xx are strictly positive for b>0.
qco=s.Poly(Q,x).all_coeffs()
assert all(s.Poly(s.diff(Q,x,2),x).all_coeffs()[j].subs(b,s.Rational(1,2))>0 for j in range(3))
assert all(all(co>=0 for co in s.Poly(c,b).all_coeffs()) for c in qco[:3])
# The exact resultant has one root in (0,1/2), one additional root beyond 1/2.
R=s.resultant(Q,s.diff(Q,x),x)
F=s.cancel(R/(-49152*b**2*(b+1)**4))
assert s.denom(F)==1
assert s.Poly(F,b).degree()==23
assert s.Poly(F,b).count_roots(0,s.Rational(1,2))==1
assert s.Poly(F,b).count_roots(s.Rational(1,2),s.oo)==1
assert s.Poly(F,b).count_roots(s.Rational(11,25),s.Rational(9,20))==1
# b>=1/2 positivity certificate: Q=a0+a1*x+a2*x^2 + positive higher terms.
a0,a1,a2=qco[-1],qco[-2],qco[-3]
S=s.cancel((4*a0*a2-a1*a1)/(b+1)**3)
assert s.denom(S)==1
shift_co=s.Poly(s.expand(S.subs(b,b+s.Rational(1,2))),b).all_coeffs()
assert all(c>0 for c in shift_co), 'Strict quadratic discriminant bound for b>=1/2'
# One exact point with two positive roots, another with zero positive roots.
assert s.Poly(Q.subs(b,s.Rational(1,10)),x).count_roots(0,s.oo)==2
assert s.Poly(Q.subs(b,s.Rational(1,2)),x).count_roots(0,s.oo)==0
# Confirm the leading k->0 sixth cumulant, useful independently for asymptotic inspection.
lim6=s.cancel((b*expected).subs(b,0))
assert s.cancel(lim6-30*(9*x*x-58*x+29)/((x+1)**5*(x+4)*(x+9)))==0
# Fourth cumulant cross-check and sign boundary is prior, not claimed as novel.
m4c=s.factor(m4-3*m2*m2)
P4=(9*b**5+60*b**4+10*b**3*x+148*b**3+12*b**2*x+166*b**2+b*x*x-8*b*x+83*b-10*x+14)
exp4=-3*P4/(8*b*H1**2*H2*J3)
assert s.cancel(m4c-exp4)==0
assert s.cancel((b*exp4).subs(b,0)-(-3*(14-10*x)/(8*(x+1)**3*(x+4))))==0
# Numerical enclosure is used only to report approximations; existence/uniqueness is exact above.
sol=s.nsolve([Q,s.diff(Q,x)],[b,x],[s.Rational(9,20),7],prec=35)
assert s.Rational(11,25)<sol[0]<s.Rational(9,20)
assert s.Rational(6,1)<sol[1]<s.Rational(8,1)
print('PASS: generator recurrence, cumulant rational identity, exact root counts, shift certificate, and asymptotics')
print('critical beta',sol[0])
print('critical squared chirality',sol[1])
print('weak-trap squared-chirality endpoints',*[str(s.N(z,16)) for z in roots0])
