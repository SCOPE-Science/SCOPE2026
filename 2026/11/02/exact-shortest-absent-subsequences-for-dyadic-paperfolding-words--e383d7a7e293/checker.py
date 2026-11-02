"""Finite transfer proof checks and independent small-instance tests.

Run: python3 checker.py. Uses only the Python standard library.
"""
from functools import lru_cache
from itertools import product

ALPHABET = "01"
PREFIX = "110110011100100"
MIDDLE = "110110001100100"
BLOCKS = [PREFIX + a + MIDDLE + b for a, b in product(ALPHABET, repeat=2)]
PAT = {"00" + a + "011001" + b + "11" for a, b in product(ALPHABET, repeat=2)}
assert len(PREFIX) == len(MIDDLE) == 15
assert all(len(b) == 32 and b[:3] == "110" for b in BLOCKS)
assert all(len(p) == 12 for p in PAT)


def suffix_absence(word):
    """Independent exact greedy-subsequence recurrence at every suffix."""
    n = len(word)
    nxt = [[n, n] for _ in range(n + 1)]
    for j in range(n - 1, -1, -1):
        nxt[j] = nxt[j + 1].copy()
        nxt[j][int(word[j])] = j
    lengths = [1] * (n + 1)
    for j in range(n - 1, -1, -1):
        lengths[j] = min(1 if nxt[j][a] == n else 1 + lengths[nxt[j][a] + 1] for a in (0, 1))

    @lru_cache(None)
    def language(i):
        out = []
        for a in (0, 1):
            t = nxt[i][a]
            if t == n:
                if lengths[i] == 1:
                    out.append(str(a))
            elif 1 + lengths[t + 1] == lengths[i]:
                out += [str(a) + x for x in language(t + 1)]
        return frozenset(out)

    return lengths, language


def symbolic_transfer(block):
    """Formal one-block recurrence. R is a variable residual language.

    The right-hand word starts 110 and satisfies:
       L(0)=L(1)=m, L(3)=m-1,
       S(0)=S(1)={0}R, S(3)=R.
    A set of strings represents the finite prefixes adjoining R.
    All shortest-subsequence recurrences stay inside the 32-letter
    block except for the three indicated right boundary states.
    """
    carrier = block + "110"
    length = {32: 100, 33: 100, 35: 99}
    language = {32: {"0"}, 33: {"0"}, 35: {""}}
    for i in range(31, -1, -1):
        candidates = []
        for bit in ALPHABET:
            j = carrier.index(bit, i) + 1
            assert j in length, (i, bit, j)
            candidates.append((bit, j, 1 + length[j]))
        current_length = min(c[2] for c in candidates)
        current_lang = {bit + residual for bit, j, ln in candidates
                        if ln == current_length for residual in language[j]}
        assert len({len(x) for x in current_lang}) == 1
        length[i] = current_length
        language[i] = current_lang
    return length, language


# Base case, including the suffix-boundary language identity.
for block in BLOCKS:
    length, language = suffix_absence(block)
    expected = PAT if block[-1] == "0" else {u + last for u in PAT for last in ALPHABET}
    assert language(0) == expected
    assert length[0] == (12 if block[-1] == "0" else 13)
    assert length[0] == length[1] == length[2] == length[3] + 1
    assert language(0) == language(1) == frozenset('0' + v for v in language(3))

# Induction step: formally substitute the right-hand language R.
for block in BLOCKS:
    length, language = symbolic_transfer(block)
    output = {u + "0" for u in PAT}
    assert [length[i] - 100 for i in range(6)] == [12, 12, 12, 11, 11, 10]
    assert [len(language[i]) for i in range(6)] == [4, 4, 10, 4, 6, 2]
    assert language[0] == language[1] == output
    assert language[3] == {u[1:] for u in output}

# Independent full-subsequence-automaton checks, all block combinations.
for q in range(1, 4):
    for blocks in product(BLOCKS, repeat=q):
        w = "".join(blocks)
        lengths, language = suffix_absence(w)
        expected = {""}
        for _ in range(q):
            expected = {prefix + x for prefix in expected for x in PAT}
        if blocks[-1][-1] == "1":
            expected = {x + a for x in expected for a in ALPHABET}
        assert language(0) == expected
        assert lengths[0] == len(next(iter(expected)))


def paperfold(n):
    """Rank-n dyadic prefix from its odd-part formula, zero based."""
    out = []
    for j in range(1, (1 << n) + 1):
        m = j
        while m % 2 == 0:
            m //= 2
        out.append("1" if m % 4 == 1 else "0")
    return "".join(out)

# Independent prefix decomposition and linear-time shortest-absence
# distance/count DP for lengths through 2048. No exponential enumeration.
for rank in range(5, 12):
    w = paperfold(rank)
    q = 1 << (rank - 5)
    assert len(w) == 32*q
    assert all(w[i:i+32] in BLOCKS for i in range(0, len(w), 32))
    n = len(w)
    nexts = [[n, n] for _ in range(n+1)]
    for j in range(n-1, -1, -1):
        nexts[j] = nexts[j+1].copy()
        nexts[j][int(w[j])] = j
    min_absent = [1]*(n+1)
    counts = [2]*(n+1)
    for j in range(n-1, -1, -1):
        options = [(1, 1) if nexts[j][a] == n
                   else (1+min_absent[nexts[j][a]+1], counts[nexts[j][a]+1])
                   for a in (0, 1)]
        best = min(x[0] for x in options)
        min_absent[j] = best
        counts[j] = sum(x[1] for x in options if x[0] == best)
    assert w[-1] == '1'
    assert min_absent[0] == 12*q+1
    assert counts[0] == 2*4**q
    print('rank',rank,'length',n,'universality',min_absent[0]-1,'SAS count',counts[0])

print('PASS: four base cases, four symbolic block transfers, 84 block products, seven dyadic prefix ranks')
