"""Exact finite checks of the scalar two-level stationary risk ordering."""
from fractions import Fraction
from itertools import combinations, product
from math import comb


def risks(g, c, s, replace):
    rows = [0] * g + [3] * c
    batches = product(range(g+c), repeat=s) if replace else combinations(range(g+c), s)
    to_corrupt = [0] * s
    to_clean = [0] * s
    for batch in batches:
        rhs = [rows[i] for i in batch]
        order_zero = sorted(rhs, key=abs)
        order_three = sorted(rhs, key=lambda x: abs(x-3))
        for j in range(s):
            to_corrupt[j] += order_zero[j] == 3
            to_clean[j] += order_three[j] == 0
    # The equal batch probabilities cancel in the stationary odds.
    return [Fraction(9*a, a+b) for a,b in zip(to_corrupt,to_clean)]


def main():
    total = 0
    for replace in (False, True):
        for g in range(2,5 if replace else 7):
            for c in range(1,g):
                for s in range(1,(5 if replace else g)+1):
                    r = risks(g,c,s,replace)
                    zeros = 0 if replace else max(0,s-c)
                    assert all(x == 0 for x in r[:zeros]), (g,c,s,r)
                    assert all(x > 0 for x in r[zeros:]), (g,c,s,r)
                    assert all(x < y for x,y in zip(r[zeros:],r[zeros+1:])), (g,c,s,r)
                    if replace:
                        assert min(r) == Fraction(9*c**s,c**s+g**s)
                    elif s <= c:
                        assert min(r) == Fraction(9*comb(c,s),comb(c,s)+comb(g,s))
                    else:
                        assert min(r) == 0
                    total += 1
    print(f'PASS: exact batch enumeration in {total} sampling-design/size cases')


if __name__ == '__main__':
    main()
