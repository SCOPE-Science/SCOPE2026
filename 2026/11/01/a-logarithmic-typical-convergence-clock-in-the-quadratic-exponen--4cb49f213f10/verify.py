"""Reproduce finite checks for directed-cycle-plus-shortcut OR dynamics.

All state-space checks are exhaustive for the stated finite dimensions; they
are sanity checks, not a substitute for the infinite-family proof.
"""
from collections import Counter


def update(state, n):
    mask = (1 << n) - 1
    rotated = ((state << 1) & mask) | (state >> (n - 1))
    if state & (1 << (n - 1)):
        rotated |= 1 << 1
    return rotated


def update_independent(state, n):
    bits = [(state >> i) & 1 for i in range(n)]
    next_bits = [bits[(i - 1) % n] for i in range(n)]
    next_bits[1] = bits[0] | bits[n - 1]
    return sum(bit << i for i, bit in enumerate(next_bits))


def gap(state, n):
    if state == (1 << n) - 1:
        return 0
    if state == 0:
        return n
    run = 0
    best = 0
    for i in range(2 * n):
        if state & (1 << (i % n)):
            run = 0
        else:
            run += 1
            best = max(best, run)
    return min(best, n - 1)


def hit_time(state, n):
    if not state:
        return 0
    target = (1 << n) - 1
    t = 0
    while state != target:
        state = update(state, n)
        t += 1
        assert t <= (n - 1) ** 2 + 1, (n, t)
    return t


def check_exhaustive():
    count = 0
    for n in range(3, 15):
        predicted = (n - 1) ** 2 + 1
        max_t = -1
        maximizers = []
        for s in range(1 << n):
            assert update(s, n) == update_independent(s, n)
            t = hit_time(s, n)
            L = gap(s, n)
            if s:
                assert t <= n * L, (n, s, t, L)
                if L >= 2:
                    assert t > n * (L - 2), (n, s, t, L)
            else:
                assert t == 0
            if t > max_t:
                max_t = t
                maximizers = [s]
            elif t == max_t:
                maximizers.append(s)
            count += 1
        assert max_t == predicted and maximizers == [1], (n, max_t, maximizers)
        for i in range(n):
            assert hit_time(1 << i, n) == predicted - i
    print('EXHAUSTIVE_STATES_OK', count)


def check_walks():
    for n in range(3, 90):
        mask = (1 << n) - 1
        for i in range(n):
            s = 1 << i
            for k in range(n):
                if k:
                    for _ in range(n):
                        s = update(s, n)
                # All k+1 forward sites are covered after k full tours.
                required = 0
                for j in range(k + 1):
                    required |= 1 << ((i + j) % n)
                assert s & required == required, (n, i, k)
    print('BOOL_WALK_INCLUSION_OK')


if __name__ == '__main__':
    check_exhaustive()
    check_walks()
    print('WIELANDT_OR_ALL_CHECKS_PASSED')
