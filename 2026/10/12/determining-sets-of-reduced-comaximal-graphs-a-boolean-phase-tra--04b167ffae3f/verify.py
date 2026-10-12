#!/usr/bin/env python3
from itertools import product, permutations, combinations
from math import prod

def build_graph(qs):
    r=len(qs)
    verts=[]
    for mask in range(1,(1<<r)-1):
        m=prod(qs[i]-1 for i in range(r) if not (mask>>i)&1)
        for j in range(m):
            verts.append((mask,j))
    adj=[[False]*len(verts) for _ in verts]
    for a,(A,_) in enumerate(verts):
        for b,(B,_) in enumerate(verts):
            if a<b and A&B==0:
                adj[a][b]=adj[b][a]=True
    return verts,adj

def automorphisms(adj):
    n=len(adj)
    deg=[sum(row) for row in adj]
    groups={}
    for i,d in enumerate(deg):
        groups.setdefault(d,[]).append(i)
    blocks=list(groups.values())
    autos=[]
    permlists=[list(permutations(b)) for b in blocks]
    for choices in product(*permlists):
        p=list(range(n))
        for b,img in zip(blocks,choices):
            for u,v in zip(b,img):
                p[u]=v
        ok=True
        for i in range(n):
            for j in range(i+1,n):
                if adj[i][j] != adj[p[i]][p[j]]:
                    ok=False
                    break
            if not ok:
                break
        if ok:
            autos.append(tuple(p))
    return autos

def determining_data(qs):
    verts,adj=build_graph(qs)
    autos=automorphisms(adj)
    n=len(verts)
    identity=tuple(range(n))
    nonid=[p for p in autos if p!=identity]
    for k in range(n+1):
        good=[]
        for S in combinations(range(n),k):
            if all(any(p[s]!=s for s in S) for p in nonid):
                good.append(S)
        if good:
            return len(verts),len(autos),k,len(good)
    raise RuntimeError("no determining set found")

def predicted_nonboolean(qs):
    r=len(qs)
    N=prod(qs)-prod(q-1 for q in qs)-1
    det=N-(2**r-2)
    count=prod((q-1)**(2**(r-1)-1) for q in qs)
    return det,count

cases=[
    ((2,3),(3,2,1,2)),
    ((3,3),(4,8,2,4)),
    ((2,2,2),(6,6,2,12)),
    ((2,2,3),(9,16,3,8)),
]
for qs,expected in cases:
    got=determining_data(qs)
    assert got==expected,(qs,got,expected)
    if any(q>2 for q in qs):
        pd,pc=predicted_nonboolean(qs)
        assert (pd,pc)==(got[2],got[3])
    else:
        assert got[2]==2
    print("CASE",qs,"vertices",got[0],"automorphisms",got[1],
          "determining",got[2],"minimum_sets",got[3])

# Closed-form checks beyond the exhaustively searched graph sizes.
for qs in [(2,3,3),(3,4,5),(2,2,5,3)]:
    r=len(qs)
    N=prod(qs)-prod(q-1 for q in qs)-1
    # Sum of one omitted vertex over every nonempty proper zero-set.
    fibre_sum=0
    min_count=1
    for Z in range(1,(1<<r)-1):
        m=prod(qs[i]-1 for i in range(r) if not (Z>>i)&1)
        fibre_sum += m-1
        min_count *= m
    assert fibre_sum==N-(2**r-2)
    assert min_count==prod((q-1)**(2**(r-1)-1) for q in qs)
    print("FORMULA",qs,"determining",fibre_sum,"minimum_sets",min_count)

# Boolean boundary: incidence-column separation.
for r in range(2,9):
    k=(r-1).bit_length()
    cols=list(range(r))
    rows=[]
    for bit in range(k):
        A={i for i,c in enumerate(cols) if (c>>bit)&1}
        assert A and len(A)<r
        rows.append(A)
    signatures=[tuple(int(i in A) for A in rows) for i in range(r)]
    assert len(set(signatures))==r
    assert k==(r-1).bit_length()
    print("BOOLEAN",r,"determining",k)

print("VERIFY_OK")
