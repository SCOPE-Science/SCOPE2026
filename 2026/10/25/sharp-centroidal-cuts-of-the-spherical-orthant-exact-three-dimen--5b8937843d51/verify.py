"""Numerical cross-checks for the spherical-octant centroidal cut profile.

Numerical reproduction. Requires Python 3 with SciPy
and numpy. The proof is analytic; these are non-certifying sanity checks.
"""
import math
import numpy as np
from scipy.integrate import quad

PI = math.pi

def exact_positive_fraction(a: float) -> float:
    assert 0 <= a <= 1
    b = 1-a
    return 1-4/PI*math.atan(math.exp(-math.asinh(a)-math.asinh(b)))

def independent_surface_integral(a: float) -> float:
    b=1-a
    def integrand(theta):
        q=a*math.cos(theta)+b*math.sin(theta)
        return q/math.sqrt(1+q*q)
    return 2/PI*quad(integrand, 0, PI/2, epsabs=1e-13, epsrel=1e-13)[0]

def second_derivative_integral(a:float)->float:
    b=1-a
    def fun(theta):
        q=a*math.cos(theta)+b*math.sin(theta)
        diff=math.cos(theta)-math.sin(theta)
        return -6/PI*q*diff*diff/(1+q*q)**2.5
    return quad(fun,0,PI/2,epsabs=1e-13)[0]

if __name__=='__main__':
    for a in [0,0.07,0.25,0.5,0.63,0.9,1.0]:
        x=exact_positive_fraction(a)
        y=independent_surface_integral(a)
        assert abs(x-y)<1e-12,(a,x,y)
        assert second_derivative_integral(a)<-0.05
        assert 0.5-1e-14<=x<=0.535441
        print(f'a={a:.2f}: analytic {x:.12f}, surface integral {y:.12f}, curvature {second_derivative_integral(a):.6f}')
    rng=np.random.default_rng(2607)
    xyz=np.abs(rng.standard_normal((800000,3)))
    for a in [0.,0.2,0.5,0.9]:
        p=np.mean(a*xyz[:,0]+(1-a)*xyz[:,1]>=xyz[:,2])
        f=exact_positive_fraction(a)
        sigma=math.sqrt(f*(1-f)/len(xyz))
        assert abs(p-f)<5*sigma
        print(f'a={a:.2f}: independent half-normal sampling {p:.6f}, analytic {f:.6f}, 5 sigma {5*sigma:.6f}')
    m=4/PI*math.atan((3-math.sqrt(5))/2)
    M=1-m
    assert abs(exact_positive_fraction(.5)-M)<1e-14
    assert m >4/9
    print('sharp range:',m,M,'Grunbaum sharp universal benchmark 4/9:',4/9)
    # Numerically check the monotone one-versus-rest probability in selected dimensions.
    lim=math.erf(1/math.sqrt(math.pi))
    for d in [2,3,4,6,10,30]:
        # Fresh independent draws for each dimension; not used to establish monotonicity.
        Y=np.abs(rng.standard_normal((250000,d)))
        observed=np.mean(Y[:,:-1].mean(axis=1)>=Y[:,-1])
        assert .45 <= observed <=lim+.01
        print(f'd={d}: one-versus-rest Monte Carlo={observed:.6f}; proven limit={lim:.6f}')
    print('All numerical cross-checks passed (not a proof).')
