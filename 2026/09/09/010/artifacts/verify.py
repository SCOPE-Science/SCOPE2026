#!/usr/bin/env python3
"""Solver-independent replay for lane-287 (stdlib only).

Re-verifies:
  R1: C7 ordinary reset length is exactly 36 (witness word + exhaustive BFS minimality).
  R2: No one-hole mutant in the C7 one-hole ball (14 mutants) is carefully synchronizing,
      via the hand-proof trap closures, re-checked by simulation, plus independent
      careful power-automaton BFS (<= 2^7 = 128 states) returning None for all 14.
  R3: Canonical completion of every mutant (restore deleted entry) is C7 -> length 36.
  R4: Full 14x7 completion-fill ordinary-length landscape matches the committed table.

Prints VERIFY_OK on success; raises AssertionError otherwise.
"""
from collections import deque

N = 7
A = [(i + 1) % N for i in range(N)]          # Cerny generator a: n-cycle
B = list(range(N)); B[N - 1] = 0             # Cerny generator b: fixes 0..5, 6 -> 0
Q = frozenset(range(N))
C7W = "baaaaaabaaaaaabaaaaaabaaaaaabaaaaaab"  # classic length-36 reset word for C7
F = frozenset(range(N - 1))                  # {0..5} = b(Q)
G = frozenset(range(1, N))                   # {1..6} = a({0..5})

# Committed fill landscape: FILL[(letter, hole_state)][fill_value] = ordinary reset
# length of the total completion, or None if non-synchronizing. Recomputed below.
FILL = {
    ('a', 0): [6, 36, 25, 17, 11, 7, 6],
    ('a', 1): [None, 6, 36, 25, 16, 10, 6],
    ('a', 2): [None, None, 6, 36, 25, 16, 9],
    ('a', 3): [None, None, None, 6, 36, 25, 16],
    ('a', 4): [None, None, None, None, 6, 36, 25],
    ('a', 5): [None, None, None, None, None, 6, 36],
    ('a', 6): [36, None, 26, None, None, None, 6],
    ('b', 0): [36, 16, 16, 16, 12, 10, None],
    ('b', 1): [9, 36, 20, 13, 12, 13, 10],
    ('b', 2): [10, 9, 36, 18, 15, 13, 12],
    ('b', 3): [15, 13, 9, 36, 18, 15, 16],
    ('b', 4): [14, 17, 12, 9, 36, 20, 15],
    ('b', 5): [13, 14, 17, 11, 9, 36, 16],
    ('b', 6): [36, 31, 26, 21, 16, 11, None],
}
ORIG = {('a', s): (s + 1) % N for s in range(N)}          # original a-entry at s
ORIG.update({('b', s): (s if s < N - 1 else 0) for s in range(N)})  # original b-entry


def simulate(da, db, w, start=None):
    S = set(range(N)) if start is None else set(start)
    for ch in w:
        d = da if ch == 'a' else db
        S = {d[q] for q in S}
    return S


def bfs_ordinary(da, db):
    """(length, word) of shortest ordinary reset word, or (None, None)."""
    dist = {Q: 0}
    par = {}
    qq = deque([Q])
    while qq:
        S = qq.popleft()
        for ch, d in (('a', da), ('b', db)):
            T = frozenset(d[q] for q in S)
            if T not in dist:
                dist[T] = dist[S] + 1
                par[T] = (S, ch)
                if len(T) == 1:
                    w = []
                    cur = T
                    while cur != Q:
                        p, c = par[cur]
                        w.append(c)
                        cur = p
                    return dist[T], ''.join(reversed(w))
                qq.append(T)
    return None, None


def bfs_careful(da, db):
    """da/db use None for the hole. Returns (length, word) or (None, None)."""
    dist = {Q: 0}
    par = {}
    qq = deque([Q])
    while qq:
        S = qq.popleft()
        for ch, d in (('a', da), ('b', db)):
            if any(d[q] is None for q in S):
                continue
            T = frozenset(d[q] for q in S)
            if T not in dist:
                dist[T] = dist[S] + 1
                par[T] = (S, ch)
                if len(T) == 1:
                    w = []
                    cur = T
                    while cur != Q:
                        p, c = par[cur]
                        w.append(c)
                        cur = p
                    return dist[T], ''.join(reversed(w))
                qq.append(T)
    return None, None


def main():
    # R1: C7 = 36 with certified witness.
    assert len(C7W) == 36, "witness length"
    assert simulate(A, B, C7W) == {0}, "C7 witness must collapse Q to a singleton"
    L, w = bfs_ordinary(A, B)
    assert L == 36, f"C7 BFS minimality, got {L}"
    assert simulate(A, B, w) == {0} or True  # BFS word ends in some singleton
    assert len(simulate(A, B, w)) == 1

    # R2a: trap closures by direct simulation (the hand-proof checks).
    assert {B[q] for q in Q} == set(F) == {0, 1, 2, 3, 4, 5}, "b(Q) = {0..5}"
    assert {B[q] for q in F} == set(F), "b fixes {0..5}"
    assert {A[q] for q in F} == set(G) == {1, 2, 3, 4, 5, 6}, "a({0..5}) = {1..6}"
    assert {B[q] for q in G} == set(F), "b({1..6}) = {0..5}"
    assert {A[q] for q in Q} == set(Q), "a permutes Q, so a(Q) = Q"
    for s in range(N - 1):
        assert s in F, f"hole state {s} lies in trap set for a-hole"
    assert 6 in G and 6 not in F, "s=6 case oscillates F <-> G"

    # R2b: independent careful BFS: all 14 mutants unsynchronizable.
    for letter in ('a', 'b'):
        for s in range(N):
            da = list(A)
            db = list(B)
            if letter == 'a':
                da[s] = None
            else:
                db[s] = None
            cl, _ = bfs_careful(da, db)
            assert cl is None, f"mutant ({letter},{s}) unexpectedly careful-sync"

    # R3: canonical completion restores C7 -> 36 for every mutant.
    for letter in ('a', 'b'):
        for s in range(N):
            da = list(A)
            db = list(B)
            v = ORIG[(letter, s)]
            if letter == 'a':
                da[s] = v
            else:
                db[s] = v
            assert da == A and db == B, "canonical completion must be C7"
            L2, w2 = bfs_ordinary(da, db)
            assert L2 == 36, f"canonical completion ({letter},{s}) -> {L2}"
            assert len(simulate(da, db, w2)) == 1

    # R4: full fill landscape matches committed table (incl. non-sync fills).
    for letter in ('a', 'b'):
        for s in range(N):
            for v in range(N):
                da = list(A)
                db = list(B)
                if letter == 'a':
                    da[s] = v
                else:
                    db[s] = v
                L2, w2 = bfs_ordinary(da, db)
                assert L2 == FILL[(letter, s)][v], \
                    f"fill ({letter},{s})={v}: got {L2}, table {FILL[(letter, s)][v]}"
                if L2 is not None:
                    assert len(simulate(da, db, w2)) == 1, \
                        f"fill word ({letter},{s})={v} must collapse"
    print("VERIFY_OK")


if __name__ == '__main__':
    main()
