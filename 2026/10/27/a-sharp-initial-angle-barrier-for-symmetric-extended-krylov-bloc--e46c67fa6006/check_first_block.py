"""Reproduce exact first-block extended Krylov angle and sharpness calculations.

Requires Python, NumPy and SymPy. All infinite assertions are proved in RESULT.md;
these checks exercise the explicit formulas and representative finite matrices.
"""
import numpy as np
import sympy as sp

r, e = sp.symbols('r e', positive=True)
weights = [e, 1-2*e, e]
lambda_ = [sp.Integer(1), r, r*r]
mu = sum((w*l for w,l in zip(weights,lambda_)), sp.Integer(0))
nu = sum((w/l for w,l in zip(weights,lambda_)), sp.Integer(0))
var = sp.factor(sum((w*(l-mu)**2 for w,l in zip(weights,lambda_)), sp.Integer(0)))
ivar = sp.factor(sum((w*(1/l-nu)**2 for w,l in zip(weights,lambda_)), sp.Integer(0)))
co = sp.factor(mu*nu-1)
t = (2*r + e*(r-1)**2)/(r*r+1-e*(r-1)**2)
assert sp.simplify(co**2 - t*t*var*ivar) == 0
assert sp.simplify(t.subs(e,0)-2*r/(r*r+1)) == 0
# Note the lower-bound strictness numerator factor is positive for e>0 and r>1.
assert sp.simplify(t-2*r/(r*r+1) - e*(r-1)**2*(r+1)**2/((r*r+1)*(r*r+1-e*(r-1)**2))) == 0

rng = np.random.default_rng(2061)
count = 0
for n in (3,5,9):
    for trial in range(150):
        eig = np.exp(rng.uniform(-2,2,size=n)); eig[0]=min(eig);eig[-1]=max(eig)
        b=rng.standard_normal(n);b/=np.linalg.norm(b)
        p=eig*b-(b@(eig*b))*b
        q=b/eig-(b@(b/eig))*b
        if np.linalg.norm(p)<1e-12 or np.linalg.norm(q)<1e-12:continue
        tt=-(p@q)/(np.linalg.norm(p)*np.linalg.norm(q))
        k=eig.max()/eig.min()
        assert (tt>2*np.sqrt(k)/(k+1)-1e-12), (n,trial,k,tt)
        if tt<1-1e-12:
            col=np.column_stack((p/np.linalg.norm(p),q/np.linalg.norm(q)))
            cond=np.linalg.cond(col)
            assert cond >= (np.sqrt(k)+1)/(np.sqrt(k)-1)-1e-9
            count+=1

for kr in (2,3,10):
    kapp=kr*kr
    for eps in (0.01,0.0001):
        b=np.sqrt([eps,1-2*eps,eps]);eig=np.array([1,kr,kapp],float)
        p=eig*b-(b@(eig*b))*b;q=b/eig-(b@(b/eig))*b
        tt=-(p@q)/(np.linalg.norm(p)*np.linalg.norm(q))
        exact=float(t.subs({r:kr,e:sp.Rational(str(eps))}))
        assert abs(tt-exact)<1e-11
        assert tt>2*kr/(kr*kr+1)
print('PASS symbolic identities and',count,'random full-rank Gram conditioning tests, six explicit sharpness checks')
