"""Exact regular-representation checks for three-atom dicyclic convolution.

Requires SymPy. All ranks are calculated over QQ, not via floating point or
modular arithmetic. Usage: python check.py [maximum_m] (default 9).
"""
from itertools import combinations
from math import gcd
from sys import argv
from sympy import QQ, zeros
from sympy.polys.matrices import DomainMatrix


def group_product(x, y, m):
    n = 2*m
    i, s = x
    j, t = y
    return ((i + (1 if s == 0 else -1)*j + m*s*t) % n, (s+t) % 2)


def predicted_nullity(triple, m):
    n = 2*m
    blocks = [[], []]
    for i,s in triple:
        blocks[s].append(i)
    if len(blocks[0]) == 3 or len(blocks[1]) == 3:
        values = blocks[0] if len(blocks[0]) == 3 else blocks[1]
        u, v = (values[1]-values[0]) % n, (values[2]-values[0]) % n
        g = gcd(n,gcd(u,v))
        q = n//g
        return 4*g if q%3 == 0 and {u//g%3, v//g%3} == {1,2} else 0
    pair = blocks[0] if len(blocks[0])==2 else blocks[1]
    u = (pair[1]-pair[0]) % n
    g = gcd(m,u)
    return 2*g if (m//g)%3 == 0 else 0


def formula_count(m):
    a=0
    r=m
    while r % 3 == 0:
        a+=1
        r//=3
    # Use exact integer formulas for each class.
    same=2*m**3*(3**(2*a)-1)//(3*3**(2*a)) if a else 0
    mixed=8*m**3*(3**a-1)//(3**a) if a else 0
    return same, mixed


def verify(m):
    n=2*m
    els = [(i,s) for s in (0,1) for i in range(n)]
    location = {e:k for k,e in enumerate(els)}
    # Matrix for multiplication on the left by an individual group element.
    mats = []
    for left in els:
        row = [location[group_product(left,right,m)] for right in els]
        mats.append(row)
    same=mixed=0
    total=0
    for triple_ids in combinations(range(2*n),3):
        M=zeros(2*n)
        for idx in triple_ids:
            perm=mats[idx]
            for col,row in enumerate(perm):
                M[row,col]+=1
        observed=2*n-DomainMatrix.from_Matrix(M).convert_to(QQ).rank()
        triple=[els[idx] for idx in triple_ids]
        expected=predicted_nullity(triple,m)
        assert observed == expected,(m,triple,observed,expected)
        if observed:
            total+=1
            if triple[0][1]==triple[1][1]==triple[2][1]:same+=1
            else:mixed+=1
    assert (same,mixed)==formula_count(m),(m,same,mixed,formula_count(m))
    return same,mixed,total


if __name__=='__main__':
    limit=int(argv[1]) if len(argv)>1 else 9
    for m in range(2,limit+1):
        a,b,c=verify(m)
        print(f'm={m} same={a} mixed={b} total={c}',flush=True)
