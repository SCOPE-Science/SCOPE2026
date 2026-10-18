"""Standalone algebraic replay for an epidemic--opinion spectral threshold.

Run: python check.py (requires SymPy and NumPy).  All exact identities
are checked symbolically; small finite matrices are illustrative only.
"""
import sympy as sp
import numpy as np

s, beta, kappa, delta, ell = sp.symbols('s beta kappa delta ell', real=True)
z = sp.Symbol('z')
g = -delta + (beta-kappa)*s - beta*s**2
alpha = beta*s*(1-2*s)
theta = kappa*s
assert sp.simplify(theta-alpha+s*sp.diff(g,s)) == 0
J = sp.Matrix([[alpha, -theta],[1, -1-ell]])
p = sp.factor(J.charpoly(z).as_expr())
assert sp.simplify(p - (z**2+(1+ell-alpha)*z+theta-alpha*(1+ell))) == 0

G = sp.factor(g.subs({delta:sp.Rational(1,3), kappa:2, beta:sp.Rational(9,2)}))
assert sp.simplify(G + sp.Rational(1,6)*(3*s-1)*(9*s-2)) == 0  # exact model equilibria
ah = alpha.subs({beta:sp.Rational(9,2), s:sp.Rational(1,3)})
th = theta.subs({kappa:2, s:sp.Rational(1,3)})
assert ah == sp.Rational(1,2) and th == sp.Rational(2,3)
assert sp.simplify(p.subs({beta:sp.Rational(9,2),kappa:2,s:sp.Rational(1,3),ell:sp.Rational(1,3)}) - z*(z+sp.Rational(5,6))) == 0
assert sp.simplify(p.subs({beta:sp.Rational(9,2),kappa:2,s:sp.Rational(1,3),ell:0}) - (z**2+z/2+sp.Rational(1,6))) == 0

w,t,u,v = sp.symbols('w t u v',real=True)
tsym = 1+2*w
u0=sp.Rational(1,2)-sp.Rational(2,9)/t
v2=sp.factor((sp.Rational(5,9)*u0-u0**2-sp.Rational(2,27)))
assert sp.factor(v2 - (4-3*t)*(5*t-4)/(324*t*t))==0
assert sp.factor(v2.subs(t,tsym) - (1-6*w)*(1+10*w)/(324*(1+2*w)**2))==0
assert sp.limit(v2.subs(t,tsym)/(sp.Rational(1,6)-w),w,sp.Rational(1,6),dir='-') == sp.Rational(1,36)

X1=u+v; X2=u-v
E1=u+v/t; E2=u-v/t
# Exact positive-endemic equilibrium residuals after eliminating v^2.
res1=-(sp.Rational(1,3)+2*E1)*X1+sp.Rational(9,2)*(1-X1)*X1**2
res2=-(sp.Rational(1,3)+2*E2)*X2+sp.Rational(9,2)*(1-X2)*X2**2
for r in (res1,res2):
    R=sp.factor(r.subs(u,u0))
    rem=sp.rem(sp.together(R).as_numer_denom()[0],sp.Poly(v*v-v2,v),v)
    assert sp.simplify(rem)==0,rem

# Whole 4-by-4 Jacobian in the negative-opinion chamber.
L=sp.Matrix([[w,-w],[-w,w]])
XX=sp.diag(X1,X2)
F=sp.diag(sp.Rational(9,2)*X1*(1-2*X1),sp.Rational(9,2)*X2*(1-2*X2))
JJ=F.row_join(-2*XX).col_join(sp.eye(2).row_join(-sp.eye(2)-L))
D=sp.factor(JJ.det())
D0=sp.factor((D+81*t*(u*u-v*v)*v*v).subs(w,(t-1)/2).subs(u,u0))
num=sp.together(D0).as_numer_denom()[0]
assert sp.simplify(sp.rem(num,sp.Poly(v*v-v2,v),v))==0

# Particular unequal equilibrium and exact negative full determinant.
ww=sp.Rational(1,12)
tt=1+2*ww
uu=u0.subs(t,tt)
vv=sp.sqrt(v2.subs(t,tt))
x1=uu+vv;x2=uu-vv
e1=uu+vv/tt;e2=uu-vv/tt
assert all(0<float(a)<sp.Rational(1,2) for a in (x1,x2,e1,e2))
assert abs(float(res1.subs({u:uu,v:vv,t:tt})))<1e-12
assert abs(float(res2.subs({u:uu,v:vv,t:tt})))<1e-12
assert sp.simplify(D.subs({u:uu,v:vv,w:ww})+81*tt*x1*x2*vv*vv)==0
assert float(D.subs({u:uu,v:vv,w:ww}))<0

# Spectral predictions on sample undirected graphs and edge weights.
for n in (2,3,4,6):
    rng=np.random.default_rng(n+2608)
    weights=rng.random((n,n)); weights=(weights+weights.T)/2
    np.fill_diagonal(weights,0.0)
    LL=np.diag(weights.sum(axis=1))-weights
    evals=np.linalg.eigvalsh(LL)
    bigJ=np.block([[float(ah)*np.eye(n),-float(th)*np.eye(n)],
                   [np.eye(n),-np.eye(n)-LL]])
    spectral=np.linalg.eigvals(bigJ)
    expected=[]
    for ev in evals:
        expected.extend(np.linalg.eigvals(np.array([[float(ah),-float(th)], [1.0,-1.0-ev]])))
    assert np.max(np.abs(np.sort_complex(spectral)-np.sort_complex(expected)))<1e-9
    assert (np.max(np.real(spectral))>1e-9)==(np.max(evals)>sp.Rational(1,3))
print('PASS: model equilibrium factorization, general modal polynomial, exact nonlinear unequal branch, four-dimensional determinant, Turing threshold and sample graph spectra.')
