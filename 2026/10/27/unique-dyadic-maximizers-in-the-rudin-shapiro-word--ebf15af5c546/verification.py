"""Exact recurrence checks for the dyadic Rudin-Shapiro extremizer theorem.

The proof in RESULT.md is inductive. This script independently checks the
base/recurrence implementation, the displayed G-matrices, legal-pair maximum,
and argmax-offset formulas for k=2,...,20. It is a finite consistency check,
not the proof of the all-k theorem.
"""
SIGMA = {"a": "ab", "b": "ac", "c": "db", "d": "dc"}
TAU = {"a": 1, "b": 1, "c": -1, "d": -1}
LEGAL_PAIRS = {tuple(p) for p in ("ab", "ac", "ba", "bd", "ca", "cd", "db", "dc")}
LETTERS = "abcd"

T = TAU.copy()
G = {(x, y): max(TAU[x], TAU[y]) for x in LETTERS for y in LETTERS}
J = {
    (x, y): ([0] if TAU[x] > TAU[y] else [1] if TAU[y] > TAU[x] else [0, 1])
    for x in LETTERS for y in LETTERS
}

for k in range(1, 21):
    old_t, old_g, old_j = T.copy(), G.copy(), J.copy()
    half = 2 ** (k - 1)
    T = {x: old_t[SIGMA[x][0]] + old_t[SIGMA[x][1]] for x in LETTERS}
    G, J = {}, {}
    for x in LETTERS:
        u, v = SIGMA[x]
        for y in LETTERS:
            s, t = SIGMA[y]
            left = old_t[v] + old_g[(u, s)]
            right = old_t[s] + old_g[(v, t)]
            G[(x, y)] = max(left, right)
            offsets = []
            if left == G[(x, y)]:
                offsets.extend(old_j[(u, s)])
            if right == G[(x, y)]:
                offsets.extend(half + z for z in old_j[(v, t)])
            J[(x, y)] = sorted(set(offsets))

    if k < 2:
        continue
    tval = 2 ** (k // 2) if k % 2 == 0 else 2 ** ((k + 1) // 2)
    if k % 2 == 0:
        expected_t = {"a": tval, "b": tval, "c": -tval, "d": -tval}
        expected_g = [
            [tval, tval, tval, tval],
            [3 * tval - 2, tval, tval, tval],
            [tval, tval, -tval, -tval],
            [3 * tval - 2, tval, tval - 2, -tval],
        ]
        target, auxiliary = ("b", "a"), ("d", "a")
    else:
        expected_t = {"a": tval, "b": 0, "c": 0, "d": -tval}
        expected_g = [
            [tval, tval, tval, tval],
            [tval, 0, 0, 0],
            [2 * tval - 2, 2 * tval - 2, 0, 0],
            [tval, tval - 2, 0, -tval],
        ]
        target, auxiliary = ("c", "a"), ("c", "b")
    assert T == expected_t, (k, T, expected_t)
    assert [[G[(x, y)] for y in LETTERS] for x in LETTERS] == expected_g, k
    j_expected = (2 * 4 ** (k // 2) + 1) // 3
    assert J[target] == [j_expected], (k, target, J[target], j_expected)
    assert J[auxiliary] == [j_expected], (k, auxiliary, J[auxiliary], j_expected)
    best = max(G[pair] for pair in LEGAL_PAIRS)
    maximizers = sorted("".join(pair) for pair in LEGAL_PAIRS if G[pair] == best)
    assert maximizers == ["".join(target)], (k, maximizers, target)

print("PASS: recurrence matrices, unique legal maximizing pair, and unique offset for k=2..20")
