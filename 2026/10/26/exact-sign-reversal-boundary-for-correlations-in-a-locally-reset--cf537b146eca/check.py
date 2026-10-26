"""Reproducible exact calculations for local-reset voter correlations.

Requires Python 3 and SymPy. This program checks the algebraic formulas;
its finite numerical tests are not substitutes for the analytic proof.
"""
from fractions import Fraction
from math import sqrt
import sympy as sp

q, c, r = sp.symbols('q c r', real=True)
a = (1-q)/(1+q)
N = 4*c**2*q**4 - 3*c*q**4 - 2*c*q**3 - 2*c*q**2 - 2*c*q + c + 2*q**3 + 2*q
G = sp.cancel(q+a*a*(q+c*(1-q*q)-c*c*q**3)/(1-c*q)**2)
assert sp.factor(G-N/((1+q)**2*(1-c*q)**2)) == 0
assert sp.factor(G.subs(c,1)-1) == 0
assert sp.factor(G.subs(c,0)-2*q*(q*q+1)/(q+1)**2) == 0
assert sp.factor(G.subs(c,-1)-(7*q**3-3*q**2+5*q-1)/(q+1)**3) == 0

P = 4*c*c*q**4-2*c*q**4-7*c*q**3+3*c*q**2-c*q-c+q**3+3*q**2-q+1
assert sp.factor(sp.diff(G,q)-2*(c-1)*P/((1+q)**3*(c*q-1)**3)) == 0
assert sp.factor(sp.diff(G,c)-(q-1)**2*(3*c*q**3-c*q-q*q-1)/((q+1)**2*(c*q-1)**3)) == 0
assert sp.factor(sp.diff(7*q**3-3*q**2+5*q-1,q)-(21*q*q-6*q+5))==0

# Explicit geometric resolvent, stationary boundary equation, and convolution.
def p(n,qq):
    return (1-qq)/(1+qq)*qq**abs(n)
def p2(n,qq):
    return ((1-qq)/(1+qq))**2*qq**abs(n)*(abs(n)+1+2*qq**2/(1-qq**2))

def direct_g1(qq,cc,cutoff=300):
    b0=sum(p2(-j,qq)*cc**abs(j) for j in range(-cutoff,cutoff+1))
    b1=sum(p2(1-j,qq)*cc**abs(j) for j in range(-cutoff,cutoff+1))
    return qq+b1-qq*b0

n_tests=0
for qq in [0.09,0.2,0.4,0.6,0.8]:
    rr=(1-qq)**2/(2*qq)
    for cc in [-1.0,-0.7,-0.25,0,0.3,0.8,1.0]:
        gg=float(G.subs({q:qq,c:cc}))
        assert abs(direct_g1(qq,cc)-gg)<1e-11
        # The Green kernel is a probability distribution, reproducing r.
        assert abs(sum(p(j,qq) for j in range(-300,301))-1)<1e-11
        assert abs(rr-(1-qq)**2/(2*qq))<1e-12
        n_tests += 3

# Rational interval checks support, but do not prove, symbolic sign arguments.
for qq in [sp.Rational(j,31) for j in range(1,31)]:
    for cc in [-sp.Rational(i,13) for i in range(0,14)]:
        assert P.subs({q:qq,c:cc}) > 0
        n_tests+=1
    for cc in [sp.Rational(i,13) for i in range(-13,14)]:
        assert sp.diff(G,c).subs({q:qq,c:cc}) > 0
        n_tests+=1

root=sp.nroots(7*q**3-3*q**2+5*q-1,maxsteps=200)
q0=float(next(z for z in root if abs(float(sp.im(z)))<1e-12 and 0<float(sp.re(z))<1))
r0=(1-q0)**2/(2*q0)
assert 0.21374036290<q0<0.21374036291
assert 1.44615693666<r0<1.44615693668
assert sp.simplify(G.subs({c:-1,q:2-sp.sqrt(3)})-(sp.Rational(5,3)-8*sp.sqrt(3)/9))==0
assert sp.simplify(G.subs({c:-1,q:3-2*sp.sqrt(2)})-(2-3*sp.sqrt(2)/2))==0
print('CHECKS PASSED')
print('Direct kernel, normalization, and formula comparisons:',n_tests)
print('Polynomial/derivative identities: PASSED')
print('Antiferromagnetic endpoint q0:',format(q0,'.15f'))
print('Minimum sign-reversal rate r0:',format(r0,'.15f'))
print('At c=-1: G1(r=1)=',format(float(sp.N(sp.Rational(5,3)-8*sp.sqrt(3)/9)),'.15f'))
print('At c=-1: G1(r=2)=',format(float(sp.N(2-3*sp.sqrt(2)/2)),'.15f'))
