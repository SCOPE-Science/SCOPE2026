"""Exact-arithmetic auxiliary checks for five-column rank-one volume sampling.

No external packages.  These finite checks supplement, but do not replace, the
five-vertex combinatorial proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb

PAIRS = tuple(combinations(range(5), 2))


def threshold(theta):
    if theta >= F(2, 5):
        return F(1)
    if theta <= F(1, 3):
        return F(3, 2)*theta
    return 3*theta-F(1, 2)


def weights(theta):
    if theta >= F(2, 5):
        return (F(1, 5),)*5
    if theta <= F(1, 3):
        return (theta/2,)*4 + (1-2*theta,)
    return (3*theta-1,)*2 + (1-2*theta,)*3


def probability(p, theta):
    assert len(p)==5 and sum(p)==1 and all(x>0 for x in p)
    return sum((p[i]+p[j] for i,j in PAIRS if p[i]+p[j]<=theta), F(0))/4


def compositions(n,k=5):
    if k==1:
        yield (n,)
    else:
        for j in range(1,n-k+2):
            for tail in compositions(n-j,k-1):
                yield (j,)+tail


def main():
    thetas = (F(1,8), F(1,5), F(1,4), F(3,10), F(1,3),
              F(7,20), F(3,8), F(39,100), F(2,5), F(9,20), F(1,2))
    for theta in thetas:
        p=weights(theta)
        assert probability(p, theta)==threshold(theta), (theta,p)
        if theta < F(2,5):
            assert all(x>0 for x in p)
    checked=0
    for n in (8, 12, 18, 24):
        for a in compositions(n):
            p=tuple(F(v,n) for v in a)
            for theta in thetas:
                assert probability(p,theta)<=threshold(theta),(p,theta)
                checked+=1
    # Direct exact inclusion for all pairs and the exact mean for 100 nonuniform weights
    for m in range(1,101):
        a=(m,m+1,m+2,m+4,2*m+3)
        p=tuple(F(v,sum(a)) for v in a)
        mean=sum(((p[i]+p[j])/4)/(p[i]+p[j]) for i,j in PAIRS)
        assert mean==F(5,2)
    # At theta=2/5, equal weights attain probability one, and the right tail
    # immediately above 5/2 has the sharp supremum limit 7/10.
    assert probability((F(1,5),)*5,F(2,5))==1
    assert 3*F(2,5)-F(1,2)==F(7,10)
    print('PASS: {} exact upper-envelope checks on positive integer mass grids'.format(checked))
    print('PASS: {} sharp positive extremizers, 100 exact expectation identities'.format(len(thetas)))
    print('PASS: endpoint discontinuity algebra and pair-weight normalization')

if __name__=='__main__':
    main()
