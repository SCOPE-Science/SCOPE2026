"""Exact finite weighted-allocation checks for the diffuse parity covariance."""
from fractions import Fraction as F
from itertools import product
from math import prod


def check(weights, n):
    m, w = len(weights), sum(weights)
    z = w**n
    odd, even = [0]*m, [0]*m
    joint = [[0]*m for _ in weights]
    for allocation in product(range(m), repeat=n):
        mass = prod(weights[j] for j in allocation)
        loads = [allocation.count(j) for j in range(m)]
        odds = [j for j,k in enumerate(loads) if k % 2]
        evens = [j for j,k in enumerate(loads) if k > 0 and k % 2 == 0]
        for i in odds:
            odd[i] += mass
            for j in evens:
                joint[i][j] += mass
        for j in evens:
            even[j] += mass
    count, total, diffuse = 0, F(0), True
    for i,j in product(range(m),repeat=2):
        obs = F(joint[i][j]*z-odd[i]*even[j], z*z)
        total += obs
        if i==j:
            assert obs<0
            continue
        p,q = F(weights[i],w),F(weights[j],w)
        s,t,d = 1-2*p,1-2*q,1-2*p-2*q
        assert 4*obs == (s*t)**n-d**n+2*(d+q)**n-2*(s*(1-q))**n
        if d>=0:
            assert obs<0
            count += 1
        else:
            diffuse = False
    if diffuse:
        assert total<0
    return count


if __name__=='__main__':
    grid = ([1,2,3,3,3],[1,1,2,2,2,4],[1,1,8])
    checks = sum(check(v,n) for v in grid for n in range(2,6))
    print(f'{checks} qualifying ordered-pair signs verified exactly.')
