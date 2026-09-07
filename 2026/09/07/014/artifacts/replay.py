"""Independent replay verifier: pure 2x2 matmul mod 13, stdlib only. Runs in seconds.
Checks: orders, w_g identity+minimality (L<=5 exhaustion), w_D value + maximality (BFS),
sphere distribution, degree, generation.
"""
from collections import deque

P = 13

def mm(A, B):
    return ((A[0]*B[0]+A[1]*B[2]) % P,
            (A[0]*B[1]+A[1]*B[3]) % P,
            (A[2]*B[0]+A[3]*B[2]) % P,
            (A[2]*B[1]+A[3]*B[3]) % P)

def neg(A):
    return ((-A[0]) % P, (-A[1]) % P, (-A[2]) % P, (-A[3]) % P)

def canon(A):
    B = neg(A)
    return A if A < B else B

a = (1, 1, 0, 1); b = (1, 0, 1, 1); ainv = (1, 12, 0, 1); binv = (1, 0, 12, 1)
GDICT = {'a': a, 'A': ainv, 'b': b, 'B': binv}
INV = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
I = (1, 0, 0, 1); NEGI = (12, 0, 0, 12)
W_D = "aaaaabbbba"
W_D_TARGET = (5, 0, 9, 8)
W_G = "aaBaaB"
SPHERES = [1, 4, 12, 25, 48, 96, 180, 279, 317, 120, 10]

def evalw(w):
    M = I
    for ch in w:
        M = mm(M, GDICT[ch])
    return M

def main():
    # 1. group order by brute force (28561 det checks)
    n = sum(1 for x0 in range(P) for x1 in range(P) for x2 in range(P) for x3 in range(P)
            if (x0*x3 - x1*x2) % P == 1)
    assert n == 2184, n
    print("PASS order SL(2,13)=2184, PSL=1092 (formula q(q^2-1))")
    # 2. generator inverses
    assert mm(a, ainv) == I and mm(b, binv) == I
    print("PASS inverses")
    # 3. girth witness replays
    assert all(W_G[i+1] != INV[W_G[i]] for i in range(len(W_G)-1)), "w_g not reduced"
    assert evalw(W_G) == NEGI, evalw(W_G)
    print("PASS w_g=%s -> -I (identity in PSL), reduced, length 6" % W_G)
    # 4. girth minimality: exhaustive reduced words L=1..5, expect 4+12+36+108+324=484 words, 0 hits
    for L in range(1, 6):
        stack = [(I, '', None)]
        total = 0
        while stack:
            prod, w, last = stack.pop()
            if len(w) == L:
                total += 1
                assert not (prod == I or prod == NEGI), "unexpected identity at L=%d: %s" % (L, w)
                continue
            for ch, G in GDICT.items():
                if last is not None and ch == INV[last]:
                    continue
                stack.append((mm(prod, G), w + ch, ch))
        expect = 4 * (3 ** (L-1))
        assert total == expect, (L, total, expect)
    print("PASS girth lower bound: no reduced identity word of length<=5 (484 words checked)")
    # 5. L=6 count cross-check (972 words, 28 hits)
    stack = [(I, '', None)]
    total = 0; hits = 0
    while stack:
        prod, w, last = stack.pop()
        if len(w) == 6:
            total += 1
            if prod == I or prod == NEGI:
                hits += 1
            continue
        for ch, G in GDICT.items():
            if last is not None and ch == INV[last]:
                continue
            stack.append((mm(prod, G), w + ch, ch))
    assert (total, hits) == (972, 28), (total, hits)
    print("PASS L=6 census: 972 reduced words, 28 identities => girth exactly 6")
    # 6. BFS diameter replay (different neighbor order than census script)
    start = canon(I)
    dist = {start: 0}
    q = deque([start])
    parent = {}
    order = ['B', 'b', 'A', 'a']
    while q:
        u = q.popleft()
        for ch in order:
            v = canon(mm(u, GDICT[ch]))
            if v not in dist:
                dist[v] = dist[u] + 1
                parent[v] = u
                q.append(v)
    assert len(dist) == 1092, len(dist)
    D = max(dist.values())
    spheres = [sum(1 for v in dist if dist[v] == i) for i in range(D+1)]
    assert spheres == SPHERES, spheres
    assert D == 10
    assert sum(1 for v in dist if dist[v] <= 9) == 1082
    print("PASS BFS covers 1092; spheres=%s; D=10" % (spheres,))
    # 7. w_D replays and is maximal
    assert len(W_D) == 10
    assert canon(evalw(W_D)) == W_D_TARGET, canon(evalw(W_D))
    assert dist[W_D_TARGET] == 10, dist[W_D_TARGET]
    print("PASS w_D=%s -> %s at distance 10" % (W_D, W_D_TARGET))
    # 8. no reduced word<=9 attains target (independent word-tree search)
    stack = [(I, '', None)]
    found = False
    while stack:
        prod, w, last = stack.pop()
        if canon(prod) == W_D_TARGET and len(w) > 0:
            # start itself is not target; any hit with len<=9 disproves maximality
            found = True
            print("FAIL shorter word to target:", w)
            break
        if len(w) >= 9:
            continue
        for ch, G in GDICT.items():
            if last is not None and ch == INV[last]:
                continue
            stack.append((mm(prod, G), w + ch, ch))
    assert not found, "target reached in <=9 steps"
    print("PASS maximality: no reduced word of length<=9 equals w_D target")
    # 9. degree / generation
    assert len(set(canon(mm(start, G)) for G in GDICT.values())) == 4
    print("PASS 4-regular, connected => <a,b>=G")
    print("ALL REPLAY CHECKS PASSED")

if __name__ == "__main__":
    main()
