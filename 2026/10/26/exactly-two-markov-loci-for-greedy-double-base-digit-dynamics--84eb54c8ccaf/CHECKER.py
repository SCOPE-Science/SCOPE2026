"""Exact rational finite-cylinder checks for a double-base digit theorem.

These finite checks corroborate the stated analytic argument, not an infinite proof.
"""
from fractions import Fraction as F
from itertools import product


def cylinder_interval(word, s, q0):
    c, r = 1/s, q0/s
    l, u = F(0), r
    for d in reversed(word):
        if d == 0:
            l, u = max(F(0), l/q0), min(c, u/q0)
        else:
            l, u = max(c, (l+1)/s), min(r, (u+1)/s)
        if l >= u:
            return F(0), F(0)
    return l, u


def check_curve(s, golden):
    q0 = 1 + 1/s if golden else s/(s-1)
    if golden:
        d0, d1 = s*(s+1)/(s+2), s*s/(s+2)
        pi = [(s+1)/(s+2), 1/(s+2)]
        P = [[s/(s+1), 1/(s+1)], [F(1), F(0)]]
    else:
        d0 = d1 = s-1
        pi = [(s-1)/s, 1/s]
        P = [list(pi), list(pi)]
    for n in range(1, 8):
        total = F(0)
        for w in product([0, 1], repeat=n):
            l,u = cylinder_interval(w,s,q0)
            actual = (d0 if w[0] == 0 else d1)*(u-l)
            predicted = pi[w[0]]
            for a,b in zip(w,w[1:]):
                predicted *= P[a][b]
            assert actual == predicted, (s,golden,w,actual,predicted)
            total += actual
        assert total == 1, (s, golden, n, total)
    return str(s), 'golden-Markov' if golden else 'full-branch-Bernoulli'


if __name__ == '__main__':
    for s in [F(3,2), F(2), F(5,3), F(5)]:
        for golden in [True, False]:
            print('PASS', *check_curve(s, golden))
    s = F(2)
    for q0 in [F(6,5), F(7,4)]:
        assert q0 != 1+1/s and q0 < s/(s-1)
        c10 = cylinder_interval((1,0),s,q0)
        c01 = cylinder_interval((0,1),s,q0)
        assert c10[1] > c10[0] and c01[1] > c01[0]
        if q0 < 1+1/s:
            assert all(cylinder_interval((1,0)*n,s,q0)==(F(0),F(0)) for n in range(20,27))
        else:
            c11 = cylinder_interval((1,1),s,q0)
            assert c11[1] > c11[0]
            assert all(cylinder_interval((1,)*n,s,q0)==(F(0),F(0)) for n in range(20,27))
    print('PASS illustrative non-Markov forbidden words')
