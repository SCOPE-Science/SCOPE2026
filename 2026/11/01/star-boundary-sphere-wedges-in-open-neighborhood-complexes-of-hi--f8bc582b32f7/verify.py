#!/usr/bin/env python3
"""Finite exact checks for neighborhood complexes of line graphs of high-girth graphs.
Only the Python standard library is needed. The all-graph claim rests on the accompanying proof.
"""
from itertools import combinations
from collections import Counter


def graph_singer(q, shifts, delete=()):
    edges={(min(i,q+(i+s)%q),max(i,q+(i+s)%q))
           for i in range(q) for s in shifts}
    return 2*q, sorted(edges-set(tuple(sorted(x)) for x in delete))


def petersen():
    edges=[(i,(i+1)%5) for i in range(5)]
    edges += [(i,i+5) for i in range(5)]
    edges += [(i+5,(i+2)%5+5) for i in range(5)]
    return 10,sorted(set(tuple(sorted(e)) for e in edges))


def bridged_petersen_and_plane():
    _, ep = petersen()
    _, ei = graph_singer(13,(0,1,3,9))
    return 36, sorted(ep+[(a+10,b+10) for a,b in ei]+[(0,10)])


def face_closure(facets):
    result={frozenset()}
    for facet in facets:
        s=sorted(facet)
        for r in range(1,len(s)+1):
            result.update(frozenset(x) for x in combinations(s,r))
    return result


def gf2_rank(columns):
    basis={}
    for z in columns:
        while z:
            i=z.bit_length()-1
            if i not in basis:
                basis[i]=z
                break
            z^=basis[i]
    return len(basis)


def reduced_bettis(faces):
    by_dim={d:sorted(f for f in faces if len(f)==d+1)
            for d in range(max(len(f) for f in faces))}
    rank={}
    for d in range(1,len(by_dim)):
        rid={f:i for i,f in enumerate(by_dim[d-1])}
        cols=[sum(1<<rid[frozenset(set(f)-{v})] for v in f)
              for f in by_dim[d]]
        rank[d]=gf2_rank(cols)
    return {d:len(v)-rank.get(d,0)-rank.get(d+1,0)-(d==0)
            for d,v in by_dim.items()}


def collapse_block(A,B):
    """Explicit codimension-one relative elementary collapses of a two-block simplex.
    Stage 1 removes all mixed faces using A excluding a0; stage 2 removes all
    mixed faces using only a0 together with B excluding b0. Both stages run
    in decreasing face size, making each lower face free when reached.
    """
    a0,b0=min(A),min(B)
    Arest=sorted(A-{a0}); Bset=sorted(B); Brest=sorted(B-{b0})
    stage1=[]
    for ra in range(1,len(Arest)+1):
        for ab in combinations(Arest,ra):
            for rb in range(1,len(Bset)+1):
                for bb in combinations(Bset,rb):
                    low=frozenset(ab+bb)
                    stage1.append((low,low|{a0}))
    stage1.sort(key=lambda pair:(-len(pair[0]),tuple(sorted(pair[0]))))
    stage2=[]
    for rb in range(1,len(Brest)+1):
        for bb in combinations(Brest,rb):
            low=frozenset((a0,)+bb)
            stage2.append((low,low|{b0}))
    stage2.sort(key=lambda pair:(-len(pair[0]),tuple(sorted(pair[0]))))
    return stage1+stage2


def check_graph(label,n,edges):
    edges=sorted(set(tuple(sorted(e)) for e in edges))
    m=len(edges)
    assert all(0<=a<b<n for a,b in edges)
    incident=[set() for _ in range(n)]
    adj=[set() for _ in range(n)]
    for i,(a,b) in enumerate(edges):
        incident[a].add(i);incident[b].add(i)
        adj[a].add(b);adj[b].add(a)
    degrees=Counter(map(len,incident))
    assert min(map(len,incident))>=3
    seen={0};stack=[0]
    while stack:
        x=stack.pop()
        for y in adj[x]-seen:seen.add(y);stack.append(y)
    assert len(seen)==n
    # No triangles: each adjacent pair has no common third neighbor.
    assert all(not (adj[a]&adj[b]) for a,b in edges)
    # No four-cycles: any pair has at most one common neighbor.
    assert all(len(adj[a]&adj[b])<=1 for a in range(n) for b in range(a+1,n))
    F=[];X=[];bridges=[];AB=[]
    for k,(u,v) in enumerate(edges):
        A=incident[u]-{k};B=incident[v]-{k}
        assert A and B and A.isdisjoint(B)
        AB.append((A,B));F.append(A|B)
        bridges.append({min(A),min(B)})
    for E in incident:
        X.extend(E-{x} for x in E)
    K=face_closure(F)
    Y=face_closure(X+bridges)
    assert Y<=K
    # Independently check defining neighborhoods, including every possible center.
    for i in range(m):
        true_neigh={j for j in range(m) if i!=j and set(edges[i])&set(edges[j])}
        assert F[i]==true_neigh
    # All cross edges belong to exactly one generating neighborhood simplex.
    for k,(A,B) in enumerate(AB):
        for a in A:
            for b in B:
                s={a,b}
                assert [i for i,f in enumerate(F) if s<=f]==[k]
    # Exact global elementary collapses, checking freeness before each removal.
    live=set(K); steps=0; removed_faces=0
    for k,(A,B) in enumerate(AB):
        for low,high in collapse_block(A,B):
            assert low in live and high in live and low not in Y and high not in Y
            assert len(high)==len(low)+1
            containing={x for x in live if low<=x}
            assert containing=={low,high}, ('not free',label,k,low)
            live.remove(low);live.remove(high)
            steps+=1;removed_faces+=2
    assert live==Y
    predicted={1:2*m-n+1+degrees[3]}
    for d,cnt in degrees.items():
        if d>=4:predicted[d-2]=cnt
    bK=reduced_bettis(K)
    bY=reduced_bettis(Y)
    assert {d:r for d,r in bK.items() if r}==predicted
    assert {d:r for d,r in bY.items() if r}==predicted
    print('%s: n=%d m=%d degrees=%s faces=%d collapse_steps=%d removed=%d retained=%d reduced_bettis=%s PASS'%
          (label,n,m,dict(sorted(degrees.items())),len(K),steps,removed_faces,len(live),predicted))
    return len(K),steps


def main():
    totalfaces=totalsteps=0
    examples=[('Petersen',*petersen()),
              ('Heawood',*graph_singer(7,(0,1,3))),
              ('Projective plane order three incidence',*graph_singer(13,(0,1,3,9))),
              ('Projective plane incidence one edge deleted',*graph_singer(13,(0,1,3,9),((0,13),))),
              ('Projective plane incidence two disjoint edges deleted',*graph_singer(13,(0,1,3,9),((0,13),(1,14)))),
              ('Petersen bridged to projective plane incidence',*bridged_petersen_and_plane())]
    for label,n,edges in examples:
        f,s=check_graph(label,n,edges)
        totalfaces+=f;totalsteps+=s
    # Genuine forbidden-short-cycle boundary examples. These do not assert
    # impossibility of extensions under additional hypotheses.
    for label,n,edges,predicted_circle_rank in [
        ('triangle boundary K4',4,list(combinations(range(4),2)),13),
        ('quadrilateral boundary K3,3',6,[(a,b) for a in range(3) for b in range(3,6)],19)]:
        true_facets=[]
        for i,e in enumerate(edges):
            true_facets.append({j for j,f in enumerate(edges)
                                if i!=j and set(e)&set(f)})
        k=face_closure(true_facets)
        bet={d:r for d,r in reduced_bettis(k).items() if r}
        assert bet.get(1,0)!=predicted_circle_rank
        print('%s: actual_reduced_bettis=%s proposed_out_of_scope_circle_rank=%d NOT_APPLICABLE PASS'%
              (label,bet,predicted_circle_rank))
    print('EXACT_GLOBAL_COLLAPSE_AND_MOD2_HOMOLOGY_OK examples=%d faces=%d collapses=%d boundary_checks=2'%
          (len(examples),totalfaces,totalsteps))

if __name__=='__main__':main()
