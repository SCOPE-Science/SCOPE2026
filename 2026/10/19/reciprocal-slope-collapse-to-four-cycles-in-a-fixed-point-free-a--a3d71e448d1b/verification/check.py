"""Exact-rational supplementary tests for a piecewise-affine return identity.

Requires Python 3 only. Rational tests are illustrations, not an infinite proof.
"""
from fractions import Fraction as Q


def forward(x, r):
    if not -r*r <= x <= r*r:
        raise ValueError('outside invariant interval')
    if x <= -r:
        return x/r + 1
    if x < 0:
        return r*x + r*r
    if x < r:
        return r*x - r*r
    return x/r - 1


def iterate(x, r, n):
    for _ in range(n):
        x = forward(x, r)
    return x


def in_core(x,r):
    return (-r*r <= x <= -r) or (1-r <= x <= r-1) or (r <= x <= r*r)


def survival(r, n):
    # Disjoint open intervals in the two holes, after n further survival steps.
    intervals = [(-r, 1-r, -1), (r-1, r, +1)]
    for _ in range(n):
        updated = []
        for left, right, side in intervals:
            if side == -1:  # preimage inside positive hole of negative survivor
                updated.append(((left+r*r)/r, (right+r*r)/r, +1))
            else:           # preimage inside negative hole of positive survivor
                updated.append(((left-r*r)/r, (right-r*r)/r, -1))
        for left,right,side in updated:
            if side == 1:
                assert r-1 <= left < right <= r
            else:
                assert -r <= left < right <= 1-r
        intervals = updated
    return sum(right-left for left,right,_ in intervals)


def run():
    tests = 0
    for r in [Q(11,10), Q(3,2), Q(2), Q(5,2), Q(3), Q(5), Q(9)]:
        q = r*r/(r+1)
        assert forward(q, r) == -q
        assert forward(-q, r) == q
        assert iterate(q, r, 2) == q
        tests += 3
        for n in range(10):
            assert survival(r, n) == 2/r**n
            tests += 1
        # Full exact rational grid tests, including all branch boundaries.
        for j in range(1001):
            x = -r*r + 2*r*r*Q(j,1000)
            assert -r*r <= forward(x, r) <= r*r
            if in_core(x,r):
                assert iterate(iterate(x,r,3),r,4) == iterate(x,r,3)
                tests += 1
            if x not in (q,-q):
                y = iterate(x, r, 300)
                assert in_core(y,r)
                assert iterate(y,r,4) == y or iterate(iterate(y,r,3),r,4)==iterate(y,r,3)
                tests += 2
            tests += 1
        print('r=',r,'passed')
    print('PASS', tests, 'exact rational checks')


if __name__ == '__main__':
    run()
