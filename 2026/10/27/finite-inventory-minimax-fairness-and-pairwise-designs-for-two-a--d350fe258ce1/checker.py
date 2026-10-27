"""Independent finite checks for two-agent binary-cost minimax fairness.

This verifies finite combinatorial statements only; the general theorem uses
an analytic proof. Requires only the Python standard library.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def price(t):
    if t <= 1:
        return Fraction(1)
    r = t // 2
    return 1 + Fraction(r * (r - 1), t * (t - 1))


def value(t, q, k):
    """Expected ex-post ratio for first all-one costs, q random first picks,
    and a k-subset of binary costs for second agent (exchangeability).
    """
    mu1 = (t + 1) // 2
    mu2 = (k + 1) // 2
    b = max(Fraction(1), Fraction(q, mu1))
    if k == 0:
        return b
    result = Fraction(0)
    for h in range(max(0, k - q), min(k, t - q) + 1):
        count = comb(t - q, h) * comb(q, k - h)
        ratio = max(b, Fraction(h, mu2))
        result += Fraction(count, comb(t, k)) * ratio
    return result


def pair_value(t, q):
    mu = (t + 1) // 2
    b = max(Fraction(1), Fraction(q, mu))
    prob = Fraction((t-q)*(t-q-1), t*(t-1))
    return b + max(Fraction(0), 2-b) * prob


def affine_sets(d):
    t = 1 << d
    for a in range(1, t):
        for b in (0, 1):
            yield frozenset(x for x in range(t) if ((a & x).bit_count() % 2) == b)


def run():
    checks = 0
    for t in range(2, 13):
        opt_q = (t + 1)//2
        target = price(t)
        assert value(t, opt_q, 2) == target
        for k in range(t+1):
            assert value(t, opt_q, k) <= target, (t,k)
            checks += 1
        for q in range(t+1):
            assert pair_value(t, q) >= target, (t,q)
            assert (pair_value(t, q) == target) == (q == opt_q), (t,q)
            checks += 1
        print('support',t,'minimax',target,'optimal picks',opt_q)
    for d in (1,2,3,4,5,6):
        t=1<<d
        blocks=list(affine_sets(d))
        assert len(blocks)==2*(t-1)
        assert all(len(b)==t//2 for b in blocks)
        pair_p=Fraction((t//2)*(t//2-1),t*(t-1))
        for x,y in combinations(range(t),2):
            actual=Fraction(sum(x in b and y in b for b in blocks),len(blocks))
            assert actual==pair_p, (d,x,y)
            checks+=1
        print('affine',t,'support size',len(blocks),'pair probability',pair_p)
    print('all checks passed:',checks)

if __name__=='__main__':run()
