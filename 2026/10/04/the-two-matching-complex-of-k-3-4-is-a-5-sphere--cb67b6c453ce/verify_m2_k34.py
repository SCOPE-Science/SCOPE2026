#!/usr/bin/env python3
from collections import Counter, deque

# Edges are indexed row-major: e=4*i+j corresponds to a_{i+1}b_{j+1}.
M,N,R=3,4,2
EDGES=[(i,j) for i in range(M) for j in range(N)]
ORDER=[7,4,6,3,2,0,10,1,9,8,11,5]
EXPECTED_FVECTOR=[12,66,204,360,324,114]
EXPECTED_BOUNDARY_RANKS=[11,55,149,211,113]
EXPECTED_CRITICAL={1:1,6:1}

def valid(mask):
    rd=[0]*M; cd=[0]*N
    for e,(i,j) in enumerate(EDGES):
        if mask>>e & 1:
            rd[i]+=1; cd[j]+=1
            if rd[i]>R or cd[j]>R:
                return False
    return True

def gf2_rank(columns):
    basis={}
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p in basis:
                x ^= basis[p]
            else:
                basis[p]=x
                break
    return len(basis)

def gf2_rank_rows(rows):
    rows=[r for r in rows if r]
    rank=0
    col=0
    while rows:
        pivot=max(rows)
        p=pivot.bit_length()-1
        new=[]
        for r in rows:
            if r==pivot: continue
            if (r>>p)&1: r ^= pivot
            if r: new.append(r)
        rows=new; rank+=1; col+=1
    return rank

def main():
    faces=[mask for mask in range(1<<(M*N)) if valid(mask)]
    assert len(faces)==1081
    counts=Counter(mask.bit_count() for mask in faces)
    assert [counts[k] for k in range(1,7)]==EXPECTED_FVECTOR
    assert counts[0]==1

    # Maximal faces are all six-edge faces, so the complex is pure of dimension five.
    F=set(faces)
    facets=[]
    for s in faces:
        if all((s|(1<<e)) not in F for e in range(M*N) if not (s>>e&1)):
            facets.append(s)
    assert Counter(s.bit_count() for s in facets)==Counter({6:114})

    # Sequential elementary matching on the nonempty face poset.
    rem=set(s for s in faces if s)
    pairs=[]
    for e in ORDER:
        step=[]
        for s in list(rem):
            if not (s>>e&1):
                t=s|(1<<e)
                if t in rem:
                    step.append((s,t))
        for s,t in step:
            assert s in rem and t in rem and t.bit_count()==s.bit_count()+1
            rem.remove(s); rem.remove(t); pairs.append((s,t))
    crit=Counter(s.bit_count() for s in rem)
    assert crit==Counter(EXPECTED_CRITICAL)
    assert rem=={128,2403}
    assert len(pairs)==539

    # Full acyclicity check: orient unmatched Hasse edges downward and matched edges upward.
    matched=set(pairs)
    nodes=[s for s in faces if s]
    out={s:[] for s in nodes}; indeg={s:0 for s in nodes}
    covers=0
    for upper in nodes:
        if upper.bit_count()<2: continue
        for e in range(M*N):
            if upper>>e&1:
                lower=upper^(1<<e)
                if lower==0: continue
                covers += 1
                if (lower,upper) in matched:
                    u,v=lower,upper
                else:
                    u,v=upper,lower
                out[u].append(v); indeg[v]+=1
    q=deque([s for s in nodes if indeg[s]==0]); seen=0
    while q:
        u=q.popleft(); seen+=1
        for v in out[u]:
            indeg[v]-=1
            if indeg[v]==0: q.append(v)
    assert seen==len(nodes)
    assert covers==4488

    # Independent mod-2 homology check by boundary ranks, using column and row elimination.
    bydim={d:[s for s in faces if s.bit_count()==d+1] for d in range(6)}
    ranks=[]
    ranks2=[]
    for k in range(1,6):
        rows=bydim[k-1]; ridx={s:i for i,s in enumerate(rows)}
        cols=[]
        rowvec=[0]*len(rows)
        for j,s in enumerate(bydim[k]):
            c=0
            for e in range(M*N):
                if s>>e&1:
                    t=s^(1<<e)
                    i=ridx[t]
                    c ^= 1<<i
                    rowvec[i] ^= 1<<j
            cols.append(c)
        ranks.append(gf2_rank(cols))
        ranks2.append(gf2_rank_rows(rowvec))
    assert ranks==EXPECTED_BOUNDARY_RANKS
    assert ranks2==EXPECTED_BOUNDARY_RANKS
    betti=[]
    for k in range(6):
        rk=0 if k==0 else ranks[k-1]
        rkp=0 if k==5 else ranks[k]
        betti.append(len(bydim[k])-rk-rkp)
    assert betti==[1,0,0,0,0,1]

    # The acyclic matching has exactly one critical 0-cell and one critical 5-cell.
    # Forman's discrete Morse theorem therefore gives S^5.
    critical_top=2403
    critical_edges=[EDGES[e] for e in range(M*N) if critical_top>>e&1]
    print('faces',len(faces),'fvector',EXPECTED_FVECTOR,'facets',len(facets),'covers',covers)
    print('matching_pairs',len(pairs),'critical_sizes',dict(crit),'critical_top_edges',critical_edges)
    print('boundary_ranks_F2',ranks,'betti_F2',betti)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
