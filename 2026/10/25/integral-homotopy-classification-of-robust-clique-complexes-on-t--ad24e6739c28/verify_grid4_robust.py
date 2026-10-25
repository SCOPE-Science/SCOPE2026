#!/usr/bin/env python3
"""Exact finite certificate for robust clique homotopy of the 4 by 4 grid.

Run: python3 verify_grid4_robust.py
Requires only Python 3 standard library. Uses integer-exact face enumeration
and an explicit complete directed Hasse-graph cycle test for every parameter.
"""
from collections import Counter, deque

SIDE = 4
V = SIDE * SIDE
M = 1 << V
NEIGHBORS = [sum(1 << (r * SIDE + c)
                 for r, c in ((i - 1, j), (i + 1, j),
                              (i, j - 1), (i, j + 1))
                 if 0 <= r < SIDE and 0 <= c < SIDE)
             for i in range(SIDE) for j in range(SIDE)]
def compute_alpha():
    a = bytearray(M)
    for mask in range(1, M):
        bit = mask & -mask
        v = bit.bit_length() - 1
        without = mask ^ bit
        a[mask] = max(a[without], 1 + a[without & ~NEIGHBORS[v]])
    assert a[M - 1] == 8
    return a

def independent_subsets():
    a = bytearray(M)
    a[0] = 1
    for mask in range(1, M):
        bit = mask & -mask
        v = bit.bit_length() - 1
        r = mask ^ bit
        a[mask] = a[r] and not (NEIGHBORS[v] & r)
    return a

def independent_k_submask_flags(independent, k):
    # Independent check, not using the independent-number recursion.
    f = bytearray(M)
    for mask in range(M):
        if independent[mask] and mask.bit_count() == k:
            f[mask] = 1
    for v in range(V):
        bit = 1 << v
        for mask in range(M):
            if (mask & bit) and f[mask ^ bit]:
                f[mask] = 1
    return f

def morse_pairs(faces):
    unmatched = set(faces)
    partners = {}
    for v in range(V):
        bit = 1 << v
        lowers = [face for face in unmatched
                  if (face & bit) == 0 and (face | bit) in unmatched]
        for low in lowers:
            upper = low | bit
            assert low in unmatched and upper in unmatched
            unmatched.remove(low)
            unmatched.remove(upper)
            partners[low] = upper
    return unmatched, partners

def confirm_acyclic(faces, partners):
    # Directed Hasse graph: reverse exactly the matched cover relations.
    adjacency = [[] for _ in range(M)]
    indegree = bytearray(M) # each vertex has at most 16 downward + 16 upward edges
    incidences = 0
    for upper in faces:
        bitset = upper
        while bitset:
            bit = bitset & -bitset
            bitset -= bit
            low = upper ^ bit
            if not low:
                continue  # exclude empty simplex from face poset
            if partners.get(low) == upper:
                src, dst = low, upper
            else:
                src, dst = upper, low
            adjacency[src].append(dst)
            indegree[dst] += 1
            incidences += 1
    queue = deque(z for z in faces if indegree[z] == 0)
    seen = 0
    while queue:
        z = queue.popleft()
        seen += 1
        for dst in adjacency[z]:
            indegree[dst] -= 1
            if indegree[dst] == 0:
                queue.append(dst)
    assert seen == len(faces), ('matching contains directed cycle', seen, len(faces))
    return incidences

def main():
    alpha = compute_alpha()
    independent = independent_subsets()
    assert sum(independent) > 0
    assert all(bool(independent[mask]) == (alpha[mask] == mask.bit_count())
               for mask in range(M))
    for k in range(2, 9):
        flag = independent_k_submask_flags(independent, k)
        assert all(bool(flag[mask]) == (alpha[mask] >= k)
                   for mask in range(M))
        faces = {mask for mask in range(1, M) if not flag[mask]}
        critical, partners = morse_pairs(faces)
        assert len(faces) == 2 * len(partners) + len(critical)
        cell_dims = Counter(mask.bit_count() - 1 for mask in critical)
        expected_rank, expected_degree = {
            2: (9, 1), 3: (36, 3), 4: (84, 5), 5: (122, 7),
            6: (102, 9), 7: (29, 11), 8: (1, 13)
        }[k]
        assert cell_dims == {0: 1, expected_degree: expected_rank}, (k, cell_dims)
        incidence_count = confirm_acyclic(faces, partners)
        euler = -1 + sum((-1) ** (mask.bit_count() - 1) for mask in faces)
        assert euler == -expected_rank, (k, euler)
        fcounts = tuple(len([z for z in faces if z.bit_count() == s])
                        for s in range(1, 16))
        print('k=%d faces=%d pairs=%d critical=%s incidences=%d euler=%d f=%s' %
              (k, len(faces), len(partners), dict(sorted(cell_dims.items())),
               incidence_count, euler, fcounts), flush=True)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
