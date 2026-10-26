#!/usr/bin/env python3
"""Self-contained finite tests for the binary sparse Abelian-unbordered spectrum.

Run: python3 check.py
Tests corroborate the symbolic proof; they do not replace it.
"""
from itertools import combinations, product
from collections import Counter
from fractions import Fraction


def abelian_unbordered(s):
    n = len(s)
    p = [0]
    for letter in s:
        p.append(p[-1] + (letter == '1'))
    for k in range(1, n):
        if p[k] == p[n] - p[n-k]:
            return False
    return True


def ordinary_unbordered(s):
    return all(s[:k] != s[-k:] for k in range(1, len(s)))


def direct_factors(a, b, c):
    word = '0'*a + '1' + '0'*b + '1' + '0'*c
    return {word[i:j] for i in range(len(word))
            for j in range(i+1, len(word)+1)
            if abelian_unbordered(word[i:j])}


def formula_factors(a, b, c):
    if a+b+c == 0:
        return {'1'}
    fs = {'0','1'}
    for k in range(1, max(a,b)+1):
        fs.add('0'*k+'1')
    for k in range(1, max(b,c)+1):
        fs.add('1'+'0'*k)
    for k in range(b+1, a+1):
        fs.add('0'*k+'1'+'0'*b+'1')
    for k in range(b+1, c+1):
        fs.add('1'+'0'*b+'1'+'0'*k)
    return fs


def T(a,b,c):
    return max(a,b,c,a+c-b)


def exact_cdf(m,t):
    if t < (m+2)//3:
        return 0
    if t >= m:
        return (m+1)*(m+2)//2
    lower = (m-t+1)//2
    return sum(m-b+1-2*max(m-b-t,0) for b in range(lower,t+1))


def run():
    factor_cases = 0
    # Complete family checks, including boundary cases with consecutive ones.
    for m in range(0,23):
        obs = Counter()
        for a in range(m+1):
            for b in range(m-a+1):
                c = m-a-b
                direct = direct_factors(a,b,c)
                predicted = formula_factors(a,b,c)
                assert direct == predicted, (m,a,b,c,direct ^ predicted)
                t = T(a,b,c)
                if m > 0:
                    assert len(direct) == 2+2*t, (a,b,c,len(direct),t)
                else:
                    assert len(direct) == 1
                obs[t] += 1
                factor_cases += 1
        assert sum(obs.values()) == (m+1)*(m+2)//2
        for t in range(m+1):
            assert sum(v for k,v in obs.items() if k <= t) == exact_cdf(m,t), (m,t)
        if m > 0:
            assert min(obs) == (m+2)//3
            assert max(obs) == m
            assert obs[m] == m+2
    # A second, composition-independent border test.
    all_words = 0
    for n in range(1,15):
        for bits in product('01', repeat=n):
            s = ''.join(bits)
            if min(s.count('0'),s.count('1')) <= 3:
                assert ordinary_unbordered(s) == abelian_unbordered(s), s
                all_words += 1
    # Explicit witness attaining the sharp support-four obstruction.
    w = '00110101'
    assert w.count('1') == w.count('0') == 4
    assert ordinary_unbordered(w) and not abelian_unbordered(w)
    assert w[:4].count('1') == w[-4:].count('1') == 2

    # Exact rational moments: check the limiting values against finite values.
    m = 600
    cnt = (m+1)*(m+2)//2
    total = total2 = 0
    for a in range(m+1):
        for b in range(m-a+1):
            t = T(a,b,m-a-b)
            total += t
            total2 += t*t
    ex = Fraction(total,cnt*m)
    ex2 = Fraction(total2,cnt*m*m)
    var = ex2-ex*ex
    assert abs(ex-Fraction(2,3)) < Fraction(1,1000)
    assert abs(var-Fraction(1,36)) < Fraction(1,1000)
    print('PASS: exact factor sets for', factor_cases, 'gap triples with total zeros <=22')
    print('PASS: exact finite cumulative law and extrema at every total zero count <=22')
    print('PASS: ordinary/Abelian border equivalence for', all_words, 'low-support words through length 14')
    print('PASS: sharp support-four counterexample 00110101')
    print('PASS: rational limiting-moment consistency at total zeros 600; E(T/m)=',ex,'Var(T/m)=',var)


if __name__ == '__main__':
    run()
