#!/usr/bin/env python3
"""Self-contained verification of finite instances of five-run square-spectrum identities.
No external packages or network access are needed.
"""
from itertools import product
from math import comb


def square_factors(word):
    """Independent definition-based enumeration of distinct nonempty XX factors."""
    out = set()
    for left in range(len(word)):
        for half in range(1, (len(word)-left)//2 + 1):
            if word[left:left+half] == word[left+half:left+2*half]:
                out.add(word[left:left+2*half])
    return out


def formulas(a, b, c, d, e):
    largest_zero = max(a, c, e)
    largest_one = max(b, d)
    alpha = int(c <= a and b <= d)
    beta = int(c <= e and d <= b)
    lower = max(1, c-e)
    upper = min(a, c-1)
    h = max(0, upper-lower+1) if b == d else 0
    return largest_zero//2 + largest_one//2 + alpha + beta + h, alpha + beta + h, h


def predicted_set(a, b, c, d, e):
    values = {'0'*(2*k) for k in range(1, max(a,c,e)//2 + 1)}
    values.update({'1'*(2*k) for k in range(1, max(b,d)//2 + 1)})
    if c <= a and b <= d:
        block = '0'*c + '1'*b
        values.add(block + block)
    if c <= e and d <= b:
        block = '1'*d + '0'*c
        values.add(block + block)
    if b == d:
        for i in range(max(1,c-e), min(a,c-1)+1):
            block = '0'*i+'1'*b+'0'*(c-i)
            values.add(block + block)
    return values


def positive_compositions(n, k=5):
    if k == 1:
        yield (n,)
    else:
        for first in range(1,n-k+2):
            for tail in positive_compositions(n-first,k-1):
                yield (first,)+tail


def h_total_coefficient(n):
    # z^6/[(1-z)^2(1-z^2)^3]
    return sum(comb(j-1,2)*(n-2*j+1) for j in range(3,n//2+1))


def h_positive_coefficient(n):
    # z^6/[(1-z)^3(1-z^2)] - z^7/[(1-z)(1-z^2)^3]
    first = sum(comb(n-6-2*j+2,2) for j in range(max(0,(n-6)//2+1)) if n-6-2*j >= 0)
    second = sum(comb(j+2,2) for j in range(max(0,(n-7)//2+1)) if n-7-2*j >= 0)
    return first-second


def main():
    checked = 0
    for tup in product(range(1,6),repeat=5):
        w='0'*tup[0]+'1'*tup[1]+'0'*tup[2]+'1'*tup[3]+'0'*tup[4]
        actual = square_factors(w)
        assert actual == predicted_set(*tup), ('complete square set mismatch',tup,actual,predicted_set(*tup))
        total,mixed,h = formulas(*tup)
        assert len(actual)==total
        assert sum('0' in v and '1' in v for v in actual)==mixed
        nonunary = {v for v in actual if '0' in v and '1' in v}
        assert len({len(v) for v in nonunary}) <= 1
        assert all(len(v) == 2*(tup[2]+min(tup[1],tup[3])) for v in nonunary)
        checked += 1

    histogram_checks=0
    for n in range(5,27):
        sums=positive=0
        max_total=max_mixed=-1
        for tup in positive_compositions(n):
            total,mixed,h=formulas(*tup)
            sums+=h
            positive+=int(h>0)
            max_total=max(max_total,total)
            max_mixed=max(max_mixed,mixed)
        assert sums == h_total_coefficient(n),(n,'H sums',sums,h_total_coefficient(n))
        assert positive == h_positive_coefficient(n),(n,'H positive',positive,h_positive_coefficient(n))
        assert max_total == n//2,(n,'maximum total',max_total,n//2)
        assert max_mixed == (n+1)//3,(n,'maximum mixed',max_mixed,(n+1)//3)
        histogram_checks+=1

    # Witnesses for all length classes and the two independent maxima.
    for n in range(5,160):
        assert formulas(n-4,1,1,1,1)[0] == n//2
        m=(n-2)//3
        delta=n-(3*m+2)
        assert formulas(m+delta,1,m,1,m)[1] == (n+1)//3
    print('VERIFY_OK complete_distinct_square_sets=%d enumerated_length_histograms=%d sharp_witness_lengths=5..159' % (checked,histogram_checks))


if __name__ == '__main__':
    main()
