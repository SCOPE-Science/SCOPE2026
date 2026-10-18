"""Independent certificate of the 16-vertex abelian Cayley obstruction.

Run: python check_exception16.py
"""
from collections import Counter
from itertools import product

points=list(product(range(4),repeat=2));index={x:i for i,x in enumerate(points)}
steps={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
A=[[False]*16 for _ in range(16)]
for i,(x,y) in enumerate(points):
    for u,v in steps:A[i][index[((x+u)%4,(y+v)%4)]]=True
assert all(not A[i][i] for i in range(16))
assert all(A[i][j]==A[j][i] for i in range(16) for j in range(16))
assert all(sum(A[i])==6 for i in range(16))
assert all(sum(A[i][k] and A[j][k] for k in range(16))==(2 if A[i][j] else 2) for i in range(16) for j in range(i+1,16))
root=0;N={j for j in range(16) if A[root][j]};far=set(range(16))-{0}-N
assert (len(N),len(far))==(6,9)
# The canonical rooted color-refinement partition is already equitable.
col=[1 if i==0 else (2 if i in N else 0) for i in range(16)]
for i in range(16):
 assert all((sum(col[j]==c and A[i][j] for j in range(16)) ==
             sum(col[j]==c and A[k][j] for j in range(16)))
            for k in range(16) if col[k]==col[i] for c in set(col))
# Distinguish two vertices in the far class using their two common
# neighbours with the marked origin; adjacency of that pair is invariant.
def signature(v):
    common=[u for u in N if A[v][u]]
    assert len(common)==2
    return A[common[0]][common[1]]
T=Counter(signature(v) for v in far)
assert T==Counter({False:3,True:6})
print('PASS: Cayley(Z4 x Z4,S), strongly regular (16,6,2,2);')
print('rooted colour classes 1,6,9; the nine-vertex class contains 3 nonadjacent- and 6 adjacent-common-neighbour vertices')
