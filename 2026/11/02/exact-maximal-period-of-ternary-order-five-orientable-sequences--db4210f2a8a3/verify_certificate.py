"""Exact self-contained certificate for the ternary order-five orientable period bound."""
from collections import Counter
from itertools import product

ALPHABET = '012'
WITNESS = (
    '000011200012212010111201211020021210010120010220210020211212201100221111021020221011222012222'
)
# Dual weights scaled by six; missing entries have weight zero.
PAIR_WEIGHT = {
    '00001': 12, '00012': 1, '00101': 6, '00102': 9,
    '00112': 6, '00120': 5, '00121': 2, '00122': 4,
    '01002': 6, '01012': 9, '01021': 3, '01102': 1,
    '01112': 18, '01120': 7, '01201': 6,
}
VERTEX_POTENTIAL = {
    '0001': -6, '0012': -1, '0102': -3, '0110': -6,
    '0111': 6, '0121': 3, '0122': 1,
}

def pattern(word):
    relabel = {}
    out = []
    for ch in word:
        if ch not in relabel:
            relabel[ch] = str(len(relabel))
        out.append(relabel[ch])
    return ''.join(out)

def pair_type(word):
    return min(pattern(word), pattern(word[::-1]))

def special(vertex):
    return vertex == vertex[::-1] and len(set(vertex)) > 1

def verify_upper_bound():
    words = [''.join(x) for x in product(ALPHABET, repeat=5)]
    nonpal = [w for w in words if w != w[::-1]]
    assert len(words) == 243 and len(nonpal) == 216
    pairs = {min(w, w[::-1]) for w in nonpal}
    assert len(pairs) == 108
    vertices = [''.join(x) for x in product(ALPHABET, repeat=4)]
    exceptional = [v for v in vertices if special(v)]
    assert len(exceptional) == 6
    assert all(sum(w[1:] == v for w in nonpal) == 3 and
               sum(w[:4] == v for w in nonpal) == 3 for v in exceptional)
    for v in exceptional:
        incoming = {w for w in nonpal if w[1:] == v}
        outgoing = {w for w in nonpal if w[:4] == v}
        assert incoming.isdisjoint(outgoing)
        assert {w[::-1] for w in incoming} == outgoing
    types = Counter(pair_type(w) for w in pairs)
    assert sum(types.values()) == 108 and len(types) == 20
    assert set(PAIR_WEIGHT).issubset(types)
    pair_sum = sum(types[k] * PAIR_WEIGHT.get(k, 0) for k in types)
    assert pair_sum == 486
    assert len(set(VERTEX_POTENTIAL)) == len(VERTEX_POTENTIAL)
    for w in nonpal:
        u, v = w[:4], w[1:]
        lhs = (PAIR_WEIGHT.get(pair_type(w), 0)
               + 12 * int(special(v))
               + VERTEX_POTENTIAL.get(pattern(v), 0)
               - VERTEX_POTENTIAL.get(pattern(u), 0))
        assert lhs >= 6, (w, lhs)
    assert (pair_sum + 12 * len(exceptional)) // 6 == 93
    assert pair_sum + 12 * len(exceptional) == 6 * 93
    print('UPPER: 216 edge inequalities, 108 reversal pairs, 6 exceptional vertices checked')
    print('UPPER: pair cap 486 + vertex cap 72 = 558 = 6*93')

def verify_lower_bound():
    assert len(WITNESS) == 93 and set(WITNESS) <= set(ALPHABET)
    windows = [''.join(WITNESS[(i+j) % 93] for j in range(5)) for i in range(93)]
    assert len(set(windows)) == 93
    assert all(x != x[::-1] for x in windows)
    assert not (set(windows) & {x[::-1] for x in windows})
    assert Counter(WITNESS) == Counter({'0':31,'1':31,'2':31})
    assert all(WITNESS != WITNESS[shift:] + WITNESS[:shift]
               for shift in range(1,93))
    print('LOWER: 93 cyclic windows distinct, nonpalindromic, reversal-disjoint')
    print('LOWER: witness has primitive period 93 and composition (31,31,31)')

if __name__ == '__main__':
    verify_upper_bound()
    verify_lower_bound()
    print('THEOREM: maximal ternary order-five orientable period is exactly 93')
