#!/usr/bin/env python3
"""Standalone finite tests for maximal edge-open packings of S(K_{2,b}).

Only stdlib is required. The all-order result uses a separate combinatorial proof.
"""
from collections import Counter
from math import comb


def original_subdivision_edges(b):
    # First two vertices are one bipartition shore; next b form the other.
    # Subdivision vertex for row r, column c has index 2+b+r*b+c.
    return [edge for r in range(2) for c in range(b)
            for edge in ((r, 2+b+r*b+c), (2+c, 2+b+r*b+c))]


def edge_conflicts_direct(b):
    edges = original_subdivision_edges(b)
    n = len(edges)
    conflict = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            endpoints_i = set(edges[i]); endpoints_j = set(edges[j])
            has_witness = any(
                set(edge).issubset(endpoints_i | endpoints_j)
                and bool(set(edge) & endpoints_i)
                and bool(set(edge) & endpoints_j)
                for k, edge in enumerate(edges) if k != i and k != j
            )
            if has_witness:
                conflict[i] |= 1 << j
                conflict[j] |= 1 << i
    return conflict


def edge_conflicts_formula(b):
    # Our edge order puts the 'row' incidence before the 'column' incidence.
    m = 4*b
    out = [0]*m
    for r in range(2):
        for c in range(b):
            i = (r*b+c)*2
            for s in range(2):
                for d in range(b):
                    j = (s*b+d)*2+1
                    if (r,c)!=(s,d) and (r==s or c==d):
                        out[i] |= 1 << j
                        out[j] |= 1 << i
    return out


def polynomial_closed(b):
    assert b >= 3
    p = Counter()
    p[2*b] += 2
    p[4] += b*(b-1)
    p[b+1] += 4*b
    p[b] += 2*(2**b-2*b-2)
    return +p


def enumeration_direct(b):
    adj = edge_conflicts_direct(b)
    m = len(adj)
    n = 1 << m
    valid = bytearray(n)
    valid[0] = 1
    dominated = [0]*n
    p = Counter()
    complete_mask = n-1
    for S in range(1, n):
        bit = S & -S
        i = bit.bit_length()-1
        prev = S ^ bit
        valid[S] = valid[prev] and not (adj[i] & prev)
        if valid[S]:
            dominated[S] = dominated[prev] | adj[i] | bit
            if dominated[S] == complete_mask:
                p[S.bit_count()] += 1
    return +p


def enumeration_closed_relational(b):
    """Independent enumeration via the closure A=N(B), B=N(A)."""
    m = 2*b
    full = (1<<m)-1
    allowed = [0]*m
    for r in range(2):
        for c in range(b):
            i=r*b+c
            allowed[i] = sum(1<<(s*b+d) for s in range(2)
                             for d in range(b)
                             if (r,c)==(s,d) or (r!=s and c!=d))
    def compatible_B(A):
        # B consists of exactly those right-incidences compatible with all A.
        B = full
        while A:
            bit = A & -A
            B &= allowed[bit.bit_length()-1]
            A -= bit
        return B
    p = Counter()
    for A in range(1<<m):
        B = compatible_B(A)
        if compatible_B(B)==A:
            p[A.bit_count()+B.bit_count()] += 1
    return +p


def run():
    checked_edges = 0
    checked_subsets = 0
    for b in range(2,10):
        direct = edge_conflicts_direct(b)
        assert direct == edge_conflicts_formula(b), (b, 'conflict relation')
        checked_edges += len(direct)
        computed = enumeration_closed_relational(b)
        expected = Counter({4:4}) if b==2 else polynomial_closed(b)
        assert computed == expected, (b, computed, expected)
        if b<=5:
            observed = enumeration_direct(b)
            assert observed == expected, (b, observed, expected)
            checked_subsets += 1 << (4*b)
        if b>=3:
            assert sum(computed.values()) == 2**(b+1)+b*b-b-2
            assert min(computed) == 4 and max(computed) == 2*b
            assert computed[2*b] == 2
    print('VERIFY_OK direct_edge_subsets=%d incidence_edges=%d closure_parameters=%d' %
          (checked_subsets,checked_edges,8))


if __name__=='__main__':
    run()
