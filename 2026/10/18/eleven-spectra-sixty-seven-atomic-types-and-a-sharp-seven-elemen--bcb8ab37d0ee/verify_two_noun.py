#!/usr/bin/env python3
"""Independent finite checks for the two-noun cardinality syllogistic theorem.

Run: python3 verify_two_noun.py
Standard library only. Counts (a,b,c,d) encode the four Boolean cells
p&q, p&not-q, not-p&q, not-p&not-q in that order.
"""
from collections import Counter

NOUNS = (0b0011, 0b1100, 0b0101, 0b1010)  # p, not-p, q, not-q


def models(n):
    for a in range(n + 1):
        for b in range(n - a + 1):
            for c in range(n - a - b + 1):
                yield a, b, c, n - a - b - c


def sign(z):
    return (z > 0) - (z < 0)


def profile(v):
    a, b, c, d = v
    s, t = b - c, a - d
    return (tuple(int(i > 0) for i in v),
            (sign(s), sign(t), sign(s + t), sign(t - s)))


def full_atomic_signature(v):
    # All 64 sentences: for each ordered noun pair, each of
    # inclusion, nonempty intersection, weak size order, strict size order.
    result = []
    for x in NOUNS:
        card_x = sum(v[i] for i in range(4) if x & (1 << i))
        for y in NOUNS:
            card_y = sum(v[i] for i in range(4) if y & (1 << i))
            result.extend((
                all(v[i] == 0 for i in range(4) if (x & (1 << i)) and not (y & (1 << i))),
                any(v[i] > 0 for i in range(4) if (x & y & (1 << i))),
                card_x >= card_y,
                card_x > card_y,
            ))
    return tuple(result)


def compressed(v):
    # Construct the bounded representative without referring to the atomic tests.
    a, b, c, d = v
    original_s, original_t = b-c, a-d
    if original_s == 0:
        s = 0
    elif original_t == 0:
        s = sign(original_s)
    elif abs(original_s) < abs(original_t):
        s = sign(original_s)
    elif abs(original_s) > abs(original_t):
        s = 2*sign(original_s)
    else:
        s = sign(original_s)
    if original_t == 0:
        t = 0
    elif original_s == 0:
        t = sign(original_t)
    elif abs(original_t) < abs(original_s):
        t = sign(original_t)
    elif abs(original_t) > abs(original_s):
        t = 2*sign(original_t)
    else:
        t = sign(original_t)

    def build_pair(x, y, delta):
        if x and y:
            return 1 + max(delta, 0), 1 + max(-delta, 0)
        if x:
            assert delta > 0
            return delta, 0
        if y:
            assert delta < 0
            return 0, -delta
        assert delta == 0
        return 0, 0

    bb, cc = build_pair(b, c, s)
    aa, dd = build_pair(a, d, t)
    return aa, bb, cc, dd


def four_cells(v):
    return all(x > 0 for x in v)


def example_condition(key, v):
    a, b, c, d = v
    p, pc, q, qc = a+b, c+d, a+c, b+d
    if key == 'T1': return True
    if key == 'T2': return p > 0 and pc > 0
    if key == 'T3': return p > 0 and pc > 0 and p > pc
    if key == 'T4': return four_cells(v)
    if key == 'T5': return four_cells(v) and p > q
    if key == 'T6': return four_cells(v) and p > q and p > qc
    if key == 'T7': return four_cells(v) and p > q and q > qc
    if key == 'E2': return p == pc
    if key == 'E4': return four_cells(v) and p == pc
    if key == 'E6': return four_cells(v) and p > q and q == qc
    raise ValueError(key)


def main():
    first = {}
    raw_by_profile = {}
    profile_by_raw = {}
    for n in range(1, 19):
        for v in models(n):
            prof, raw = profile(v), full_atomic_signature(v)
            compressed_model = compressed(v)
            assert 1 <= sum(compressed_model) <= 7
            assert full_atomic_signature(compressed_model) == raw
            if prof in raw_by_profile:
                assert raw_by_profile[prof] == raw
            else:
                raw_by_profile[prof] = raw
            if raw in profile_by_raw:
                assert profile_by_raw[raw] == prof
            else:
                profile_by_raw[raw] = prof
            first.setdefault(prof, (n, v))
    assert len(first) == len(raw_by_profile) == len(profile_by_raw) == 67
    hist = Counter(n for n, _ in first.values())
    assert dict(sorted(hist.items())) == {1: 4, 2: 6, 3: 16, 4: 9, 5: 20, 6: 4, 7: 8}
    assert 2 * 2 + 2 * 4 + 4 * 2 + 3 * 4 * 4 - 1 == 67

    # These are actual 4-cell cardinalities for the ten nonempty spectra.
    witnesses = {'T1': (1, 0, 0, 0),
                 'T2': (1, 0, 1, 0),
                 'T3': (1, 1, 0, 1),
                 'T4': (1, 1, 1, 1),
                 'T5': (1, 2, 1, 1),
                 'T6': (2, 2, 1, 1),
                 'T7': (3, 2, 1, 1),
                 'E2': (1, 0, 1, 0),
                 'E4': (1, 1, 1, 1),
                 'E6': (2, 2, 1, 1)}
    for key, w in witnesses.items():
        assert example_condition(key, w), (key, w)
        bound = int(key[1:])
        for n in range(1, 19):
            actual = any(example_condition(key, v) for v in models(n))
            expected = n >= bound and (not key.startswith('E') or n % 2 == 0)
            assert actual == expected, (key, n, actual, expected)
    assert not any(example_condition('T7', v) for n in range(1, 7) for v in models(n))
    print('TWO_NOUN_CARDINALITY_VERIFY_OK')
    print('semantic_types=67; least_rep_distribution=' + repr(dict(sorted(hist.items()))))
    print('spectra=empty,T1..T7,E2,E4,E6; sharp_bound=7')


if __name__ == '__main__':
    main()
