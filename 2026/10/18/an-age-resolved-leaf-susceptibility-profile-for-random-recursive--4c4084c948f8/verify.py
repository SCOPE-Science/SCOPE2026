#!/usr/bin/env python3
"""Exact independent checks for leaf-age and total path length in recursive trees."""
from fractions import Fraction as Q
from itertools import product
from math import prod

def harmonic(k):
    return sum((Q(1,t) for t in range(1,k+1)),Q(0))

def predicted_mean(n):
    return n*(harmonic(n)-1)

def predicted_cond_mean(n,j):
    return predicted_mean(n) - (harmonic(n-1)-harmonic(j-1))

def predicted_cov(n,j):
    return -Q(j-1,n-1)*(harmonic(n-1)-harmonic(j-1))

def exact(n):
    options = [range(1,k) for k in range(2,n+1)]
    samples = prod(k-1 for k in range(2,n+1))
    total = 0
    leaf_sum = [0]*(n+1)
    depth_leaf_sum = [0]*(n+1)
    for choices in product(*options):
        depth = [0]*(n+1)
        has_child = [False]*(n+1)
        depth_sum = 0
        for k,parent in enumerate(choices,2):
            depth[k] = depth[parent]+1
            has_child[parent] = True
            depth_sum += depth[k]
        total += depth_sum
        for j in range(2,n+1):
            if not has_child[j]:
                leaf_sum[j] += 1
                depth_leaf_sum[j] += depth_sum
    assert Q(total,samples)==predicted_mean(n),(n,'mean')
    assert leaf_sum[1]==0
    for j in range(2,n+1):
        assert Q(leaf_sum[j],samples)==Q(j-1,n-1),(n,j,'leaf probability')
        assert Q(depth_leaf_sum[j],leaf_sum[j])==predicted_cond_mean(n,j),(n,j,'conditional mean')
        assert Q(depth_leaf_sum[j],samples)-Q(total,samples)*Q(leaf_sum[j],samples)==predicted_cov(n,j),(n,j,'covariance')
    assert sum((predicted_cov(n,j) for j in range(2,n+1)),Q(0)) == -Q(n-2,4)
    return samples

if __name__=='__main__':
    assert sum(exact(n) for n in range(2,10))==46233
    for n in range(2,61):
        H=harmonic(n-1)
        cumulative=sum((Q(j-1,n-1)*(H-harmonic(j-1)) for j in range(2,n+1)), Q(0))
        assert cumulative==Q(n-2,4)
        for j in range(2,n):
            a = (j-1)*(H-harmonic(j-1))
            b = j*(H-harmonic(j))
            assert b-a==H-harmonic(j-1)-1
    print('PASS: exhaustive recursive trees n=2..9, exact first moments and covariances, plus 59 symbolic harmonic checks')
