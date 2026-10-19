#!/usr/bin/env python3
"""Exact symbolic and finite numerical checks for the signed-simplex mean-field theorem.

Requires Python 3 and SymPy. This program checks identities and examples;
it does not replace the Descartes-rule proof for arbitrary parameters.
"""
import sympy as sp

q, e, k = sp.symbols('q e k', positive=True)
b1, b2, mu, tri = sp.symbols('b1 b2 mu tri', positive=True)
g1, g2, g3, g4, g5 = sp.symbols('g1 g2 g3 g4 g5', nonnegative=True)
r = sp.symbols('r', real=True)
G = g2 + 2*g3
B = b1*(1-e)
C = b2*e
Lam = tri/mu*((1-e)**3*g1+e*(1-e)**2*G)
The = tri/mu*(g4*e**2*(1-e)+g5*e**3)
F = -mu + B*k + (-k*(B+C)+mu*Lam)*r-mu*(Lam+The)*r*r
h = B/(B+C)
g = -(B+C)**2 + B*C*Lam-B**2*The
assert sp.simplify(F.subs(r,h)-mu*g/(B+C)**2)==0
assert sp.simplify(sp.diff(F,k)-(B-(B+C)*r))==0

P = -(b1+b2*q)**2*(1+q)**3 + tri/mu*(b1*b2*g1*q + (b1*b2*G-b1*b1*g4)*q*q - b1*b1*g5*q**3)
assert sp.simplify((1+q)**5*g.subs(e,q/(1+q))-P)==0
coeff = [sp.factor(sp.Poly(P,q).coeff_monomial(q**j)) for j in range(6)]
print('Polynomial coefficients low to high:', coeff)
assert coeff[0] == -b1**2
assert coeff[5] == -b2**2
assert sp.simplify(coeff[4]+3*b2*b2+2*b1*b2)==0
assert sp.simplify(coeff[3]+b1*b1+6*b1*b2+3*b2*b2+tri/mu*b1*b1*g5)==0

f = e*(1-e)**3*(1+2*e)
p = sp.factor(8*f-1)
assert sp.simplify(p + (2*e-1)*(8*e**4-16*e**3+4*e**2+6*e-1)) == 0
assert sp.factor(sp.diff(f,e)) == -(e-1)**2*(10*e**2-1)
c = sp.sqrt(10)/10
critical = sp.simplify(1/f.subs(e,c))
assert sp.simplify(critical-(2500+3400*sp.sqrt(10))/2187)==0
assert 6 < critical < 8
print('Sharp triangle threshold for symmetric rates:', critical, sp.N(critical,16))
curvature = sp.simplify(sp.diff(f,e,2).subs(e,c))
opening = sp.simplify(2/critical*sp.sqrt(-2/curvature))
assert curvature < 0
print('Square-root opening coefficient:', sp.N(opening,16))
for epsilon in (sp.Rational(1,100),sp.Rational(1,1000)):
    fun = sp.Poly((critical + epsilon)*f-1,e)
    rr = sorted(float(sp.re(root)) for root in sp.nroots(fun,maxsteps=500) if abs(float(sp.im(root))) < 1e-9 and 0<float(sp.re(root))<1)
    assert len(rr)==2
    measured = (rr[1]-rr[0])/float(sp.sqrt(epsilon))
    assert abs(measured-float(opening)) < 0.015
    print('Opening ratio at excess',epsilon,':',measured)
assert sp.simplify(p.subs(e,sp.Rational(1,2)))==0
assert p.subs(e,sp.Rational(159,1000)) < 0
assert p.subs(e,sp.Rational(160,1000)) > 0
for evalue, expected_sign in [(sp.Rational(1,10),-1),(sp.Rational(3,10),1),(sp.Rational(1,2),0),(sp.Rational(7,10),-1)]:
    gv = p.subs(e,evalue)
    sign = sp.sign(gv)
    assert sign==expected_sign
    vals = []
    for kval in (24,48):
        ll = 8*(1-evalue)**2*(1+2*evalue)
        ff = -1+(1-evalue)*kval +(-kval+ll)*r-ll*r*r
        assert ff.subs(r,0)>0 and ff.subs(r,1)<0
        roots = sp.solve(ff,r)
        phys = [z for z in roots if 0<float(sp.N(z))<1]
        assert len(phys)==1
        vals.append(phys[0])
    order = sp.sign(sp.N(vals[1]-vals[0],50))
    assert order == -expected_sign
    print('eta:',evalue,'g:',gv,'prevalences:',[str(sp.N(z,16)) for z in vals])
print('PASS: exact identities, coefficient constraints, threshold, isolating interval, and four degree-order tests')
