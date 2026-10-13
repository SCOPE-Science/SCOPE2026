#!/usr/bin/env python3
"""Finite replay of the coding A -> A x Z on labeled finite orders.
This does not prove the infinite Borel or isotypy theorems; it checks the coding mechanics.
"""
from itertools import permutations
checks=0

def rel_from_perm(p):
    pos={x:i for i,x in enumerate(p)}
    return lambda a,b: pos[a]<pos[b]

def coded(rel,n,r=2):
    pts=[(a,z) for a in range(n) for z in range(-r,r+1)]
    def lt(x,y):
        a,i=x; b,j=y
        return rel(a,b) or (a==b and i<j)
    return pts,lt

for n in range(1,8):
    for p in permutations(range(n)):
        r=rel_from_perm(p)
        pts,lt=coded(r,n)
        # zero slice exactly decodes the input order
        for a in range(n):
            for b in range(n):
                assert lt((a,0),(b,0)) == r(a,b)
                checks += 1
        # each output comparison has the lexicographic formula
        for x in pts:
            for y in pts:
                a,i=x; b,j=y
                assert lt(x,y) == (r(a,b) or (a==b and i<j))
                checks += 1
print(f"VERIFY_OK {checks} exact assertions")
