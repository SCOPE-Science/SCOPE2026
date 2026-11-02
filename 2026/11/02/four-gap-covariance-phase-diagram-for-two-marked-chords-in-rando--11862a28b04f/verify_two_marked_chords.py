"""Exact checks for joint crossing degrees at two prescribed chords.

Uses only Python standard library; no external data and no random sampling.
Run: python verify_two_marked_chords.py
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product


@lru_cache(maxsize=None)
def matchings(indices):
    """Return all perfect matchings of labeled positions, recursively."""
    if not indices:
        return ((),)
    first = indices[0]
    return tuple(((first, indices[i]),) + tail
                 for i in range(1, len(indices))
                 for tail in matchings(indices[1:i] + indices[i + 1:]))


def crossing(edge, other):
    left, right = sorted(edge)
    return (left < other[0] < right) != (left < other[1] < right)


def cells(total, fixed_a, fixed_b):
    ends = set(fixed_a + fixed_b)
    rem = [j for j in range(total) if j not in ends]
    a0, a1 = sorted(fixed_a)
    b0, b1 = sorted(fixed_b)
    u = lambda v: a0 < v < a1
    v = lambda v: b0 < v < b1
    return tuple(sum(int(u(j) == e1 and v(j) == e2) for j in rem)
                 for e1, e2 in [(True, True), (True, False),
                                 (False, True), (False, False)])


def covariance_formula(cell):
    a, b, c, d = cell
    N = a + b + c + d
    return Fraction(2 * (a*d*(a-1)*(d-1) + b*c*(b-1)*(c-1)
                           - 2*a*b*c*d), (N-1)**2*(N-3))


def covariance_pair_count(cell):
    a,b,c,d = cell
    N = a+b+c+d
    M = N-1
    A = (a+b)*(c+d)
    B = (a+c)*(b+d)
    C = a*d+b*c
    Q = (a*(c+d)*(b+d) + b*(c+d)*(a+c)
         + c*(a+b)*(b+d) + d*(a+b)*(a+c))
    return (Fraction(C,M) + Fraction(A*B-Q+C,M*(M-2))
            - Fraction(A*B,M*M))


def verify_case(gaps, pairing, pairings):
    g1, g2, g3, g4 = gaps
    n = (sum(gaps) + 4) // 2
    endpoints = (0, g1+1, g1+g2+2, g1+g2+g3+3)
    a = (endpoints[pairing[0]], endpoints[pairing[1]])
    b = (endpoints[pairing[2]], endpoints[pairing[3]])
    endset = set(endpoints)
    remaining = [v for v in range(2*n) if v not in endset]
    cell = cells(2*n, a, b)
    xsum = ysum = xysum = 0
    for matching in pairings:
        x = sum(crossing(a, (remaining[i], remaining[j])) for i, j in matching)
        y = sum(crossing(b, (remaining[i], remaining[j])) for i, j in matching)
        xsum += x
        ysum += y
        xysum += x*y
    m = len(pairings)
    observed = Fraction(m*xysum-xsum*ysum, m*m)
    predicted = covariance_formula(cell)
    assert observed == predicted, (gaps, pairing, cell, observed, predicted)
    N = 2*n-4
    a0,b0,c0,d0 = cell
    A=(a0+b0)*(c0+d0)
    B=(a0+c0)*(b0+d0)
    assert Fraction(xsum,m)==Fraction(A,N-1)
    assert Fraction(ysum,m)==Fraction(B,N-1)
    if not crossing(a,b):
        assert observed >= 0
        assert (observed > 0) == (a0*d0*(a0-1)*(d0-1) +
                                  b0*c0*(b0-1)*(c0-1) > 0)
    return observed, cell


def all_gaps(total):
    for a in range(total+1):
        for b in range(total-a+1):
            for c in range(total-a-b+1):
                yield a,b,c,total-a-b-c


def run():
    counts = {'exact_cases':0, 'negative_crossing':0,
              'positive_crossing':0, 'zero_crossing':0,
              'negative_noncrossing':0, 'matchings_enumerated':0}
    examples = {}
    for n in range(4,8):
        N=2*n-4
        pairings=matchings(tuple(range(N)))
        for gaps in all_gaps(N):
            for pairing in [(0,1,2,3),(0,2,1,3),(0,3,1,2)]:
                value,cell=verify_case(gaps,pairing,pairings)
                counts['exact_cases']+=1
                counts['matchings_enumerated']+=len(pairings)
                if pairing==(0,2,1,3):
                    tag=('positive' if value>0 else 'negative' if value<0 else 'zero')+'_crossing'
                else:
                    tag=('negative_noncrossing' if value<0 else 'other_noncrossing')
                counts[tag]=counts.get(tag,0)+1
                examples.setdefault((n,tag),(gaps,cell,str(value)))
    algebraic_checks=0
    for N in range(4,30,2):
        for cell in all_gaps(N):
            assert covariance_formula(cell) == covariance_pair_count(cell)
            algebraic_checks += 1
    counts['algebraic_checks']=algebraic_checks
    for n in (4,5):
        assert all(covariance_formula((a,b,c,d))<0
                   for a,b,c,d in all_gaps(2*n-4)
                   if min(a,b,c,d)>=1)
    assert covariance_formula((1,1,1,1))==Fraction(-4,9)
    assert covariance_formula((3,1,1,3))==Fraction(36,245)
    assert covariance_formula((2,2,2,2))==Fraction(-48,245)
    assert counts['negative_noncrossing']==0
    print('PASS',counts)
    print('First positive crossing case at n=6: (a,b,c,d)=(3,1,1,3), cov=36/245')
    print('Contrasting negative crossing case same n: (2,2,2,2), cov=-48/245')
    print('Exhaustive cyclic gaps and all three marked-chord pairings checked for n=4,...,7')


if __name__ == '__main__':
    run()
