#!/usr/bin/env python3
"""Independent finite numerical checks of cone pair-distance dispersion.

The theorem and its global uniqueness proof are analytic. This script is only a
reproducible supplementary numerical test using Python's standard library.
"""
import math
import random

PI=math.pi

def energy_over_slant_squared(alpha):
    return 1.0 - (8.0/9.0) * (math.sin(alpha)/alpha)

def energy_over_area(alpha):
    return energy_over_slant_squared(alpha)/alpha

def stationary_numerator(alpha):
    return 8*(2*math.sin(alpha)-alpha*math.cos(alpha))-9*alpha

def bisect(fn, left, right, iterations=100):
    fl=fn(left)
    if fl*fn(right)>=0: raise ValueError('root not bracketed')
    for _ in range(iterations):
        middle=(left+right)/2
        if middle==left or middle==right: break
        if fl*fn(middle)>0:
            left,fl=middle,fn(middle)
        else:
            right=middle
    return (left+right)/2

def sample_mean_squared_intrinsic(alpha, samples, seed):
    rng=random.Random(seed)
    total=0.0
    for _ in range(samples):
        u,v = rng.random(), rng.random()
        r,s = math.sqrt(u), math.sqrt(v)
        theta1,theta2 = 2*alpha*rng.random(),2*alpha*rng.random()
        separation=abs(theta1-theta2)
        delta=min(separation,2*alpha-separation)
        # A straight chord in the appropriate planar unfolding of the cone.
        dx=r-s*math.cos(delta)
        dy=s*math.sin(delta)
        total+=dx*dx+dy*dy
    return total/samples

def main():
    first=bisect(stationary_numerator,0.8,1.1)
    second=bisect(stationary_numerator,2.7,3.1)
    assert 0.9253<first<0.9255
    assert 2.9221<second<2.9223
    assert energy_over_area(first)<energy_over_area(PI/3)<1/PI
    assert energy_over_area(first)<energy_over_area(second)
    assert 0.25140<energy_over_area(first)<0.25143
    max_error=0.0
    for index, alpha in enumerate([0.2,0.4,0.8,first,1.2,2.0,second,3.1]):
        empirical=sample_mean_squared_intrinsic(alpha,300000,12643+index)
        predicted=energy_over_slant_squared(alpha)
        err=abs(empirical-predicted)
        max_error=max(err,max_error)
        assert err<0.009, (alpha,err)
    # Paired coupling gives pointwise strict angular monotonicity.
    rng=random.Random(43912)
    for _ in range(200000):
        rad1=math.sqrt(rng.random());rad2=math.sqrt(rng.random())
        fraction=rng.random()
        def squared(a):
            return rad1*rad1+rad2*rad2-2*rad1*rad2*math.cos(a*fraction)
        assert squared(0.25)<squared(1.5)<squared(3.0)
    print('alpha_min = %.15f' % first)
    print('normalized_min = %.15f' % energy_over_area(first))
    print('alpha_local_max = %.15f' % second)
    print('normalized_local_max = %.15f' % energy_over_area(second))
    print('maximum_sample_error = %.9f' % max_error)
    print('eight independent Monte Carlo configurations: PASS')
    print('200000 monotone-coupling configurations: PASS')

if __name__=='__main__':main()
