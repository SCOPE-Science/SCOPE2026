import math
import numpy as np
import sympy as s
from scipy.special import roots_legendre
from itertools import product

def hyperbolic_simplex_numeric(d, t, quadrature=12):
    beta=math.acos(1/d); c=math.cos(beta-t)
    R2=d*(d*c-1)/(1+c)
    nodes, weights=roots_legendre(quadrature)
    nodes=(nodes+1)/2; weights=weights/2
    integral=0.
    for inds in product(range(quadrature),repeat=d):
        tt=nodes[list(inds)]; ww=np.prod(weights[list(inds)])
        lambdas=np.zeros(d+1); remain=1.; jac=1.
        for i,z in enumerate(tt):
            lambdas[i]=remain*z; jac*=remain; remain*=1-z
        lambdas[-1]=remain
        normsq=((d+1)*sum(lambdas*lambdas)-1)/d
        integral+=ww*jac*(1-R2*normsq)**(-(d+1)/2)
    return (d+1)**((d+1)/2)/(math.factorial(d)*d**(d/2)) * (R2**(d/2))*math.factorial(d)*integral

d=s.symbols('d',integer=True,positive=True)
Bdelta=d**2*(d**2-2)/(2*(d+1)*(d+2))
assert s.simplify((Bdelta*s.sqrt(d*d-1)/d-d/(4*s.sqrt(d*d-1))).subs(d,2)) == 0
assert s.simplify((Bdelta*s.sqrt(d*d-1)/d-d/(4*s.sqrt(d*d-1))).subs(d,4)-13*s.sqrt(15)/15)==0
for t in [0.04,0.02,0.01,0.005]:
    v=hyperbolic_simplex_numeric(4,t)
    model=10*math.sqrt(5)*t*t*(1+(13*math.sqrt(15)/15)*t)
    print('d=4 t=',t,'v=',v,'model=',model,'relative_residual_per_t_squared=', (v/model-1)/t**2)
for t in [0.04,0.02,0.01]:
    v=hyperbolic_simplex_numeric(2,t)
    assert abs(v-3*t)<1e-11
print('Exact d=2 area cross-check passed')
