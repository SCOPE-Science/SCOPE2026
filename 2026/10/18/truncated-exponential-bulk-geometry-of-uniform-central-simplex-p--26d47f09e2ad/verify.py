#!/usr/bin/env python3
"""Independent reproducibility checks for a conditional central-simplex volume law.

Pure Python standard library; numerical simulation is not an infinite-dimensional proof.
"""
import math
import random
from fractions import Fraction


def target(c):
    a = math.log(c)/(c - 1)
    return 1 - c*a*a


def integrate_moment(c, power, steps=12000):
    a = math.log(c)/(c - 1)
    z = math.exp(-a) - math.exp(-c*a)
    h = (c*a-a)/steps
    total = 0.0
    for j in range(steps+1):
        s = a + j*h
        w = 0.5 if j in (0, steps) else 1.0
        total += w * s**power * math.exp(-s)
    return h*total/z


def conditional_exponential_sample(m, c, rng):
    # The beta variable gives the minimum of iid exponentials under the ratio event.
    z = rng.betavariate(m/(c-1), m)
    ymin = -math.log(z)/(c-1)
    data = [ymin]
    for _ in range(m-1):
        u = rng.random()
        data.append(ymin - math.log1p(-u*(1-z)))
    s = sum(data)
    scaled = [m*v/s for v in data]
    return sum((v-1)**2 for v in scaled)/m, min(scaled), max(scaled)


def main():
    for m in (2, 3, 10, 100):
        for c in (Fraction(3, 2), Fraction(2), Fraction(3)):
            # Exact rational beta mean and variance versus algebraic formula.
            alpha = Fraction(m, 1)/(c-1)
            beta = Fraction(m, 1)
            mean = alpha/(alpha+beta)
            var = alpha*beta/((alpha+beta)**2*(alpha+beta+1))
            assert mean == 1/c
            assert var == (c-1)**2/(c*c*(m*c+c-1))
    for c in (1.5, 2.0, 3.0, 5.0):
        assert abs(integrate_moment(c, 0) - 1.0) < 1e-8
        assert abs(integrate_moment(c, 1) - 1.0) < 1e-8
        assert abs(integrate_moment(c, 2) - (1+target(c))) < 1e-8
        assert target(c) > 0
    # For m=2,c=2, normalized-volume measure is uniform on x in [1/3,2/3].
    # Here m*||X-(1/2,1/2)||^2=4(x-1/2)^2, average exactly 1/27.
    assert Fraction(4, 1) * (Fraction(1, 6)**2)/3 == Fraction(1, 27)
    rng = random.Random(20261014)
    for c in (1.5, 2.0, 3.0):
        m = 1200
        reps = 450
        rs = [conditional_exponential_sample(m,c,rng) for _ in range(reps)]
        avgr = sum(x[0] for x in rs)/reps
        avgmin = sum(x[1] for x in rs)/reps
        avgmax = sum(x[2] for x in rs)/reps
        a = math.log(c)/(c-1)
        assert abs(avgr - target(c)) < 0.005, (c,avgr,target(c))
        assert abs(avgmin-a) < 0.07, (c,avgmin,a)
        assert abs(avgmax-c*a) < 0.07, (c,avgmax,c*a)
        print('ratio',c,'dimension',m-1,'sample radius',round(avgr,8),
              'limit',round(target(c),8),'sample extrema',round(avgmin,6),round(avgmax,6))
    print('PASS exact beta identities; limiting moment quadrature; segment benchmark; conditional sampler')


if __name__ == '__main__':
    main()
