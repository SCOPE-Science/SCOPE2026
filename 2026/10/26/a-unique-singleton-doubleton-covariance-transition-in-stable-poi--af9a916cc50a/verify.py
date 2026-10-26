"""Finite Chinese-restaurant enumeration and root checks for PD(alpha,0)."""
from fractions import Fraction as Q
from collections import defaultdict
from math import factorial, lgamma, log, log1p, exp


def rise(x, k):
    v = 1
    for j in range(k):
        v *= x + j
    return v


def moments_from_formula(n, a):
    e1 = n * rise(a, n-1) / factorial(n-1)
    e2 = Q(n*(n-1), 2) * (1-a) * rise(a, n-2) / factorial(n-1)
    e12 = Q(n*(n-1)*(n-2), 2) * a*(1-a)*rise(2*a, n-3) / factorial(n-1)
    return e1, e2, e12


def enumerate_crp(n, a):
    p = {(1,): Q(1)}
    for m in range(1,n):
        t = defaultdict(Q)
        for state, weight in p.items():
            k = len(state)
            for index, size in enumerate(state):
                new_state = list(state)
                new_state[index] += 1
                t[tuple(sorted(new_state))] += weight*(size-a)/m
            t[tuple(sorted(state+(1,)))] += weight*k*a/m
        p = dict(t)
    assert sum(p.values()) == 1
    e1 = sum(weight*state.count(1) for state,weight in p.items())
    e2 = sum(weight*state.count(2) for state,weight in p.items())
    e12 = sum(weight*state.count(1)*state.count(2) for state,weight in p.items())
    return e1,e2,e12


def R(n,a):
    return exp(log(n-2)-log(n)+log(a)+lgamma(n)+lgamma(n-3+2*a)-lgamma(2*a)-lgamma(n-1+a)-lgamma(n-2+a)+2*lgamma(a))


def root(n):
    lo=0.0
    hi=1.0
    for _ in range(85):
        m=(lo+hi)/2
        if R(n,m)>1:
            lo=m
        else:
            hi=m
    return (lo+hi)/2


if __name__=='__main__':
    for n in range(3,10):
        for a in (Q(1,4),Q(2,5),Q(1,2),Q(3,4),Q(9,10)):
            actual=enumerate_crp(n,a)
            expected=moments_from_formula(n,a)
            assert actual==expected, (n,a,actual,expected)
    roots=[(n,root(n)) for n in (3,4,5,8,10,20,100,1000)]
    assert all(roots[i][1] < roots[i+1][1] for i in range(len(roots)-1))
    assert abs(root(3)-( (11/3)**0.5-1)/2) < 1e-12
    assert abs(1000*(1-root(1000))-2)<0.01
    for n,a in roots:
        print(f'n={n:4d} critical={a:.12f} n*(1-critical)={n*(1-a):.10f}')
    print('PASS: exact rational CRP enumeration and moments for n=3..9 at 5 discounts; numerical root tests.')
