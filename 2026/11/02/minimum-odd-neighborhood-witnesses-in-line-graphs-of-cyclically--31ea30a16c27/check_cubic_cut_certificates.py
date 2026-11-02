#!/usr/bin/env python3
"""Independent finite checks of the 4-cut lemma and girth-five cycle census."""
from itertools import combinations

def make_graph(kind):
    if kind=='Petersen':
        n=5
        return 2*n,[(i,(i+1)%n) for i in range(n)]+[(i,i+n) for i in range(n)]+[(n+i,n+(i+2)%n) for i in range(n)]
    if kind=='Heawood':
        # Nonzero vectors of GF(2)^3, lines are pairwise spans.
        lines=sorted({tuple(sorted((a,b,a^b))) for a in range(1,8) for b in range(a+1,8) if a^b})
        assert len(lines)==7
        return 14,[(p-1,7+j) for j,line in enumerate(lines) for p in line]
    if kind=='Dodecahedral':
        n=10
        return 2*n,[(i,(i+1)%n) for i in range(n)]+[(i,i+n) for i in range(n)]+[(n+i,n+(i+2)%n) for i in range(n)]
    raise AssertionError(kind)

def cycles5(N, E):
    adj=[set() for _ in range(N)]
    for u,v in E: adj[u].add(v);adj[v].add(u)
    out=set()
    for root in range(N):
        def rec(path):
            if len(path)==5:
                if root in adj[path[-1]]:
                    verts=path+[root]; ed=frozenset(tuple(sorted((verts[i],verts[i+1]))) for i in range(5))
                    out.add(ed)
                return
            for v in adj[path[-1]]:
                if v>root and v not in path:rec(path+[v])
        rec([root])
    return out

def verify(kind, expected5):
    N, E=make_graph(kind)
    E={tuple(sorted(e)) for e in E}
    assert len(E)==3*N//2
    nbr=[0]*N
    for u,v in E:nbr[u]|=1<<v;nbr[v]|=1<<u
    assert all(m.bit_count()==3 for m in nbr)
    cuts={3:0,4:0}
    for S in range(1,1<<(N-1)):
        boundary=sum((nbr[v]&~S).bit_count() for v in range(N) if S>>v&1)
        if boundary<=4:
            # If a cut has size 3, its small shore is one vertex;
            # if it has size 4, its small shore is exactly one edge.
            R=((1<<N)-1)^S
            sh=[S,R]
            if boundary==3:
                assert any(x.bit_count()==1 for x in sh),(kind,S)
            elif boundary==4:
                assert any(x.bit_count()==2 and (nbr[x.bit_length()-1]&x) for x in sh),(kind,S)
            else:raise AssertionError((kind,S,boundary))
            cuts[boundary]+=1
    c5=cycles5(N,E)
    assert len(c5)==expected5,(kind,len(c5),expected5)
    print(kind,'n',N,'3cuts',cuts[3],'4cuts',cuts[4],'5cycles',len(c5))

if __name__=='__main__':
    verify('Petersen',12)
    verify('Heawood',0)
    verify('Dodecahedral',12)
    print('INDEPENDENT_CUT_AND_CYCLE_PASS')
