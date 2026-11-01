#!/usr/bin/env python3
"""Exact finite certificate for the vertex-induced forest filtration of KG(5,2).

Run: python3 verify_petersen_forest.py
Only Python's standard library is required. All masks, incidences and integer
cancellations are reconstructed rather than loaded from a table.
"""
from collections import Counter, defaultdict
from itertools import combinations
import json

PAIRS=list(combinations(range(5),2))
N=len(PAIRS)
EDGES=[(u,v) for u in range(N) for v in range(u+1,N)
       if set(PAIRS[u]).isdisjoint(PAIRS[v])]
ADJ=[0]*N
for u,v in EDGES:
    ADJ[u]|=1<<v
    ADJ[v]|=1<<u
assert N==10 and len(EDGES)==15
assert all(x.bit_count()==3 for x in ADJ)
assert all((ADJ[u]&ADJ[v]).bit_count()==(0 if (ADJ[u]>>v)&1 else 1)
           for u,v in combinations(range(N),2))


def face_union_find(mask, bound):
    vertices=[i for i in range(N) if mask>>i&1]
    if any((ADJ[i]&mask).bit_count()>bound for i in vertices):return False
    parent=list(range(N))
    def root(i):
        while parent[i]!=i:i=parent[i]
        return i
    for u,v in EDGES:
        if (mask>>u)&1 and (mask>>v)&1:
            a,b=root(u),root(v)
            if a==b:return False
            parent[a]=b
    return True


def face_dfs(mask,bound):
    """Independent verification: count edges and connected components."""
    verts={i for i in range(N) if mask>>i&1}
    selected_edges=[(u,v) for u,v in EDGES if u in verts and v in verts]
    deg=Counter()
    subadj={u:set() for u in verts}
    for u,v in selected_edges:
        deg[u]+=1;deg[v]+=1
        subadj[u].add(v);subadj[v].add(u)
    if any(deg[v]>bound for v in verts):return False
    remaining=set(verts);components=0
    while remaining:
        components+=1
        stack=[remaining.pop()]
        while stack:
            u=stack.pop()
            newly=subadj[u]&remaining
            remaining.difference_update(newly)
            stack.extend(newly)
    return len(selected_edges)==len(verts)-components


def toggle_matching(faces,order):
    unmatched=set(faces)-{0}; pairs=[]
    for v in order:
        bit=1<<v
        for a in sorted(tuple(unmatched),key=lambda x:(x.bit_count(),x)):
            b=a|bit
            if not a&bit and a in unmatched and b in unmatched:
                unmatched.remove(a);unmatched.remove(b)
                pairs.append((a,b))
    return pairs,unmatched


def hasse_acyclic(faces,pairs):
    """Fully test directed Hasse incidences: matched up, others down."""
    nonempty=set(faces)-{0}
    index={s:i for i,s in enumerate(sorted(nonempty))}
    output=[[] for _ in index];indegree=[0]*len(index)
    matched=set(pairs);arcs=0
    for hi in nonempty:
        for v in range(N):
            if (hi>>v)&1:
                lo=hi^(1<<v)
                if lo not in nonempty:continue
                a,b=(lo,hi) if (lo,hi) in matched else (hi,lo)
                output[index[a]].append(index[b]);indegree[index[b]]+=1
                arcs+=1
    todo=[i for i,d in enumerate(indegree) if d==0];visited=0
    while todo:
        u=todo.pop();visited+=1
        for v in output[u]:
            indegree[v]-=1
            if indegree[v]==0:todo.append(v)
    assert visited==len(nonempty),(visited,len(nonempty))
    return arcs


def signed_morse_boundary(faces,pairs):
    """Perform exact integer unit-pivot algebraic Morse cancellations."""
    remaining=set(faces)-{0}
    boundary={}
    for s in remaining:
        boundary[s]={s^(1<<v):(-1)**((s&((1<<v)-1)).bit_count())
                      for v in range(N) if (s>>v)&1 and (s^(1<<v)) in remaining}
    for lo,hi in pairs:
        coeff=boundary[hi].get(lo,0)
        assert abs(coeff)==1,('nonunit',lo,hi,coeff)
        row={r:a for r,a in boundary[hi].items() if r!=lo}
        upper=[(t,boundary[t][lo]) for t in remaining
               if t!=hi and t.bit_count()==hi.bit_count() and lo in boundary[t]]
        for t,c in upper:
            for r,a in row.items():
                boundary[t][r]=boundary[t].get(r,0)-c*a*coeff
                if boundary[t][r]==0: del boundary[t][r]
            del boundary[t][lo]
        for t in remaining:
            boundary[t].pop(hi,None)
            boundary[t].pop(lo,None)
        del boundary[lo];del boundary[hi]
        remaining.remove(lo);remaining.remove(hi)
    return boundary


def mod2_betti(faces):
    bydim=defaultdict(list)
    for s in sorted(faces):
        if s:bydim[s.bit_count()-1].append(s)
    ranks={}
    for k in range(1,max(bydim)+1):
        idx={s:i for i,s in enumerate(bydim[k-1])}
        pivot={}
        for hi in bydim[k]:
            col=0
            for v in range(N):
                if hi>>v&1:col^=1<<idx[hi^(1<<v)]
            while col:
                r=col.bit_length()-1
                if r not in pivot:
                    pivot[r]=col;break
                col^=pivot[r]
        ranks[k]=len(pivot)
    betti={k:len(v)-ranks.get(k,0)-ranks.get(k+1,0)
           for k,v in bydim.items()}
    betti[0]-=1 # reduced H_0, the complex is connected
    return {k:v for k,v in betti.items() if v},ranks


def main():
    bounds=[0,1,2,3]
    families=[];records=[]
    for d in bounds:
        F={s for s in range(1<<N) if face_union_find(s,d)}
        assert F=={s for s in range(1<<N) if face_dfs(s,d)}
        families.append(F)
        order=list(reversed(range(N))) if d==2 else list(range(N))
        matching,critical=toggle_matching(F,order)
        arcs=hasse_acyclic(F,matching)
        B=signed_morse_boundary(F,matching)
        assert set(B)==critical
        assert all(not col for col in B.values())
        expected={0:{0:1,2:4},1:{0:1,3:1},2:{0:1,3:1},3:{0:1,5:6}}[d]
        crits=dict(sorted(Counter(x.bit_count()-1 for x in critical).items()))
        assert crits==expected,(d,crits)
        mod2,ranks=mod2_betti(F)
        assert mod2=={k:v for k,v in expected.items() if k>0}
        facets=[s for s in F if not any(s|1<<i in F for i in range(N) if not (s>>i)&1)]
        count=dict(sorted(Counter(s.bit_count()-1 for s in F).items()))
        facet_dims=dict(sorted(Counter(s.bit_count()-1 for s in facets).items()))
        records.append({'d':d,'face_count_including_empty':len(F),
          'face_counts_by_dimension':count,'facet_dimensions':facet_dims,
          'morse_pairs':len(matching),'hasse_arcs':arcs,
          'critical_cells_by_dimension':crits,'mod2_reduced_betti':mod2,
          'mod2_boundary_ranks':ranks})
    assert families[0]<families[1]<families[2]<families[3]
    assert len(families[2]-families[1])==360
    # The third higher-independence complex restricts component cardinality,
    # not maximum degree; it is strictly smaller than the linear-forest stage.
    ind3=set()
    for mask in range(1<<N):
        remaining={v for v in range(N) if mask>>v&1}
        acceptable=True
        while remaining:
            start=remaining.pop(); stack=[start]; component_size=0
            while stack:
                u=stack.pop(); component_size+=1
                nxt={v for v in remaining if ADJ[u]>>v&1}
                remaining.difference_update(nxt);stack.extend(nxt)
            if component_size>3:
                acceptable=False;break
        if acceptable:ind3.add(mask)
    assert len(ind3)==381 and ind3<families[2]
    assert len(families[2]-ind3)==240
    relative=families[2]-families[1]
    matching,critical=toggle_matching(relative,range(N))
    arcs=hasse_acyclic(relative,matching)
    B=signed_morse_boundary(relative,matching)
    lower=[s for s in critical if s.bit_count()==4]
    upper=[s for s in critical if s.bit_count()==5]
    assert len(lower)==len(upper)==1
    boundary_coefficient=B[upper[0]][lower[0]]
    assert abs(boundary_coefficient)==1
    relative_record={'new_faces':len(relative),'morse_pairs':len(matching),
      'hasse_arcs':arcs,'critical_3_simplex_mask':lower[0],
      'critical_4_simplex_mask':upper[0],
      'integral_boundary_coefficient':boundary_coefficient,
      'relative_homology_zero':True}
    print(json.dumps({'graph':'KG(5,2)','stages':records,'relative_F2_over_F1':relative_record,
                      'integral_homotopy':'F0 = wedge_4 S2; F1 = F2 = S3; F3 = F_infty = wedge_6 S5',
                      'F1_to_F2_homotopy_equivalence':True,
                      'induced_component_size_three_faces':len(ind3),
                      'F2_extra_faces_over_Ind3':len(families[2]-ind3),
                      'verification':'PETERSEN_FOREST_FILTRATION_EXACT_INTEGRAL_MORSE_OK'},
                     sort_keys=True,indent=2))
if __name__=='__main__':main()
