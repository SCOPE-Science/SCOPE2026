#!/usr/bin/env python3
"""Exact, standalone verification for higher-independence complexes of two 16-vertex graphs.

The graph generators are the group Z4 x Z4; each nonempty simplex is
encoded by a 16-bit mask with vertex x+4*y. The element-matching rule
and its acyclicity are verified directly on all Hasse incidences.
"""
from collections import Counter,deque
N=16
GENERATORS={
 "shrikhande":((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)),
 "rook":((1,0),(-1,0),(2,0),(0,1),(0,-1),(0,2))
}
ORDERS={
 "shrikhande":(3,10,5,7,13,0,1,8,4,9,11,14,6,12,15,2),
 "rook":(2,0,12,1,15,7,9,3,8,4,13,6,10,14,11,5)
}
EXPECTED={
 "shrikhande": {"f":(16,120,384,544,240,32),"crit":58,"h3":57,"faces":1337},
 "rook": {"f":(16,120,384,528,144),"crit":106,"h3":105,"faces":1193}
}

def verify(name):
    def vid(x,y):return (x%4)+4*(y%4)
    increments=GENERATORS[name]
    neighbors=tuple(sum(1<<vid(v%4+a,v//4+b) for a,b in increments) for v in range(N))
    # Both graphs are six-regular and have two common neighbors per vertex pair.
    assert all(m.bit_count()==6 for m in neighbors)
    assert all((neighbors[u]&(1<<v))==((neighbors[v]&(1<<u))!=0)*(1<<v) for u in range(N) for v in range(N) if u!=v)
    assert all(u!=v or not(neighbors[u]&(1<<v)) for u in range(N) for v in range(N) if u==v)
    assert all((neighbors[u]&neighbors[v]).bit_count()==2
               for u in range(N) for v in range(u+1,N))

    def is_dissociation_degree(m):
        return all((neighbors[i]&m).bit_count()<=1 for i in range(N) if m&(1<<i))

    def is_dissociation_component(m):
        unseen=m
        while unseen:
            pending=unseen&-unseen;unseen^=pending;size=0
            while pending:
                bit=pending&-pending
                pending^=bit
                i=bit.bit_length()-1
                size+=1
                if size>2:return False
                new=neighbors[i]&unseen
                unseen^=new
                pending|=new
        return True

    valid=[]
    for m in range(1<<N):
        a=is_dissociation_degree(m)
        assert a==is_dissociation_component(m),(name,m)
        if a:valid.append(m)
    face_set=set(valid)-{0}
    assert len(valid)==EXPECTED[name]['faces']
    f=Counter(m.bit_count()-1 for m in valid)
    assert tuple(f[k] for k in range(max(f)+1))==EXPECTED[name]['f']
    assert f[-1]==1
    f_order=sorted(face_set,key=lambda m:(m.bit_count(),m))
    live=set(face_set)
    pairs=[]
    for pivot in ORDERS[name]:
        b=1<<pivot
        for m in f_order:
            if m in live and not(m&b) and (m|b) in live:
                live.remove(m);live.remove(m|b)
                pairs.append((m,m|b))
    assert len(live)==EXPECTED[name]['crit']
    assert Counter(m.bit_count()-1 for m in live)==Counter({0:1,3:EXPECTED[name]['h3']})
    assert len(pairs)*2+len(live)==len(face_set)
    # Independent acyclicity check: Kahn ordering of matched upward
    # and unmatched downward codimension-one incidences.
    idx={m:i for i,m in enumerate(f_order)}
    matched=set(pairs)
    succ=[[] for _ in f_order]
    indegree=[0]*len(f_order)
    incidence_count=0
    for upper in f_order:
        rest=upper
        while rest:
            bit=rest&-rest;rest^=bit
            lower=upper^bit
            if not lower:continue
            incidence_count+=1
            if (lower,upper) in matched: src,dst=idx[lower],idx[upper]
            else:src,dst=idx[upper],idx[lower]
            succ[src].append(dst);indegree[dst]+=1
    q=deque(i for i,d in enumerate(indegree) if d==0)
    popped=0
    while q:
        u=q.popleft();popped+=1
        for v in succ[u]:
            indegree[v]-=1
            if indegree[v]==0:q.append(v)
    assert popped==len(f_order)
    # Independent simplicial mod-2 boundary ranks, as a homology cross-check.
    dimensions=range(max(f))
    dimfaces={d:[m for m in f_order if m.bit_count()==d+1] for d in range(max(f)+1)}
    ranks={}
    for d in range(1,max(f)+1):
        lowerindex={m:i for i,m in enumerate(dimfaces[d-1])}
        basis={}
        for upper in dimfaces[d]:
            column=0
            rest=upper
            while rest:
                bit=rest&-rest;rest^=bit
                column^=1<<lowerindex[upper^bit]
            while column:
                pivot=column.bit_length()-1
                if pivot not in basis:
                    basis[pivot]=column
                    break
                column^=basis[pivot]
        ranks[d]=len(basis)
    betti=[f[d]-ranks.get(d,0)-ranks.get(d+1,0) for d in range(max(f)+1)]
    assert betti==[1]+[0]*2+[EXPECTED[name]['h3']]+[0]*(max(f)-3)
    assert sum(f[d]*(-1)**d for d in range(max(f)+1))==1-EXPECTED[name]['h3']
    return {"graph":name,"augmented_faces":len(valid),"face_vector":[f[d] for d in range(max(f)+1)],"matched_pairs":len(pairs),"critical_vector":str(dict(sorted(Counter(m.bit_count()-1 for m in live).items()))),"incidences":incidence_count,"acyclic_vertices":popped,"boundary_ranks_mod2":list(ranks.values()),"betti_mod2":betti}

if __name__=='__main__':
    for k in GENERATORS:
        print(verify(k))
    print('SHRIKHANDE_ROOK_SECOND_INDEPENDENCE_WEDGES_VERIFIED')
