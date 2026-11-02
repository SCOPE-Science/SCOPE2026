#!/usr/bin/env python3
"""Standalone exact verification of phase-resolved two-example momentum covariances.
Requires Python 3 and SymPy. Finite checks supplement, not replace, the proof.
"""
import sympy as sp

b,t=sp.symbols('b t', real=True)
c=1+b-t
A=sp.Matrix([[c,-b],[1,0]])
g=sp.Matrix([t,0])
s11,s12,s22=sp.symbols('s11 s12 s22')
S=sp.Matrix([[s11,s12],[s12,s22]])

def solve_cov(M,noise):
    F=S-M*S*M.T-noise*noise.T
    unknowns=[s11,s12,s22]
    # SymPy exact rational linear solve: all polynomial identities remain exact
    eq=[F[0,0],F[0,1],F[1,1]]
    sol=sp.solve(eq,unknowns,dict=True, simplify=False)
    assert len(sol)==1
    return S.subs(sol[0])

S_i=solve_cov(A,g)
S_e=solve_cov(A*A,(A*g-g))
S_o=A*S_e*A.T+g*g.T
D=(1-b)*(2*(1+b)-t)
G=(t-1-b)**2+(1-b)**2
F_i=t*(1+b)/D
F_e=t*t/D-t*t*(1+b-t)/((1+b)*G)
F_o=t*t/D+t*t*(1+b-t)/((1+b)*G)
for obtained,target in [(S_i[0,0],F_i),(S_e[0,0],F_e),(S_o[0,0],F_o),
                        (S_e[1,1],F_o),((S_e[0,0]+S_o[0,0])/2,t*t/D),
                        (F_i-F_e,t*(1+b-t)*(1/D+t/((1+b)*G))),
                        (F_i-F_o,2*t*(1+b-t)*((t-1-b)**2-b*(1-b*b))/(D*(1+b)*G))]:
    assert sp.cancel(obtained-target)==0, str((obtained,target))
assert sp.simplify(F_i.subs({b:sp.Rational(1,2),t:1})-sp.Rational(3,2))==0
assert sp.simplify(F_e.subs({b:sp.Rational(1,2),t:1})-sp.Rational(1,3))==0
assert sp.simplify(F_o.subs({b:sp.Rational(1,2),t:1})-sp.Rational(5,3))==0
checks=7+3
for bb in [sp.Rational(1,8),sp.Rational(1,3),sp.Rational(1,2),sp.Rational(4,5)]:
    root=sp.sqrt(bb*(1-bb*bb))
    thresholds=[1+bb-root,1+bb,1+bb+root]
    assert all(0 < float(z) < 2*(1+float(bb)) for z in thresholds)
    for tt in [sp.Rational(1,8),sp.Rational(1,2),sp.Rational(7,8),
               1+bb,sp.Rational(5,4),sp.Rational(7,4),sp.Rational(9,4)]:
        if not 0 < tt < 2*(1+bb): continue
        val={b:bb,t:tt}
        assert sp.simplify(F_i.subs(val)) > 0
        assert sp.simplify(F_e.subs(val)) >= 0
        assert sp.simplify(F_o.subs(val)) >= 0
        assert sp.simplify(((F_e+F_o)/2-t*t/D).subs(val))==0
        checks+=4
print(f'VERIFY_OK symbolic={7} rational_and_boundary={checks-7}; exact stationary covariance identities and two-phase reversals')
