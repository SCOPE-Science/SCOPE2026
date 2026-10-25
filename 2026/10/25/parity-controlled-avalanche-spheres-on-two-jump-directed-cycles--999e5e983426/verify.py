#!/usr/bin/env python3
"""Exact finite tests for the two-jump avalanche theorem; Python standard library.

The general theorem is proved in RESULT.md. These finite checks do not
establish its unbounded quantifiers.
"""
from collections import defaultdict


def simulate(n, q, root=0):
    c = [2] * n
    c[root] = q
    visited, records = {}, []
    for t in range(n + 5):
        state = tuple(c)
        if state in visited:
            return records, visited[state], t
        visited[state] = t
        firing = frozenset(i for i in range(n) if c[i] >= 2)
        assert firing, (n, q, 'premature stabilization')
        records.append((state, firing))
        nxt = c[:]
        for i in firing:
            nxt[i] -= 2
            nxt[(i+1) % n] += 1
            nxt[(i+2) % n] += 1
        assert min(nxt) >= 0 and sum(nxt) == sum(c)
        c = nxt
    raise AssertionError('Period not detected')


def expected_holes(n, q, root=0):
    k = n // 2
    blocks = [{root}]
    for t in range(1, k + 1):
        if n % 2 == 0 and q == 1 and t == k:
            block = {n-1}
        else:
            block = {(2*t-1) % n, (2*t) % n}
        blocks.append({(root+i)%n for i in block})
    return blocks


def boundary_rank_gf2(columns):
    pivots = {}
    for v in columns:
        while v:
            i = v.bit_length()-1
            if i not in pivots:
                pivots[i] = v
                break
            v ^= pivots[i]
    return len(pivots)


def mod2_betti(facets, n):
    """Build actual downward-closed faces, then exact boundary matrices."""
    faces_by_dim = defaultdict(set)
    for facet in facets:
        sub = facet
        while sub:
            faces_by_dim[sub.bit_count()-1].add(sub)
            sub = (sub-1)&facet
    assert faces_by_dim[0]
    max_dim = max(faces_by_dim)
    faces = {d: sorted(faces_by_dim[d]) for d in range(max_dim+1)}
    ranks = {0:0, max_dim+1:0}
    for d in range(1, max_dim+1):
        index = {face:i for i,face in enumerate(faces[d-1])}
        columns=[]
        for f in faces[d]:
            column = 0
            left = f
            while left:
                bit = left & -left
                column ^= 1 << index[f ^ bit]
                left ^= bit
            columns.append(column)
        ranks[d] = boundary_rank_gf2(columns)
    result = [len(faces[d])-ranks[d]-ranks[d+1] for d in range(max_dim+1)]
    result[0]-=1
    assert min(result)>=0
    return tuple(result)


def check_all():
    orbit_checks=0; direct_checks=0
    for n in range(5,82):
        k=n//2
        for q in (0,1):
            records, start, end = simulate(n,q)
            blocks=expected_holes(n,q)
            assert end == k+1, (n,q,end,k+1)
            assert start == (1 if n%2==0 and q==0 else 0)
            assert len(records)==len(blocks)
            for t, (_,firing) in enumerate(records):
                assert set(range(n))-set(firing) == blocks[t], (n,q,t)
            # An independent deficit evolution reproduces the firing sequence.
            d=[2-x for x in records[0][0]]
            for _, firing in records:
                got={i for i in range(n) if d[i]<=0}
                assert got==set(firing)
                nxt=d[:]
                for i in range(n):
                    h=1 if i not in got else 0
                    nxt[i] += -2*h + (1 if (i-1)%n not in got else 0) + (1 if (i-2)%n not in got else 0)
                d=nxt
            # Every proper prefix's generating simplices share a cone vertex.
            for t in range(k):
                intersection=set(range(n))
                for hole in blocks[:t+1]:
                    intersection-=hole
                assert intersection
            if n%2==1 or q==1:
                assert set.union(*blocks)==set(range(n))
                assert all(set(range(n))-set.union(*(blocks[:j]+blocks[j+1:])) for j in range(len(blocks)))
                assert all(blocks[i].isdisjoint(blocks[j]) for i in range(k+1) for j in range(i+1,k+1))
            else:
                assert n%2==0
                assert blocks[0] == {0}
                assert blocks[k] == {0,n-1}
                # Last firing simplex lies inside the first; surviving union is a cone.
                first=set(range(n))-blocks[0]
                last=set(range(n))-blocks[k]
                assert last<=first
                assert n-1 not in set.union(*blocks[:k])
            orbit_checks+=1
            if n <= 12:
                V=(1<<n)-1
                facet_masks=[]
                for _,firing in records:
                    f=sum(1<<i for i in firing)
                    assert f==V-sum(1<<i for i in set(range(n))-set(firing))
                    facet_masks.append(f)
                # Direct homology of avalanche complex, rather than its nerve.
                expected=(k-1) if (n%2==1 or q==1) else None
                for t in range(k+1):
                    betti=mod2_betti(facet_masks[:t+1],n)
                    assert betti==(tuple(1 if j==expected else 0 for j in range(max(len(betti),expected+1))) if (t==k and expected is not None) else (0,)*len(betti)),(n,q,t,betti,expected)
                    direct_checks+=1
    # Translation of root position is a symmetry of the directed circulant.
    for n in range(5,19):
        for q in (0,1):
            for root in range(n):
                records, start, end=simulate(n,q,root)
                assert [set(range(n))-set(f) for _,f in records]==expected_holes(n,q,root)
                orbit_checks+=1
    print(f'VERIFY_OK orbit_cases={orbit_checks} direct_mod2_stages={direct_checks}')

if __name__=='__main__':
    check_all()
