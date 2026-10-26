"""Exact enumeration of short-radius endomorphisms of the golden-mean shift.

All statements are proved using finite predecessor graphs; this script reproduces
the complete finite certificates and independently expands the length-21 example.
Run: python verify.py
"""
from collections import Counter, deque
from itertools import product
from pathlib import Path
import csv


def legal_words(n):
    return [''.join(t) for t in product('01', repeat=n)
            if '11' not in ''.join(t)]


def local_bits(mask, w, indices):
    return (mask >> indices[w]) & 1


def preserving_masks(width):
    W = legal_words(width)
    idx = {w: i for i, w in enumerate(W)}
    pair_constraints = [(idx[s[:-1]], idx[s[1:]])
                        for s in legal_words(width + 1)]
    masks = [m for m in range(1 << len(W))
             if all(not ((m >> i & 1) and (m >> j & 1))
                    for i, j in pair_constraints)]
    return W, idx, masks


def shortest_omitted(mask, width):
    """BFS on subsets of predecessor vertices crossed with last output bit.

    Every finite predecessor path extends to a full point of the golden-mean shift
    by appending zeroes at both ends. Thus exactly the output language is tested.
    """
    V = legal_words(width - 1)
    W = legal_words(width)
    vi = {w: i for i, w in enumerate(V)}
    base = [[0, 0] for _ in V]
    for i, w in enumerate(W):
        base[vi[w[:-1]]][(mask >> i) & 1] |= 1 << vi[w[1:]]
    nstates = 1 << len(V)
    subset_next = [[0, 0] for _ in range(nstates)]
    for s in range(1, nstates):
        lb = s & -s
        i = lb.bit_length() - 1
        tail = s ^ lb
        subset_next[s][0] = subset_next[tail][0] | base[i][0]
        subset_next[s][1] = subset_next[tail][1] | base[i][1]

    start = (nstates - 1, 0)
    seen = {start}
    queue = deque([(start[0], start[1], '')])
    while queue:
        s, last, word = queue.popleft()
        for b in (0, 1):
            if last and b:
                continue
            nxt = subset_next[s][b]
            w = word + str(b)
            if nxt == 0:
                return w
            pair = (nxt, b)
            if pair not in seen:
                seen.add(pair)
                queue.append((nxt, b, w))
    return None


def periodic_output(mask, word, idx):
    n = len(word)
    return ''.join(str(local_bits(mask,
        ''.join(word[(i + delta) % n] for delta in range(-2, 3)), idx))
        for i in range(n))


def expanded_length21_language(mask, idx):
    """Independent direct input-block generation (length 25 -> length 21)."""
    block_index = [-1] * 32
    for word, i in idx.items():
        block_index[int(word, 2)] = i
    outputs = set()
    counts = [0]

    def rec(pos, last_four, output_int):
        if pos == 25:
            counts[0] += 1
            outputs.add(output_int)
            return
        for bit in (0, 1):
            if pos and (last_four & 1) and bit:
                continue
            block = ((last_four << 1) | bit) & 31
            new_output = output_int
            if pos >= 4:
                j = block_index[block]
                assert j >= 0
                new_output = (output_int << 1) | ((mask >> j) & 1)
            rec(pos + 1, block & 15, new_output)

    rec(0, 0, 0)
    assert counts[0] == 196418
    return outputs


def all_golden_word_numbers(n):
    def gen(pos, last, val):
        if pos == n:
            yield val
            return
        yield from gen(pos + 1, 0, val << 1)
        if not last:
            yield from gen(pos + 1, 1, (val << 1) | 1)
    return set(gen(0, 0, 0))


def classify():
    W5, idx5, preserving = preserving_masks(5)
    assert W5 == ['00000', '00001', '00010', '00100', '00101',
                  '01000', '01001', '01010', '10000', '10001',
                  '10010', '10100', '10101']
    assert len(legal_words(4)) == 8 and len(legal_words(6)) == 21
    assert len(preserving) == 229
    assert Counter(m.bit_count() for m in preserving) == {
        0: 1, 1: 12, 2: 49, 3: 85, 4: 63, 5: 17, 6: 2}

    omitted = {m: shortest_omitted(m, 5) for m in preserving}
    onto = sorted(m for m, w in omitted.items() if w is None)
    assert onto == [100, 162, 224, 388, 792, 1060,
                    1156, 2570, 4690, 6168, 7936]
    dist = Counter(len(w) for w in omitted.values() if w is not None)
    assert dist == {1: 1, 3: 30, 4: 23, 5: 39, 6: 45, 7: 42,
                    8: 27, 9: 5, 10: 4, 15: 1, 21: 1}
    assert [m for m, w in omitted.items() if w and len(w) == 21] == [4132]

    shifts = {delta: sum(1 << i for i, w in enumerate(W5)
                         if w[delta + 2] == '1')
              for delta in range(-2, 3)}
    assert shifts == {-2: 7936, -1: 224, 0: 6168,
                      1: 1156, 2: 4690}
    assert set(shifts.values()).issubset(onto)
    collision_words = {100: '01', 162: '001', 388: '001',
                       792: '01', 1060: '01', 2570: '01'}
    assert set(onto) - set(shifts.values()) == set(collision_words)
    for m, word in collision_words.items():
        assert periodic_output(m, word, idx5) == '0' * len(word)
        assert periodic_output(m, '0', idx5) == '0'

    W3, _, preserving3 = preserving_masks(3)
    assert len(preserving3) == 7
    onto3 = [m for m in preserving3 if shortest_omitted(m, 3) is None]
    assert onto3 == [4, 18, 24]
    assert W3 == ['000', '001', '010', '100', '101']

    actual21 = expanded_length21_language(4132, idx5)
    all21 = all_golden_word_numbers(21)
    assert len(all21) == 28657
    assert len(actual21) == 28655
    miss21 = sorted(format(m, '021b') for m in all21 - actual21)
    assert miss21 == ['100010010001010010001',
                      '100010010100010010001']
    all20 = {m >> 1 for m in all21}
    image20 = {m >> 1 for m in actual21}
    assert all20 == image20

    outcsv = Path(__file__).resolve().parent / 'classification.csv'
    with outcsv.open(newline='', encoding='utf-8') as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == 229
    expected = [(str(m), 'yes' if omitted[m] is None else 'no',
                 str(len(omitted[m])) if omitted[m] else '',
                 omitted[m] or '') for m in preserving]
    actual = [(r['mask'], r['onto'], r['shortest_missing_length'],
               r['shortest_missing_word']) for r in rows]
    assert actual == expected
    print('VERIFY_OK: 8192 five-site rules, 229 self maps, 11 onto, 5 shifts,')
    print('6 noninjective surjections; all 218 nonsurjections witnessed by length <=21;')
    print('unique sharp mask 4132, 2 missing words of length 21;')
    print('direct 196418 input blocks certify all 28655 image words of length 21;')
    print('radius-one baseline: 7 self maps, exactly 3 onto shifts.')
    return preserving, omitted


if __name__ == '__main__':
    classify()
