"""Standalone integer-only checks for two-denomination upgrade allocation.

Usage: python verify_two_size_upgrades.py
Every tested prefix is checked against an independently enumerated MMS and
against both agents' itemwise-injection and EFX conditions.
"""
from functools import lru_cache
from itertools import product

@lru_cache(None)
def mms(r, H, L):
    return max(min(r * h + l, r * (H - h) + (L - l))
               for h in range(H + 1) for l in range(L + 1))


def delta(r, L):
    return max(d for d in range(min(r, L) + 1) if (d - L) % 2 == 0)


def advance(r, state, incoming):
    # State is (high_agent_0, high_agent_1, low_agent_0, low_agent_1).
    h = list(state[:2]); l = list(state[2:]); H = sum(h); L = sum(l)
    if incoming == 1:
        if H % 2 == 0:
            receiver = 0 if l[0] <= l[1] else 1
        else:
            high_rich = 0 if h[0] > h[1] else 1
            receiver = 1 - high_rich if delta(r, L + 1) > delta(r, L) else high_rich
        l[receiver] += 1
    else:
        assert incoming == r
        if H % 2 == 0:
            receiver = 0 if l[0] <= l[1] else 1
            move = (delta(r, L) - (L % 2)) // 2
        else:
            receiver = 0 if h[0] < h[1] else 1
            move = (delta(r, L) - (L % 2)) // 2
        assert 0 <= move <= 1
        assert l[receiver] >= move
        h[receiver] += 1
        l[receiver] -= move
        l[1 - receiver] += move
    after = (h[0], h[1], l[0], l[1])
    # For two denominations, existence of an itemwise upgrade injection is
    # equivalent to these high-good and total-cardinality inequalities.
    for i in (0, 1):
        assert after[i] >= state[i]
        assert after[i] + after[2 + i] >= state[i] + state[2 + i]
    H1 = sum(after[:2]); L1 = sum(after[2:])
    assert H1 == H + (incoming == r) and L1 == L + (incoming == 1)
    values = [r * after[i] + after[2 + i] for i in (0, 1)]
    mu = mms(r, H1, L1)
    assert min(values) == mu
    # For each agent i, EFX requires the weaker agent's total to exceed the
    # other bundle's value after *each* positively valued good is removed.
    for i in (0, 1):
        j = 1 - i
        if after[j]:
            assert values[i] >= values[j] - r
        if after[2 + j]:
            assert values[i] >= values[j] - 1
    return after


def run_all(max_depth=14):
    nodes = 0
    terminal_histories = 0
    for r in (2, 3):
        for word in product((1, r), repeat=max_depth):
            state = (0, 0, 0, 0)
            for item in word:
                state = advance(r, state, item)
                nodes += 1
            terminal_histories += 1
    # Independent obstruction: after four unit goods, exact MMS forces a
    # 2-to-2 distribution. With one new good of size >=4, every exact MMS
    # allocation must put the large good alone and all four units opposite.
    for r in range(4, 31):
        assert mms(r, 0, 4) == 2
        assert mms(r, 1, 4) == 4
        allowed = []
        for old_l0 in range(5):
            old_l1 = 4 - old_l0
            if min(old_l0, old_l1) < 2:
                continue
            for new_h0 in (0, 1):
                new_h1 = 1 - new_h0
                for new_l0 in range(5):
                    new_l1 = 4 - new_l0
                    if min(r * new_h0 + new_l0, r * new_h1 + new_l1) < 4:
                        continue
                    if (new_h0 + new_l0 >= old_l0 and
                            new_h1 + new_l1 >= old_l1):
                        allowed.append((r, old_l0, new_h0, new_l0))
        assert not allowed
    print(f"VERIFY_OK histories={terminal_histories} prefix_checks={nodes} "
          "ratios=2,3 obstruction_ratios=4..30")

if __name__ == '__main__':
    run_all()
