"""Reproduce the algebraic spectral criterion and independent resolvent checks.

Dependencies: Python 3, sympy, numpy. Run: python verify_reentrant_mrna.py
All PSDs refer to the stationary Gaussian approximation, not finite-volume jump-process spectra.
"""
import numpy as np
import sympy as sp

q, x, w = sp.symbols('q x w', real=True)
K = sp.Matrix([[-10, -q], [1, -1]])
D = sp.diag(20, 2)
H = (K - sp.I * w * sp.eye(2)).inv()
S = sp.simplify(H * D * H.conjugate().T)
F = x*x + (101-2*q)*x + (10+q)**2
Smm = 20*(x+1)+2*q*q
Spp = 2*(x+110)
for jj, numerator in [(0, Smm), (1, Spp)]:
    actual = sp.factor(S[jj,jj])
    expected = (numerator/F).subs(x, w*w)
    assert sp.simplify(actual - expected) == 0, (jj, actual)

P = 2*q**3-91*q*q+220*q-10
u = 1+q*q/sp.Integer(10)
B = 101-2*q
c = 10+q
assert sp.simplify(10*(c*c-u*B)-P) == 0
# Denominator derivative identity exactly:
assert sp.expand((sp.diff(Smm,x)*F-Smm*sp.diff(F,x)) - 20*(P/10-2*u*x-x*x)) == 0
assert sp.expand((sp.diff(Spp,x)*F-Spp*sp.diff(F,x)) - 2*(q*q+240*q-11010-220*x-x*x)) == 0
assert (P.subs(q,0),P.subs(q,1),P.subs(q,5)) == (-10,121,-935)
assert sp.diff(P,q).subs(q,1)>0 and sp.diff(P,q).subs(q,5)<0
q_turns = sp.solve(sp.diff(P,q),q)
assert 1<float(q_turns[0])<5 and float(q_turns[1])>81/4
roots = sorted(float(sp.re(r)) for r in sp.nroots(P))
assert 0<roots[0]<1<roots[1]<5<81/4<roots[2]
for qq in [0,0.01,0.05,1,2.5,3,5,19,20.2]:
    Knum = np.array([[-10.,-qq],[1.,-1.]])
    Dnum = np.diag([20.,2.])
    xx = np.array([0.,0.001,0.02,0.1,0.6,2.5,10.,500.])
    for xx0 in xx:
        ww=float(np.sqrt(xx0))
        h=np.linalg.inv(Knum-1j*ww*np.eye(2))
        spect=h@Dnum@h.conj().T
        ff=xx0**2+(101-2*qq)*xx0+(10+qq)**2
        assert np.allclose([spect[0,0].real,spect[1,1].real],
            [(20*(xx0+1)+2*qq**2)/ff,(220+2*xx0)/ff],rtol=1e-11,atol=1e-11)
    val=float(P.subs(q,qq))
    xstar=(-float(u.subs(q,qq))+np.sqrt(float(u.subs(q,qq))**2+val/10)) if val>0 else 0.
    grid=np.linspace(0,25,5000)
    sg=(20*(grid+1)+2*qq**2)/(grid**2+(101-2*qq)*grid+(10+qq)**2)
    assert sg.max() <= (20*(xstar+1)+2*qq**2)/(xstar**2+(101-2*qq)*xstar+(10+qq)**2)+1e-12
    # Pp strictly decreasing for all 0<=q<=81/4.
    assert float((q*q+240*q-11010).subs(q,qq)) < 0
print('PASS: symbolic PSD identities, global derivative criteria, cubic roots and 72 independent numerical resolvent checks')
print('Thresholds:',roots[:2],'; real-pole boundary:',81/4)
