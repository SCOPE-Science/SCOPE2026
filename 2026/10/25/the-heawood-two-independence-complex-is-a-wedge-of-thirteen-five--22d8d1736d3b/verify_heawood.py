#!/usr/bin/env python3
"""Exact finite proof checks for the 2-independence complex of the Fano incidence graph."""
from collections import Counter, deque
from itertools import combinations

LINES = ((0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5))
N=14

def graph():
    adj=[0]*N
    for j,L in enumerate(LINES):
        for p in L:
            adj[p]|=1<<(7+j)
            adj[7+j]|=1<<p
    return adj

def faces_by_local_degree(adj):
    return {s for s in range(1<<N) if all(((s&adj[v]).bit_count()<=1) for v in range(N) if s>>v&1)}

def faces_by_components(adj):
    out=set()
    for s in range(1<<N):
        unseen=s
        admissible=True
        while unseen and admissible:
            v=(unseen&-unseen).bit_length()-1
            component=1<<v
            fringe=component
            unseen^=component
            while fringe:
                bit=fringe&-fringe
                u=bit.bit_length()-1
                fringe ^=bit
                fresh=unseen&adj[u]
                unseen ^=fresh
                fringe |=fresh
                component |=fresh
                if component.bit_count()>2:
                    admissible=False
                    break
        if admissible:out.add(s)
    return out

def build_matching(faces):
    remaining=set(faces)
    pairs=[]
    for v in range(N):
        b=1<<v
        for s in sorted(remaining):
            t=s|b
            if (s&b)==0 and t in remaining:
                pairs.append((s,t))
                remaining.remove(s)
                remaining.remove(t)
    assert (0,1) in pairs
    return [x for x in pairs if x!=(0,1)], (remaining | {1})-{0}

def check_acyclic(faces,pairs):
    nonempty=faces-{0}
    matching_edges=set(pairs)
    outgoing={s:[] for s in nonempty}
    indegree={s:0 for s in nonempty}
    edges=0
    for t in nonempty:
        rem=t
        while rem:
            bit=rem&-rem
            rem^=bit
            s=t^bit
            if s==0:continue
            if (s,t) in matching_edges:
                a,b=s,t
            else:
                a,b=t,s
            outgoing[a].append(b)
            indegree[b]+=1
            edges+=1
    q=deque(s for s in nonempty if indegree[s]==0)
    visited=0
    while q:
        s=q.popleft()
        visited+=1
        for t in outgoing[s]:
            indegree[t]-=1
            if indegree[t]==0:q.append(t)
    assert visited==len(nonempty), ('cycle',len(nonempty)-visited)
    return edges,visited

def mod2_bettis(faces):
    bydim={d:sorted(s for s in faces if s.bit_count()==d+1) for d in range(7)}
    ranks={}
    for d in range(1,7):
        lower={face:i for i,face in enumerate(bydim[d-1])}
        basis={}
        for t in bydim[d]:
            col=0
            mask=t
            while mask:
                bit=mask&-mask
                mask-=bit
                col^=1<<lower[t^bit]
            while col:
                pivot=col.bit_length()-1
                if pivot in basis:col^=basis[pivot]
                else:
                    basis[pivot]=col
                    break
        ranks[d]=len(basis)
    betti={d:len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(7)}
    betti[0]-=1
    return ranks,betti

def main():
    adj=graph()
    assert all(x.bit_count()==3 for x in adj)
    assert len({tuple(sorted(p)) for L in LINES for p in combinations(L,2)})==21
    assert all(sum({a,b}<=set(L) for L in LINES)==1 for a,b in combinations(range(7),2))
    assert all(not(adj[v]&(((1<<7)-1) if v<7 else (((1<<7)-1)<<7))) for v in range(N))
    f1=faces_by_local_degree(adj)
    f2=faces_by_components(adj)
    assert f1==f2
    counts=Counter(s.bit_count()-1 for s in f1)
    expected={-1:1,0:14,1:91,2:322,3:651,4:728,5:392,6:58}
    assert counts==expected,(counts,expected)
    pairs,critical=build_matching(f1)
    assert len(pairs)==1121
    assert all(s in f1 and t in f1 and (t^s).bit_count()==1 and (s&t)==s for s,t in pairs)
    assert len({s for pair in pairs for s in pair})==2*len(pairs)
    assert not (set(critical)&{x for pair in pairs for x in pair})
    assert len(critical)==14
    critvec=Counter(s.bit_count()-1 for s in critical)
    assert critvec=={0:1,5:13},critvec
    directed_edges,visited=check_acyclic(f1,pairs)
    ranks,betti=mod2_bettis(f1)
    assert betti=={0:0,1:0,2:0,3:0,4:0,5:13,6:0},betti
    reduced_euler=sum((-1)**d*n for d,n in counts.items())
    assert reduced_euler==-13
    print('FANO_PAIRS_UNIQUE=21; GRAPH_VERTICES=14; GRAPH_EDGES=21')
    print('TWO_INDEPENDENCE_FACES_WITH_EMPTY='+str(len(f1)))
    print('F_VECTOR_DIM_-1_TO_6='+str([counts[d] for d in range(-1,7)]))
    print('MATCHED_NONEMPTY_PAIRS='+str(len(pairs)))
    print('CRITICAL_DIMENSIONS='+str(dict(sorted(critvec.items()))))
    print('CRITICAL_SIX_VERTEX_MASKS='+str(sorted(s for s in critical if s.bit_count()==6)))
    print('DIRECTED_HASSE_EDGES='+str(directed_edges)+'; TOPOLOGICAL_SORT_VISITED='+str(visited))
    print('MOD2_BOUNDARY_RANKS='+str([ranks[d] for d in range(1,7)]))
    print('MOD2_REDUCED_BETTI='+str([betti[d] for d in range(7)]))
    print('REDUCED_EULER='+str(reduced_euler))
    print('VERIFY_OK')
if __name__=='__main__':main()
