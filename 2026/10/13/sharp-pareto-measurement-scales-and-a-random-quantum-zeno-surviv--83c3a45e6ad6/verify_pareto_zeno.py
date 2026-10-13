#!/usr/bin/env python3
"""Numerical checks for the Pareto-distributed projective-measurement model.
Uses only NumPy and SciPy; output is corroborative, not a proof of limiting laws.
"""
import math
import numpy as np
from scipy.integrate import quad

rng = np.random.default_rng(20261009)

def analytic_mean(alpha):
    return math.exp(-math.pi * 2.0 ** (alpha-2.0) /
                    (math.gamma(alpha) * math.sin(math.pi*alpha/2.0)))

def analytic_second(alpha):
    k = math.pi * 2.0 ** (alpha-2.0) / (math.gamma(alpha)*math.sin(math.pi*alpha/2.0))
    return math.exp(-k*(1+2**(alpha-2)))

def sample_survival(alpha, m, batch, c=1.0):
    if alpha < 2:
        b = m**(-1.0/alpha)
    elif alpha == 2:
        b = 1/math.sqrt(m*math.log(m))
    else:
        b = 1/math.sqrt(m)
    b *= c
    data = np.maximum(rng.random((batch,m)),1e-15)**(-1.0/alpha)
    z = b*data
    return np.exp(np.sum(np.log(np.maximum(np.cos(z)**2,1e-300)),axis=1))

def main():
    for alpha in (0.9,1.5):
        m = 20000
        batches = [sample_survival(alpha,m,200) for _ in range(10)]
        v=np.concatenate(batches)
        target=analytic_mean(alpha)
        target2=analytic_second(alpha)
        err=0.055
        print('nondegenerate',alpha,'E',v.mean(),target,'E2',(v*v).mean(),target2,'var',v.var())
        assert abs(v.mean()-target)<err
        assert abs(np.mean(v*v)-target2)<err
        assert target2 > target*target
    for alpha,m,target in ((2.0,100000,math.exp(-1)),(3.5,10000, math.exp(-3.5/1.5))):
        v=sample_survival(alpha,m,200)
        print('deterministic regime',alpha,m,'mean',v.mean(),'median',np.median(v),'limit',target)
        assert abs(np.median(v)-target)<(0.14 if alpha == 2 else 0.08)
    # Sample a second non-unit critical amplitude to test the power c^alpha.
    alpha,c,m=1.0,0.7,3000
    v=np.concatenate([sample_survival(alpha,m,300,c) for _ in range(7)])
    predicted=analytic_mean(alpha)**(c**alpha)
    print('amplitude check',alpha,c,'empirical',v.mean(),'limit',predicted)
    assert abs(v.mean()-predicted)<0.05
    # Independent numerical Fourier-integral calculation for alpha=1.
    integral,err=quad(lambda z:math.sin(z)**2/z**2,0,1000,epsabs=1e-9,limit=600)
    assert abs(integral-math.pi/2)<0.001
    print('VERIFY_OK pareto_survival=passed critical_log=passed regular_regime=passed Fourier_constant=passed')

if __name__ == '__main__':
    main()
