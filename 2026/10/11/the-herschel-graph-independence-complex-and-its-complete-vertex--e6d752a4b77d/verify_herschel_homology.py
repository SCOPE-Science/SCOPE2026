#!/usr/bin/env python3
"""Independent subset recursion and mod-two boundary-rank check."""
from collections import Counter
from fractions import Fraction

N=11
NEIGHBORS={
 0:{5,6,9,10},1:{5,6,7,8},2:{7,8,9,10},
 3:{5,7,9},4:{6,8,10},
 5:{0,1,3},6:{0,1,4},7:{1,2,3},8:{1,2,4},9:{0,2,3},10:{0,2,4},
}


def make_faces(allowed):
    """DFS independent subsets; no bitmask-through-2^11 enumeration."""
    out={}
    def go(chosen,available):
        if chosen:
            out.setdefault(len(chosen)-1,[]).append(frozenset(chosen))
        for j,v in enumerate(available):
            go(chosen+(v,),[w for w in available[j+1:] if w not in NEIGHBORS[v]])
    go((),sorted(allowed))
    return out


def mod2_rank(columns):
    pivots={}
    for c in columns:
        x=c
        while x:
            k=x.bit_length()-1
            if k not in pivots:
                pivots[k]=x
                break
            x^=pivots[k]
    return len(pivots)


def reduced_betti(bydim):
    maxdim=max(bydim)
    sizes=[len(bydim.get(k,[])) for k in range(maxdim+1)]
    # Add augmentation rank 1 to compute reduced degree-zero homology.
    rank=[1]
    for k in range(1,maxdim+1):
        rows={f:i for i,f in enumerate(bydim[k-1])}
        boundary=[]
        for f in bydim[k]:
            col=0
            for v in f:
                col|=1<<rows[f-{v}]
            boundary.append(col)
        rank.append(mod2_rank(boundary))
    rank.append(0)
    betti={k:sizes[k]-rank[k]-rank[k+1] for k in range(maxdim+1)}
    assert min(betti.values())>=0
    return {k:v for k,v in betti.items() if v},sizes,rank


def expected(kind,v):
    if kind=='full':return {2:2}
    if kind=='deletion':return {} if v in (3,4) else {2:1}
    if kind=='link':return {1:2} if v in (3,4) else {1:1}


def charpoly_coeffs():
    mat=[[int(j in NEIGHBORS[i]) for j in range(N)] for i in range(N)]
    def times(a,b):
        return [[sum(a[i][k]*b[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
    P=[[int(i==j) for j in range(N)] for i in range(N)]
    traces=[0]
    for d in range(1,N+1):
        P=times(P,mat)
        traces.append(sum(P[i][i] for i in range(N)))
    c=[1]
    for k in range(1,N+1):
        num=sum(c[k-i]*traces[i] for i in range(1,k+1))
        assert num%k==0
        c.append(-num//k)
    return c


def run():
    assert all(v not in neigh for v,neigh in NEIGHBORS.items())
    assert all(v in NEIGHBORS[w] for w,neigh in NEIGHBORS.items() for v in neigh)
    assert sum(map(len,NEIGHBORS.values()))==36
    assert sorted(map(len,NEIGHBORS.values()))==[3]*8+[4]*3
    assert charpoly_coeffs()==[1,0,-18,0,93,0,-188,0,132,0,0,0],charpoly_coeffs()
    print('charpoly',charpoly_coeffs())
    number=0
    for kind,v in [('full',None)]+[('deletion',i) for i in range(N)]+[('link',i) for i in range(N)]:
        allowed=set(range(N))
        if kind=='deletion':allowed.remove(v)
        elif kind=='link':allowed.difference_update(NEIGHBORS[v]|{v})
        bydim=make_faces(allowed)
        betti,sizes,ranks=reduced_betti(bydim)
        assert betti==expected(kind,v),(kind,v,betti)
        if kind=='full': assert sizes==[11,37,45,22,7,1]
        print(kind,v,'f',sizes,'rank',ranks,'reduced F2 Betti',betti)
        number+=1
    assert number==23
    print('HERSCHEL_HOMOLOGY_OK',number)

if __name__=='__main__':run()
