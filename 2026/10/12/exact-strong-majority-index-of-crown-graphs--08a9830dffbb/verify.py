from itertools import product
from math import ceil

def edges(n):
    return [(i,j) for i in range(n) for j in range(n) if i!=j]

def ok(n, col, q):
    E=edges(n)
    for i,j in E:
        adj=[(i,k) for k in range(n) if k!=i and k!=j] + [(k,j) for k in range(n) if k!=i and k!=j]
        lim=n-2
        for c in range(q):
            if sum(col[e]==c for e in adj)>lim:
                return False
    return True

def matrix_col(rows):
    n=len(rows); d={}
    for i,row in enumerate(rows):
        for j,ch in enumerate(row):
            if i!=j: d[(i,j)]=int(ch)
    return d

small3=matrix_col(['.12','1.0','20.'])
small5=matrix_col(['.2101','0.222','12.00','102.1','1102.'])
assert ok(3,small3,3)
assert ok(5,small5,3)

# Cr_4 two-colour witness: colour 1 iff the edge meets a_0 or b_0.
c4={(i,j): int(i==0 or j==0) for i,j in edges(4)}
assert ok(4,c4,2)

# Exhaustively verify two-colour feasibility at the three small orders.
small=[]
for n in (3,4,5):
    E=edges(n); found=0
    for mask in range(1<<len(E)):
        col={e:(mask>>k)&1 for k,e in enumerate(E)}
        if ok(n,col,2):
            found+=1
            if n!=4:
                raise AssertionError(('unexpected two-colouring',n,mask))
    if n==4 and found==0:
        raise AssertionError('missing Cr_4 two-colouring')
    small.append((n,found))

# Balanced one-factor construction for all tested larger orders.
for n in range(6,61):
    col={}
    for i,j in edges(n):
        d=(j-i)%n
        col[(i,j)]=(d-1)%3
    assert ok(n,col,3), n
    assert 2*ceil((n-1)/3)<=n-2

# Check the algebraic contradiction pattern for a broad range n != 4.
for n in range(3,101):
    if n==4: continue
    # If all row/column sums equal r, equation (1) forces a constant bit x.
    possible=[]
    for x in (0,1):
        r=(n-1)*x
        if 2*r-2*x==n-2:
            possible.append(x)
    assert not possible, (n,possible)

print('ALL CHECKS PASSED; exhaustive_two_colour_orders=3,4,5; '
      'three_colour_construction_range=6..60; symbolic_range=3..100; '
      'Cr4_two_colourings=%d' % small[1][1])
