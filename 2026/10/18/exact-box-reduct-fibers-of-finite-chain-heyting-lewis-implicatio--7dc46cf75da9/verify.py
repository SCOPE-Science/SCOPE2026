#!/usr/bin/env python3
"""Exact finite checks for the box-forgetful spectrum on finite Heyting-Lewis chains."""
from itertools import product
from collections import Counter
from math import comb

def arrow(delta, a, b, n):
    return n if a <= b else min(delta[b:a])

def box_signature(delta, n):
    return tuple(arrow(delta, n, b, n) for b in range(n))

def assert_axioms(table, n):
    for a,b,c in product(range(n+1), repeat=3):
        v=lambda x,y: table[(x,y)]
        assert min(v(a,b),v(a,c)) == v(a,min(b,c))
        assert min(v(a,c),v(b,c)) == v(max(a,b),c)
        assert min(v(a,b),v(b,c)) <= v(a,c)
        assert v(a,a)==n

def expected_fiber(signature, n):
    assert len(signature)==n and tuple(sorted(signature))==signature
    out=1
    for i in range(n-1):
        if signature[i]==signature[i+1]:out *= n-signature[i]+1
    return out

def test(n):
    fibers=Counter()
    for delta in product(range(n+1),repeat=n):
        table={(a,b):arrow(delta,a,b,n) for a,b in product(range(n+1),repeat=2)}
        assert_axioms(table,n)
        sig=box_signature(delta,n)
        fibers[sig]+=1
    assert len(fibers)==comb(2*n,n)
    assert sum(fibers.values())==(n+1)**n
    assert all(m==expected_fiber(s,n) for s,m in fibers.items())
    singleton=sum(m==1 for m in fibers.values())
    assert singleton==2**n
    assert max(fibers.values())==(n+1)**(n-1)
    return len(fibers),sum(fibers.values()),singleton,max(fibers.values())

# Completely independent enumeration of ALL binary operations on a three-element
# chain against the defining axioms (not merely the candidate normal forms).
all_tables=[]
for cells in product(range(3), repeat=9):
    table={(a,b):cells[3*a+b] for a,b in product(range(3),repeat=2)}
    try:assert_axioms(table,2)
    except AssertionError:continue
    all_tables.append(tuple(cells))
forms=set()
for d in product(range(3),repeat=2):
    forms.add(tuple(arrow(d,a,b,2) for a,b in product(range(3),repeat=2)))
assert set(all_tables)==forms
for n in range(1,6):
    print('N',n,'BOXES TOTAL SINGLETON MAXFIBER',*test(n))
print('BRUTE_ALL_BINARY_TABLES_ON_3_ELEMENTS',len(all_tables))
print('VERIFY_OK')
