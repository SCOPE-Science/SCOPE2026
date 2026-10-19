"""Independent verification by enumerating every original minimum total dominating set.

Python 3 standard library only.  This is separate from the edge-deleted-grid
min-plus dynamic program in check_total_bondage.cpp.
"""
from functools import lru_cache
from itertools import combinations


def verify(n):
    edges = []
    for i in range(n):
        for j in range(4):
            v = 4*i+j
            if i+1 < n:
                edges.append((v,v+4))
            if j+1 < 4:
                edges.append((v,v+1))
    E=len(edges)
    incident=[0]*(4*n)
    for e,(u,v) in enumerate(edges):
        incident[u] |= 1<<e
        incident[v] |= 1<<e

    def local(m):
        return ((m<<1)|(m>>1)) & 15

    @lru_cache(None)
    def optimum(i,previous,current):
        # Min number of selected vertices strictly after the current row.
        choices = (0,) if i+1==n else range(16)
        best=10**6
        for following in choices:
            if (local(current)|previous|following) != 15:
                continue
            candidate=following.bit_count()
            if i+1<n:
                candidate+=optimum(i+1,current,following)
            best=min(best,candidate)
        return best

    costs=[a.bit_count()+optimum(0,0,a) for a in range(16)]
    gamma=min(costs)
    minsets=[]
    def extend(i,previous,current,acc):
        if i+1==n:
            if (local(current)|previous)==15:
                minsets.append(acc)
            return
        for following in range(16):
            if (local(current)|previous|following)!=15:
                continue
            if following.bit_count()+optimum(i+1,current,following)!=optimum(i,previous,current):
                continue
            extend(i+1,current,following,acc|(following<<(4*(i+1))))
    for a in range(16):
        if costs[a]==gamma:
            extend(0,0,a,a)
    assert len(set(minsets))==len(minsets)

    for D in minsets:
        for v in range(n*4):
            assert any((D>>u)&1 for u in range(4*n) if (u,v) in edges or (v,u) in edges)

    # Encode each vertex's entire set of edges leading to selected neighbors.
    clauses=[]
    for D in minsets:
        cd=[]
        for v in range(4*n):
            c=0
            for e,(u,w) in enumerate(edges):
                if u==v and ((D>>w)&1): c |= 1<<e
                if w==v and ((D>>u)&1): c |= 1<<e
            assert c
            cd.append(c)
        clauses.append(cd)

    counts={}
    for k in range(1,4):
        admissible=damaging=0
        for index in combinations(range(E),k):
            F=sum(1<<e for e in index)
            if any((F&incident[v])==incident[v] for v in range(4*n)):
                continue
            admissible+=1
            # A minimum set remains valid iff none of its row-wise witnesses
            # has been entirely destroyed by the removed edges.
            survives=False
            for Dclauses in clauses:
                if all((F&c)!=c for c in Dclauses):
                    survives=True
                    break
            if not survives:
                damaging+=1
        counts[k]=(admissible,damaging)
    expected={5:(8,256,[(31,0),(461,0),(4369,40)]),
              7:(10,121,[(45,0),(986,0),(14004,727)]),
              8:(12,2916,[(52,0),(1322,0),(21884,0)])}
    g,count,rows=expected[n]
    assert gamma==g and len(minsets)==count
    assert [counts[k] for k in range(1,4)]==rows
    print(f'rows={n} min_total_domination={gamma} optimum_sets={len(minsets)}')
    for k in range(1,4):
        print(f' k={k} admissible={counts[k][0]} damaging={counts[k][1]}')

if __name__=='__main__':
    for n in (5,7,8):
        verify(n)
    print('independent optimal-set checks passed')
