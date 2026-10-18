"""Reproduce sharp local tuning of the two-state Acc-Sinkhorn map.

Dependency: numpy. Runs deterministic exact-rational checks, spectral checks,
finite-difference Sinkhorn Jacobians, and nearby nonlinear trajectories.
The analytic theorem, not the finite tests, proves the infinite statements.
"""
import math
from fractions import Fraction as F
import numpy as np

checks = 0

def check(cond, detail=''):
    global checks
    checks += 1
    if not bool(cond):
        raise AssertionError(detail)

def matrix(alpha, lam):
    d = 1 + alpha
    return np.array([[lam/d,1/d],
        [lam*(alpha*alpha-2+2*lam)/(d*d),
         (alpha*alpha+alpha-1+2*lam)/(d*d)]], dtype=float)

def rho(alpha,lam):
    return float(max(abs(np.linalg.eigvals(matrix(alpha,lam)))))

def optimum(L):
    t=math.sqrt(L)
    if L == 0:
        alpha=(math.sqrt(5)-1)/2
    elif L<=0.25:
        alpha=(-1+t+math.sqrt(t*t+2*t+5))/2
    else:
        def f(alpha):
            return (alpha+3)*L + alpha*alpha+alpha-1 -2*t*(1+alpha)
        lo, hi=0.,1.
        for j in range(90):
            mid=(lo+hi)/2
            if f(mid)>0: hi=mid
            else: lo=mid
        alpha=(lo+hi)/2
    return alpha, (t/(1+alpha) if L>0 else 0)

# Exact algebraic trace and determinant in rational arithmetic.
for ia in range(1,18):
    a=F(ia,17)
    for il in range(0,17):
        lam=F(il,17)
        d=1+a
        A=lam/d; B=1/d
        C=lam*(a*a-2+2*lam)/(d*d)
        D=(a*a+a-1+2*lam)/(d*d)
        tr=A+D; det=A*D-B*C
        check(tr==((a+3)*lam+a*a+a-1)/(d*d),'trace')
        check(det==lam/(d*d),'det')
        check(1-tr+det==(a+2)*(1-lam)/(d*d),'Schur plus')
        check(1+tr+det==(2*a*a+3*a+(a+4)*lam)/(d*d),'Schur minus')

# Exact minimax phase frontier, endpoint dominance and strict relation with SK.
for L in [0.0,1e-5,.0025,.01,.04,.0625,.16,.2499,.25,.2501,.36,.49,.64,.81,.96,.995]:
    alpha, R=optimum(L)
    check(0 < alpha < math.sqrt(2),'feasible alpha')
    check(abs(max(rho(alpha,0),rho(alpha,L))-R)<2e-7,'endpoint at optimum')
    for z in range(201):
        cand=0.001+z*(math.sqrt(2)-0.002)/200
        worst=max(rho(cand,0),rho(cand,L))
        check(worst+1e-8>=R,('minimax',L,cand,worst,R))
        for lam in np.linspace(0,L,7):
            check(rho(cand,lam)<=worst+1e-10,'endpoint dominance')
    if 0<L<.25: check(R>L,'small coupling can be slower than SK')
    if .25<L<1: check(R<L,'large coupling accelerates SK')
    if L == .25: check(abs(R-L)<1e-12,'phase boundary')

# Finite difference of the entire normalized Sinkhorn map.
def normalized_sinkhorn(x,P):
    m,n=P.shape
    a=P.sum(axis=1); b=P.sum(axis=0)
    ex=np.exp(x)
    u=a/(P@ex)
    col=(u@P)*ex
    v=x+np.log(b/col)
    return v-v.mean()

rng=np.random.default_rng(20261016)
for case in range(9):
    if case <4:
        t=[0.05,0.4,0.77,0.95][case]
        signs=np.array([1.,-1.])
        q=np.array([1.,1.,-1.,-1.])
        P=(1+t*signs[:,None]*q[None,:])/8
    else:
        P=rng.uniform(.5,2,size=(3,6)); P=P/P.sum()
    a=P.sum(axis=1);b=P.sum(axis=0)
    J=(P.T/a)@P/b[:,None]
    # J_ij = b_i^{-1} sum_k P_ki a_k^{-1} P_kj.
    check(np.allclose(J@np.ones(len(b)),np.ones(len(b)),atol=2e-13),'stochastic J')
    n=len(b); projector=np.eye(n)-np.ones((n,n))/n
    for j in range(12):
        v=rng.standard_normal(n);v-=v.mean()
        h=1e-6
        finite=(normalized_sinkhorn(h*v,P)-normalized_sinkhorn(-h*v,P))/(2*h)
        predicted=projector@J@v
        check(np.max(np.abs(finite-predicted))<2e-8,'Sinkhorn derivative')
    sym=(np.sqrt(b)[:,None]*J)/np.sqrt(b)[None,:]
    eig=np.linalg.eigvalsh(sym)
    check(np.min(eig)>-1e-13,'PSD Hessian')
    check(abs(eig[-1]-1)<1e-12,'unit gauge eigenvalue')
    check(sum(abs(eig)<1e-10)>=2,'zero eigenmodes')
    L=float(eig[-2]); alpha,R=optimum(L)
    check(R<1,'local contraction')
    if case <4: check(abs(L-t*t)<1e-12,'explicit family spectrum')
    # Actual full nonlinear update near fixed point, checked against its derivative.
    for _ in range(10):
        v=rng.standard_normal(n);v-=v.mean()
        w=rng.standard_normal(n);w-=w.mean()
        eps=1e-6; d=1+alpha
        x1=(eps*w+normalized_sinkhorn(eps*v,P))/d
        w1=(eps*w+(alpha*alpha-2)*x1+2*normalized_sinkhorn(x1,P))/d
        xlin=(w+J@v)/d; xlin-=xlin.mean()
        wlin=(w+(alpha*alpha-2)*xlin+2*J@xlin)/d;wlin-=wlin.mean()
        check(max(np.max(abs(x1/eps-xlin)),np.max(abs(w1/eps-wlin)))<2e-5,'full two-state derivative')

print('PASS',checks,'deterministic checks; source update, exact algebra, minimax, geometry, Jacobians, local maps')
