#!/usr/bin/env python3
"""Exact finite certificate for graphical Lie-algebra adjoint-rank polynomials.

Requires only the Python standard library. The general identity is proved in RESULT.md.
"""
from itertools import combinations, permutations, product
from collections import defaultdict

EXAMPLE_A = ((0,1),(0,2),(0,3),(0,4),(1,4),(2,3),(3,5))
EXAMPLE_B = ((0,4),(0,5),(1,3),(1,4),(2,3),(2,4),(3,4))


def all_edges(n):
    return tuple(combinations(range(n), 2))


def graph_from_mask(n, mask):
    ee = all_edges(n)
    return tuple(e for i,e in enumerate(ee) if mask >> i & 1)


def adjacency(n, edges):
    adj = [0]*n
    for u,v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return adj


def components(n, adj, subset):
    count = 0
    remaining = subset
    while remaining:
        count += 1
        bit = remaining & -remaining
        remaining -= bit
        queue = bit
        while queue:
            cur = queue & -queue
            queue -= cur
            i = cur.bit_length()-1
            newly = adj[i] & remaining
            queue |= newly
            remaining &= ~newly
    return count


def signature(n, edges):
    """Exact integers: coefficients of (q-1)^k t^r."""
    adj = adjacency(n, edges)
    out = defaultdict(int)
    for s in range(1 << n):
        neighbor = 0
        for i in range(n):
            if s >> i & 1:
                neighbor |= adj[i]
        neighbor &= ~s
        rank = s.bit_count() + neighbor.bit_count() - components(n, adj, s)
        out[(rank,s.bit_count())] += 1
    return tuple(sorted(out.items()))


def relabel_mask(n, mask, perm):
    idx = {edge:i for i,edge in enumerate(all_edges(n))}
    ans = 0
    for i,(a,b) in enumerate(all_edges(n)):
        if mask >> i & 1:
            u,v = sorted((perm[a],perm[b]))
            ans |= 1 << idx[(u,v)]
    return ans


def canonical_mask(n, mask):
    return min(relabel_mask(n,mask,perm) for perm in permutations(range(n)))


def minimality_check():
    expected_classes = (1,1,2,4,11,34)
    for n in range(6):
        groups = defaultdict(set)
        for mask in range(1 << (n*(n-1)//2)):
            edges = graph_from_mask(n, mask)
            key = signature(n,edges)
            canonical = canonical_mask(n,mask)
            groups[key].add(canonical)
        assert all(len(v)==1 for v in groups.values()), n
        count = len({next(iter(v)) for v in groups.values()})
        assert count == expected_classes[n], (n,count)
        print(f'GRAPH_N_{n}_OK classes={count}; spectra={len(groups)}')


def rank_mod_p(rows,p):
    a = [[v%p for v in row] for row in rows]
    r=0
    for col in range(len(a[0]) if a else 0):
        pivot = next((j for j in range(r,len(a)) if a[j][col]),None)
        if pivot is None:
            continue
        a[r],a[pivot] = a[pivot],a[r]
        inv = pow(a[r][col],-1,p)
        a[r] = [(v*inv)%p for v in a[r]]
        for j in range(r+1,len(a)):
            if a[j][col]:
                factor=a[j][col]
                a[j] = [(x-factor*y)%p for x,y in zip(a[j],a[r])]
        r+=1
        if r==len(a):
            break
    return r


def direct_counts(n, edges, p):
    out = defaultdict(int)
    for x in product(range(p), repeat=n):
        rows = []
        for u,v in edges:
            row=[0]*n
            row[u] = (-x[v])%p
            row[v] = x[u]%p
            rows.append(row)
        out[rank_mod_p(rows,p)] += 1
    return dict(out)


def formula_counts(n, edges, q):
    counts=defaultdict(int)
    for (rank,weight),mult in signature(n,edges):
        counts[rank] += mult*(q-1)**weight
    return dict(counts)


def witness_check():
    n=6
    a=tuple(sorted(tuple(sorted(x)) for x in EXAMPLE_A))
    b=tuple(sorted(tuple(sorted(x)) for x in EXAMPLE_B))
    assert len(set(a))==len(set(b))==7
    assert signature(n,a)==signature(n,b)
    ma=sum(1<<all_edges(n).index(e) for e in a)
    mb=sum(1<<all_edges(n).index(e) for e in b)
    assert canonical_mask(n,ma) != canonical_mask(n,mb)
    # The triangle intersection property also distinguishes the examples.
    def triangles(edges):
        ee=set(edges)
        return [frozenset(s) for s in combinations(range(n),3)
                if all((u,v) in ee for u,v in combinations(s,2))]
    ta=triangles(a);tb=triangles(b)
    assert len(ta)==len(tb)==2
    assert len(ta[0]&ta[1])==1 and len(tb[0]&tb[1])==2
    assert signature(n,a)==(
       ((0,0),1), ((1,1),1), ((2,1),3), ((2,2),2),
       ((3,1),1), ((3,2),6), ((3,3),5), ((3,4),1),
       ((4,1),1), ((4,2),6), ((4,3),11), ((4,4),8), ((4,5),2),
       ((5,2),1), ((5,3),4), ((5,4),6), ((5,5),4), ((5,6),1))
    print('SIX_VERTEX_COLLISION_OK dimensions=13 triangle_overlap=1_vs_2')
    for q in (2,3,5):
        f=formula_counts(n,a,q)
        assert f==formula_counts(n,b,q)
        assert sum(f.values())==q**6
        assert f==direct_counts(n,a,q)==direct_counts(n,b,q)
        print(f'RANK_DIRECT_{q}_OK counts={tuple(f.get(i,0) for i in range(6))}')




def six_vertex_census():
    """Exhaust all 2^15 labelled graphs using explicitly generated S_6 orbits."""
    n=6
    ee=all_edges(n)
    idx={e:i for i,e in enumerate(ee)}
    transformations=[]
    for perm in permutations(range(n)):
        transformations.append(tuple(1 << idx[tuple(sorted((perm[u],perm[v])))] for u,v in ee))

    seen=set()
    classes=defaultdict(list)
    reps=0
    for mask in range(1 << len(ee)):
        if mask in seen:
            continue
        orbit=set()
        for transform in transformations:
            temp=mask
            translated=0
            while temp:
                bit=temp & -temp
                translated |= transform[bit.bit_length()-1]
                temp -= bit
            orbit.add(translated)
        assert mask in orbit
        assert not (orbit & seen)
        seen.update(orbit)
        canonical=min(orbit)
        assert canonical==mask  # scan in increasing mask order
        reps+=1
        classes[signature(n,graph_from_mask(n,canonical))].append(canonical)
    assert len(seen)==(1<<len(ee))
    assert reps==156
    assert len(classes)==149
    doubles=sorted((sorted(cc) for cc in classes.values() if len(cc)==2))
    assert len(doubles)==7
    assert all(len(cc)<=2 for cc in classes.values())
    for i,(a,b) in enumerate(doubles,1):
        a_edges=graph_from_mask(n,a)
        b_edges=graph_from_mask(n,b)
        assert signature(n,a_edges)==signature(n,b_edges)
        assert len(a_edges)==len(b_edges)
        print(f'SIX_PAIR_{i}: {a_edges} / {b_edges}')
    print(f'SIX_CENSUS_OK isoclasses={reps} distinct_polynomials={len(classes)} collision_pairs={len(doubles)}')

def main():
    minimality_check()
    witness_check()
    six_vertex_census()
    print('GRAPHICAL_BREADTH_CERTIFICATE_OK')

if __name__=='__main__':main()
