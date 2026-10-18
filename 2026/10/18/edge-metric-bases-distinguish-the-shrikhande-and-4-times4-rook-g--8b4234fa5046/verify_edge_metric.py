#!/usr/bin/env python3
"""Exact edge-metric basis and exchange-graph census for two 16-vertex graphs.

Uses only the Python standard library. Vertex (a,b) has label 4*a+b.
A landmark v distinguishes edges e,f when min distance(v,e) differs.
"""
from collections import Counter, deque
from itertools import combinations, permutations, product

V = tuple(range(16))
DIFFERENCES = {(1,0), (3,0), (0,1), (0,3), (1,1), (3,3)}


def coords(v):
    return divmod(v, 4)


def label(a,b):
    return 4*(a%4)+(b%4)


def build_graph(which):
    adj = [set() for _ in V]
    for u in V:
        a,b=coords(u)
        for v in V:
            if u==v: continue
            c,d=coords(v)
            if which=='Shrikhande':
                yes=((c-a)%4, (d-b)%4) in DIFFERENCES
            else:
                yes=a==c or b==d
            if yes:adj[u].add(v)
    assert all(len(a)==6 for a in adj)
    assert all(u in adj[v] for u in V for v in adj[u])
    edges=tuple((u,v) for u in V for v in sorted(adj[u]) if u<v)
    assert len(edges)==48
    return adj,edges


def distance_matrix(adj):
    ds=[]
    for v in V:
        d=[-1]*16
        d[v]=0
        Q=deque([v])
        while Q:
            x=Q.popleft()
            for y in adj[x]:
                if d[y]<0:d[y]=d[x]+1;Q.append(y)
        assert sorted(Counter(d).items())==[(0,1),(1,6),(2,9)]
        ds.append(d)
    return ds


def edge_distances(ds,edges):
    return tuple(tuple(min(ds[v][a],ds[v][b]) for a,b in edges) for v in V)


def pair_witness_masks(E):
    return tuple(sum(1<<v for v in V if E[v][i]!=E[v][j])
                 for i in range(48) for j in range(i+1,48))


def resolvable_via_signatures(landmarks,E):
    signatures={tuple(E[v][i] for v in landmarks) for i in range(48)}
    return len(signatures)==48


def bases_from_two_tests(E):
    pairmasks=pair_witness_masks(E)
    assert len(pairmasks)==1128 and all(pairmasks)
    # Independently inspect edge signatures and intersect every pair-separator.
    for k in range(1,17):
        ok=[]
        for S in combinations(V,k):
            mask=sum(1<<v for v in S)
            a=resolvable_via_signatures(S,E)
            b=all(mask & pm for pm in pairmasks)
            assert a==b, ('independent-resolution-disagreement', k, S)
            if a:ok.append(mask)
        if ok:
            return k,tuple(ok)
    raise AssertionError('No edge metric basis')


def shrinkhande_automorphisms(adj):
    # All invertible Z4-linear maps preserving the six Cayley generators,
    # composed with every translation. Exactly 16*12 maps.
    maps=[]
    for a,b,c,d in product(range(4),repeat=4):
        if (a*d-b*c)%2!=1:continue
        transformed={((a*x+b*y)%4,(c*x+d*y)%4) for x,y in DIFFERENCES}
        if transformed!=DIFFERENCES:continue
        maps.extend(tuple(label(a*x+b*y+p,c*x+d*y+q)
                          for x,y in map(coords,V))
                    for p,q in product(range(4),repeat=2))
    assert len(maps)==len(set(maps))==192
    for perm in maps:
        assert all(perm[v] in adj[perm[u]] for u in V for v in adj[u])
    # For every nonneighbor w of 0, N(0) cap N(w) gives a unique pair.
    # The six neighbors of 0 form C6. Thus automorphisms fixing 0
    # act faithfully on an induced six-cycle (at most 12 choices).
    around=adj[0]
    assert all(sum(int(z in adj[w]) for z in around)==2
               for w in V if w!=0 and w not in around)
    profiles=[frozenset(around & adj[w]) for w in V
              if w!=0 and w not in around]
    assert len(profiles)==len(set(profiles))==9
    assert len(around)==6 and all(len(adj[v] & around)==2 for v in around)
    seen={next(iter(around))}
    frontier=list(seen)
    while frontier:
        z=frontier.pop()
        for w in (adj[z] & around)-seen:
            seen.add(w);frontier.append(w)
    assert len(seen)==6  # Connected 2-regular graph on 6 vertices is C6.
    return maps


def rook_automorphisms(adj):
    maps=[]
    ps=list(permutations(range(4)))
    for p,q,t in product(ps,ps,(0,1)):
        maps.append(tuple(label(*( (p[b],q[a]) if t else (p[a],q[b]) ))
                          for a,b in map(coords,V)))
    assert len(maps)==len(set(maps))==1152
    for perm in maps:
        assert all(perm[v] in adj[perm[u]] for u in V for v in adj[u])
    # N(0) consists of two disjoint triangles; each nonneighbor is
    # determined by its pair of neighbors in N(0). Stabilizer <= 72.
    around=adj[0]
    induced={v:frozenset(adj[v]&around) for v in around}
    assert sorted(Counter(len(a) for a in induced.values()).items())==[(2,6)]
    components=[]
    unseen=set(around)
    while unseen:
        root=next(iter(unseen)); comp={root};todo=[root];unseen.remove(root)
        while todo:
            a=todo.pop()
            for b in induced[a] & unseen:
                unseen.remove(b);comp.add(b);todo.append(b)
        components.append(comp)
    assert sorted(map(len,components))==[3,3]
    profiles=[frozenset(around&adj[w]) for w in V
              if w!=0 and w not in around]
    assert len(profiles)==len(set(profiles))==9
    return maps


def orbits(bases,autos):
    B=set(bases);rem=set(B);sizes=[];reps=[]
    while rem:
        x=min(rem)
        orbit={sum(1<<p[v] for v in V if x>>v&1) for p in autos}
        assert orbit <= B
        assert orbit <= rem
        rem.difference_update(orbit)
        sizes.append(len(orbit));reps.append((len(orbit),x))
    return sorted(sizes),sorted(reps)


def exchange_structure(bases):
    B=set(bases)
    adjacency={x:set() for x in B}
    for x in B:
        ones=[v for v in V if x>>v&1]
        zeros=[v for v in V if not(x>>v&1)]
        for v in ones:
            for w in zeros:
                y=x^(1<<v)^(1<<w)
                if y in B:adjacency[x].add(y)
    assert all(x in adjacency[y] for y in B for x in adjacency[y])
    degrees=Counter(len(neighbors) for neighbors in adjacency.values())
    n_edges=sum(d*cnt for d,cnt in degrees.items())//2
    rem=set(B);components=[]
    while rem:
        x=min(rem)
        seen={x};queue=[x];rem.remove(x)
        while queue:
            u=queue.pop()
            for y in adjacency[u] - seen:
                seen.add(y);queue.append(y);rem.remove(y)
        components.append(len(seen))
    return n_edges,dict(sorted(degrees.items())),sorted(components)


def vertex_metric_bases(ds):
    # Contextual check: these cospectral graphs also share ordinary dim 4.
    for k in range(1,17):
        good=0
        for S in combinations(V,k):
            code={tuple(ds[v][u] for v in S) for u in V}
            good += len(code)==16
        if good:return k,good
    raise AssertionError('No vertex metric basis')


def main():
    expect={
     'Shrikhande':(6,736,4128,{6:64,10:192,11:192,13:192,14:96},[736],
                    [48,48,64,96,96,192,192]),
     'Rook':(5,576,3744,{13:576},[576],[576])
    }
    for name in ('Shrikhande','Rook'):
        adj,edges=build_graph(name)
        # Both examples have exactly the same (16,6,2,2) parameters.
        for a in V:
            for b in V:
                if a!=b:
                    assert len(adj[a] & adj[b])==2
        D=distance_matrix(adj)
        E=edge_distances(D,edges)
        k,B=bases_from_two_tests(E)
        n_edges,degrees,components=exchange_structure(B)
        autos=shrinkhande_automorphisms(adj) if name=='Shrikhande' else rook_automorphisms(adj)
        orbit_sizes,representatives=orbits(B,autos)
        computed=(k,len(B),n_edges,degrees,components,orbit_sizes)
        assert computed==expect[name], (name, computed)
        assert vertex_metric_bases(D)==({'Shrikhande':(4,48),'Rook':(4,144)}[name])
        rep_expect={'Shrikhande':[(48,0x30f),(48,0x70b),(64,0x114b),
                 (96,0x36c),(96,0x116c),(192,0x32e),(192,0x34b)],
                    'Rook':[(576,0x13c)]}
        assert representatives==rep_expect[name], (name,representatives)
        print('VERIFY_OK',name,computed,'reps',[(n,hex(v)) for n,v in representatives])

if __name__=='__main__':main()
