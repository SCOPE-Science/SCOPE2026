from itertools import product

ALPHABET = "012"


def self_nonoverlap(w):
    return all(w[:k] != w[-k:] for k in range(1, len(w)))


def compatible(x, y):
    if x in y or y in x:
        return False
    for k in range(1, min(len(x), len(y)) + 1):
        if x[:k] == y[-k:] or y[:k] == x[-k:]:
            return False
    return True


words = []
for n in range(2, 6):
    for t in product(ALPHABET, repeat=n):
        w = "".join(t)
        if self_nonoverlap(w):
            words.append(w)

N = len(words)
adj = [0] * N
for i in range(N):
    for j in range(i + 1, N):
        if compatible(words[i], words[j]):
            adj[i] |= 1 << j
            adj[j] |= 1 << i


def color_sort(P):
    # Greedy coloring of the induced compatibility graph.  Vertices assigned
    # the same color form an independent set, hence the color number is a
    # rigorous upper bound on the size of any clique in the corresponding
    # remaining prefix of the returned order.
    order, bounds = [], []
    U = P
    color = 0
    while U:
        color += 1
        Q = U
        while Q:
            b = Q & -Q
            v = b.bit_length() - 1
            order.append(v)
            bounds.append(color)
            U &= ~b
            Q &= ~b
            Q &= ~adj[v]
    return order, bounds


def max_clique(P):
    best = []

    def expand(cur, P):
        nonlocal best
        if not P:
            if len(cur) > len(best):
                best = cur[:]
            return
        order, bounds = color_sort(P)
        for idx in range(len(order) - 1, -1, -1):
            if len(cur) + bounds[idx] <= len(best):
                return
            v = order[idx]
            vb = 1 << v
            if P & vb:
                cur.append(v)
                expand(cur, P & adj[v])
                cur.pop()
                P &= ~vb

    expand([], P)
    return best


full = max_clique((1 << N) - 1)
short_indices = [i for i, w in enumerate(words) if len(w) < 5]
best_forced = []
best_short = None
for i in short_indices:
    c = [i] + max_clique(adj[i])
    if len(c) > len(best_forced):
        best_forced = c
        best_short = i

full_words = [words[i] for i in full]
mixed_words = [words[i] for i in best_forced]


def verify_code(code):
    assert len(code) == len(set(code))
    for w in code:
        assert 2 <= len(w) <= 5
        assert self_nonoverlap(w)
    for i, x in enumerate(code):
        for y in code[i + 1:]:
            assert compatible(x, y)


verify_code(full_words)
verify_code(mixed_words)
assert len(full) == 17
assert len(best_forced) == 16
assert any(len(w) < 5 for w in mixed_words)
assert all(len(w) == 5 for w in full_words)

print("candidate_counts=" + repr({n: sum(len(w) == n for w in words) for n in range(2, 6)}))
print("candidate_total=" + str(N))
print("maximum_cardinality=" + str(len(full)))
print("maximum_with_a_short_word=" + str(len(best_forced)))
print("maximum_witness=" + repr(sorted(full_words)))
print("short_word_witness=" + repr(sorted(mixed_words, key=lambda w: (len(w), w))))
print("VERIFY_OK")
