#!/usr/bin/env python3
"""Independent finite reconstruction of a eight-cycle strong-matching complex.

Only the standard library is required. Each vector-field vertex is an
incidence (vertex,edge) of the eight-cycle. A permutation of graph vertices
produces the strong vertex-filtration matching by pairing a vertex to its
unique earlier incident edge, if exactly one neighbor is earlier.
"""
import collections
import functools
import itertools

N=8
EDGES=tuple(tuple(sorted((i,(i+1)%N))) for i in range(N))
INCIDENCES=tuple((v,i) for i,e in enumerate(EDGES) for v in e)
INDEX={inc:i for i,inc in enumerate(INCIDENCES)}


def build_complex():
    generated=set()
    for order in itertools.permutations(range(N)):
        preceding=set()
        mask=0
        for v in order:
            older=[u for u in ((v-1)%N,(v+1)%N) if u in preceding]
            if len(older)==1:
                edge_idx=EDGES.index(tuple(sorted((v,older[0]))))
                mask |= 1<<INDEX[(v,edge_idx)]
            preceding.add(v)
        generated.add(mask)
    faces={0}
    for top in generated:
        sub=top
        while sub:
            faces.add(sub)
            sub=(sub-1)&top
    return generated,faces


def match_faces(faces):
    remaining=faces-{0}
    pairs=[]
    for pivot in range(len(INCIDENCES)):
        for lower in sorted(tuple(remaining),key=lambda m:(m.bit_count(),m)):
            if lower not in remaining or ((lower>>pivot)&1):
                continue
            upper=lower|(1<<pivot)
            if upper in remaining:
                remaining.remove(lower)
                remaining.remove(upper)
                pairs.append((lower,upper))
    return remaining,pairs


def verify_acyclicity(faces,pairs):
    nodes=faces-{0}
    upper_to_lower={high:low for low,high in pairs}
    arrows=collections.defaultdict(list)
    indegree=collections.Counter()
    incidence_count=0
    for upper in nodes:
        for j in range(len(INCIDENCES)):
            if not ((upper>>j)&1):
                continue
            lower=upper^(1<<j)
            if lower==0:
                continue
            assert lower in nodes
            incidence_count+=1
            if upper_to_lower.get(upper)==lower:
                a,b=lower,upper
            else:
                a,b=upper,lower
            arrows[a].append(b)
            indegree[b]+=1
    queue=collections.deque(x for x in nodes if indegree[x]==0)
    visited=0
    while queue:
        a=queue.popleft()
        visited+=1
        for b in arrows[a]:
            indegree[b]-=1
            if indegree[b]==0:
                queue.append(b)
    assert visited==len(nodes), (visited,len(nodes))
    return incidence_count


def mod_p_rank(columns,p):
    pivots={}
    rank=0
    for col in columns:
        while col:
            i=max(col)
            if i not in pivots:
                inv=pow(col[i],-1,p)
                pivots[i]={j:(v*inv)%p for j,v in col.items() if v%p}
                rank+=1
                break
            q=pivots[i]
            fac=col[i]
            for j,v in q.items():
                nv=(col.get(j,0)-fac*v)%p
                if nv:col[j]=nv
                else:col.pop(j,None)
    return rank


def verify_field_homology(faces):
    chain={k:sorted(x for x in faces if x and x.bit_count()==k+1) for k in range(6)}
    for p in (2,3,5):
        ranks={}
        for d in range(1,6):
            lower_index={f:i for i,f in enumerate(chain[d-1])}
            columns=[]
            for x in chain[d]:
                vertices=[j for j in range(len(INCIDENCES)) if (x>>j)&1]
                columns.append({lower_index[x^(1<<j)]:(-1)**i%p for i,j in enumerate(vertices)})
            ranks[d]=mod_p_rank(columns,p)
        betti={d:len(chain[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(6)}
        assert betti=={0:1,1:0,2:0,3:5,4:0,5:0},(p,betti)


def verify_word_criterion(faces):
    # A separate local characterization: opposite signs cannot be adjacent;
    # single-sign selections need two successive unmatched vertices so an
    # opposite edge orientation can break the directed cycle.
    for mask in range(1<<len(INCIDENCES)):
        signs=[0]*N
        legal=True
        for k,(vertex,edge_idx) in enumerate(INCIDENCES):
            if not ((mask>>k)&1):continue
            new_sign=1 if edge_idx==vertex else -1
            if signs[vertex]:
                legal=False;break
            signs[vertex]=new_sign
        if legal:
            legal=all(not signs[i] or not signs[(i+1)%N] or signs[i]==signs[(i+1)%N] for i in range(N))
            used={v for v in signs if v}
            if len(used)==1 and not any(signs[i]==signs[(i+1)%N]==0 for i in range(N)):
                legal=False
        assert (mask in faces)==legal,mask


def earlier_pure_equal_full():
    outcome=[]
    for n in range(3,8):
        edges=[tuple(sorted((i,(i+1)%n))) for i in range(n)]
        incidences=[(v,i) for i,e in enumerate(edges) for v in e]
        index={pair:i for i,pair in enumerate(incidences)}
        generated=set()
        for order in itertools.permutations(range(n)):
            prior=set()
            m=0
            for v in order:
                old=[u for u in ((v-1)%n,(v+1)%n) if u in prior]
                if len(old)==1:
                    m|=1<<index[(v,edges.index(tuple(sorted((v,old[0])))))]
                prior.add(v)
            generated.add(m)
        max_size=max(m.bit_count() for m in generated)
        full={0};pure={0}
        for m in generated:
            x=m
            while x:
                full.add(x)
                if m.bit_count()==max_size:pure.add(x)
                x=(x-1)&m
        assert full==pure, n
        outcome.append((n,len(full)))
    return outcome


def main():
    earlier=earlier_pure_equal_full()
    generated,faces=build_complex()
    verify_word_criterion(faces)
    assert len(generated)==253
    assert len(faces)==1061
    vector=tuple(sum(x.bit_count()==k for x in faces) for k in range(1,7))
    assert vector==(16,96,272,380,240,56),vector
    maximal={x for x in faces if x and not any(y!=x and (y&x)==x for y in faces)}
    facet_sizes=collections.Counter(x.bit_count()-1 for x in maximal)
    assert facet_sizes=={5:56,3:4},facet_sizes
    top_size=max(x.bit_count() for x in generated)
    pure_facets={x for x in generated if x.bit_count()==top_size}
    pure_faces={0}
    for top in pure_facets:
        sub=top
        while sub:
            pure_faces.add(sub)
            sub=(sub-1)&top
    assert len(pure_faces)==1057 and len(faces-pure_faces)==4
    assert faces-pure_faces == {x for x in maximal if x.bit_count()==4}
    critical,pairs=match_faces(faces)
    assert len(pairs)==527
    count=collections.Counter(x.bit_count()-1 for x in critical)
    assert dict(count)=={0:1,3:5},count
    incidences=verify_acyclicity(faces,pairs)
    verify_field_homology(faces)
    print('VERIFY_OK',f'permutations={40320}',f'generated={len(generated)}',f'faces={len(faces)-1}',f'facets={dict(facet_sizes)}',f'pure_faces={len(pure_faces)-1}',f'face_vector={vector}',f'incidences={incidences}',f'matched_pairs={len(pairs)}',f'critical={dict(count)}',f'extra_nonpure_facets={sorted(faces-pure_faces)}','field_homology=2,3,5',f'earlier_pure_full_agree={earlier}')

if __name__=='__main__':main()
