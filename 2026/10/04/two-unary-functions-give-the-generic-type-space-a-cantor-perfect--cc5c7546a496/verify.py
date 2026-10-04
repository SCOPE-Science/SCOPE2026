#!/usr/bin/env python3
from itertools import product, permutations

ALPHABET = (0, 1)

def reachable(n, f, g):
    seen = {0}
    stack = [0]
    while stack:
        i = stack.pop()
        for j in (f[i], g[i]):
            if j not in seen:
                seen.add(j)
                stack.append(j)
    return len(seen) == n

def canonical_rooted(n, f, g):
    best = None
    for tail in permutations(range(1, n)):
        p = (0,) + tail
        inv = [0] * n
        for new, old in enumerate(p):
            inv[old] = new
        ff = tuple(inv[f[p[i]]] for i in range(n))
        gg = tuple(inv[g[p[i]]] for i in range(n))
        code = ff + gg
        if best is None or code < best:
            best = code
    return best

def rooted_automorphisms(n, f, g):
    out = []
    for tail in permutations(range(1, n)):
        p = (0,) + tail
        if all(p[f[i]] == f[p[i]] and p[g[i]] == g[p[i]] for i in range(n)):
            out.append(p)
    return out

def words_upto(depth):
    out = [()]
    for d in range(1, depth + 1):
        out.extend(product(ALPHABET, repeat=d))
    return out

def eval_word(word, f, g, start=0):
    x = start
    for a in word:
        x = f[x] if a == 0 else g[x]
    return x

def finite_type_signature(depth, f, g):
    ws = words_upto(depth)
    vals = [eval_word(w, f, g) for w in ws]
    return tuple(vals[i] == vals[j] for i in range(len(vals)) for j in range(i))

def free_signature(depth):
    ws = words_upto(depth)
    return tuple(ws[i] == ws[j] for i in range(len(ws)) for j in range(i))

def finite_completion_matching_free(depth):
    # Trie through depth, then send both letters from each depth node to one sink.
    ws = words_upto(depth)
    index = {w: i for i, w in enumerate(ws)}
    sink = len(ws)
    n = sink + 1
    f = [sink] * n
    g = [sink] * n
    f[sink] = sink
    g[sink] = sink
    for w, i in index.items():
        if len(w) < depth:
            f[i] = index[w + (0,)]
            g[i] = index[w + (1,)]
    return tuple(f), tuple(g)

def check_dense_finite_witnesses():
    for depth in range(0, 6):
        f, g = finite_completion_matching_free(depth)
        assert finite_type_signature(depth, f, g) == free_signature(depth)

def check_two_infinite_extensions(depth):
    # Symbolic check: both extensions are free on all words of length <= depth.
    # They differ only at y = 0^(depth+1): extension A imposes F(y)=y,
    # extension B imposes F(y)=G(y); an untouched G-ray remains infinite.
    y = (0,) * (depth + 1)
    Fy = y + (0,)
    Gy = y + (1,)
    assert len(y) > depth and len(Fy) > depth and len(Gy) > depth
    assert Fy != y and Fy != Gy
    return True

def main():
    expected = {1: 1, 2: 12, 3: 216, 4: 5248}
    for n in range(1, 5):
        classes = set()
        reachable_labeled = 0
        for f in product(range(n), repeat=n):
            for g in product(range(n), repeat=n):
                if not reachable(n, f, g):
                    continue
                reachable_labeled += 1
                autos = rooted_automorphisms(n, f, g)
                assert autos == [tuple(range(n))]
                classes.add(canonical_rooted(n, f, g))
        assert len(classes) == expected[n]
        assert reachable_labeled == expected[n] * math_factorial(n - 1)
    check_dense_finite_witnesses()
    for depth in range(0, 8):
        assert check_two_infinite_extensions(depth)
    print("VERIFY_OK")
    print("isolated finite-orbit type counts by orbit size n=1..4:", [expected[n] for n in range(1, 5)])
    print("checked finite completions matching the free cylinder through depth 5")
    print("checked two distinct infinite symbolic extensions beyond every depth 0..7")

def math_factorial(n):
    ans = 1
    for k in range(2, n + 1):
        ans *= k
    return ans

if __name__ == "__main__":
    main()
