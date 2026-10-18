"""Exact-rational checks for leaf/path-length covariance in Hoppe trees.

Run with Python 3 (standard library only): python verify.py
"""
from fractions import Fraction as F
from itertools import product
from math import factorial


def expected_covariance(n, t):
    if n == 2:
        return F(0)
    harmonic = sum((F(1, 1)/(t + j) for j in range(2, n - 1)), F(0))
    return -(n + t - 3) / 4 + t*(t - 1)/(2*(t + n - 2)) * (1 + harmonic - (t - 1)/(2*(t + 1)))


def expected_leaves(n, t):
    return (t+n-1)/2 + t*(1-t)/(2*(t+n-2))


def expected_path_length(n, t):
    return (t+n-1) * sum((1/(t+j) for j in range(1,n)),F(0))


def exact_distribution(n,t):
    # A parent list (parent[2], ..., parent[n]) labels every recursive tree.
    ep=el=epl=F(0)
    count=0
    for parents in product(*(range(1, vertex) for vertex in range(2, n+1))):
        weight=F(1)
        depths=[0]*(n+1)
        outdegree=[0]*(n+1)
        for vertex, parent in enumerate(parents, start=2):
            weight *= (t if parent==1 else F(1)) /(t+vertex-2)
            depths[vertex]=depths[parent]+1
            outdegree[parent]+=1
        leaves=sum(outdegree[vertex]==0 for vertex in range(1,n+1))
        path=sum(depths)
        ep+=weight*path
        el+=weight*leaves
        epl+=weight*leaves*path
        count+=1
    return el,ep,epl-el*ep,count


def run():
    tests=0; trees=0
    for t in [F(1,3), F(1,2), F(1), F(2), F(5)]:
        for n in range(2,10):
            leaves,path,cov,count=exact_distribution(n,t)
            assert count==factorial(n-1)
            assert leaves==expected_leaves(n,t),(n,t,leaves,expected_leaves(n,t))
            assert path==expected_path_length(n,t),(n,t,path,expected_path_length(n,t))
            assert cov==expected_covariance(n,t),(n,t,cov,expected_covariance(n,t))
            assert cov < 0 if n >= 3 else cov==0
            tests+=4
            trees+=count
        if t==1:
            for n in range(2,50):
                assert expected_covariance(n,t)==-F(n-2,4)
                tests+=1
    print(f'VERIFY_OK parameter_size_pairs=40 trees={trees} exact_assertions={tests}')

if __name__=='__main__':run()
