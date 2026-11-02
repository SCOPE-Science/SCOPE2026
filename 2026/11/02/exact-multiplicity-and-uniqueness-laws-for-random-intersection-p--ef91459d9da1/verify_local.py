"""Exact local random-intersection-poset maximum counts, without stable-matching code."""
from itertools import permutations, product
from math import comb, factorial
from fractions import Fraction

for m in range(1, 5):
    orders = list(permutations(range(m)))
    for t in (1, 2, 3):
        if factorial(m)**t > 10000:
            continue
        sum_max = 0
        count_unique = 0
        cases = 0
        for profile in product(orders, repeat=t):
            rank = [{x: row.index(x) for x in range(m)} for row in profile]
            maximal = [x for x in range(m) if not any(
                y != x and all(r[y] < r[x] for r in rank)
                for y in range(m))]
            sum_max += len(maximal)
            count_unique += len(maximal) == 1
            cases += 1
        f = sum(Fraction((-1)**(j-1)*comb(m, j), j**(t-1))
                for j in range(1, m+1))
        assert Fraction(sum_max, cases) == f, (m, t, 'mean')
        assert Fraction(count_unique, cases) == Fraction(1, m**(t-1)), (m, t, 'uniqueness')
        print('m,t=', m,t,'profiles=',cases,'expected_max=',str(f),'unique=',str(Fraction(count_unique,cases)))
