#!/usr/bin/env python3
"""Independent finite checks of the pseudo-Frobenius spectrum theorem.

Only integer arithmetic and the Python standard library are used.
The finite computations corroborate, but do not replace, the proof.
"""
import argparse
from heapq import heappush, heappop


def apery(gens, e):
    """Shortest distances from residue zero in the additive residue graph."""
    inf = 10**18
    dist = [inf] * e
    dist[0] = 0
    heap = [(0, 0)]
    while heap:
        val, r = heappop(heap)
        if val != dist[r]:
            continue
        for a in gens:
            j = (r+a) % e
            x = val+a
            if x < dist[j]:
                dist[j] = x
                heappush(heap, (x, j))
    assert all(x < inf for x in dist)
    return dist


def test_case(e, k, j):
    gens = [e+a for a in range(e) if not j <= a < j+k]
    assert gens[0] == e and gens[-1] == 2*e-1
    # Finite independent shortest-path membership test.
    ap = apery(gens, e)
    pred = lambda x: (x >= 0 and x >= ap[x % e])
    actual_gaps = {x for x in range(max(ap)-e+1) if not pred(x)}
    # A second route, unbounded-coin change by a forward dynamic program,
    # checks the Dijkstra membership method on all small parameter cases.
    if e <= 22:
        bound = 4*e
        reachable = [False]*(bound+1)
        reachable[0] = True
        for x in range(1, bound+1):
            reachable[x] = any(x >= a and reachable[x-a] for a in gens)
        for x in range(bound+1):
            assert pred(x) == reachable[x], (e,k,j,'dp',x)
    if j <= k:
        expected_gaps = (set(range(1,e)) |
                         set(range(e+j,e+j+k)) |
                         set(range(2*e+2*j-1,2*e+j+k)))
        expected_pf = set(range(2*e+2*j-1, 2*e+j+k))
        expect_F = 2*e+j+k-1
        expect_genus = e+2*k-j
        expect_type = k-j+1
        expect_defect = 2*(k-j)
    else:
        expected_gaps = set(range(1,e)) | set(range(e+j,e+j+k))
        expected_pf = set(range(j+k,e)) | set(range(e+j,e+j+k))
        expect_F = e+j+k-1
        expect_genus = e+k-1
        expect_type = e-j
        expect_defect = k-1
    assert actual_gaps == expected_gaps, (e,k,j,'gap',sorted(actual_gaps ^ expected_gaps))
    actual_pf = {x for x in actual_gaps if all(pred(x+a) for a in gens)}
    assert actual_pf == expected_pf, (e,k,j,'pf',sorted(actual_pf ^ expected_pf))
    assert max(actual_gaps) == expect_F
    assert len(actual_gaps) == expect_genus
    assert len(actual_pf) == expect_type
    assert 2*len(actual_gaps)-max(actual_gaps)-len(actual_pf) == expect_defect
    return len(actual_gaps)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-e', type=int, default=48)
    args=parser.parse_args()
    checked=0
    gap_checks=0
    for e in range(7,args.max_e+1):
        for k in range(3,(e-1)//2+1):
            types=[]
            for j in range(1,e-k):
                gap_checks += test_case(e,k,j)
                types.append((k-j+1) if j<=k else (e-j))
                checked += 1
            assert sorted(types) == list(range(1,e-k)), (e,k,types)
    print(f'VERIFY_OK cases={checked} checked_gap_counts={gap_checks} e_max={args.max_e}')

if __name__=='__main__':
    main()
