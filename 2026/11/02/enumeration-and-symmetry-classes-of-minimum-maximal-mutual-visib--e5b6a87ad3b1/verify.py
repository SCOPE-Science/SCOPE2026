"""Independently enumerate optimal maximal mutual-visibility configurations.

Each board square corresponds to an edge of the complete bipartite root.
The primary check applies the shortest-path mutual-visibility definition directly.
"""
from itertools import combinations, permutations
from math import comb, factorial


def mutually_visible(square_mask, m, n):
    """Original rook shortest-path visibility test, pair by pair."""
    cells = [i for i in range(m*n) if square_mask & (1 << i)]
    for p, q in combinations(cells, 2):
        r1, c1 = divmod(p, n)
        r2, c2 = divmod(q, n)
        if r1 != r2 and c1 != c2:
            # Two possible length-two geodesics; at least one has
            # no occupied internal square.
            w1, w2 = r1*n+c2, r2*n+c1
            if square_mask & (1 << w1) and square_mask & (1 << w2):
                return False
    return True


def minimal_size_maximal_masks(m, n):
    size = m+n-1
    result=[]
    for choices in combinations(range(m*n), size):
        mask=sum(1<<x for x in choices)
        if not mutually_visible(mask,m,n):
            continue
        if all(not mutually_visible(mask | (1 << e),m,n)
               for e in range(m*n) if not (mask & (1 << e))):
            result.append(mask)
    return result


def has_universal_root(mask, m, n):
    # Some row vertex touches every column or a column touches every row.
    return (any(all(mask & (1 << (r*n+c)) for c in range(n))
                for r in range(m))
            or any(all(mask & (1 << (r*n+c)) for r in range(m))
                   for c in range(n)))


def restricted_partition_count(total, max_parts):
    # Independent integer-partition dynamic recursion.
    from functools import lru_cache
    @lru_cache(None)
    def part(rem, largest, parts):
        if not rem:
            return 1
        if parts == 0 or largest == 0:
            return 0
        return part(rem,largest-1,parts)+part(rem-largest,largest,parts-1) if rem>=largest else part(rem,largest-1,parts)
    return part(total,total,max_parts)


def canonical_orbit(mask,m,n):
    perms_r=list(permutations(range(m)))
    perms_c=list(permutations(range(n)))
    es=[divmod(j,n) for j in range(m*n) if mask & (1<<j)]
    return min(tuple(sorted((pr[r],pc[c]) for r,c in es))
               for pr in perms_r for pc in perms_c)


def transposed_mask(mask,n):
    return sum(1 << (c*n+r) for r in range(n) for c in range(n)
               if mask & (1 << (r*n+c)))


def run():
    boards=[(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5)]
    tested=0
    for m,n in boards:
        masks=minimal_size_maximal_masks(m,n)
        predicted=m*n**(m-1)+n*m**(n-1)-m*n
        assert len(masks)==predicted,(m,n,len(masks),predicted)
        assert all(has_universal_root(mask,m,n) for mask in masks)
        tested+=comb(m*n,m+n-1)
        if (m,n)!=(4,5):
            orbits={canonical_orbit(mask,m,n) for mask in masks}
            expected=(restricted_partition_count(m-1,n)
                      +restricted_partition_count(n-1,m)-1)
            assert len(orbits)==expected,(m,n,len(orbits),expected)
            if m==n:
                full_orbits={min(canonical_orbit(mask,m,n),
                                 canonical_orbit(transposed_mask(mask,n),m,n))
                             for mask in masks}
                full_expected=restricted_partition_count(n-1,n)
                assert len(full_orbits)==full_expected,(m,n,len(full_orbits),full_expected)
        print(f"({m},{n}): {len(masks)} minimal-cardinality maximal sets; formula exact")
    print(f"Original geodesic visibility and saturation checked over {tested} candidate subsets.")
    print("VERIFY_OK")

if __name__=='__main__':
    run()
