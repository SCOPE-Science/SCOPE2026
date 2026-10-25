#!/usr/bin/env python3
"""Independent geometric and numerical checks of the exact cube-shadow radius tail.
Run: python3 VERIFY.py. Requires numpy and scipy.
Analytic arguments in RESULT.md, not numerical tests, establish the theorem.
"""
import itertools
import math
import numpy as np
from scipy.integrate import quad
from scipy.stats import qmc

V=np.array([[1.,1.,1.],[1.,1.,-1.],[1.,-1.,1.],[-1.,1.,1.]])
ALL=np.array(list(itertools.product([-1.,1.],repeat=3)))


def pair_probability(t):
    a=t/math.sqrt(3.)
    c=1/3
    s=2*math.sqrt(2)/3
    def integrand(y):
        d=s*math.sqrt(1-y*y)
        return (math.asin((a-c*y)/d)-math.asin((-a-c*y)/d))/(2*math.pi)
    return quad(integrand,-a,a,epsabs=1e-13,epsrel=1e-13)[0]


def exact_tail(t):
    assert 0<t<=1/math.sqrt(3)+1e-13
    return 4*t/math.sqrt(3)-6*pair_probability(t)


def projected_circumradius(u):
    # All eight projected cube vertices, not the four-belt formula.
    projected=ALL - np.outer(ALL@u,u)
    return np.max(np.linalg.norm(projected,axis=1))


def check():
    assert np.allclose(V.T@V,4*np.eye(3))
    for ix in itertools.combinations(range(4),3):
        mat=V[list(ix)]
        inv=np.linalg.inv(mat)
        corner_norms=[np.linalg.norm(inv@np.array(s,dtype=float))
                      for s in itertools.product([-1.,1.],repeat=3)]
        assert abs(max(corner_norms)-math.sqrt(3))<1e-12
    print('EXACT_TRIPLE_BELT_THRESHOLD_AND_TIGHT_FRAME_OK')

    rng=np.random.default_rng(211703)
    for u in rng.normal(size=(2048,3)):
        u=u/np.linalg.norm(u)
        r=projected_circumradius(u)
        m=np.min(np.abs(V@u))
        assert abs(r*r-(3-m*m))<2e-13
    print('DIRECT_EIGHT_VERTEX_PROJECTED_CIRCUMRADIUS_IDENTITY_OK')

    tol=1/math.sqrt(3)
    # Extra geometric independence: independently sample a uniformly
    # oriented plane, then compare the eight projected vertices with the
    # exact inclusion-exclusion probabilities.
    sobol=qmc.Sobol(2,scramble=True,seed=211703)
    x=sobol.random_base2(20)
    z=2*x[:,0]-1
    phi=2*math.pi*x[:,1]
    U=np.column_stack((np.sqrt(1-z*z)*np.cos(phi),
                       np.sqrt(1-z*z)*np.sin(phi),z))
    m=np.min(np.abs(U@V.T),axis=1)
    for t in [0.08,0.15,0.30,0.40,0.55,tol]:
        empirical=np.mean(m<t)
        theory=exact_tail(t)
        assert abs(empirical-theory)<0.00014, (t,empirical,theory)
        print('BELT_TAIL_DISTRIBUTION_OK',format(t,'.8f'),
              format(theory,'.11f'),format(empirical,'.11f'))

    c2=1/(math.pi*math.sqrt(2))
    c4=1/(8*math.pi*math.sqrt(2))
    for t in [0.1,0.05,0.025]:
        j=pair_probability(t)
        inferred=(j-c2*t*t)/(t**4)
        assert abs(inferred-c4)<0.00012
    print('EXACT_PAIR_OVERLAP_TAYLOR_COEFFICIENTS_OK')

    # Differentiate or expand analytically in RESULT.md; here we verify the
    # epsilon-parametrization and endpoint normalization numerically.
    for eps in [1e-4,4e-5,1e-5]:
        t=math.sqrt(2*math.sqrt(3)*eps-eps*eps)
        expansion=4*math.sqrt(2/math.sqrt(3))*math.sqrt(eps)-6*math.sqrt(6)/math.pi*eps
        assert abs(exact_tail(t)-expansion)<10*eps**1.5
    assert math.sqrt(2)-1e-14<=projected_circumradius(np.array([1.,0.,0.]))<=math.sqrt(2)+1e-14
    assert abs(projected_circumradius(np.array([1.,-1.,0.])/math.sqrt(2))-math.sqrt(3))<1e-13
    print('ENDPOINT_SUPPORT_AND_SQUARE_ROOT_TAIL_NORMALIZATION_OK')
    print('ALL_CUBE_SHADOW_CIRCUMRADIUS_CHECKS_OK')

if __name__=='__main__':
    check()
