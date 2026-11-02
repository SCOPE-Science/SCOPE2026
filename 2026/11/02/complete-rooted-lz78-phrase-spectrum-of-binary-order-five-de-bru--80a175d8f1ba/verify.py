#!/usr/bin/env python3
"""Self-contained exhaustive verifier for order-five binary de Bruijn LZ78 profiles.

Use: python3 verify.py
Only Python standard library is needed. Assertions are the finite certificate.
"""
from collections import Counter
from hashlib import sha256

ORDER = 5
PERIOD = 1 << ORDER


def canonical(word):
    assert len(word) == PERIOD
    i = (word + word).find('00000')
    assert 0 <= i < PERIOD
    w = (word + word)[i:i + PERIOD]
    assert w[:5] == '00000'
    assert len({(w + w)[j:j+5] for j in range(PERIOD)}) == PERIOD
    return w


def feedback_cycles():
    """All successor permutations on five-bit states with one orbit."""
    words = []
    count = 0
    for m in range(1 << 16):
        state = 0
        visited = 0
        bits = []
        for _ in range(PERIOD):
            if (visited >> state) & 1:
                break
            visited |= 1 << state
            bits.append(str((state >> 4) & 1))
            tail = state & 15
            nxt = ((state >> 4) & 1) ^ ((m >> tail) & 1)
            state = (tail << 1) | nxt
        if len(bits) == PERIOD and state == 0:
            count += 1
            words.append(canonical(''.join(bits)))
    assert count == 2048 and len(set(words)) == count
    return set(words)


def euler_cycles():
    """Independent directed-Euler-trail enumeration on the 16 four-bit vertices.

    Fix the edge 00000 to be first, ensuring one trail per cyclic de Bruijn word.
    """
    words = set()
    raw_tours = 0
    def visit(vertex, used, edge_bits):
        nonlocal raw_tours
        if used.bit_count() == PERIOD:
            if vertex == 0:
                raw_tours += 1
                w = canonical(edge_bits[-4:] + edge_bits[:-4])
                words.add(w)
            return
        for bit in (0, 1):
            edge = 2 * vertex + bit
            if not ((used >> edge) & 1):
                visit(edge & 15, used | (1 << edge), edge_bits + str(bit))
    visit(0, 1, '0')
    assert raw_tours == 2048 and len(words) == raw_tours
    return words


def parse_set(word):
    """Incremental LZ78 with a possible already-known final phrase."""
    seen = set()
    phrases = []
    pos = 0
    while pos < len(word):
        end = pos + 1
        while end <= len(word) and word[pos:end] in seen:
            end += 1
        if end > len(word):
            phrases.append(word[pos:])
            break
        phrase = word[pos:end]
        if len(phrase) > 1:
            assert phrase[:-1] in seen
        assert phrase not in seen
        seen.add(phrase)
        phrases.append(phrase)
        pos = end
    assert ''.join(phrases) == word
    assert len(set(phrases[:-1])) == len(phrases)-1
    return len(phrases)


def parse_trie(word):
    """Independent longest-known-trie-path parser, including terminal suffix."""
    root = {}
    i = 0
    count = 0
    while i < len(word):
        p = root
        j = i
        while j < len(word) and word[j] in p:
            p = p[word[j]]
            j += 1
        count += 1
        if j == len(word):
            break
        p[word[j]] = {}
        i = j + 1
    return count


EXPECTED_ROOT = {11:80, 12:7586, 13:55690, 14:2180}
EXPECTED_MIN = {11:50, 12:1918, 13:80}
EXPECTED_MAX = {13:782, 14:1266}
EXPECTED_JOINT = {
    (11,13):6, (11,14):44, (12,13):746,
    (12,14):1172, (13,13):30, (13,14):50,
}


def main():
    a = feedback_cycles()
    b = euler_cycles()
    assert a == b
    roots = Counter()
    minimums = Counter()
    maximums = Counter()
    joints = Counter()
    hashed_rows = []
    witnesses = {}
    for word in sorted(a):
        vals = []
        doubled = word + word
        for i in range(PERIOD):
            root = doubled[i:i+PERIOD]
            s = parse_set(root)
            t = parse_trie(root)
            assert s == t
            roots[s] += 1
            vals.append(s)
        m, M = min(vals), max(vals)
        minimums[m] += 1
        maximums[M] += 1
        joints[(m,M)] += 1
        witnesses.setdefault((m,M), word)
        hashed_rows.append(word + '\t' + ''.join(str(v-10) for v in vals) + '\n')
    assert dict(roots) == EXPECTED_ROOT, roots
    assert dict(minimums) == EXPECTED_MIN, minimums
    assert dict(maximums) == EXPECTED_MAX, maximums
    assert dict(joints) == EXPECTED_JOINT, joints
    assert sum(roots.values()) == 2048 * PERIOD == 65536
    checksum = sha256(''.join(hashed_rows).encode('ascii')).hexdigest()
    print('VERIFY_OK')
    print('cycles', len(a), 'rooted traversals', sum(roots.values()))
    print('LZ78 rooted', sorted(roots.items()))
    print('LZ78 cycle minima', sorted(minimums.items()))
    print('LZ78 cycle maxima', sorted(maximums.items()))
    print('LZ78 per-cycle (minimum,maximum)', sorted(joints.items()))
    print('row_hash', checksum)
    for key in sorted(witnesses):
        print('example', key, witnesses[key])

if __name__ == '__main__':
    main()
