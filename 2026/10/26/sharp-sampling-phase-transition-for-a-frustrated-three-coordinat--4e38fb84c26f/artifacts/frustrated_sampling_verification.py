"""Reproducible checks for optimal one-step randomized-coordinate sampling.

The proof is analytic; these checks verify the symbolic transition and
independently compare the predicted optimum with direct numerical optimization.
Requires sympy, numpy and scipy. Run: python frustrated_sampling_verification.py
"""
import sympy as s
import numpy as np
from scipy.optimize import minimize, minimize_scalar

r, c, u, q = s.symbols('r c u q', real=True)
a, b = 1-r, 1+r
v=1-2*u
F=s.expand((b*u-q)*(v-q)-2*c*c*u*v)
u_boundary=(r-c*c)/(r*(3-r)-2*c*c)
q_boundary=s.factor(a*u_boundary)
u_smooth=(1+c)/(3+r+4*c)
q_smooth=(1+r-2*c*c)/(3+r+4*c)
assert s.simplify(F.subs({u:u_boundary,q:a*u_boundary}))==0
assert s.simplify(F.subs({u:u_smooth,q:q_smooth}))==0
assert s.simplify(s.diff(F,u).subs({u:u_smooth,q:q_smooth}))==0
# The smooth-block maximizer changes the active mode exactly at the root
# of 2*c*c + (1-r)*c - 2*r.
transition=2*c*c+(1-r)*c-2*r
assert s.simplify((q_smooth-a*u_smooth)*(3+r+4*c)+transition)==0
print('SYMBOLIC: intersection, smooth optimum and transition identities hold')

for cr, cc in [(s.Rational(1,2),s.Rational(1,3)),
               (s.Rational(1,2),s.Rational(2,3)),
               (s.Rational(1,5),s.Rational(1,4))]:
    th=(- (1-cr)+s.sqrt((1-cr)**2+16*cr))/4
    uu=s.factor((u_boundary if cc<=th else u_smooth).subs({r:cr,c:cc}))
    qq=s.factor((q_boundary if cc<=th else q_smooth).subs({r:cr,c:cc}))
    C=s.Matrix([[1,cr,cc],[cr,1,cc],[cc,cc,1]])
    P=s.diag(uu,uu,1-2*uu)
    # Similar to C^(1/2) P C^(1/2) by nonsingular similarity.
    cp=P*C
    ev=cp.eigenvals()
    mineig=min(float(s.N(z,30)) for z in ev)
    assert abs(float(qq)-mineig)<1e-12
    print('RATIONAL CHECK',cr,cc,'p=',uu,uu,1-2*uu,'q=',qq,'spectrum=',ev)

rng=np.random.default_rng(78239)
max_abs=0.0
for k in range(90):
    rr=float(rng.uniform(0.05,0.95))
    aa=float(rng.uniform(0.005,0.997*np.sqrt(rr)))
    C=np.array([[1,rr,aa],[rr,1,aa],[aa,aa,1]],float)
    threshold=(- (1-rr)+np.sqrt((1-rr)**2+16*rr))/4
    ub=(rr-aa*aa)/(rr*(3-rr)-2*aa*aa)
    us=(1+aa)/(3+rr+4*aa)
    expected=(1-rr)*ub if aa<=threshold else (1+rr-2*aa*aa)/(3+rr+4*aa)
    uopt=ub if aa<=threshold else us
    eig_pred=np.linalg.eigvalsh(C*np.sqrt(np.outer([uopt,uopt,1-2*uopt],[uopt,uopt,1-2*uopt])))[0]
    assert abs(eig_pred-expected)<2e-12
    def value(p):
        if min(p)<0: return -1.0
        return np.linalg.eigvalsh(C*np.sqrt(np.outer(p,p)))[0]
    starts=[np.array([1/3,1/3,1/3]),np.array([uopt,uopt,1-2*uopt])]
    for _ in range(3):
        starts.append(rng.dirichlet([2,2,2]))
    candidates=[]
    for start in starts:
        opt=minimize(lambda t:-value(t),start,method='SLSQP',constraints=[{'type':'eq','fun':lambda t:sum(t)-1}],bounds=[(1e-7,1)]*3, options={'maxiter':120,'ftol':1e-12})
        candidates.append(value(opt.x))
    max_abs=max(max_abs,abs(max(candidates)-expected))
    assert max(candidates) <= expected+3e-8
    assert max(candidates) >= expected-3e-7
print('NUMERICAL: 90 two-parameter instances × five unrestricted simplex optimizations passed; max discrepancy',max_abs)
print('ALL CHECKS PASSED')
