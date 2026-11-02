"""Exact finite-state certificate for the even-one-run binary sumset.
Run with Python 3 standard library: python3 verify.py
"""
from collections import deque

BITS = (0, 1)
START = (0, 0, 0)  # parity of currently open one-runs of x,y; carry


def run_step(parity, digit):
    if digit:
        return 1 - parity
    return 0 if parity == 0 else None


def next_states(state, output):
    px, py, carry = state
    targets = set()
    for x in BITS:
        for y in BITS:
            t = x + y + carry
            if t % 2 != output:
                continue
            qx, qy = run_step(px, x), run_step(py, y)
            if qx is not None and qy is not None:
                targets.add((qx, qy, t // 2))
    return targets


def successors(configuration, output):
    subset, mod3, digit_parity = configuration
    new_subset = frozenset(
        new_state for state in subset
        for new_state in next_states(state, output)
    )
    return (new_subset, (mod3 + output * (1 if digit_parity == 0 else -1)) % 3,
            1 - digit_parity)


def verify_finite_automaton():
    first = (frozenset([START]), 0, 0)
    queue = deque([first])
    index = {first: 0}
    pairs = []
    while queue:
        q = queue.popleft()
        assert (START in q[0]) == (q[1] == 0), (
            'An integer with residue zero is not accepted, or vice versa', q)
        targets = []
        for digit in BITS:
            target = successors(q, digit)
            if target not in index:
                index[target] = len(index)
                queue.append(target)
            targets.append(index[target])
        pairs.append(tuple(targets))
    assert len(index) == 10, len(index)
    assert pairs == [
        (1, 2), (3, 4), (5, 0), (1, 6), (7, 1),
        (8, 7), (5, 3), (9, 5), (5, 3), (7, 1)
    ], pairs
    state_order = sorted(index, key=index.get)
    print('EXACT_DFA_OK reachable_states=10')
    for n, q in enumerate(state_order):
        print('STATE', n, 'NFA_SUBSET', sorted(q[0]), 'MOD3', q[1],
              'BIT_PARITY', q[2], 'NEXT0_NEXT1', pairs[n])


def eligible(n):
    if n < 0:
        return False
    previous = 0
    parity = 0
    while n:
        digit = n & 1
        if not digit and previous == 1 and parity:
            return False
        if digit:
            parity ^= 1
        else:
            parity = 0
        previous = digit
        n >>= 1
    return parity == 0


def independently_test_small_numbers(bound=16384):
    allowed = [n for n in range(bound) if eligible(n)]
    hit = bytearray(bound)
    for a in allowed:
        for b in allowed:
            s = a+b
            if s < bound:
                hit[s] = 1
            elif b >= bound-a:
                break
    for n in range(bound):
        assert bool(hit[n]) == (n % 3 == 0), n
    assert eligible(0) and eligible(3) and eligible(6)
    assert not eligible(9)
    print('DIRECT_ENUMERATION_OK limit=', bound, 'eligible_count=', len(allowed))


if __name__ == '__main__':
    verify_finite_automaton()
    independently_test_small_numbers()
    print('VERIFY_OK')
