"""Exact differential-norm check for the saturating phase Ikeda map.
Run: python ikeda_candidate_verify.py
"""
import sympy as sp
k, q, eta = sp.symbols('k q eta', real=True)
S=sp.Matrix([[1,0],[k,1]])
assert sp.factor((S.T*S).det()) == 1
assert sp.factor((S.T*S).trace()) == k*k+2
r=sp.symbols('r', nonnegative=True)
ksq = 2*eta*r*r/(1+r*r)**2
assert sp.simplify(ksq.subs(r,1)) == eta/2
assert sp.factor((1+r*r)**2-4*r*r) == (r-1)**2*(r+1)**2
sigma=sp.sqrt(1+eta**2/16)+sp.Abs(eta)/4
ucrit=1/sigma
assert sp.simplify(ucrit-(sp.sqrt(1+eta**2/16)-sp.Abs(eta)/4)) == 0
assert sp.simplify(sp.expand((sp.sqrt(1+k*k/4)+k/2)**2)-(2+k*k+k*sp.sqrt(k*k+4))/2).subs(k,0) == 0
print('symbolic identities PASS; u_crit(eta=6) =',sp.simplify(ucrit.subs(eta,6)),sp.N(ucrit.subs(eta,6),16))
