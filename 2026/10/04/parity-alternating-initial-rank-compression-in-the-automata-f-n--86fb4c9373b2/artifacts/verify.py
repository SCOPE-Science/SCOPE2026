#!/usr/bin/env python3
from collections import deque

def image(n, subset, letter):
    if letter == "b":
        return frozenset((x + 1) % n for x in subset)
    return frozenset(1 if x == n - 1 else x for x in subset)

def act(n, word):
    s = frozenset(range(n))
    for c in word:
        s = image(n, s, c)
    return s

def expected(s):
    return 3*s - 2 if s % 2 else 3*s - 3

def witness(s):
    if s % 2:
        r = (s - 1)//2
        return "a" + ("babbb" + "a")*r
    r = s//2
    return "a" + ("babbb" + "a")*(r - 1) + "ba"

def expected_holes_1based(n, s):
    if s % 2:
        r = (s - 1)//2
        h = {n}
        for j in range(r):
            h.update((4*j + 3, 4*j + 4))
        return h
    r = s//2
    h = {1, n}
    for j in range(1, r):
        h.update((4*j, 4*j + 1))
    return h

def bfs_lambdas(n, upto):
    q0 = frozenset(range(n))
    dist = {q0: 0}
    q = deque([q0])
    ans = [None]*(upto + 1)
    while q and any(ans[s] is None for s in range(1, upto + 1)):
        S = q.popleft()
        d = dist[S]
        deficiency = n - len(S)
        for s in range(1, min(deficiency, upto) + 1):
            if ans[s] is None:
                ans[s] = d
        for c in "ab":
            T = image(n, S, c)
            if T not in dist:
                dist[T] = d + 1
                q.append(T)
    return ans

def main():
    # Exact power-automaton minima on all odd sizes through 17 states.
    for n in range(5, 18, 2):
        h = (n + 1)//2
        lam = bfs_lambdas(n, h)
        want = [None] + [expected(s) for s in range(1, h + 1)]
        assert lam == want, (n, lam, want)

    # Direct all-parameter witness and hole-formula replay through n=301.
    for n in range(5, 302, 2):
        h = (n + 1)//2
        for s in range(1, h + 1):
            w = witness(s)
            assert len(w) == expected(s), (n, s, len(w), expected(s))
            im = act(n, w)
            holes = {x + 1 for x in range(n) if x not in im}
            assert holes == expected_holes_1based(n, s), (n, s, holes, expected_holes_1based(n,s))
            assert len(im) == n - s
    print("BFS_ODD_N_5_TO_17_OK")
    print("WITNESS_AND_HOLE_FORMULA_ODD_N_5_TO_301_OK")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
