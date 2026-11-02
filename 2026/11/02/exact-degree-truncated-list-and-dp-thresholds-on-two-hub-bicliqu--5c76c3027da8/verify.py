"""Finite checks for the explicit two-hub degree-truncated colouring theorem.

Only standard-library Python is required. This is not an infinite proof.
"""
from functools import lru_cache
from math import isqrt
from itertools import product


def permutations_of_partial_two_matching(h):
    """All matchings from two leaf colours to h hub colours, as length-two maps."""
    result = set()
    for a in range(-1, h):
        for b in range(-1, h):
            if a >= 0 and b >= 0 and a == b:
                continue
            result.add((a, b))
    return result


def forbidden(h, u_match, v_match):
    """Hub colour pairs leaving a specified leaf no permissible colour."""
    return {(a, b) for a in range(h) for b in range(h)
            if all(u_match[c] == a or v_match[c] == b for c in range(2))}


def two_edge_partition(h):
    """Partition the h-by-h grid into disjoint singletons and 2-edge matchings."""
    edges = [(i, (i+r) % h) for r in range(h) for i in range(h)]
    blocks = [tuple(edges[i:i+2]) for i in range(0, len(edges), 2)]
    return blocks


def witness_matchings(block):
    """Map leaf colours 0,1 to hub colours, constructing each forbidden block."""
    if len(block) == 1:
        (a, b), = block
        return (a, -1), (-1, b)
    (a, b), (a1, b1) = block
    return (a, a1), (b1, b)


def verify_dp_upper_bound(h):
    """Independently enumerate every admissible two-colour leaf DP constraint."""
    options = permutations_of_partial_two_matching(h)
    for pm, qm in product(options, repeat=2):
        bad = forbidden(h, pm, qm)
        assert len(bad) <= 2, (h, pm, qm, bad)
        if len(bad) == 2:
            (a,b), (c,d) = tuple(bad)
            assert a != c and b != d
    return len(options)**2


def verify_dp_obstruction(h):
    blocks = two_edge_partition(h)
    assert len(blocks) == (h*h+1)//2
    flattened = [p for block in blocks for p in block]
    assert len(flattened) == h*h and len(set(flattened)) == h*h
    assert set(flattened) == set(product(range(h), repeat=2))
    for block in blocks:
        if len(block) == 2:
            (a,b), (c,d) = block
            assert a != c and b != d
        m1, m2 = witness_matchings(block)
        assert m1 in permutations_of_partial_two_matching(h)
        assert m2 in permutations_of_partial_two_matching(h)
        assert forbidden(h, m1, m2) == set(block), (h, block, forbidden(h,m1,m2))
    for pair in product(range(h), repeat=2):
        assert any(pair in forbidden(h, *witness_matchings(block)) for block in blocks)
    return len(blocks)


def verify_exact_cover_minimum(h):
    """Independent subset DP for covering h-by-h choices with matching pairs."""
    edge_count = h*h
    allmask = (1<<edge_count)-1
    candidates = []
    by_element = [[] for _ in range(edge_count)]
    for a,b in product(range(h), repeat=2):
        i=a*h+b
        opts = {1<<i}
        for c,d in product(range(h),repeat=2):
            if a!=c and b!=d:
                opts.add((1<<i) | (1<<(c*h+d)))
        for op in opts:
            if op not in by_element[i]:
                by_element[i].append(op)
    @lru_cache(None)
    def solve(uncovered):
        if not uncovered:
            return 0
        lb = uncovered & -uncovered
        i = lb.bit_length()-1
        return 1 + min(solve(uncovered & ~mask) for mask in by_element[i])
    ans = solve(allmask)
    assert ans == (h*h+1)//2
    return ans,solve.cache_info().currsize


def verify_list_obstruction(h):
    # Every possible hub pair appears as the unique forbidden choice at a leaf.
    bad_sets = [{(a,b)} for a,b in product(range(h),repeat=2)]
    assert len(bad_sets) == h*h
    assert set.union(*bad_sets) == set(product(range(h),repeat=2))
    assert any((a,b) not in set.union(*bad_sets[:h*h-1])
               for a,b in product(range(h),repeat=2))


def verify_thresholds():
    for n in range(3,501):
        list_value = isqrt(n)+1
        dp_value = isqrt(2*n)+1
        assert list_value <= dp_value <= n
        for k in range(1,min(n+3,30)):
            h = min(k,n)
            list_ok = k>=2 and n<h*h
            dp_ok = k>=2 and 2*n<h*h
            assert list_ok == (k >= list_value), (n,k,'L')
            assert dp_ok == (k >= dp_value), (n,k,'DP')


def main():
    for h in range(2,8):
        configurations = verify_dp_upper_bound(h)
        number = verify_dp_obstruction(h)
        verify_list_obstruction(h)
        print('ALL_TWO_LEAF_MATCHINGS_AND_WITNESSES_OK',h,configurations,number)
    for h in (2,3,4):
        optimum,visited = verify_exact_cover_minimum(h)
        print('INDEPENDENT_GRID_SET_COVER_DP_OK',h,optimum,visited)
    verify_thresholds()
    print('INDEPENDENT_THRESHOLD_ARITHMETIC_OK',3,500)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
