#!/usr/bin/env python3
"""Exact finite certificates for synchronous three-state excitation on square bouquets."""
from itertools import product

STATES = (0, 1, 2)
TRIPLES = list(product(STATES, repeat=3))


def next_color(x, has_excited_neighbor):
    if x == 1:
        return 2
    if x == 2:
        return 0
    return int(has_excited_neighbor)


def petal_step(h, triple):
    a, b, c = triple
    return (
        next_color(a, h == 1 or b == 1),
        next_color(b, a == 1 or c == 1),
        next_color(c, b == 1 or h == 1),
    )


def local_winding(values):
    def delta(x, y):
        return int(x == 0 and y == 1) - int(x == 1 and y == 0)
    return sum(delta(values[i], values[(i + 1) % 4]) for i in range(4))


def permitted_hub_next(h, a, c):
    if h == 1:
        return (2,)
    if h == 2:
        return (0,)
    return (1,) if (a == 1 or c == 1) else (0, 1)


def hub_words(length):
    def walk(prefix):
        if len(prefix) == length:
            yield tuple(prefix)
            return
        h = prefix[-1]
        for hh in ((0, 1) if h == 0 else (2,) if h == 1 else (0,)):
            yield from walk(prefix + [hh])
    for h in STATES:
        yield from walk([h])


def trace(h_word, triple):
    xs = [triple]
    for h in h_word[:-1]:
        xs.append(petal_step(h, xs[-1]))
    return xs


def hub_feasibility(word):
    zeros = [t for t in range(len(word) - 1) if word[t] == 0 and word[t + 1] == 0]
    ones = [t for t in range(len(word) - 1) if word[t] == 0 and word[t + 1] == 1]
    allowed = []
    for triple in TRIPLES:
        xs = trace(word, triple)
        if all(xs[t][0] != 1 and xs[t][2] != 1 for t in zeros):
            allowed.append((triple, xs))
    ok = bool(allowed) and all(
        any(xs[t][0] == 1 or xs[t][2] == 1 for _, xs in allowed)
        for t in ones
    )
    return ok, allowed


def phase_condition(phase):
    h, a, b, c = phase
    p = (h, a, b, c)
    ns = ((1, 3), (0, 2), (1, 3), (0, 2))
    return all(
        all(p[w] != (p[v] + 2) % 4 for w in ns[v])
        for v in range(4)
    ) and all(
        any(p[w] == (p[v] - 1) % 4 for w in ns[v])
        for v in (1, 2, 3)
    )


def all_states_small(k):
    n = 3 * k + 1
    def step(s):
        h = s[0]
        petals = [s[1 + 3 * j:4 + 3 * j] for j in range(k)]
        hn = next_color(h, any(a == 1 or c == 1 for a, b, c in petals))
        return (hn,) + tuple(x for p in petals for x in petal_step(h, p))
    for s in product(STATES, repeat=n):
        yield s, step


def main():
    checks = 0
    count_zero = []
    for h in STATES:
        hist = {w: 0 for w in (-1, 0, 1)}
        for triple in TRIPLES:
            hist[local_winding((h,) + triple)] += 1
        assert hist == {-1: 4, 0: 19, 1: 4}
        count_zero.append(hist[0])
    print('WINDING_HISTOGRAM_OK', count_zero)

    # Every petal-local configuration and every globally possible hub successor.
    for h, a, b, c in product(STATES, repeat=4):
        following = petal_step(h, (a, b, c))
        for hh in permitted_hub_next(h, a, c):
            assert local_winding((h, a, b, c)) == local_winding((hh,) + following)
            checks += 1
    print('WINDING_INVARIANCE_OK', checks, 'local transitions')

    profiles = [triple for triple in product(range(4), repeat=3) if phase_condition((0,) + triple)]
    assert profiles == [(1, 2, 1), (1, 2, 3), (3, 2, 1)]
    print('PHASE_LOCAL_PROFILES_OK', profiles)

    finite_words = []
    for word in hub_words(11):
        feasible, allowed = hub_feasibility(word)
        if not feasible:
            continue
        assert word[6] == word[10]
        assert all(xs[6] == xs[10] for _, xs in allowed)
        finite_words.append((''.join(map(str, word)), len(allowed)))
    expected_words = [
        ('00000000000', 9), ('00120000000', 10), ('00120012001', 12),
        ('01200000000', 19), ('01200120012', 27), ('12000000000', 19),
        ('12001200120', 25), ('12012001200', 27), ('20000000000', 18),
        ('20012001200', 22), ('20120000000', 19), ('20120012001', 27),
    ]
    assert finite_words == expected_words
    print('HUB_TRACE_CLASSIFICATION_OK', len(finite_words))
    print('hub_word_0_to_10,admissible_petal_types')
    for word, k in finite_words:
        print(word, k, sep=',')

    n1 = 0
    for s, step in all_states_small(1):
        x = s
        seq = [x]
        for i in range(8):
            x = step(x)
            seq.append(x)
        assert seq[4] == seq[8]
        n1 += 1
    assert n1 == 81
    print('ONE_PETAL_F8_EQUALS_F4_OK', n1)
    for k, example, t in [
        (1, (0, 0, 0, 1), 4),
        (2, (0, 0, 0, 0, 0, 1, 0), 6),
        (3, (0, 0, 0, 0, 0, 1, 0, 0, 0, 0), 6),
    ]:
        x = example
        history = [x]
        _, step = next(all_states_small(k))
        for _ in range(t + 4):
            x = step(x)
            history.append(x)
        assert history[t] == history[t+4]
        assert history[t - 1] != history[t + 3]
        print('SHARP_WITNESS_OK', k, t, ''.join(map(str, example)))
    print('FINITE_CERTIFICATE_OK')

if __name__ == '__main__':
    main()
