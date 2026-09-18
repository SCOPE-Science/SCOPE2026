#!/usr/bin/env python3
"""Finite sanity checks for two neutral-letter examples used in the QEACom note."""

from itertools import product


def compose(f, g):
    """Transformation for first applying f, then g."""
    return tuple(g[i] for i in f)


def generated_monoid(generators, nstates):
    ident = tuple(range(nstates))
    seen = {ident}
    todo = [ident]
    gens = list(generators.values())
    while todo:
        x = todo.pop()
        for g in gens:
            y = compose(x, g)
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return seen


def is_aperiodic(monoid):
    for x in monoid:
        y = x
        found = False
        for _ in range(1, len(monoid) + 2):
            yy = compose(y, x)
            if yy == y:
                found = True
                break
            y = yy
        if not found:
            return False
    return True


def is_commutative(monoid):
    return all(compose(x, y) == compose(y, x) for x in monoid for y in monoid)


def threshold_example():
    # States record min(number of a's, 2).  '$' is neutral.
    gens = {
        'a': (1, 2, 2),
        '$': (0, 1, 2),
    }
    monoid = generated_monoid(gens, 3)
    assert is_aperiodic(monoid)
    assert is_commutative(monoid)
    assert compose(gens['a'], gens['a']) != gens['a']
    return len(monoid)


def forbidden_erasure_example():
    # Accept every nonempty word except those whose deletion of '$' is exactly 'acd'.
    # States 0,1,2,3 track exact prefixes '', 'a', 'ac', 'acd'; 4 is mismatch/extra.
    target = 'acd'
    n = len(target)
    dead = n + 1
    gens = {}
    for ch in 'acd$':
        trans = []
        for s in range(n + 2):
            if ch == '$':
                ns = s
            elif s == dead:
                ns = dead
            elif s < n and ch == target[s]:
                ns = s + 1
            else:
                ns = dead
            trans.append(ns)
        gens[ch] = tuple(trans)
    monoid = generated_monoid(gens, n + 2)
    assert gens['$'] == tuple(range(n + 2))
    assert is_aperiodic(monoid)
    assert not is_commutative(monoid)
    cd = compose(gens['c'], gens['d'])
    dc = compose(gens['d'], gens['c'])
    assert cd != dc
    # After reading prefix 'a', 'cd' ends at the unique rejecting exact-target state,
    # whereas 'dc' goes to the accepting dead/mismatch state.
    state_after_a = gens['a'][0]
    assert cd[state_after_a] == n
    assert dc[state_after_a] == dead
    return len(monoid), cd[state_after_a], dc[state_after_a]


def main():
    tsize = threshold_example()
    fsize, cd_state, dc_state = forbidden_erasure_example()
    print(f"threshold_monoid_size={tsize}")
    print("threshold: aperiodic=True commutative=True generator_a_idempotent=False")
    print(f"forbidden_erasure_monoid_size={fsize}")
    print(f"forbidden_erasure: aperiodic=True commutative=False cd_state={cd_state} dc_state={dc_state}")
    print("PASS")


if __name__ == '__main__':
    main()
