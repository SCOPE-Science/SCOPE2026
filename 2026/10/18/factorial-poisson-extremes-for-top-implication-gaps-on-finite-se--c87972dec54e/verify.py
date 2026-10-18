#!/usr/bin/env python3
"""Exhaustive finite checks for top-consequent reduction of semi-Heyting operations.
Run with Python 3 standard library: python verify.py
"""
from itertools import product
from collections import Counter
from math import factorial, prod
from fractions import Fraction


def generated_rows(n, i):
    if i == n-1:
        yield tuple(list(range(n-1)) + [n-1]); return
    for j in range(i,n):
        for vals in product(*(range(k,n) for k in range(i+1,j+1))):
            yield tuple([*range(i),n-1,*vals,*([j]*(n-1-j))])


def check_axioms(table, n):
    for x,y,z in product(range(n), repeat=3):
        if min(x,table[x][y]) != min(x,y): return False
        if min(x,table[y][z]) != min(x,table[min(x,y)][min(x,z)]): return False
    return all(table[x][x] == n-1 for x in range(n))


def brute_all_tables(n):
    out = set()
    for vals in product(range(n),repeat=n*n):
        tab = tuple(tuple(vals[i*n:(i+1)*n]) for i in range(n))
        if check_axioms(tab,n): out.add(tab)
    return out


def verify(n):
    rows=[tuple(generated_rows(n,i)) for i in range(n)]
    expected=prod(sum(Fraction(factorial(m),factorial(k)) for k in range(m+1)) for m in range(1,n))
    assert expected.denominator==1
    assert prod(len(r) for r in rows)==expected.numerator
    if n<=5:
        tables=set(product(*rows))
        assert len(tables)==expected.numerator
        assert all(check_axioms(table,n) for table in tables)
        fibers=Counter(tuple(table[i][-1] for i in range(n)) for table in tables)
        assert len(fibers)==factorial(n)
        assert sum(fibers.values())==expected.numerator
        for r,c in fibers.items():
            kval=[n-1-r[i] for i in range(n-1)]
            assert c==prod(factorial(n-1-i)//factorial(kval[i]) for i in range(n-1))
        assert sum(c==1 for c in fibers.values()) == 2 if n>=2 else 1
        assert max(fibers.values()) == prod(factorial(m) for m in range(1,n))
        assert sum(c==max(fibers.values()) for c in fibers.values()) == 2**(n-1)
        # Independently compare direct row-value histograms to truncated factorial weights.
        for i in range(n-1):
            hist=Counter(n-1-r[-1] for r in rows[i])
            for k in range(n-1-i+1):
                assert hist[k]==factorial(n-1-i)//factorial(k)
    if n<=3:
        brute=brute_all_tables(n)
        assert brute==set(product(*rows))
    print('CHECKED',n,'algebras',expected.numerator,'reducts',factorial(n),'rows',[len(r) for r in rows])

for n in range(1,6): verify(n)
print('VERIFY_OK independent_full_axioms_n_le_3 19683_candidate_tables_n3 generated_axioms_n_le_5 10400_algebras_n5')
