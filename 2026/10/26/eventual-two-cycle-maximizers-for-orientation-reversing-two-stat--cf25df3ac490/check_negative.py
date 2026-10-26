"""Exact finite checks for a theorem on orientation-reversing two-state PFAs.

Requires Python 3.9+; uses only the standard library. Finite checks are
corroboration, not a substitute for the proof for arbitrary word lengths.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial
from random import Random


def one_run_per_letter(word):
    compressed = []
    for c in word:
        if not compressed or compressed[-1] != c:
            compressed.append(c)
    return len(compressed) == len(set(compressed))


def B(q, m):
    if m == 0:
        return 1
    return sum(factorial(q) // factorial(q-r) * comb(m-1, r-1)
               for r in range(1, min(q,m)+1))


def word_values(q, den, maps, p, n):
    values = {}
    for word in product(range(q), repeat=n):
        x = p
        for a in word:
            A, C = maps[a]
            x = (Fraction(C) - A*x)/den
        values[word] = x
    return values


def check_case(q, den, maps, p, max_n):
    low, high = p, p
    count_max, count_min = 1, 1
    for n in range(1, max_n+1):
        vals = word_values(q, den, maps, p, n)
        mx, mn = max(vals.values()), min(vals.values())
        maximum = [w for w,v in vals.items() if v == mx]
        minimum = [w for w,v in vals.items() if v == mn]
        new_high = max((Fraction(C)-A*low)/den for A,C in maps)
        new_low = min((Fraction(C)-A*high)/den for A,C in maps)
        Acount = sum((Fraction(C)-A*low)/den == new_high for A,C in maps)
        Bcount = sum((Fraction(C)-A*high)/den == new_low for A,C in maps)
        assert (mx,mn) == (new_high,new_low)
        assert (len(maximum),len(minimum)) == (count_min*Acount,count_max*Bcount)
        low,high = new_low,new_high
        count_max,count_min = len(maximum),len(minimum)
        if len(maximum) == 1:
            w=maximum[0]
            assert one_run_per_letter(w[::2])
            assert one_run_per_letter(w[1::2])
        if len(minimum) == 1:
            w=minimum[0]
            assert one_run_per_letter(w[::2])
            assert one_run_per_letter(w[1::2])
    return sum(q**n for n in range(1,max_n+1))


def run():
    total = 0
    cases = 0
    R=Random(20261018)
    for q, nmax, samples in [(2,9,50), (3,7,90), (4,6,50)]:
        den=20
        allowed=[(A,C) for A in range(1,den+1) for C in range(A,den+1)]
        for _ in range(samples):
            maps=[R.choice(allowed) for _ in range(q)]
            p=Fraction(R.randrange(den+1),den)
            total += check_case(q,den,maps,p,nmax)
            cases += 1
    for q in (2,3,4):
        for n in range(1,8):
            actual=sum(one_run_per_letter(x[::2]) and one_run_per_letter(x[1::2])
                       for x in product(range(q),repeat=n))
            assert actual == B(q,(n+1)//2)*B(q,n//2)
    ex=[(4,4),(2,17),(14,20)]
    vals=word_values(3,20,ex,Fraction(2,5),3)
    winners=sorted(vals.items(), key=lambda kv:kv[1],reverse=True)
    assert winners[0]==((1,0,2),Fraction(4867,5000))
    assert winners[1]==((2,0,2),Fraction(1201,1250))
    assert winners[0][1]-winners[1][1]==Fraction(63,5000)
    print('PASS: %s rational automata, %s directly enumerated words' % (cases,total))
    print('PASS: two-step extremal recurrences, multiplicities, parity-run necessity')
    print('PASS: parity-run counting identity for q=2,3,4, n=1,...,7')
    print('PASS: ternary witness 102, score=4867/5000, gap=63/5000')
    print('LIMIT: finite enumeration does not prove eventual regularity')

if __name__=='__main__':
    run()
