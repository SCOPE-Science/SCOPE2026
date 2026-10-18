#!/usr/bin/env python3
"""Complete reproducible face, discrete Morse, and homology check for a finite multipath complex."""
import collections
from functools import lru_cache

V=range(6)
ARCS=tuple((u,v) for u in V for v in V if (u<3)!=(v<3))
ORDER=(12,0,17,11,16,14,10,13,5,15,7,4,8,9,3,6,2,1)

def good(mask):
    succ={}; targets=set()
    for i,(u,v) in enumerate(ARCS):
        if mask>>i&1:
            if u in succ or v in targets: return False
            succ[u]=v;targets.add(v)
    for u in succ:
        visited=set();w=u
        while w in succ:
            if w in visited:return False
            visited.add(w);w=succ[w]
    return True

def incidence(mask):
    bits=[1<<i for i in range(len(ARCS)) if mask&(1<<i)]
    return [(mask^v,(-1 if i%2 else 1)) for i,v in enumerate(bits)]

def main():
    faces={m for m in range(1,1<<len(ARCS)) if good(m)}
    assert len(ARCS)==18 and len(faces)==714
    sizes=collections.Counter(m.bit_count()-1 for m in faces)
    assert sizes=={0:18,1:108,2:264,3:252,4:72},sizes
    unmatched=set(faces)
    matched_lower={};matched_upper={}
    for i in ORDER:
        bit=1<<i
        # Sort for reproducibility but pairing set is independent of order
        for lower in sorted(unmatched):
            upper=lower|bit
            if lower&bit==0 and upper in unmatched:
                unmatched.remove(lower);unmatched.remove(upper)
                matched_lower[lower]=upper
                matched_upper[upper]=lower
    critical=sorted(unmatched)
    counts=collections.Counter(m.bit_count()-1 for m in critical)
    assert counts=={0:1,3:19,4:12},counts
    assert len(matched_lower)==341
    # Hasse DAG: unmatched cofaces point down and matched cover arrows reverse.
    outdegree=collections.Counter();adj={m:[] for m in faces}
    indegree={m:0 for m in faces};covers=0
    for upper in faces:
        if upper.bit_count()==1:continue
        for lower,coeff in incidence(upper):
            covers+=1
            if matched_upper.get(upper)==lower:u,v=lower,upper
            else:u,v=upper,lower
            adj[u].append(v);indegree[v]+=1
    queue=collections.deque(m for m,d in indegree.items() if d==0)
    visited=0
    while queue:
        u=queue.popleft();visited+=1
        for v in adj[u]:
            indegree[v]-=1
            if indegree[v]==0:queue.append(v)
    assert visited==len(faces),(visited,len(faces))
    # Algebraic Morse projection using the actual signed incidence relations.
    @lru_cache(None)
    def projection(s):
        if s in unmatched:return {s:1}
        if s in matched_upper:return {}
        upper=matched_lower[s]
        signed=dict(incidence(upper)); unit=signed[s]
        out=collections.defaultdict(int)
        for lower,coeff in signed.items():
            if lower==s:continue
            for k,v in projection(lower).items():out[k]-=unit*coeff*v
        return {k:v for k,v in out.items() if v}
    # Only critical four-cell boundaries may land in critical degree 3.
    crit4=[s for s in critical if s.bit_count()==5]
    differential={}
    for c in crit4:
        bd=collections.defaultdict(int)
        for s,coeff in incidence(c):
            for z,v in projection(s).items():bd[z]+=coeff*v
        differential[c]={z:v for z,v in bd.items() if v}
    assert all(not vals for vals in differential.values()),differential
    # Independent F_2 boundary ranks for every simplicial degree.
    fbydim=collections.defaultdict(list)
    for f in sorted(faces):fbydim[f.bit_count()-1].append(f)
    ranks={}
    for k in range(1,5):
        index={s:i for i,s in enumerate(fbydim[k-1])}
        basis={}
        for f in fbydim[k]:
            col=0
            for s,_ in incidence(f):col^=1<<index[s]
            while col:
                pivot=col.bit_length()-1
                if pivot in basis:col^=basis[pivot]
                else:basis[pivot]=col;break
        ranks[k]=len(basis)
    betti={k:len(fbydim[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in range(5)}
    assert betti=={0:1,1:0,2:0,3:19,4:12},betti
    print('arc_order=',ARCS)
    print('faces_by_dim=',dict(sorted(sizes.items())))
    print('total_nonempty_faces=',len(faces))
    print('cover_relations=',covers,'dag_vertices_visited=',visited)
    print('matching_pairs=',len(matched_lower))
    print('critical_by_dim=',dict(sorted(counts.items())))
    print('critical_4_to_3_integral_boundary_nonzero_entries=',sum(len(x) for x in differential.values()))
    print('mod2_boundary_ranks=',ranks)
    print('mod2_betti=',betti)
    print('reduced_integral_homotopy_type= wedge(19 S^3, 12 S^4)')

if __name__=='__main__':main()
