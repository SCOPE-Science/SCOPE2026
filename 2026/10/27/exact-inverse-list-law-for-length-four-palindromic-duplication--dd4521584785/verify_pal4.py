"""Reproducible finite cross-checks for the PAL-4 inverse-parent theorem.
Run: python3 verify_pal4.py
The finite census tests the analytic proof; it is not its replacement.
"""
from itertools import product


def parents(y):
    out = set()
    for i in range(len(y) - 7):
        if y[i:i+4] == y[i+4:i+8][::-1]:
            out.add(y[:i+4] + y[i+8:])
    return out


def proof_overlap_symbolic(shift):
    length = 8 + shift
    father = list(range(length))

    def find(v):
        while father[v] != v:
            v = father[v]
        return v

    def union(a, b):
        father[find(a)] = find(b)

    for start in (0, shift):
        for t in range(4):
            union(start+t, start+7-t)

    reps = [find(j) for j in range(length)]
    first = reps[:4] + reps[8:]
    second = reps[:shift+4] + reps[shift+8:]
    assert first == second, (shift, first, second)
    return len(set(reps))


assert proof_overlap_symbolic(1) == 1
assert proof_overlap_symbolic(2) == 2

cases = 0
for q, max_n in ((2, 14), (3, 8), (4, 6), (5, 5)):
    symbols = tuple(range(q))
    for n in range(4, max_n+1):
        maximum = 0
        for letters in product(symbols, repeat=n+4):
            size = len(parents(letters))
            if size > maximum:
                maximum = size
            assert size <= (n-1)//3, (q, n, letters, size)
            cases += 1
        assert maximum == (n-1)//3, (q, n, maximum)
        print(f'EXHAUSTIVE q={q} n={n} maximum={maximum}')

for n in range(4, 301):
    for a, b in ((0, 1), (1, 0)):
        word = tuple((a, a, b)[j % 3] for j in range(n+4))
        assert len(parents(word)) == (n-1)//3
print(f'VERIFY_OK: {cases} exhaustively tested output words and 594 long construction checks')
