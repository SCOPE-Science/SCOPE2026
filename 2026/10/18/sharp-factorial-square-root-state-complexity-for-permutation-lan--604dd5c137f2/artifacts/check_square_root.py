#!/usr/bin/env python3
"""Finite, exact checks for the deterministic square-root construction.

No external packages. The general theorem rests on the accompanying proof.
"""
from itertools import permutations
from math import factorial


def compose(p, q):
    """Composition p after q, with permutations as image tuples."""
    return tuple(p[q[i]] for i in range(len(p)))


def verify(n):
    identity = tuple(range(n))
    cycle = tuple((i + 1) % n for i in range(n))
    swap = list(range(n))
    swap[0], swap[1] = swap[1], swap[0]
    swap = tuple(swap)

    # Verify the binary generators reach every permutation.
    orbit = {identity}
    queue = [identity]
    for g in queue:
        for letter in (cycle, swap):
            nxt = compose(letter, g)
            if nxt not in orbit:
                orbit.add(nxt)
                queue.append(nxt)
    assert len(orbit) == factorial(n)

    # Original n-state machine: reachability and pairwise distinguishability.
    states = {g[0] for g in orbit}
    assert states == set(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            assert any((g[i] == 0) != (g[j] == 0) for g in orbit)

    # Square-root accepts exactly the group elements squaring 0 to 0.
    accepted = {g for g in orbit if g[g[0]] == 0}
    # The Cayley-state equivalences are right translations preserving accepted.
    stabilizer = [h for h in orbit if all((compose(t,h) in accepted) == (t in accepted) for t in orbit)]
    expected = 1 if n <= 2 else factorial(n)
    assert len(orbit) // len(stabilizer) == expected
    assert len(stabilizer) == (factorial(n) if n <= 2 else 1)
    # Stronger direct separation of each pair for n <= 5.
    if 3 <= n <= 5:
        for g in orbit:
            for h in orbit:
                if g == h:
                    continue
                assert any((compose(t,g) in accepted) != (compose(t,h) in accepted) for t in orbit)
    print(f'n={n} generators={len(orbit)} original_states={len(states)} accepted_permutations={len(accepted)} '
          f'right_stabilizer={len(stabilizer)} min_root_DFA={len(orbit)//len(stabilizer)}')


if __name__ == '__main__':
    for size in range(2, 7):
        verify(size)
    print('ALL CHECKS PASSED')
