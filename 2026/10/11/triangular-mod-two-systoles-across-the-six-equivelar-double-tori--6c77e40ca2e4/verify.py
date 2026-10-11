from itertools import combinations
from collections import Counter, defaultdict

FACETS = [
[(1,2,3),(1,2,4),(1,3,5),(1,4,6),(1,5,7),(1,6,8),(1,7,8),(2,3,6),(2,4,7),(2,6,9),(2,7,10),(2,9,10),(3,5,9),(3,6,11),(3,9,12),(3,11,12),(4,6,9),(4,7,8),(4,8,12),(4,9,12),(5,7,11),(5,9,10),(5,10,12),(5,11,12),(6,8,11),(7,10,11),(8,10,11),(8,10,12)],
[(1,2,3),(1,2,4),(1,3,5),(1,4,6),(1,5,7),(1,6,8),(1,7,8),(2,3,6),(2,4,7),(2,6,9),(2,7,10),(2,9,10),(3,5,10),(3,6,11),(3,9,10),(3,9,11),(4,6,9),(4,7,8),(4,8,12),(4,9,12),(5,7,12),(5,8,11),(5,8,12),(5,10,11),(6,8,11),(7,10,12),(9,11,12),(10,11,12)],
[(1,2,3),(1,2,4),(1,3,5),(1,4,6),(1,5,7),(1,6,8),(1,7,8),(2,3,6),(2,4,8),(2,6,9),(2,8,10),(2,9,10),(3,4,8),(3,4,11),(3,5,11),(3,6,8),(4,6,12),(4,11,12),(5,7,9),(5,9,12),(5,10,11),(5,10,12),(6,9,12),(7,8,10),(7,9,11),(7,10,12),(7,11,12),(9,10,11)],
[(1,2,3),(1,2,4),(1,3,5),(1,4,6),(1,5,7),(1,6,8),(1,7,8),(2,3,6),(2,4,8),(2,6,9),(2,8,10),(2,9,10),(3,4,8),(3,4,11),(3,5,11),(3,6,8),(4,6,12),(4,11,12),(5,7,12),(5,9,10),(5,9,11),(5,10,12),(6,9,12),(7,8,10),(7,9,11),(7,9,12),(7,10,11),(10,11,12)],
[(1,2,3),(1,2,4),(1,3,5),(1,4,6),(1,5,7),(1,6,8),(1,7,8),(2,3,6),(2,4,9),(2,6,10),(2,7,9),(2,7,10),(3,5,9),(3,6,8),(3,8,11),(3,9,11),(4,5,9),(4,5,11),(4,6,12),(4,11,12),(5,7,10),(5,10,11),(6,10,12),(7,8,12),(7,9,12),(8,10,11),(8,10,12),(9,11,12)],
[(1,2,3),(1,2,4),(1,3,5),(1,4,6),(1,5,7),(1,6,8),(1,7,8),(2,3,6),(2,4,9),(2,6,10),(2,7,9),(2,7,10),(3,5,9),(3,6,11),(3,9,12),(3,11,12),(4,6,10),(4,9,11),(4,10,12),(4,11,12),(5,7,10),(5,8,10),(5,8,11),(5,9,11),(6,8,11),(7,8,12),(7,9,12),(8,10,12)],
]
EXPECTED_COUNTS=[20,24,24,24,18,18]
EXPECTED_MULTS=[
[4,4,4,4,2,2],
[4,4,4,4,4,4],
[4,4,4,4,4,4],
[4,4,4,4,4,4],
[4,4,2,2,2,2,1,1],
[4,4,4,1,1,1,1,1,1],
]

def gf2_basis(vecs):
    piv={}
    for v in vecs:
        x=v
        while x:
            p=x.bit_length()-1
            if p in piv: x ^= piv[p]
            else:
                piv[p]=x
                break
    return piv

def reduce_vec(x,piv):
    while x:
        p=x.bit_length()-1
        if p in piv: x ^= piv[p]
        else: break
    return x

def rank(vecs): return len(gf2_basis(vecs))

def check_surface(F):
    F={tuple(sorted(t)) for t in F}
    assert len(F)==28
    edges=sorted({tuple(sorted(e)) for t in F for e in combinations(t,2)})
    assert len(edges)==42
    edge_index={e:i for i,e in enumerate(edges)}
    edge_deg=Counter(tuple(sorted(e)) for t in F for e in combinations(t,2))
    assert set(edge_deg.values())=={2}
    vertex_deg=Counter(v for e in edges for v in e)
    assert [vertex_deg[v] for v in range(1,13)]==[7]*12
    # Links: seven vertices, seven link edges, every link vertex degree two and connected.
    for v in range(1,13):
        link_edges=[]
        for t in F:
            if v in t:
                a,b=sorted(set(t)-{v}); link_edges.append((a,b))
        assert len(link_edges)==7
        ld=Counter(x for e in link_edges for x in e)
        assert len(ld)==7 and set(ld.values())=={2}
        adj=defaultdict(set)
        for a,b in link_edges: adj[a].add(b); adj[b].add(a)
        seen=set(); stack=[next(iter(adj))]
        while stack:
            x=stack.pop()
            if x in seen: continue
            seen.add(x); stack.extend(adj[x]-seen)
        assert len(seen)==7
    # Chain ranks over F2.
    d1=[]
    for a,b in edges: d1.append((1<<(a-1)) | (1<<(b-1)))
    d2=[]
    for t in sorted(F):
        vec=0
        for e in combinations(t,2): vec ^= 1<<edge_index[tuple(sorted(e))]
        d2.append(vec)
    r1=rank(d1); r2=rank(d2)
    assert (r1,r2)==(11,27)
    assert len(edges)-r1-r2==4
    b2=gf2_basis(d2)
    clique3=[]
    E=set(edges)
    for T in combinations(range(1,13),3):
        if all(tuple(sorted(e)) in E for e in combinations(T,2)): clique3.append(T)
    missing=[T for T in clique3 if T not in F]
    # Every missing triangle boundary is a cycle and nonzero modulo B1=im d2.
    cycles=[]
    for T in missing:
        vec=0
        for e in combinations(T,2): vec ^= 1<<edge_index[tuple(sorted(e))]
        assert reduce_vec(vec,b2)!=0
        cycles.append(vec)
    # Facial boundaries are zero in H1.
    for t in F:
        vec=0
        for e in combinations(t,2): vec ^= 1<<edge_index[tuple(sorted(e))]
        assert reduce_vec(vec,b2)==0
    # Group by exact homology equivalence: c~d iff c+d lies in im(d2).
    groups=[]
    unused=set(range(len(cycles)))
    while unused:
        i=min(unused); grp=[]
        for j in sorted(list(unused)):
            if reduce_vec(cycles[i]^cycles[j],b2)==0:
                grp.append(j)
        for j in grp: unused.remove(j)
        groups.append(grp)
    mult=sorted((len(g) for g in groups), reverse=True)
    return len(clique3),len(missing),mult,r1,r2

out=[]
for i,F in enumerate(FACETS,1):
    vals=check_surface(F)
    assert vals[1]==EXPECTED_COUNTS[i-1],(i,vals)
    assert vals[2]==EXPECTED_MULTS[i-1],(i,vals)
    out.append(vals)

print('VERIFY_OK f=12,42,28 H1_F2_dim=4 missing3=' + ','.join(str(x[1]) for x in out) +
      ' class_mults=' + ';'.join('+'.join(map(str,x[2])) for x in out) +
      ' all_missing3_nonzero=yes')
