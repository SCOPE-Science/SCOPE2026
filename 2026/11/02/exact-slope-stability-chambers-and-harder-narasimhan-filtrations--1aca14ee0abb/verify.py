#!/usr/bin/env python3
"""Exact finite regression tests for the Segre--Veronese kernel's two wall filtrations.
The infinite stability theorem relies on the mathematical argument, not on sampling.
"""
from fractions import Fraction


def rank_rational(rows):
    if not rows:
        return 0
    a = [[Fraction(x) for x in row] for row in rows]
    m, n, r = len(a), len(a[0]), 0
    for col in range(n):
        piv = next((i for i in range(r, m) if a[i][col]), None)
        if piv is None:
            continue
        a[r], a[piv] = a[piv], a[r]
        scale = a[r][col]
        a[r] = [v / scale for v in a[r]]
        for i in range(m):
            if i != r and a[i][col]:
                f = a[i][col]
                a[i] = [a[i][j] - f * a[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def test_fiber_evaluations(a, b):
    # These are evaluation matrices at the common nonzero point ([2:5],[3:7]).
    s = [2 ** (a-i) * 5 ** i for i in range(a+1)]
    t = [3 ** (b-j) * 7 ** j for j in range(b+1)]
    N = (a+1)*(b+1)
    eval_total = [s[i]*t[j] for i in range(a+1) for j in range(b+1)]
    stage_s = [[s[i] if j == row else 0
                for i in range(a+1) for j in range(b+1)]
               for row in range(b+1)]
    stage_t = [[t[j] if i == row else 0
                for i in range(a+1) for j in range(b+1)]
               for row in range(a+1)]
    assert [sum(t[j]*stage_s[j][q] for j in range(b+1))
            for q in range(N)] == eval_total
    assert [sum(s[i]*stage_t[i][q] for i in range(a+1))
            for q in range(N)] == eval_total
    assert rank_rational([eval_total]) == 1
    assert rank_rational(stage_s) == b+1
    assert rank_rational(stage_t) == a+1
    assert N-(b+1) == a*(b+1)
    assert N-(a+1) == b*(a+1)


def test_all():
    tests=0
    for a in range(1, 11):
        for b in range(1, 11):
            R = (a+1)*(b+1)-1
            nA,nB = a*(b+1),b
            nC,nD = b*(a+1),a
            assert nA+nB == nC+nD == R
            # The two extension sequences have first Chern class (-a,-b).
            assert -nA + a*nB == -a
            assert -nB == -b
            assert -nD == -a
            assert -nC + b*nD == -b
            for alpha in range(1, 30):
                for beta in range(1, 30):
                    alpha,beta = Fraction(alpha),Fraction(beta)
                    mu = -(a*beta+b*alpha)/R
                    muA,muB = -beta,a*beta-alpha
                    muC,muD = -alpha,b*alpha-beta
                    assert nA*muA+nB*muB == R*mu
                    assert nC*muC+nD*muD == R*mu
                    wall_plus = alpha == (a+1)*beta
                    wall_minus = beta == (b+1)*alpha
                    if alpha > (a+1)*beta:
                        assert muA > mu > muB
                    elif wall_plus:
                        assert muA == mu == muB
                    if beta > (b+1)*alpha:
                        assert muC > mu > muD
                    elif wall_minus:
                        assert muC == mu == muD
                    assert not (alpha > (a+1)*beta and beta > (b+1)*alpha)
                    tests += 1
    for a in range(1,5):
        for b in range(1,5):
            test_fiber_evaluations(a,b)
    print('VERIFY_OK',tests,'slope comparisons; 16 exact evaluation factorizations')


if __name__=='__main__':
    test_all()
