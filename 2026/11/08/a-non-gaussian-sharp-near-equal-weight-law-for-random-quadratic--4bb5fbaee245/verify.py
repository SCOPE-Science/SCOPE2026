"""Reproduce finite-dimensional checks for a quadratic random-node quadrature law.

Requires Python 3.10+, NumPy and SciPy. Run: python verify.py
The stochastic weak-convergence assertion is an analytic theorem, not a finite test.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import linprog


def limiting_norm(a, b):
    a, b = abs(float(a)), abs(float(b))
    if b <= a:
        return a / 2.0
    return (a * a + b * b) / (4.0 * b)


def numerical_norm(a, b):
    from scipy.optimize import minimize_scalar
    def objective(c):
        return quad(lambda x: abs(c + a*x + b*(x*x-1.0/3.0))/2.0,
                    -1.0, 1.0, epsabs=1.e-10, epsrel=1.e-10,
                    limit=500, points=[-0.5, 0.0, 0.5])[0]
    return minimize_scalar(objective, bounds=(-2.0, 2.0),
                           method='bounded', options={'xatol':1e-12}).fun


def empirical_optimum(x):
    m = len(x)
    g = np.vstack([np.ones(m), x, x*x-1.0/3.0])
    target = np.array([0.0, -np.sum(x), -np.sum(x*x-1.0/3.0)])
    c = np.r_[np.zeros(m),1.0]
    A = np.vstack([np.c_[np.eye(m),-np.ones(m)],
                   np.c_[-np.eye(m),-np.ones(m)]])
    solution = linprog(c,A_ub=A,b_ub=np.zeros(2*m),A_eq=np.c_[g,np.zeros(3)],
                       b_eq=target,bounds=[(None,None)]*m+[(0,None)],method='highs')
    assert solution.success, solution.message
    assert np.max(abs(g@solution.x[:m]-target))<1e-7
    return solution.x[-1]


def support_norm(u,v):
    return 2.0*(abs(v)+math.hypot(u,v))


def main():
    rng = np.random.default_rng(20261105)
    checks=0
    for a,b in [(0,1),(1,0),(1,1),(2,1),(0.3,1),(-0.4,1),(3,-2),(-3,-5)]:
        q=numerical_norm(a,b)
        assert abs(q-limiting_norm(a,b))<1e-8,(a,b,q,limiting_norm(a,b))
        checks+=1
    for i in range(80):
        a,b=rng.standard_normal(2)
        val=numerical_norm(a,b)
        assert abs(val-limiting_norm(a,b))<2e-8,(i,a,b,val)
        checks+=1
    for i in range(100):
        u,v=rng.standard_normal(2)
        z=math.hypot(u,v)
        if z:
            # A supporting point in the curved unit-norm branch, with signs.
            a=2*u/z
            b=math.copysign(2+2*abs(v)/z,v)
            assert abs(limiting_norm(a,b)-1)<1e-12
            assert abs(a*u+b*v-support_norm(u,v))<1e-12
            checks+=2
    for m in [10,30,60,100]:
        for i in range(6):
            x=rng.uniform(-1,1,size=m)
            opt=empirical_optimum(x)
            assert opt>=0
            # Explicit feasible least-norm correction always has max-norm >= optimum.
            mat=np.vstack([np.ones(m),x,x*x-1/3])
            delta=np.linalg.lstsq(mat, np.array([0.,-sum(x),-sum(x*x-1/3)]),rcond=None)[0]
            assert opt<=np.max(abs(delta))+2e-8
            checks+=2
    sigma1=math.sqrt(1/3);sigma2=math.sqrt(4/45)
    gaussian=rng.normal(0,sigma1,20000)
    gaussian2=rng.normal(0,sigma2,20000)
    w=2*(abs(gaussian2)+np.hypot(gaussian,gaussian2))
    assert min(w)>=0 and 0.0<np.mean(w<3.0)<1.0
    checks+=2
    print('PASS:',checks,'analytic-shape, support, LP, and law consistency checks')

if __name__=='__main__':main()
