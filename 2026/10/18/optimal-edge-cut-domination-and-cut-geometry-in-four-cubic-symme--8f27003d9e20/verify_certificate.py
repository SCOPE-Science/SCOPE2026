#!/usr/bin/env python3
"""Check finite edge-cut-domination and automorphism certificates using Python stdlib."""
import collections, itertools, json, pathlib, re
HERE=pathlib.Path(__file__).resolve().parent
cert=json.loads((HERE/'certificate.json').read_text(encoding='utf-8'))
assert cert['schema_version']==1
raw=(HERE/'bruteforce.out').read_text(encoding='utf-8').splitlines()
part=(HERE/'partition.out').read_text(encoding='utf-8').splitlines()
for name,g in cert['graphs'].items():
    n=g['vertices'];edges=[tuple(z) for z in g['edges']];m=len(edges);k=g['minimum_edge_cut_dominating_size']
    assert sorted(set(tuple(sorted(z)) for z in edges))==sorted(tuple(sorted(z)) for z in edges)
    assert len(set(sum(([u,v] for u,v in edges),[])))==n
    adj=[set() for _ in range(n)]
    for u,v in edges:
        assert u!=v and 0<=u<n and 0<=v<n
        adj[u].add(v);adj[v].add(u)
    assert all(len(row)==3 for row in adj)
    def describe(mask):
        assert 0<=mask<(1<<m)
        touch=set()
        for i,(u,v) in enumerate(edges):
            if mask>>i&1:touch.update((u,v))
        dominated=all(u in touch or v in touch for u,v in edges)
        residual=[set() for _ in range(n)]
        for i,(u,v) in enumerate(edges):
            if not(mask>>i&1):residual[u].add(v);residual[v].add(u)
        components=[];seen=set()
        for j in range(n):
            if j in seen:continue
            q=[j];seen.add(j)
            for u in q:
                for v in residual[u]:
                    if v not in seen:seen.add(v);q.append(v)
            components.append(set(q))
        return dominated,sorted(components,key=lambda x:(len(x),min(x)))
    masks=g['minimum_edge_cut_dominating_masks']
    assert len(masks)==len(set(masks)) and masks==sorted(masks)
    for mask in masks:
        dom,components=describe(mask)
        assert mask.bit_count()==k and dom and len(components)==2
    orbit_seen=[];summ=[]
    edge_dict={frozenset((u,v)):i for i,(u,v) in enumerate(edges)}
    for orbit in g['orbits']:
        representative=orbit['representative_mask']; assert representative in masks
        target_shape=orbit['residual_component_sizes']
        crossing=orbit['crossing_edges']
        witnesses=orbit['witnesses'];seen=set()
        for w in witnesses:
            t=w['mask'];perm=w['vertex_permutation']
            assert t in masks and len(perm)==n and sorted(perm)==list(range(n))
            image=[edge_dict[frozenset((perm[u],perm[v]))] for u,v in edges]
            assert len(set(image))==m  # The permutation preserves every adjacency.
            mapped=sum(1<<image[i] for i in range(m) if representative>>i&1)
            assert t==mapped
            _,comps=describe(t)
            sizes=[len(z) for z in comps]
            assert sizes==target_shape
            delta=sum(1 for u,v in edges if (u in comps[0])!=(v in comps[0]))
            assert delta in crossing
            assert t not in seen;seen.add(t)
        assert seen
        orbit_seen.extend(seen)
        summ.append((target_shape,len(seen)))
    assert sorted(orbit_seen)==masks  # No overlaps and no missing orbit representatives.
    # Verify all direct-enumeration counts, including zero at every smaller level.
    idx=raw.index(f'GRAPH {name} {n} {m}')
    level_lines=[]
    for z in raw[idx+1:]:
        if z.startswith('GRAPH '):break
        if z.startswith('LEVEL '):level_lines.append(z)
    assert set(int(z.split()[1]) for z in level_lines)==set(range(1,k+1))
    for z in level_lines:
        _,lev,total,domcount,cutcount,both= z.split()
        expected=g['levels_through_minimum'][lev]
        assert (int(total),int(domcount),int(cutcount),int(both)) == tuple(expected[x] for x in ('total','edge_dominating','edge_cuts','edge_cut_dominating'))
        assert int(total)==__import__('math').comb(m,int(lev))
        assert int(both)==(len(masks) if int(lev)==k else 0)
    direct=set(map(int,raw[next(i for i in range(idx+1,len(raw)) if raw[i].startswith('SETS'))].split()[1:]))
    assert direct==set(masks)
    # The second verifier enumerates vertex partitions first, with alternate edge ordering
    # for the two generalized Petersen representations. Normalize by unordered endpoints.
    li=next(i for i,z in enumerate(part) if z.startswith(name+' '));summary=part[li]
    assert summary==f'{name} count_previous=0 count_min={len(masks)}'
    alt=list(map(int,part[li+1].split()[1:]))
    if name in ('MobiusKantor','Desargues'):
        N=8 if name=='MobiusKantor' else 10
        alt_edges=[]
        for i in range(N):alt_edges.extend([(i,(i+1)%N),(N+i,N+(i+3)%N),(i,N+i)])
        translation=[edge_dict[frozenset(e)] for e in alt_edges]
    else:translation=list(range(m))
    converted=set(sum(1<<translation[i] for i in range(m) if z>>i&1) for z in alt)
    assert converted==set(masks)
    print(name,':',len(masks),'minimum sets, k=',k,'orbits=',summ,'independent enumerations agree')
print('VERIFIED: all four complete optimum families, lower bounds, cut profiles and automorphism witnesses')
