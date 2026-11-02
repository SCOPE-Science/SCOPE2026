"""Reproduce numerical checks for priced alternating cycles.

Run with Python 3, NumPy, and SciPy. Computational tests corroborate, not replace, the analytical proof.
"""
import numpy as np
from scipy.optimize import minimize, minimize_scalar


def laplacian(m, weights):
    n = 2*m
    L = np.zeros((n,n))
    for i,w in enumerate(weights):
        j = (i+1)%n
        L[i,i] += w; L[j,j] += w
        L[i,j] -= w; L[j,i] -= w
    return L


def gap(m,weights):
    return float(np.linalg.eigvalsh(laplacian(m,weights))[1])


def optimum(m,p,q,B=1.0):
    g=np.cos(np.pi/m)
    h=np.sin(np.pi/m)**2
    s=np.sqrt(p*q)
    den = m*(2*p*q*g+(p+q)*s)
    a=B*(q*g+s)/den
    b=B*(p*g+s)/den
    t=2*B*h/(m*(p+q+2*s*g))
    return a,b,t


rng=np.random.default_rng(20261026)
count=0
random_checks=0
optim_checks=0
for m in range(2,15):
    for p,q in [(1,1),(1,4),(4,1),(0.125,11),(13,0.2),(3,7)]:
        a,b,t=optimum(m,p,q)
        weights=np.tile([a,b],m)
        assert abs(m*(p*a+q*b)-1)<5e-12
        assert abs(gap(m,weights)-t)<1e-10,(m,p,q,a,b,t,gap(m,weights))
        count+=1
        for k in range(25):
            v=rng.dirichlet(np.ones(2*m))
            cost=np.tile([p,q],m)
            v=v/(cost@v)
            assert gap(m,v)<=t+2e-10,(m,p,q,k,gap(m,v),t)
            random_checks+=1
        if m<=7:
            init=np.tile([1.0/(m*(p+q)),1.0/(m*(p+q))],m)
            cons={'type':'eq','fun':lambda x,co=np.tile([p,q],m):co@x-1}
            res=minimize(lambda x:-gap(m,x),init,bounds=[(0,None)]*(2*m),constraints=cons,
                         method='SLSQP',options={'maxiter':350,'ftol':2e-11})
            if res.success:
                assert -res.fun<=t+1e-7
                optim_checks+=1
scalar_checks=0
for m in range(2,20):
    for p,q in [(1,1),(1,4),(4,1),(0.125,11),(13,0.2),(3,7)]:
        a,b,t=optimum(m,p,q)
        def objective(z):
            A=1.0/(m*(p+q*z)); B=z*A
            return -gap(m,np.tile([A,B],m))
        res=minimize_scalar(objective,bounds=(1e-5,1000),method='bounded',options={'xatol':1e-10})
        assert abs(-res.fun-t)<1e-8,(m,p,q,-res.fun,t)
        scalar_checks+=1
print('PASS',{'analytic_spectrum_checks':count,'asymmetric_feasible_checks':random_checks,
              'constrained_optimizer_upper_checks':optim_checks,'independent_scalar_checks':scalar_checks})
