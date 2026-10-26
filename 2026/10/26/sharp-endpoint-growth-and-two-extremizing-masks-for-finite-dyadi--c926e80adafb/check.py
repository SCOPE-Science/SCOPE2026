#!/usr/bin/env python3
"""Reproducible exact arithmetic checks for finite dyadic level projections."""
from fractions import Fraction

ASSERTIONS = 0

def ck(truth, context):
    global ASSERTIONS
    ASSERTIONS += 1
    assert truth, context

def formula(n, mask):
    s = 0
    z = Fraction(0)
    for h in range(n):
        bit = (mask >> h) & 1
        z += Fraction(abs(s - bit*(1 << h)), 1 << (h+1))
        s += bit*(1 << h)
    return z + Fraction(s, 1 << n)

def predicted(n):
    return Fraction(n,3) + Fraction(7,9) + Fraction((-1)**n,9*(1 << (n-1)))

def optimum_masks(n):
    if n == 1:
        return {1}
    if n == 2:
        return {3}
    outcomes = set()
    for first in (0, 1):
        b = [1, first]
        while len(b) < n-1:
            b.append(1-b[-1])
        b.append(1)
        outcomes.add(sum(bit << i for i,bit in enumerate(b)))
    return outcomes

def kernel(n, mask, x, y):
    h = 0
    for t in range(n):
        if ((x >> t)&1) != ((y >> t)&1):
            break
        h += 1
    if h == n:
        return sum((mask>>t &1)*(1<<t) for t in range(n))
    return sum((mask>>t &1)*(1<<t) for t in range(h)) - ((mask>>h)&1)*(1<<h)

def main():
    for n in range(1, 13):
        all_values = [formula(n,mask) for mask in range(1<<n)]
        top = max(all_values)
        winners = {mask for mask,val in enumerate(all_values) if val == top}
        ck(top == predicted(n), ('maximum',n,top,predicted(n)))
        ck(winners == optimum_masks(n), ('masks',n,winners,optimum_masks(n)))
        for mask in range(1<<n):
            ck(all_values[mask] <= top, ('bound',n,mask))
    # Independently construct every row of the actual projection kernel.
    for n in range(1, 7):
        for mask in range(1<<n):
            expected = formula(n,mask)
            for x in range(1<<n):
                row = sum(abs(kernel(n,mask,x,y)) for y in range(1<<n))
                ck(Fraction(row,1<<n) == expected, ('matrix row',n,mask,x))
            for x in (0, (1<<n)-1):
                ck(sum(kernel(n,mask,x,y) for y in range(1<<n))==0, ('constants',n,mask,x))
    # Verify the Bellman solution for all binary-rational states on small grids.
    def bellman(r,x):
        if r == 0:
            return x
        return max(x/2+bellman(r-1,x/2), (1-x)/2+bellman(r-1,(1+x)/2))
    for r in range(1, 8):
        slope = Fraction(1,3) + Fraction(2,3) * Fraction((-1)**r,2**r)
        for k in range(17):
            x = Fraction(k,16)
            actual = bellman(r,x)
            expected = predicted(r) - slope*min(x,1-x)
            ck(actual == expected, ('bellman',r,x,actual,expected))
    print('PASS exact-rational assertions',ASSERTIONS)

if __name__=='__main__':
    main()
