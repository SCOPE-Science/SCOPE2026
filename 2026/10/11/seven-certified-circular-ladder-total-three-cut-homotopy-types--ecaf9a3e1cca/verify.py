"""Exact finite discrete-Morse certificates for total three-cut complexes of circular ladders.

Run: python3 verify_circular_total3.py
Requires only the Python standard library.  No external datasets.
"""
from collections import Counter, deque
from itertools import combinations

EXPECTED = {
    4: (8, 134, 9),
    5: (30, 805, 14),
    6: (76, 3761, 22),
    7: (154, 15906, 29),
    8: (272, 64890, 37),
    9: (438, 261305, 46),
    10: (660, 1047519, 56),
}


def build_faces(n):
    """Nonempty faces of Delta^t_3(C_n square K_2), encoded by bitsets."""
    N = 2*n
    edges = set()
    for i in range(n):
        j = (i+1) % n
        edges.add(tuple(sorted((i,j))))
        edges.add(tuple(sorted((n+i,n+j))))
        edges.add((i,n+i))
    assert len(edges) == 3*n
    adjacent = [0]*N
    for a,b in edges:
        adjacent[a] |= 1 << b
        adjacent[b] |= 1 << a
    full = (1 << N) - 1
    facets = []
    for a,b,c in combinations(range(N),3):
        if not (adjacent[a] & (1 << b) or adjacent[a] & (1 << c)
                or adjacent[b] & (1 << c)):
            facets.append(full ^ (1 << a) ^ (1 << b) ^ (1 << c))
    faces = set()
    for facet in facets:
        sub = facet
        while sub:
            faces.add(sub)
            sub = (sub-1) & facet
    assert all(s > 0 for s in faces)
    return faces,len(facets)


def element_matching(faces,n):
    remaining = set(faces)
    pairs=[]
    for vertex in range(2*n):
        bit=1<<vertex
        for low in sorted(remaining):
            if not low & bit:
                up=low | bit
                if up in remaining:
                    remaining.remove(low)
                    remaining.remove(up)
                    pairs.append((low,up))
    assert len(remaining) + 2*len(pairs) == len(faces)
    assert all(low.bit_count()+1 == up.bit_count() for low,up in pairs)
    return remaining,pairs


def confirm_acyclic(faces,pairs):
    """Kahn topological sort on ALL Hasse arrows, with matched arrows reversed."""
    matched_down={up:low for low,up in pairs}
    matched_up={low:up for low,up in pairs}
    indegree={s:0 for s in faces}
    edge_count=0
    for high in faces:
        z=high
        while z:
            bit=z & -z
            z-=bit
            low=high ^ bit
            if low not in faces:
                continue
            edge_count+=1
            # Ordinary Hasse arrows are high -> low; reverse matched arrows.
            if matched_down.get(high)==low:
                indegree[high]+=1
            else:
                indegree[low]+=1
    queue=deque(s for s,degree in indegree.items() if degree==0)
    seen=0
    while queue:
        current=queue.popleft()
        seen+=1
        # Ordinary arrows from current to its codimension-one faces.
        z=current
        while z:
            bit=z & -z
            z-=bit
            low=current ^ bit
            if low in faces and matched_down.get(current)!=low:
                indegree[low]-=1
                if indegree[low]==0:
                    queue.append(low)
        # One reversed matched arrow from current to upper.
        up=matched_up.get(current)
        if up is not None:
            indegree[up]-=1
            if indegree[up]==0:
                queue.append(up)
    assert seen == len(faces), (seen,len(faces))
    return edge_count


def main():
    for n,(expected_facets,expected_faces,expected_wedges) in EXPECTED.items():
        faces,facets=build_faces(n)
        critical,pairs=element_matching(faces,n)
        counts=Counter(s.bit_count()-1 for s in critical)
        assert facets==expected_facets,(n,facets)
        assert len(faces)==expected_faces,(n,len(faces))
        assert counts=={0:1, 2*n-6:expected_wedges},(n,counts)
        if n>=6:
            assert expected_wedges == n*(n+1)//2+1
        arrows=confirm_acyclic(faces,pairs)
        print(f"n={n}: facets={facets}, faces={len(faces)}, "
              f"matched_pairs={len(pairs)}, critical={dict(counts)}, "
              f"Hasse_edges={arrows}, DAG=PASS",flush=True)
    print("VERIFY_OK 7 complete complexes; every Hasse incidence checked")

if __name__=='__main__':
    main()
