#!/usr/bin/env python3
"""Independent exhaustive quandle closure enumerator for explicit finite Alexander quandles."""
from itertools import product
from fractions import Fraction
from math import factorial


def test(name, moduli, mat, ks, expected):
    elems=list(product(*(range(m) for m in moduli)))
    n=len(elems)
    pos={e:i for i,e in enumerate(elems)}
    def op(x,y):
        diff=[x[j]-y[j] for j in range(len(moduli))]
        return tuple((y[i]+sum(mat[i][j]*diff[j] for j in range(len(moduli))))%moduli[i] for i in range(len(moduli)))
    table=[[pos[op(x,y)] for y in elems] for x in elems]
    def gen(tup):
        S=set(tup)
        while True:
            t=S.copy()
            for a in S:
                for b in S:
                    t.add(table[a][b])
            if len(t)==len(S):
                return len(t)==n
            S=t
    for k in ks:
        count=sum(gen(x) for x in product(range(n),repeat=k))
        pred=expected[k]
        assert Fraction(count,n**k)==pred, (name,k,count,Fraction(count,n**k),pred)
        print(f'{name}: size={n} k={k} generating={count}/{n**k} probability={pred}')

if __name__=='__main__':
    test('trivial Z/4', (4,), ((1,),), [1,2,3,4], {1:Fraction(0),2:Fraction(0),3:Fraction(0),4:Fraction(3,32)})
    test('involutive Z/8', (8,), ((7,),), [1,2,3], {1:Fraction(0),2:Fraction(1,2),3:Fraction(3,4)})
    test('connected Z/9 multiplier 2', (9,), ((2,),), [1,2,3], {1:Fraction(0),2:Fraction(2,3),3:Fraction(8,9)})
    test('Jordan unipotent F3^2', (3,3), ((1,1),(0,1)), [2,3], {2:Fraction(0),3:Fraction(2,9)})
    test('mixed F3 eigen1 and eigen2', (3,3), ((1,0),(0,2)), [2,3], {2:Fraction(0),3:Fraction(16,81)})
    test('two eigenspaces -1 F3^2', (3,3), ((2,0),(0,2)), [2,3], {2:Fraction(0),3:Fraction(16,27)})
    test('Jordan eigen-1 F3^2', (3,3), ((2,1),(0,2)), [2,3], {2:Fraction(2,3),3:Fraction(8,9)})
    test('F4 irreducible F2^2', (2,2), ((0,1),(1,1)), [2,3], {2:Fraction(3,4),3:Fraction(15,16)})
    test('mixed Z2 x Z3', (2,3), ((1,0),(0,2)), [2,3], {2:Fraction(1,3),3:Fraction(2,3)})
    print('VERIFY_OK')
