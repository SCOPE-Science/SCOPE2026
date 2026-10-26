"""Independent exact checks for interval nearest-neighbor fragmentation/length covariance.

Requires Python 3, standard library only. All expectations use Fraction arithmetic.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import factorial
from collections import Counter


def expected_order_statistics(N):
    harmonic = [Q(0)]
    for k in range(1, N + 1):
        harmonic.append(harmonic[-1] + Q(1, k))
    return [None] + [harmonic[N] - harmonic[N-r] for r in range(1, N+1)]


def rank_covariance(n):
    N = n - 1
    ex = expected_order_statistics(N)
    ec, ez, ecz = Q(0), Q(0), Q(0)
    for ranks in permutations(range(1, N+1)):
        peaks = {i for i in range(1, N-1)
                 if ranks[i] > ranks[i-1] and ranks[i] > ranks[i+1]}
        c = 1 + len(peaks)
        z = sum((ex[v] for i,v in enumerate(ranks) if i not in peaks), Q(0))
        ec += c
        ez += z
        ecz += c*z
    fact = factorial(N)
    # Uniform spacings: normalized iid Exp(1), with n+1 exponentials total.
    return (ecz/Q(fact) - ec*ez/Q(fact*fact))/Q(n+1)


def theoretical_covariance(n):
    if n <= 3:
        return Q(0)
    if n == 4:
        return -Q(11,135)
    return -Q(139*n+405,2700*(n+1))


def verify_local_moments():
    exp3 = expected_order_statistics(3)
    local = sum((exp3[ranks[1]] for ranks in permutations((1,2,3))
                 if ranks[1]>ranks[0] and ranks[1]>ranks[2]), Q(0))/6
    assert local == Q(11,18)
    exp5 = expected_order_statistics(5)
    weighted = Counter()
    for rank in permutations((1,2,3,4,5)):
        if rank[1]>rank[0] and rank[1]>rank[2] and rank[3]>rank[2] and rank[3]>rank[4]:
            weighted[rank[3]] += 1
    assert sum(weighted.values()) == 16
    joint = sum((Q(num,120)*exp5[r] for r,num in weighted.items()), Q(0))
    assert joint == Q(413,1800)
    assert joint-Q(11,54) == Q(139,5400)
    print('Local exponential moment: 11/18; two-apart joint: 413/1800; mixed covariance: 139/5400')


def verify_graph_model():
    for N in range(2,7):
        for gaps in permutations(range(1,N+1)):
            points = [0]
            for gap in gaps:
                points.append(points[-1] + gap)
            unique_edges=set()
            for i,x in enumerate(points):
                j=min((j for j in range(N+1) if j != i),
                      key=lambda j: abs(x-points[j]))
                unique_edges.add((min(i,j),max(i,j)))
            cuts={i for i in range(1,N-1)
                  if gaps[i]>gaps[i-1] and gaps[i]>gaps[i+1]}
            predicted={(i,i+1) for i in range(N) if i not in cuts}
            assert unique_edges==predicted, (N,gaps,unique_edges,predicted)
            assert sum(points[j]-points[i] for i,j in unique_edges) == sum(
                gap for i,gap in enumerate(gaps) if i not in cuts)
    print('Undirected graph-vs-peak deletion checked for distinct gap permutations N=2,...,6')


def main():
    verify_local_moments()
    verify_graph_model()
    for n in range(2,10):
        actual=rank_covariance(n)
        expected=theoretical_covariance(n)
        assert actual==expected, (n,actual,expected)
        print('n=%d covariance=%s (exact permutation enumeration)' % (n, actual))
    print('ALL EXACT CHECKS PASSED')

if __name__ == '__main__':
    main()
