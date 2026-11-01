#!/usr/bin/env python3
"""Standalone exact checker for the cuboctahedral perfect-matching complex.
All computations are finite integer/bitset operations, no dependencies.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import permutations, product
import json

def graph():
    cube_edges=sorted((u,v) for u in range(8) for v in range(u+1,8) if (u^v).bit_count()==1)
    assert len(cube_edges)==12
    line_edges=[(i,j) for i,a in enumerate(cube_edges) for j,b in enumerate(cube_edges) if i<j and (set(a)&set(b))]
    assert len(line_edges)==24
    return cube_edges,line_edges

def facets(E):
    adj=[[] for _ in range(12)]
    for i,(u,v) in enumerate(E):adj[u].append((v,i));adj[v].append((u,i))
    def rec(covered,matching):
        if covered == (1<<12)-1:
            yield matching;return
        u=next(k for k in range(12) if not covered>>k&1)
        for v,i in adj[u]:
            if not covered>>v&1:yield from rec(covered|1<<u|1<<v,matching|1<<i)
    return sorted(set(rec(0,0)))

def boundary(s):
    pos=0
    while s:
        bit=s&-s
        yield bit,(-1 if pos&1 else 1)
        s-=bit;pos+=1

def mod2_rank(columns):
    piv={}
    for col in columns:
        while col:
            k=col.bit_length()-1
            if k not in piv:
                piv[k]=col;break
            col ^= piv[k]
    return len(piv)

def automorphism_table(cube_edges,line_edges,faces):
    cube_edge_id={edge:i for i,edge in enumerate(cube_edges)}
    line_edge_id={edge:i for i,edge in enumerate(line_edges)}
    # Signed permutation cycles classify B3 conjugacy types (positive and negative cycles).
    character={}
    for perm in permutations(range(3)):
        for t in range(8):
            def map_vertex(v):
                out=t
                for k in range(3):
                    if v>>k&1:out ^= (1<<perm[k])
                return out
            cube_perm=[]
            for u,v in cube_edges:
                cube_perm.append(cube_edge_id[tuple(sorted((map_vertex(u),map_vertex(v))))])
            line_perm=[]
            for a,b in line_edges:
                line_perm.append(line_edge_id[tuple(sorted((cube_perm[a],cube_perm[b])) )])
            assert sorted(line_perm)==list(range(24))
            # Signed cycle decomposition of (t,perm) on coordinate directions.
            unvisited=set(range(3));pos=[];neg=[]
            while unvisited:
                j=min(unvisited);orbit=[];k=j
                while k not in orbit:
                    orbit.append(k);unvisited.discard(k);k=perm[k]
                assert k==j
                parity=sum(t>>a&1 for a in orbit)%2
                (neg if parity else pos).append(len(orbit))
            ct=(tuple(sorted(pos)),tuple(sorted(neg)))
            # Signed simplicial Lefschetz character on H2: reduced chain Euler trace.
            trace= -1 # reduced correction = -1 for the empty simplex in ordinary chain computation
            for s in faces:
                if not s:continue
                mapped=0;seq=[]
                for i in range(24):
                    if s>>i&1:
                        j=line_perm[i];mapped|=1<<j;seq.append(j)
                assert mapped in faces
                if mapped!=s:continue
                inversions=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
                sign= -1 if inversions%2 else 1
                trace+=((-1)**(len(seq)-1))*sign
            if ct in character:
                assert character[ct][0]==trace, (ct,trace,character[ct])
                character[ct][1]+=1
            else:character[ct]=[trace,1]
    assert sum(n for _,n in character.values())==48
    assert len(character)==10
    assert character[((1,1,1),())][0]==43
    invariants=sum(tr*n for tr,n in character.values())
    assert invariants % 48 == 0,(invariants,character)
    return character,invariants//48

def verify():
    cube_edges,E=graph();F=facets(E)
    assert len(F)==32 and all(f.bit_count()==6 for f in F)
    faces={0}
    for f in F:
        s=f
        while s:
            faces.add(s);s=(s-1)&f
    assert len(faces)==1429
    fv=Counter(s.bit_count()-1 for s in faces if s)
    # Independent verification: an edge set is extendable iff a residual perfect matching exists.
    adj=[[] for _ in range(12)]
    for i,(u,v) in enumerate(E):adj[u].append(v);adj[v].append(u)
    @lru_cache(None)
    def complete(uncovered):
        if not uncovered:return True
        u=next(v for v in range(12) if uncovered>>v&1)
        return any((uncovered>>w&1) and complete(uncovered^(1<<u)^(1<<w)) for w in adj[u])
    for s in faces:
        covered=0
        for i,(u,v) in enumerate(E):
            if s>>i&1:
                assert not (covered>>u&1 or covered>>v&1)
                covered|=(1<<u)|(1<<v)
        assert complete(((1<<12)-1)^covered)
    # Sequential element matchings and exact full Hasse DAG.
    remaining=set(faces);up={}
    for i in range(24):
        pairs=[(s,s|(1<<i)) for s in remaining if not s>>i&1 and (s|(1<<i)) in remaining]
        for low,high in pairs:
            remaining.remove(low);remaining.remove(high);up[low]=high
    assert len(up)==693
    assert Counter(s.bit_count()-1 for s in remaining)==Counter({2:43})
    assert 0 not in remaining
    indegree={s:0 for s in faces};out=defaultdict(list);inc=0
    for s in faces:
        for bit,_ in boundary(s):
            if not s:continue
            low=s^bit
            if up.get(low)==s:a,b=low,s
            else:a,b=s,low
            out[a].append(b);indegree[b]+=1;inc+=1
    q=deque(s for s,d in indegree.items() if d==0);visited=0
    while q:
        s=q.popleft();visited+=1
        for h in out[s]:
            indegree[h]-=1
            if indegree[h]==0:q.append(h)
    assert visited==len(faces)
    # Entire uncompressed simplicial chain mod 2, independent of Morse matching.
    ranks={};levels={k:[s for s in faces if s.bit_count()==k] for k in range(1,7)}
    for k in range(2,7):
        low={s:i for i,s in enumerate(levels[k-1])}
        columns=[]
        for s in levels[k]:
            vec=0
            for bit,_ in boundary(s):vec|=1<<low[s^bit]
            columns.append(vec)
        ranks[k-1]=mod2_rank(columns)
    betti={d:len(levels[d+1])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(6)}
    betti[0]-=1
    assert betti=={0:0,1:0,2:43,3:0,4:0,5:0},(ranks,betti)
    chars,invariant=automorphism_table(cube_edges,E,faces)
    report={
     'graph':'line graph L(Q3) of 3-cube (cuboctahedral graph)',
     'vertices':12,'edges':24,'perfect_matching_facets':len(F),
     'nonempty_faces':len(faces)-1,'f_vector':[fv[i] for i in range(6)],
     'morse_pairs':len(up),'critical_2_cells':43,'other_critical_cells':0,
     'directed_hasse_vertices':visited,'directed_hasse_incidences':inc,'acyclic':True,
     'independent_mod2_ranks':{str(k):v for k,v in sorted(ranks.items())},
     'independent_reduced_mod2_betti':{str(k):v for k,v in betti.items() if v},
     'symmetry_group':'Aut(Q3)=(Z/2)^3 semidirect S3',
     'symmetry_order':48,
     'homology_character_by_signed_coordinate_cycle_type':[
       {'positive_cycles':list(p),'negative_cycles':list(n),'character_H2':tr,'group_elements':mult}
       for (p,n),(tr,mult) in sorted(chars.items())],
     'symmetry_invariant_dimension':invariant,
     'integral_homotopy_type':'wedge of 43 two-spheres','result':'PASS'
    }
    print(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2))
    return report
if __name__=='__main__':verify()
