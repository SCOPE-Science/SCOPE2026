#!/usr/bin/env python3
"""Independent mod-2 boundary rank cross-check for the first six 3-row rook graphs.
Run with Python 3 standard library.
"""
from itertools import combinations
from collections import defaultdict

def finite_faces(n):
    # Independently generate faces using selected row and column population.
    cells=[(i,j) for i in range(3) for j in range(n)]
    F=defaultdict(list)
    for k in range(1,min(6,3*n)+1):
        for chosen in combinations(range(3*n),k):
            rc=[0,0,0];cc=[0]*n
            for z in chosen:
                i,j=cells[z];rc[i]+=1;cc[j]+=1
            if all(rc[cells[z][0]]+cc[cells[z][1]]<=3 for z in chosen):
                F[k-1].append(chosen)
    return F

def binary_rank(vectors):
    pivots={}
    for z in vectors:
        while z:
            pos=z.bit_length()
            if pos in pivots:z^=pivots[pos]
            else:
                pivots[pos]=z
                break
    return len(pivots)

def homology(n):
    F=finite_faces(n)
    ranks={0:0}
    for d in range(1,max(F)+1):
        positions={face:i for i,face in enumerate(F[d-1])}
        columns=[]
        for sigma in F[d]:
            col=0
            for k in range(len(sigma)):
                facet=sigma[:k]+sigma[k+1:]
                col ^= 1<<positions[facet]
            columns.append(col)
        ranks[d]=binary_rank(columns)
    betti={d:len(fs)-ranks[d]-ranks.get(d+1,0)-(d==0) for d,fs in F.items()}
    return {d:b for d,b in betti.items() if b}

if __name__=='__main__':
    expected={1:{1:1},2:{1:4},3:{2:5},4:{3:13},5:{3:61},6:{3:113,4:7}}
    for n in range(1,7):
        got=homology(n)
        assert got==expected[n],(n,got,expected[n])
        print('n=%d reduced_F2_Betti=%s PASS' % (n,got))
    print('ALL INDEPENDENT MOD-2 CHECKS PASSED')
