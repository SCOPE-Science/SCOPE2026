#!/usr/bin/env python3
"""Direct integer-state replay of the prescribed traveling-front identity."""

def advance(state, r):
    size = len(state)
    nxt = []
    for i, c in enumerate(state):
        if i < r:
            neighbors = (j for j in range(size) if j != i)
        else:
            neighbors = list(range(r))
            if i > r:
                neighbors.append(i - 1)
            if i + 1 < size:
                neighbors.append(i + 1)
        held = c == 2 and any(state[j] == 1 for j in neighbors)
        nxt.append(c if held else (c + 1) % 3)
    return tuple(nxt)


def expected(r, a, b):
    n = a + b + 1
    stages = []
    for k in range(b):
        m = a + k
        stages += [
            (2,) * r + (2,) * m + (0,) + (1,) * (b - k),
            (2,) * r + (0,) * m + (1,) + (2,) * (b - k),
            (2,) * r + (1,) * m + (2, 2) + (0,) * (b - k - 1),
        ]
    stages += [
        (2,) * r + (2,) * (n - 1) + (0,),
        (0,) * r + (0,) * (n - 1) + (1,),
        (1,) * r + (1,) * (n - 1) + (2,),
        (2,) * (r + n),
    ]
    return stages


def main():
    count = 0
    for r in (1, 3, 11):
        for n in range(2, 29):
            for a in range(1, n):
                b = n - a - 1
                seq = expected(r, a, b)
                assert len(seq) == 3 * (b + 1) + 1
                assert all(len(x) == r + n for x in seq)
                for i, state in enumerate(seq[:-1]):
                    assert len(set(state)) > 1, (r, a, b, i)
                    assert advance(state, r) == seq[i + 1], (r, a, b, i)
                    count += 1
                assert len(set(seq[-1])) == 1
                assert advance(seq[-1], r) == (0,) * (r + n)
    print(f'PASS: {count} consecutive one-step equalities of the claimed wave, all stages nonsynchronous before first sync; r in (1,3,11), 2<=n<=28, 1<=a<n.')
    print('The unbounded proof is the blockwise local-neighborhood induction in RESULT.md; this finite test only checks examples.')

if __name__ == '__main__':
    main()
