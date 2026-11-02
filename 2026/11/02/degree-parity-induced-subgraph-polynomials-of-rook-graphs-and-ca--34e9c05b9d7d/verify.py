#!/usr/bin/env python3
"""Direct graph-level checks for odd/even induced-subgraph enumerators of rook graphs.

Requires only Python 3.9+ standard library. Empty induced subgraphs are included.
"""
from collections import Counter
from functools import lru_cache
from math import comb


def directly_enumerate(m, n):
    """Vertex-subset enumeration using actual rook-graph adjacency, not cell degrees."""
    adj = []
    for i in range(m):
        for j in range(n):
            mask = 0
            for k in range(m):
                for ell in range(n):
                    if (k, ell) != (i, j) and (i == k or j == ell):
                        mask |= 1 << (k * n + ell)
            adj.append(mask)
    even, odd = Counter(), Counter()
    for selected in range(1 << (m * n)):
        parity = None
        remaining = selected
        while remaining:
            one = remaining & -remaining
            vertex = one.bit_length() - 1
            remaining -= one
            degree_parity = (adj[vertex] & selected).bit_count() & 1
            if parity is None:
                parity = degree_parity
            elif parity != degree_parity:
                break
        else:
            # The empty graph satisfies both conditions vacuously.
            if selected == 0:
                even[0] += 1
                odd[0] += 1
            elif parity == 0:
                even[selected.bit_count()] += 1
            else:
                odd[selected.bit_count()] += 1
    return +even, +odd


@lru_cache(None)
def parity_matrix(r, s, alpha, beta):
    """Independent finite matrix enumeration for the four parity-controlled blocks."""
    ans = Counter()
    for bits in range(1 << (r * s)):
        if any(sum((bits >> (i * s + j)) & 1 for j in range(s)) % 2 != alpha
               for i in range(r)):
            continue
        if any(sum((bits >> (i * s + j)) & 1 for i in range(r)) % 2 != beta
               for j in range(s)):
            continue
        ans[bits.bit_count()] += 1
    return +ans


def product(p, q):
    ans = Counter()
    for a, pa in p.items():
        for b, qb in q.items():
            ans[a + b] += pa * qb
    return ans


def parity_block_enumerate(m, n):
    even, odd = Counter(), Counter()
    for r in range(m + 1):
        for s in range(n + 1):
            weight = comb(m, r) * comb(n, s)
            pe = product(parity_matrix(r, s, 0, 0),
                         parity_matrix(m-r, n-s, 1, 1))
            po = product(parity_matrix(r, n-s, 0, 1),
                         parity_matrix(m-r, s, 1, 0))
            for k, v in pe.items():
                even[k] += weight * v
            for k, v in po.items():
                odd[k] += weight * v
    return +even, +odd


def closed_prism(n):
    # Count matrices with disjoint supports in the two rows, then completely
    # doubled columns. This is independent of the Fourier proof.
    even, odd = Counter(), Counter()
    for top in range(n + 1):
        for bottom in range(n - top + 1):
            c = comb(n, top) * comb(n - top, bottom)
            if (top == 0 or top % 2 == 1) and (bottom == 0 or bottom % 2 == 1):
                even[top + bottom] += c
            if top % 2 == 0 and bottom % 2 == 0:
                odd[top + bottom] += c
    for common in range(1, n + 1):
        if common % 2 == 0:
            even[2 * common] += comb(n, common)
        else:
            odd[2 * common] += comb(n, common)
    return +even, +odd



def fourier_binomial_matrix(r, s, alpha, beta):
    """Evaluate the stated binomial Fourier transform coefficientwise."""
    co = Counter()
    for p in range(r + 1):
        for q in range(s + 1):
            minus = r*q + s*p - 2*p*q
            plus = r*s - minus
            scale = (-1 if (alpha*p + beta*q) % 2 else 1) * comb(r, p) * comb(s, q)
            for i in range(plus + 1):
                for j in range(minus + 1):
                    co[i+j] += scale * comb(plus, i) * comb(minus, j) * (-1 if j % 2 else 1)
    den = 1 << (r+s)
    assert all(x % den == 0 for x in co.values())
    return +Counter({k:v//den for k,v in co.items() if v})

def main():
    fourier_blocks = 0
    for r in range(4):
        for s in range(4):
            for alpha in (0, 1):
                for beta in (0, 1):
                    assert fourier_binomial_matrix(r, s, alpha, beta) == parity_matrix(r, s, alpha, beta)
                    fourier_blocks += 1
    graphs = 0
    subsets = 0
    for m in range(1, 5):
        for n in range(1, 7):
            if m*n > 12:
                continue
            actual = directly_enumerate(m, n)
            expected = parity_block_enumerate(m, n)
            assert actual == expected, (m, n, actual, expected)
            graphs += 1
            subsets += 1 << (m*n)
    prism_graphs = 0
    for n in range(1, 11):
        actual = directly_enumerate(2, n)
        expected = closed_prism(n)
        assert actual == expected, (n, actual, expected)
        expected_odd_support = set(range(0, 2*(n//2)+1, 2)) | {
            2*t for t in range(1, n+1, 2)}
        expected_even_support = set(range(n+1)) | {
            2*t for t in range(2, n+1, 2)}
        assert set(actual[1]) == expected_odd_support
        assert set(actual[0]) == expected_even_support
        prism_graphs += 1
        subsets += 1 << (2*n)
    for n in range(1, 61):
        even, odd = closed_prism(n)
        assert set(even) == (set(range(n+1)) | {2*t for t in range(2,n+1,2)})
        assert set(odd) == (set(range(0,2*(n//2)+1,2)) | {2*t for t in range(1,n+1,2)})
    print(f'VERIFY_OK general_graphs={graphs} prism_graphs={prism_graphs} '
          f'direct_vertex_subsets={subsets} fourier_blocks={fourier_blocks} symbolic_support_orders=60')


if __name__ == '__main__':
    main()
