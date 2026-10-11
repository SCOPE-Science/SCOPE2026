#!/usr/bin/env python3
"""Exact reproducible computation for the ordinary three-cut complex of the cuboctahedral graph.
Requires Python 3.10+ standard library only. No external files or downloaded tables.
"""
import collections
import fractions
import itertools
import math


def vertices(mask):
    return tuple(i for i in range(12) if mask & (1 << i))


def determinant(a):
    # Fraction-free Bareiss, with row swaps.
    b = [r[:] for r in a]
    n = len(b)
    sign = 1
    den = 1
    for k in range(n-1):
        p = next((i for i in range(k,n) if b[i][k]), None)
        if p is None:
            return 0
        if p != k:
            b[k], b[p] = b[p], b[k]
            sign *= -1
        pivot = b[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                v = b[i][j]*pivot-b[i][k]*b[k][j]
                assert v % den == 0
                b[i][j] = v // den
            b[i][k] = 0
        den = pivot
    return sign*b[-1][-1]


def rational_rank(a):
    b = [[fractions.Fraction(v) for v in row] for row in a]
    if not b: return 0
    rank = 0
    for j in range(len(b[0])):
        i = next((i for i in range(rank,len(b)) if b[i][j]), None)
        if i is None: continue
        b[rank], b[i] = b[i], b[rank]
        x = b[rank][j]
        for jj in range(j,len(b[0])): b[rank][jj] /= x
        for ii in range(rank+1,len(b)):
            x = b[ii][j]
            if not x:continue
            for jj in range(j,len(b[0])): b[ii][jj] -= x*b[rank][jj]
        rank += 1
        if rank == len(b):break
    return rank


def mod2_rank(rows):
    basis = {}
    for v in rows:
        while v:
            p = v.bit_length()-1
            if p in basis: v ^= basis[p]
            else:
                basis[p] = v
                break
    return len(basis)


def main():
    # Vertices of cube Q_3 are 0,...,7, with binary-coordinate adjacency.
    cube_edges = sorted((x,y) for x in range(8) for y in range(x+1,8)
                        if (x ^ y).bit_count() == 1)
    assert len(cube_edges) == 12
    # A cuboctahedral graph vertex is one edge of Q_3; its edges meet at cube vertices.
    adj = [sum(1<<j for j,b in enumerate(cube_edges)
               if j!=i and not set(a).isdisjoint(b)) for i,a in enumerate(cube_edges)]
    assert [v.bit_count() for v in adj] == [4]*12
    assert sum(v.bit_count() for v in adj)//2 == 24
    allv=(1<<12)-1
    disconnected=[]
    for t in itertools.combinations(range(12),3):
        edges=sum(bool(adj[x]&(1<<y)) for x,y in itertools.combinations(t,2))
        if edges <= 1: disconnected.append(t)
    assert len(disconnected) == 164
    facets=[allv ^ sum(1<<v for v in t) for t in disconnected]
    assert len(set(facets)) == 164
    faces=set()
    for f in facets:
        s=f
        while s:
            faces.add(s)
            s=(s-1)&f
    fv=[sum(s.bit_count()==k for s in faces) for k in range(1,10)]
    assert fv == [12,66,220,495,792,924,792,489,164], fv
    assert sum((-1)**i*c for i,c in enumerate(fv))==6
    print('FACETS',len(facets),'NONEMPTY_FACES',len(faces),'FVECTOR',fv)

    # Element matching: at stage vertex v, toggle v on each remaining pair.
    free=set(faces)
    up={}
    for v in range(12):
        bit=1<<v
        for s in sorted(free,key=lambda s:(s.bit_count(),vertices(s))):
            t=s|bit
            if not(s&bit) and s in free and t in free:
                free.remove(s)
                free.remove(t)
                up[s]=t
    down={hi:lo for lo,hi in up.items()}
    assert len(up) == 1968
    assert len(free)==18
    critical=collections.Counter(s.bit_count()-1 for s in free)
    assert critical == {0:1,7:6,8:11},critical
    print('MATCHED_PAIRS',len(up),'CRITICAL',dict(critical))

    # Verify complete directed Hasse graph acyclic: matched cover lower->upper,
    # every unmatched cover upper->lower. No hidden unexamined cover relations.
    edges=collections.defaultdict(list)
    indeg={s:0 for s in faces}
    cover_count=0
    for s in faces:
        for v in vertices(s):
            lo=s^(1<<v)
            if not lo:continue
            assert lo in faces
            cover_count+=1
            if up.get(lo)==s: a,b=lo,s
            else: a,b=s,lo
            edges[a].append(b)
            indeg[b]+=1
    queue=collections.deque(s for s,deg in indeg.items() if deg==0)
    visited=0
    while queue:
        s=queue.popleft()
        visited+=1
        for t in edges[s]:
            indeg[t]-=1
            if indeg[t]==0:queue.append(t)
    assert visited==len(faces), ('acyclicity failure',visited,len(faces))
    print('HASSE_COVERS',cover_count,'DAG_VISITED',visited)

    # Algebraic Morse cancellation over Z. Eliminating each matched lower face
    # via the signed boundary of its matched upper face gives a chain-equivalent
    # Morse complex. The DAG proves termination of all recursive substitutions.
    from functools import lru_cache
    @lru_cache(None)
    def reduced(s):
        if s in free: return {s:1}
        if s not in up:return {}
        T=vertices(up[s])
        missing=next(i for i,v in enumerate(T) if not(s&(1<<v)))
        total=collections.Counter()
        for i,v in enumerate(T):
            if i==missing:continue
            coeff=(-1)**(missing+i+1)
            for target,c in reduced(up[s]^(1<<v)).items():
                total[target]+=coeff*c
        return {s:c for s,c in total.items() if c}

    rows=sorted((s for s in free if s.bit_count()==8),key=vertices)
    cols=sorted((s for s in free if s.bit_count()==9),key=vertices)
    M=[[0 for _ in cols] for _ in rows]
    for j,s in enumerate(cols):
        total=collections.Counter()
        for i,v in enumerate(vertices(s)):
            for target,c in reduced(s^(1<<v)).items():
                total[target]+=(-1)**i*c
        for i,t in enumerate(rows): M[i][j]=total[t]
    assert rational_rank(M)==5
    # A unit maximal-rank 5x5 minor proves the five nonzero Smith invariant
    # factors are 1. Therefore integral homology has no torsion.
    unit_minor=None
    for rr in itertools.combinations(range(6),5):
        for cc in itertools.combinations(range(11),5):
            d=determinant([[M[i][j] for j in cc] for i in rr])
            if abs(d)==1:
                unit_minor=(rr,cc,d)
                break
        if unit_minor:break
    assert unit_minor is not None
    assert mod2_rank([sum((1<<j) for j,v in enumerate(row) if v&1) for row in M])==5
    print('MORSE_BOUNDARY_MATRIX',M)
    print('MORSE_RANK',5,'UNIT_MINOR',unit_minor)

    # Independent face-level rank computation in every dimension over F2.
    levels={k: sorted((s for s in faces if s.bit_count()==k)) for k in range(1,10)}
    ranks=[]
    for k in range(2,10):
        idx={s:i for i,s in enumerate(levels[k-1])}
        columns=[]
        for s in levels[k]:
            col=0
            for v in vertices(s): col^=1<<idx[s^(1<<v)]
            columns.append(col)
        ranks.append(mod2_rank(columns))
    assert ranks == [11,55,165,330,462,462,330,158],ranks
    betti=[len(levels[k])-ranks[k-2]-(ranks[k-1] if k<=8 else 0)
           for k in range(2,10)]
    # Betti for degrees 1..8: subtract previous boundary rank, next rank.
    assert betti==[0,0,0,0,0,0,1,6],betti
    print('BOUNDARY_RANKS_GF2',ranks,'POSITIVE_BETTI_GF2',betti)
    # Critical 0-cell + six 7-cells + eleven 8-cells, Morse boundary rank 5
    # and unit Smith entries -> S^7 wedge (six S^8), by cellular cancellation
    # of unit-degree attaching maps in the (7,8)-dimensional CW model.
    print('VERIFY_OK')

if __name__ == '__main__':main()
