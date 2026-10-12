#!/usr/bin/env python3
from itertools import product

checks = 0

def ok(cond, msg='assertion failed'):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def partitions_rgs(N):
    if N == 0:
        yield ()
        return
    def rec(a, maxv):
        if len(a) == N:
            yield tuple(a)
            return
        for v in range(maxv + 2):
            yield from rec(a + [v], max(maxv, v))
    yield from rec([0], 0)

def rgs_to_blocks(rgs, elems=None):
    if elems is None:
        elems = list(range(1, len(rgs) + 1))
    d = {}
    for e, b in zip(elems, rgs):
        d.setdefault(b, []).append(e)
    return [tuple(v) for _, v in sorted(d.items())]

def canon(blocks):
    return tuple(sorted((tuple(sorted(b)) for b in blocks), key=lambda b: (min(b) if b else -1, len(b), b)))

def invariant_indices(T):
    n = len(T)
    return [x for x in range(1, n) if all(T[y][x] == x for y in range(x))]

def smallest_invariant_index(T):
    inv = invariant_indices(T)
    if not inv:
        return 0
    return max(inv)

def extend_table(T, p, c):
    # T is on x_0 > ... > x_{s-1}, with logical unit x_0.
    # Add new least element x_s. Proposition 4.4 gives the unique extension
    # after choosing c = p * x_s.
    s = len(T)
    new = s
    U = [[None] * (s + 1) for _ in range(s + 1)]
    for i in range(s):
        for j in range(s):
            U[i][j] = T[i][j]

    if c == new:
        for a in range(s):
            U[a][new] = new
    else:
        for a in range(s):
            if a < p:  # a > p in the chain
                U[a][new] = new
            else:      # a <= p in the chain
                U[a][new] = T[T[p][a]][c]

    for a in range(s):
        U[new][a] = 0
    U[new][new] = 0
    return U

def build_from_partition(blocks, n):
    # Recursive inverse Psi_n from a partition of {x_1,...,x_{n-1}}.
    if n == 1:
        return [[0]]
    last = n - 1
    distinguished = next(set(b) for b in blocks if last in b)
    A = distinguished - {last}
    C = sorted(set(range(1, n - 1)) - A)
    m = len(C) + 1

    # Standardize the partition on C to {1,...,m-1}.
    inv = {c: i + 1 for i, c in enumerate(C)}
    subblocks = []
    for b0 in blocks:
        b = set(b0)
        if last in b:
            continue
        subblocks.append(tuple(sorted(inv[x] for x in b)))

    T = build_from_partition(subblocks, m)

    # First adjoin x_m as a new invariant element.
    p0 = smallest_invariant_index(T)
    T = extend_table(T, p0, len(T))
    p = m

    # Then adjoin the remaining lower elements.  The values c are precisely A,
    # taken from high to low in the ambient chain.
    for c in sorted(A):
        T = extend_table(T, p, c)
    ok(len(T) == n, 'wrong recursive size')
    return T

def phi_from_table(T):
    # Recursive forward map Phi_n.
    n = len(T)
    if n == 1:
        return ()
    m = smallest_invariant_index(T)
    ok(1 <= m <= n - 1, 'smallest invariant outside range')
    A = {T[m][j] for j in range(m + 1, n)}
    ok(0 not in A, 'logical unit entered A')
    ok(all(1 <= a <= n - 2 for a in A), 'A outside ambient nonunit prefix')
    C = sorted(set(range(1, n - 1)) - A)
    ok(len(C) == m - 1, 'wrong complement size')

    T0 = [row[:m] for row in T[:m]]
    sub = phi_from_table(T0)
    transport = {i + 1: c for i, c in enumerate(C)}
    blocks = [tuple(sorted(transport[x] for x in b)) for b in sub]
    blocks.append(tuple(sorted(A | {n - 1})))
    return canon(blocks)

def check_L(T):
    n = len(T)
    for x in range(n):
        ok(T[0][x] == x, 'left unit failed')
        ok(T[x][0] == 0, 'right unit failed')
        ok(T[x][x] == 0, 'idempotent-to-unit failed')
    for x in range(n):
        for y in range(n):
            ok(not (T[x][y] == 0 and T[y][x] == 0 and x != y), 'antisymmetry axiom failed')
            ok((T[x][y] == 0) == (x >= y), 'natural order is not the target chain')
            for z in range(n):
                lhs = T[T[x][y]][T[x][z]]
                rhs = T[T[y][x]][T[y][z]]
                ok(lhs == rhs, 'cycloid equation failed')

expected = {1:1, 2:1, 3:2, 4:5, 5:15, 6:52, 7:203, 8:877}
total = 0
for n in range(1, 9):
    seen = set()
    count = 0
    for rgs in partitions_rgs(n - 1):
        blocks = canon(rgs_to_blocks(rgs))
        T = build_from_partition(blocks, n)
        check_L(T)
        recovered = phi_from_table(T)
        ok(recovered == blocks, f'Phi(Psi(pi)) failed at n={n}')
        key = tuple(tuple(row) for row in T)
        ok(key not in seen, f'noninjective table construction at n={n}')
        seen.add(key)
        count += 1
    ok(count == expected[n], f'Bell count mismatch at n={n}')
    ok(len(seen) == expected[n], f'distinct table count mismatch at n={n}')
    total += count

print(f'VERIFY_OK {checks} exact assertions; {total} partitions/tables checked through n=8')
