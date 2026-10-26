"""Exact-rational verification of selective unanimity subdivision in simple voting games.

Requires only the Python 3 standard library. Not a substitute for the general proof.
"""
from fractions import Fraction


def exact_concentration_from_coalitions(a, m, t):
    # Minimal winning coalitions: each contains all co-required seats 0,...,t-1
    # and one of m disjoint a-seat committees.
    minimal = []
    for j in range(m):
        minimal.append(set(range(t)) | set(range(t+j*a, t+(j+1)*a)))
    assert len({frozenset(s) for s in minimal}) == m
    assert all(not (s < u) for s in minimal for u in minimal)
    n = t + a*m
    dp = [sum((Fraction(1, m*len(S)) for S in minimal if i in S), Fraction(0))
          for i in range(n)]
    assert sum(dp) == 1
    return sum((p*p for p in dp), Fraction(0)), dp


def closed_form(a, m, t):
    return Fraction(m*t+a, m*(a+t)*(a+t))


def gain_numerator(a, m, t):
    return (t-1)*(m*(a*a-t)-a*(2*a+t+1))


def check():
    nchecks = 0
    for a in range(1, 12):
        for m in range(1, 11):
            prev = None
            for t in range(1, 9):
                calculated, dp = exact_concentration_from_coalitions(a,m,t)
                assert calculated == closed_form(a,m,t)
                assert all(dp[i] == Fraction(1, a+t) for i in range(t))
                assert all(dp[i] == Fraction(1, m*(a+t)) for i in range(t, len(dp)))
                if t >= 2:
                    assert (calculated > closed_form(a,m,1)) == (gain_numerator(a,m,t)>0)
                    assert (calculated == closed_form(a,m,1)) == (gain_numerator(a,m,t)==0)
                if prev is not None:
                    # Numerator of the adjacent increment after positive scaling.
                    v = m*(a*a-t*(t-1))-a*(2*a+2*(t-1)+1)
                    assert (calculated>prev)==(v>0)
                    assert (calculated==prev)==(v==0)
                prev = calculated
                nchecks += 1
    assert closed_form(3,4,1)==Fraction(7,64)
    assert closed_form(3,4,2)==Fraction(11,100)
    assert closed_form(3,4,2)-closed_form(3,4,1)==Fraction(1,1600)
    for a in range(1,12):
        for m in range(1,12):
            if 1+a*m<13:
                assert closed_form(a,m,2)<=closed_form(a,m,1)
    for t in range(2, 11):
        for a in [t+1, 10*t, 100*t]:
            m=a*a
            ratio = closed_form(a,m,t)/closed_form(a,m,1)
            assert ratio<t
        assert closed_form(10000,10000*10000,t)/closed_form(10000,10000*10000,1)>Fraction(98*t,100)
    print(f'PASS: {nchecks} independent coalition-based exact-rational instances')
    print('PASS: sharp 13-member petal-family witness and smaller-family exclusion')
    print('PASS: exact adjacent increments, comparisons, and near-t-fold amplification')


if __name__ == '__main__':
    check()
