"""Exact small-tree checks for a joint-depth convolution and frozen covariance.
Pure Python 3, no dependencies. These checks are finite and do not replace proofs.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product


def all_joint(weights):
    n = len(weights)
    ans = {(i, j): defaultdict(Fraction) for i in range(3, n) for j in range(i+1, n+1)}
    total = [sum(weights[:k]) for k in range(1, n+1)]
    for parents in product(*(range(k-1) for k in range(2, n+1))):
        probability = Fraction(1)
        depths = [0]
        for index, parent in enumerate(parents, start=2):
            probability *= Fraction(weights[parent], total[index-2])
            depths.append(depths[parent]+1)
        for (i, j), dist in ans.items():
            dist[depths[i-1], depths[j-1]] += probability
    return {key: dict(val) for key, val in ans.items()}


def bernoulli_sum(weights, begin, end):
    dist = {0: Fraction(1)}
    for k in range(begin, end):
        p = Fraction(weights[k-1], sum(weights[:k]))
        next_dist = defaultdict(Fraction)
        for t, mass in dist.items():
            next_dist[t] += mass * (1-p)
            next_dist[t+1] += mass*p
        dist = dict(next_dist)
    return dist


def covariance(dist):
    mx = sum(Fraction(x)*p for (x, y),p in dist.items())
    my = sum(Fraction(y)*p for (x, y),p in dist.items())
    return sum((x-mx)*(y-my)*p for (x, y),p in dist.items())


def test(weights):
    n = len(weights)
    joints = all_joint(weights)
    total = 0
    for i in range(3, n):
        base = joints[i, i+1]
        baseline_cov = covariance(base)
        assert baseline_cov > 0
        for j in range(i+1, n+1):
            shifted = defaultdict(Fraction)
            for (x,y), p in base.items():
                for step,q in bernoulli_sum(weights, i+1, j).items():
                    shifted[x,y+step] += p*q
            assert dict(shifted) == joints[i,j], (weights, i, j)
            assert covariance(joints[i,j]) == baseline_cov, (weights,i,j)
            assert sum(joints[i,j].values()) == 1
            total += 3
    return total

if __name__ == '__main__':
    cases = [[1]*7, [1,2,3,4,5,6,7], [7,2,5,1,9,4,3], [1,1,1,1,1,1,5]]
    count = sum(test(weights) for weights in cases)
    print(f"PASS: {count} exact rational assertions across {len(cases)} weight cases")
