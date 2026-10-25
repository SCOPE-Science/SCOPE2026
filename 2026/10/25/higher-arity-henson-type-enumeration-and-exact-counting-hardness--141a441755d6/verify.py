"""Exact finite checks for injective tuple-type enumeration in the triangle-free Henson graph.

Only Python's standard library is required. All counts use exact integers.
"""
from itertools import combinations
from math import comb


def edge_pairs(n):
    return tuple(combinations(range(n), 2))


def graphs(n):
    pairs = edge_pairs(n)
    for mask in range(1 << len(pairs)):
        yield frozenset(e for j, e in enumerate(pairs) if (mask >> j) & 1)


def triangle_free(n, edges):
    E = set(edges)
    return not any((a, b) in E and (a, c) in E and (b, c) in E
                   for a, b, c in combinations(range(n), 3))


def independence_count(n, edges):
    nbr = [0] * n
    for a, b in edges:
        nbr[a] |= 1 << b
        nbr[b] |= 1 << a
    result = 0
    for s in range(1 << n):
        if all(not (s & (1 << v)) or not (s & nbr[v]) for v in range(n)):
            result += 1
    return result


def box_edges(b, G, r, F):
    return frozenset(tuple(sorted((a*r+i, c*r+i)))
                     for i in range(r) for a, c in G) | frozenset(
        tuple(sorted((a*r+i, a*r+j))) for a in range(b) for i, j in F)


def direct_profile_count(b, G, r, F):
    """Check K3-freeness by *building the actual finite extension*."""
    universe = b + r
    E = set(G) | {(b+i, b+j) for i, j in F}
    answer = 0
    for s in range(1 << (b*r)):
        augmented = set(E)
        for a in range(b):
            for i in range(r):
                if (s >> (a*r + i)) & 1:
                    augmented.add((a, b+i))
        if triangle_free(universe, augmented):
            answer += 1
    return answer


def all_triangle_free(r):
    return [F for F in graphs(r) if triangle_free(r, F)]


def root_floor_power(z, r):
    lo, hi = 0, 1
    while hi**r <= z:
        hi *= 2
    while lo+1 < hi:
        mid = (lo+hi)//2
        if mid**r <= z:
            lo = mid
        else:
            hi = mid
    return lo


def is_bipartite(n, E):
    a=[[] for _ in range(n)]
    for x,y in E:
        a[x].append(y);a[y].append(x)
    col=[-1]*n
    for root in range(n):
        if col[root]>=0:continue
        col[root]=0;Q=[root]
        for v in Q:
            for w in a[v]:
                if col[w]<0:col[w]=1-col[v];Q.append(w)
                elif col[w]==col[v]:return False
    return True


def run():
    tested_direct = 0
    for r in (2,3,4):
        for b in range(0, (3 if r==4 else 4)):
            for G in graphs(b):
                if not triangle_free(b, G):
                    continue
                for F in all_triangle_free(r):
                    want=direct_profile_count(b,G,r,F)
                    got=independence_count(b*r,box_edges(b,G,r,F))
                    assert got == want, (b,r,G,F,got,want)
                    tested_direct += 1

    tested_edgeless = 0
    for m in range(7):
        for r in (2,3):
            count=sum(independence_count(r,F)**m for F in all_triangle_free(r))
            predicted=(4**m+3**m if r==2 else 8**m+3*6**m+3*5**m)
            assert count==predicted,(m,r,count,predicted)
            tested_edgeless+=1

    tested_hardness=0
    for b in range(6):
        for B in graphs(b):
            if not is_bipartite(b,B):continue
            ind=independence_count(b,B)
            for r in (2,3,4):
                if (r==3 and b>3) or (r==4 and b>2):continue
                C=comb(r,2)
                m=3*(r*b+C+2)
                weighted=sum(independence_count(b*r,box_edges(b,B,r,F)) *
                            (independence_count(r,F)**m) for F in all_triangle_free(r))
                denom=2**(r*m)
                extracted=weighted//denom
                assert extracted==ind**r,(b,r,B,extracted,ind**r)
                assert root_floor_power(extracted,r)==ind
                tested_hardness+=1
    print('DIRECT_EXTENSION_VS_PRODUCT_PASS', tested_direct)
    print('INDEPENDENT_PARAMETER_EXACT_PROFILES_PASS', tested_edgeless)
    print('ONE_QUERY_METRIC_REDUCTION_PASS', tested_hardness)
    print('ALL_TESTS_PASS')


if __name__=='__main__':
    run()
