"""Replay exact tetrahedral partial-plank orientation comparison.

Requires Python 3 and SymPy; no input files, network, or approximation oracle.
"""
import sympy as sp

w, z, t = sp.symbols('w z t', real=True)
r3 = sp.sqrt(3)
V = sp.Matrix([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]])
assert V.T*V == 4*sp.eye(3)
assert list(sp.ones(1,4)*V) == [0,0,0]
# A sum of two of four uniform barycentric coordinates has Beta(2,2).
fz = sp.factor(6*((z+1)/2)*(1-(z+1)/2)/2)
assert sp.simplify(fz-sp.Rational(3,4)*(1-z*z))==0
assert sp.integrate(fz,(z,-1,1))==1
G=sp.integrate(fz,(z,-w/2,w/2))
# One of four barycentric coordinates has Beta(1,3).
ft=3*(1-t)**2
assert sp.integrate(ft,(t,0,1))==1
F=sp.integrate(ft,(t,0,r3*w/4))
assert sp.simplify(G-(3*w/sp.Integer(4)-w**3/16))==0
assert sp.simplify(F-(1-(1-r3*w/4)**3))==0
w1=8*r3-12
w2=(20*r3-12)/11
assert sp.simplify((F-G)-(4+3*r3)*w*(w-w1)*(w-w2)/64)==0
assert 0 < float(w1) < 2 < float(w2)
assert 0 < float(F.subs(w,1)-G.subs(w,1))
assert 0 > float(F.subs(w,sp.Rational(19,10))-G.subs(w,sp.Rational(19,10)))
assert sp.simplify(G.subs(w,2)-1)==0
print('PASS: coordinate frame, beta densities, exact integrals, factorization, roots, and boundary checks')
print('W* =',sp.N(w1,17))
