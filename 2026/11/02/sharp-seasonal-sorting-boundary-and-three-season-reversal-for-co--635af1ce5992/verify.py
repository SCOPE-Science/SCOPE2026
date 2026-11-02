"""Numerical and rational cross-checks for seasonal Hassell map ordering.

Analytical inequalities are proved in RESULT.md; sampling here is not a proof.
Runs on Python 3.10+ without third-party dependencies.
"""
from fractions import Fraction
from itertools import permutations
from math import isclose
from random import Random


def hassell(a, p, K, x):
    return x * ((1.0 + a * K) / (1.0 + a * x))**p


def apply_order(order, p, K, x):
    for a in order:
        x = hassell(a, p, K, x)
    return x


def comparison(a, b, p, K, x):
    return hassell(b, p, K, hassell(a, p, K, x)) - hassell(a, p, K, hassell(b, p, K, x))


def exact_counterexample():
    p = 2
    K = Fraction(1)
    a, b, c = Fraction(1, 2), Fraction(1), Fraction(2)
    x = Fraction(1, 2)

    def f(k, v):
        return v * ((1+k*K)/(1+k*v))**p

    def A(params):
        z=x
        for k in params:
            z=f(k,z)
        return z

    sorted_value=A((a,b,c))
    swapped_value=A((b,a,c))
    assert swapped_value > sorted_value
    print('Exact counterexample: sorted=', sorted_value)
    print('Exact counterexample: swapped=', swapped_value)
    print('Exact positive difference=', swapped_value-sorted_value)


def test():
    rng=Random(20261025)
    cnt=0
    for p in (0.2,0.5,0.95,1.05,1.5,2.0,3.0,5.0):
        for i in range(1100):
            K=10**rng.uniform(-1,1)
            a=10**rng.uniform(-1,0.7)/K
            b=a+10**rng.uniform(-1,0.7)/K
            x=K*10**rng.uniform(-1.2,1.2)
            if abs(x/K-1)<0.05:
                continue
            lhs=comparison(a,b,p,K,x)
            first=hassell(b,p,K,hassell(a,p,K,x))
            second=hassell(a,p,K,hassell(b,p,K,x))
            # Relative margin is larger than rounding away from the fixed point.
            assert (lhs>0) == (p>1), (p,K,a,b,x,lhs)
            assert abs(lhs) > 5e-14*max(first,second)
            cnt += 1
    for i in range(400):
        K=10**rng.uniform(-1,1)
        a,b=sorted((10**rng.uniform(-1,0.7)/K for _ in range(2)))
        x=K*10**rng.uniform(-1.2,1.2)
        l=comparison(a,b,1.,K,x)
        assert isclose(l,0.,abs_tol=1e-12,rel_tol=1e-11)
        cnt+=1
    for p in (.4,.8,1.05,1.2,1.5,2.,3.,4.):
        for i in range(300):
            K=10**rng.uniform(-.5,.5)
            if p>1:
                aa=sorted((rng.uniform(.03,.94)/(K*(p-1)) for _ in range(4)))
                x=rng.uniform(.05,.9)*K
            else:
                aa=sorted((rng.uniform(.1,2.)/K for _ in range(4)))
                x=K*10**rng.uniform(-.7,1.2)
            vals=[(o,apply_order(o,p,K,x)) for o in permutations(aa)]
            asc=apply_order(aa,p,K,x)
            desc=apply_order(list(reversed(aa)),p,K,x)
            scale=max(v for _,v in vals)
            err=2e-11*scale
            if p>1:
                assert all(asc+err>=v>=desc-err for _,v in vals)
            else:
                assert all(desc+err>=v>=asc-err for _,v in vals)
            cnt+=1
    exact_counterexample()
    print(f'PASS: {cnt} sampled pair and permutation comparisons, plus exact-rational witness')


if __name__ == '__main__':
    test()
