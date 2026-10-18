#!/usr/bin/env python3
"""Exact independent finite checks for Euclidean type-A root Rips homology."""
from itertools import combinations, permutations

def roots(n):
    return [(i,j) for i in range(n) for j in range(n) if i!=j]

def squared_distance(a,b):
    v={}
    for x,s in ((a[0],1),(a[1],-1),(b[0],-1),(b[1],1)):
        v[x]=v.get(x,0)+s
    return sum(z*z for z in v.values())

def rank2(rows, width):
    basis={}
    for row in rows:
        v=row
        while v:
            p=v.bit_length()-1
            if p in basis: v ^= basis[p]
            else:
                basis[p]=v
                break
    return len(basis)

def graph_cycle_action(n):
    # Oriented crown edges L_i -> R_j. Integer spanning-tree cycles give Z-basis.
    E=[(i,n+j) for i in range(n) for j in range(n) if i!=j]
    eid={e:k for k,e in enumerate(E)}
    adj=[[] for _ in range(2*n)]
    for k,(a,b) in enumerate(E):
        adj[a].append((b,k,1))
        adj[b].append((a,k,-1))
    parent={0:(-1,-1,0)}
    frontier=[0]
    for u in frontier:
        for v,k,sgn in adj[u]:
            if v not in parent:
                parent[v]=(u,k,sgn)
                frontier.append(v)
    assert len(parent)==2*n
    tree={k for p,k,sgn in parent.values() if k>=0}
    chords=[k for k in range(len(E)) if k not in tree]
    assert len(chords)==n*(n-3)+1

    def walk(v,u):
        # Tree path v -> u; coefficient of each oriented edge.
        pred={v:(None,None,None)}
        q=[v]
        for x in q:
            if x==u: break
            for y,k,sgn in adj[x]:
                if k not in tree or y in pred:continue
                pred[y]=(x,k,sgn)
                q.append(y)
        assert u in pred
        chain={}
        cur=u
        while cur!=v:
            pre,k,sgn=pred[cur]
            chain[k]=chain.get(k,0)+sgn
            cur=pre
        return chain

    col=[]
    for j in chords:
        a,b=E[j]
        z={j:1}
        for k,sgn in walk(b,a).items():
            z[k]=z.get(k,0)+sgn
        # Direct signed boundary zero.
        bd=[0]*(2*n)
        for k,c in z.items():
            x,y=E[k];bd[x]-=c;bd[y]+=c
        assert not any(bd)
        tz={}
        for k,c in z.items():
            i,v=E[k]; j2=v-n
            kk=eid[(j2,n+i)]
            tz[kk]=tz.get(kk,0)-c
        col.append([tz.get(k,0) for k in chords])
    b=len(chords)
    A=[[col[j][i] for j in range(b)] for i in range(b)]
    assert all(sum(A[i][p]*A[p][j] for p in range(b))==int(i==j)
               for i in range(b) for j in range(b))
    masks=[sum(((A[i][j]+int(i==j))&1)<<j for j in range(b)) for i in range(b)]
    rk=rank2(masks,b)
    assert rk==n*(n-3)//2,(n,rk)
    assert sum(A[i][i] for i in range(b))==1
    return b,rk

def test_distance_cliques(n):
    R=roots(n)
    allowed={2,4,6,8}
    ds={squared_distance(a,b) for a,b in combinations(R,2)}
    assert ds==allowed,(n,ds)
    assert all(squared_distance(a,b)==8 for a,b in combinations(R,2) if a==(b[1],b[0]))
    assert sum(squared_distance(a,b)==8 for a,b in combinations(R,2))==n*(n-1)//2
    # Every triangle of the threshold sqrt(2) complex is a common-tail or common-head star.
    neighbors={a:set() for a in R}
    for a,b in combinations(R,2):
        if squared_distance(a,b)==2:neighbors[a].add(b);neighbors[b].add(a)
    for a,b,c in combinations(R,3):
        if b in neighbors[a] and c in neighbors[a] and c in neighbors[b]:
            assert (a[0]==b[0]==c[0]) or (a[1]==b[1]==c[1])
    # Equivalence of pairwise disjoint tail/head condition with distance <=2.
    for a,b in combinations(R,2):
        if squared_distance(a,b)<=4:
            assert not ({a[0],b[0]} & {a[1],b[1]})
        else:
            assert ({a[0],b[0]} & {a[1],b[1]})
    return len(R),len(neighbors)

def char_formula(n):
    R=roots(n)
    for perm in permutations(range(n)):
        fixed=sum(perm[i]==i for i in range(n))
        trans=sum(perm[i]>i and perm[perm[i]]==i for i in range(n))
        # Lefschetz character of oriented crown edges / vertices.
        tr_edges=sum(perm[i]==i and perm[j]==j for i,j in R)
        tr_vertices=2*fixed
        assert tr_edges-tr_vertices+1==fixed*fixed-3*fixed+1
        tr_inverted_edges=-sum(perm[j]==i and perm[i]==j for i,j in R)
        assert tr_inverted_edges+1==1-2*trans

if __name__=='__main__':
    for n in range(4,13):
        b,r=graph_cycle_action(n)
        print('INTEGRAL_INVOLUTION',n,'H1_rank',b,'index_power',r)
    for n in range(4,8):
        print('METRIC_CLIQUE',n,test_distance_cliques(n))
    for n in range(4,8):
        char_formula(n)
    print('VERIFY_OK_TYPE_A_EUCLIDEAN_RIPS_INTEGRAL_EIGENLATTICE')
