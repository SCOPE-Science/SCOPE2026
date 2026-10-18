#!/usr/bin/env python3
"""Independent finite checks of inversion distances for cyclically deleted bicliques.
Uses orientation-vector BFS for small n and separate binary linear-system construction.
"""
from collections import deque, Counter
from random import Random


def graph_edges(n):
    return [(i,j) for i in range(n) for j in range(n)
            if j != i and j != (i+1)%n]


def all_masks(n):
    edges = graph_edges(n)
    masks = set()
    # Each inversion selects independently subsets of the two vertex classes.
    for L in range(1<<n):
        for R in range(1<<n):
            m = 0
            for t,(i,j) in enumerate(edges):
                if (L>>i)&1 and (R>>j)&1:
                    m |= 1<<t
            if m: masks.add(m)
    return masks


def bfs_diameter(n):
    edges=graph_edges(n)
    assert len(edges)==n*(n-2)
    masks=all_masks(n)
    size=1<<len(edges)
    depth=[-1]*size
    depth[0]=0
    q=deque([0])
    while q:
        v=q.popleft()
        for g in masks:
            w=v^g
            if depth[w]<0:
                depth[w]=depth[v]+1
                q.append(w)
    assert -1 not in depth
    return max(depth), dict(sorted(Counter(depth).items())),len(masks)


def proper_three_coloring(n):
    # Labels are all nonzero GF(2)^2 vectors, adjacent cyclic positions differ.
    if n%2==0:
        cols=[1+(i%2) for i in range(n)]
    else:
        cols=[1+(i%2) for i in range(n-1)]+[3]
    assert all(cols[i]!=cols[(i+1)%n] for i in range(n))
    return cols


def nullspace_basis(row_masks, n):
    """GF2 kernel, columns encoded as integer n-bit vectors."""
    rows=list(row_masks)
    pivot=[]
    j=0
    for col in range(n):
        t=next((r for r in range(j,len(rows)) if rows[r]>>col&1),None)
        if t is None: continue
        rows[j],rows[t]=rows[t],rows[j]
        for r in range(len(rows)):
            if r!=j and (rows[r]>>col)&1: rows[r]^=rows[j]
        pivot.append(col);j+=1
        if j==len(rows):break
    free=[col for col in range(n) if col not in pivot]
    basis=[]
    for col in free:
        vector=1<<col
        for r,p in enumerate(pivot):
            if (rows[r]>>col)&1: vector|=1<<p
        assert all((vector & row).bit_count()%2==0 for row in row_masks)
        basis.append(vector)
    return basis


def basis_rows(n):
    colors=proper_three_coloring(n)
    H=[sum((1<<i) for i,c in enumerate(colors) if c&bit) for bit in (1,2)]
    basis=nullspace_basis(H,n)
    assert len(basis)==n-2
    return [sum((1<<t) for t,b in enumerate(basis) if (b>>i)&1) for i in range(n)]


def solve_binary(A,b,k):
    """Solve k independent binary equations in k unknowns, rows are k-bit ints."""
    rows=[A[i] | ((b[i]&1)<<k) for i in range(k)]
    for col in range(k):
        j=next((r for r in range(col,k) if (rows[r]>>col)&1),None)
        assert j is not None, (k,A,b)
        rows[col], rows[j]=rows[j],rows[col]
        for r in range(k):
            if r!=col and ((rows[r]>>col)&1): rows[r]^=rows[col]
    return sum(((rows[i]>>k)&1)<<i for i in range(k))


def construct_masks(n, target):
    """Construct exactly n-2 masks whose XOR matches target on every edge."""
    edges=graph_edges(n)
    row=basis_rows(n); k=n-2
    matrix=[[0]*n for _ in range(n)]
    for t,(i,j) in enumerate(edges): matrix[i][j]=(target>>t)&1
    col=[]
    for j in range(n):
        neighbors=[i for i in range(n) if i!=j and (j!=(i+1)%n)]
        assert len(neighbors)==k
        col.append(solve_binary([row[i] for i in neighbors],[matrix[i][j] for i in neighbors],k))
    masks=[]
    for t in range(k):
        L=sum((1<<i) for i in range(n) if row[i]>>t&1)
        R=sum((1<<j) for j in range(n) if col[j]>>t&1)
        mask=sum(1<<e for e,(i,j) in enumerate(edges) if (L>>i)&1 and (R>>j)&1)
        masks.append(mask)
    xor=0
    for mask in masks:xor^=mask
    assert xor==target,(n,target,xor)
    return masks


def rank_binary(rows,ncols):
    pivots={}
    rank=0
    for x in rows:
        while x:
            t=x.bit_length()-1
            if t in pivots:x^=pivots[t]
            else:
                pivots[t]=x; rank+=1; break
    return rank


def lower_witness(n):
    """Known entries force the (n-2)x(n-2) unit triangular minor."""
    edges=graph_edges(n)
    target=sum(1<<t for t,(i,j) in enumerate(edges) if i<n-2 and j==i+2)
    assert len(construct_masks(n,target))==n-2
    # Assert that all choices of undefined entries leave the lower-bound minor full rank.
    for hole in range(1<<(2*n)) if n<=5 else (0,):
        matrix=[[0]*n for _ in range(n)]
        for t,(i,j) in enumerate(edges):matrix[i][j]=(target>>t)&1
        for i in range(n):
            matrix[i][i]=(hole>>(2*i))&1
            matrix[i][(i+1)%n]=(hole>>(2*i+1))&1
        rows=[sum(matrix[i][j]<<(j-2) for j in range(2,n)) for i in range(n-2)]
        assert rank_binary(rows,n-2)==n-2
    return target



def derangements(n):
    from itertools import permutations
    return (p for p in permutations(range(n)) if all(p[i]!=i for i in range(n)))


def factor_colors(p):
    n=len(p)
    colors=[0]*n
    for start in range(n):
        if colors[start]: continue
        cycle=[];v=start
        while v not in cycle:
            cycle.append(v);v=p[v]
        assert v==start
        for j,v in enumerate(cycle):
            colors[v]=1+(j%2)
        if len(cycle)%2:colors[cycle[-1]]=3
    assert all(colors[i]!=colors[p[i]] for i in range(n))
    return colors


def check_general_factor(n,p,targets):
    colors=factor_colors(p)
    H=[sum(1<<i for i,c in enumerate(colors) if c&bit) for bit in (1,2)]
    basis=nullspace_basis(H,n)
    assert len(basis)==n-2
    rows=[sum((1<<t) for t,b in enumerate(basis) if b>>i&1) for i in range(n)]
    edges=[(i,j) for i in range(n) for j in range(n) if j!=i and j!=p[i]]
    assert len(edges)==n*(n-2)
    missing_by_col=[{j,next(i for i in range(n) if p[i]==j)} for j in range(n)]
    for target in targets:
        values={(i,j):target>>e&1 for e,(i,j) in enumerate(edges)}
        col=[]
        for j in range(n):
            neigh=[i for i in range(n) if i not in missing_by_col[j]]
            col.append(solve_binary([rows[i] for i in neigh],[values[i,j] for i in neigh],n-2))
        for i,j in edges:
            assert (rows[i]&col[j]).bit_count()%2==values[i,j]


def main():
    rng=Random(94376)
    for n in (3,4,5):
        diam,spectrum,ng=bfs_diameter(n)
        assert diam==n-2,(n,diam)
        print('BFS',n,'edges',len(graph_edges(n)),'distinct inversions',ng,
              'diameter',diam,'distance_spectrum',spectrum)
        # Independently construct an optimal-or-better sequence for ALL differences.
        for target in range(1<<len(graph_edges(n))):construct_masks(n,target)
        lower_witness(n)
    for n in range(6,33):
        lower_witness(n)
        for sample in range(32):
            target=rng.getrandbits(len(graph_edges(n)))
            construct_masks(n,target)
        print('Constructive',n,'32 random target edge patterns passed')
    from itertools import islice
    for n in range(3,9):
        perms=list(derangements(n)) if n<=7 else list(islice(derangements(n),200))
        for p in perms:
            edges=n*(n-2)
            patterns=[0,(1<<edges)-1,rng.getrandbits(edges)]
            check_general_factor(n,p,patterns)
        print('GENERAL_CO_TWO_FACTOR',n,'derangements checked',len(perms),'targets each',3)
    print('ALL_VERIFICATION_CHECKS_PASSED')

if __name__=='__main__':main()
