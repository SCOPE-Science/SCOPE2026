#!/usr/bin/env python3
"""Direct evaluation of explicit rank-one/rank-two separating group sentences."""
from itertools import permutations

def mul(x,y): return tuple(x[i] for i in y)

def separating_values(n):
    e=tuple(range(n));ps=list(permutations(range(n)))
    squares={x:mul(x,x) for x in ps}
    has_nontrivial=any(x!=e for x in ps)
    has_nonsquare1=any(x!=e and squares[x]!=e for x in ps)
    square_image=set(squares.values())
    rooted_involution=any(x!=e and squares[x]==e and x in square_image for x in ps)
    longer_than_four=any(squares[x] not in (e,x) and squares[squares[x]] not in (e,x) for x in ps)
    rooted_order_four=any(x in square_image and squares[x]!=e and squares[squares[x]]==e for x in ps)
    return tuple(int(t) for t in (has_nontrivial,has_nonsquare1,rooted_involution,longer_than_four,rooted_order_four))

if __name__=='__main__':
    expected={1:(0,0,0,0,0), 2:(1,0,0,0,0),3:(1,1,0,0,0),4:(1,1,1,0,0),5:(1,1,1,1,0),6:(1,1,1,1,0),7:(1,1,1,1,0),8:(1,1,1,1,1)}
    for n in range(1,9):
        got=separating_values(n)
        assert got==expected[n],(n,got,expected[n])
        print('SEPARATING_FORMULAS_OK n=%d bits=%s'%(n,''.join(map(str,got))))
    print('SENTENCES_VERIFY_OK')
