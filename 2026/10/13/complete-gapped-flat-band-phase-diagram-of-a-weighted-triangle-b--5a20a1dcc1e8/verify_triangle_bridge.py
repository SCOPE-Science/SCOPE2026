"""Exact algebra checks for the weighted triangle-bridge chain flat-band classification.

Uses SymPy for Laurent-polynomial identities over rational functions.
All inequalities and the spectral-gap assertion are justified analytically in the proof.
"""
import sympy as sp

z, p, q, r, s = sp.symbols('z p q r s', nonzero=True)
QA, QB, QC, E = sp.symbols('QA QB QC E', real=True)
H = sp.Matrix([
    [QA, p+s*z, r],
    [p+s/z, QB, q],
    [r, q, QC],
])
xA, xB, xC = QA-E, QB-E, QC-E
L = sp.factor((H - E*sp.eye(3)).det())
C = xA*xB*xC-q*q*xA-r*r*xB-(p*p+s*s)*xC+2*p*q*r
K = s*(q*r-p*xC)
assert sp.cancel(L-(C+K*(z+1/z))) == 0

g=q*r/p
alpha=QA-QC+g-p*r/q
beta=QB-QC+g-p*q/r
lam=QC-g
assert sp.cancel(L.subs(E,lam)-g*(alpha*beta-s*s)) == 0
QB_tuned=sp.solve(sp.Eq(beta,s*s/alpha),QB)[0]
H_tuned=H.subs(QB,QB_tuned)
v=sp.Matrix([-s*z,alpha,(r*s*z-q*alpha)/g])
res=(H_tuned-lam*sp.eye(3))*v
assert all(sp.cancel(x)==0 for x in res)
# The principal two-by-two minor on A,C is g*alpha: always nonzero on tuning.
assert sp.cancel(((QA-lam)*g-r*r)-g*alpha) == 0
# Distinguished unweighted instances on both branches, for two nontrivial quasimomenta.
for a in (sp.Integer(1),sp.Integer(-1)):
    H0=H.subs({p:1,q:1,r:1,s:1,QA:a,QB:a,QC:0})
    for zz in (sp.Integer(1),sp.Integer(-1)):
        M0=H0.subs(z,zz)
        assert (M0+sp.eye(3)).det()==0
        assert (M0+sp.eye(3)).rank()==2
        oth=[v2.evalf() for v2 in M0.eigenvals() if v2 != -1]
        assert len(oth)==2
        if a>0:
            assert all(float(v2)>-1 for v2 in oth)
        else:
            assert sum(float(v2)<-1 for v2 in oth)==1
            assert sum(float(v2)>-1 for v2 in oth)==1
print('VERIFY_OK exact_Laurent=1 flat_locus=1 CLS_kernel=1 simple_isolation=1 branch_samples=4')
