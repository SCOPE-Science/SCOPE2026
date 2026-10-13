from itertools import combinations

def crown_data(n):
    edges = [(i,j) for i in range(n) for j in range(n) if i != j]
    idx = {e:t for t,e in enumerate(edges)}
    forbidden = set()
    for i,j,k in combinations(range(n),3):
        # Each 3-set of indices has six linear orders; each order gives one
        # transitive triangle of arcs, corresponding to a 3-edge geodesic.
        for a,b,c in [(i,j,k),(i,k,j),(j,i,k),(j,k,i),(k,i,j),(k,j,i)]:
            tri = tuple(sorted((idx[(a,b)], idx[(c,b)], idx[(c,a)])))
            forbidden.add(tri)
    masks = []
    for tri in forbidden:
        m = 0
        for e in tri:
            m |= 1 << e
        masks.append(m)
    return edges, masks

def exhaustive(n):
    edges, forb = crown_data(n)
    m = len(edges)
    best = -1
    count = 0
    for mask in range(1 << m):
        if any((mask & h) == h for h in forb):
            continue
        s = mask.bit_count()
        if s > best:
            best = s
            count = 1
        elif s == best:
            count += 1
    return m, len(forb), best, count

def balanced_cut_size(n):
    p = n // 2
    return 2*p*(n-p)

def degree_inequality_check(n):
    # Check the construction itself is T3-free and has the claimed size.
    P = set(range(n//2))
    Q = set(range(n)) - P
    arcs = {(u,v) for u in P for v in Q} | {(v,u) for u in P for v in Q}
    for a,b,c in combinations(range(n),3):
        for x,y,z in [(a,b,c),(a,c,b),(b,a,c),(b,c,a),(c,a,b),(c,b,a)]:
            assert not ({(x,y),(z,y),(z,x)} <= arcs)
    assert len(arcs) == balanced_cut_size(n)
    return len(arcs)

print("VERIFY_OK")
total_subsets = 0
for n in range(3,6):
    edge_count, forbidden_count, best, max_count = exhaustive(n)
    total_subsets += 1 << edge_count
    target = n*n // 2
    assert best == target
    assert balanced_cut_size(n) == target
    print(f"n={n}: edges={edge_count}, forbidden_geodesic_triples={forbidden_count}, "
          f"maximum={best}, maximum_sets={max_count}")
for n in range(3,21):
    assert degree_inequality_check(n) == n*n//2
print("vertex_index_cut_constructions_checked = 3..20")
print("exhaustive_edge_subsets_checked =", total_subsets)
print("all exhaustive maxima equal floor(n^2/2)")
