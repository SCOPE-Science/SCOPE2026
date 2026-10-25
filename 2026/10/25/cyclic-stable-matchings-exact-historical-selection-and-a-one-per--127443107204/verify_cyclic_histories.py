#!/usr/bin/env python3
"""Finite checks for cyclic marriage markets and one historical auxiliary participant.
Pure Python standard library. Run: python verify_cyclic_histories.py
The proof for arbitrary market size is mathematical, not computational.
"""
from itertools import permutations
from collections import deque


def market(n, auxiliary):
    men = tuple(range(n))
    women = tuple(range(n, 2 * n))
    spare = 2 * n if auxiliary else None
    people = men + women + ((spare,) if auxiliary else ())
    ranking = {}
    for i in men:
        ranking[i] = tuple(n + (i + j) % n for j in range(n))
    for j in range(n):
        ranking[n + j] = tuple((j + k) % n for k in range(1, n + 1))
    if auxiliary:
        ranking[spare] = (n,)
        seq = list(ranking[n])
        assert seq[-2] == n - 1 and seq[-1] == 0
        seq.insert(n - 1, spare)
        ranking[n] = tuple(seq)
    return people, men, women, spare, ranking


def stable(active, partners, men, ranking):
    a = set(active)
    p = dict(partners)
    for x in a:
        mate = p.get(x)
        if mate is not None:
            if mate not in a or p.get(mate) != x or mate not in ranking[x] or x not in ranking[mate]:
                return False
    for m in men:
        if m not in a:
            continue
        for w in ranking[m]:
            if w not in a:
                continue
            if p.get(m) == w:
                break
            if m in ranking[w] and (p.get(w) is None or
                    ranking[w].index(m) < ranking[w].index(p[w])):
                return False
    return True


def event(active, partners, person, enter, men, ranking):
    a = set(active)
    p = dict(partners)
    if enter:
        assert person not in a
        a.add(person)
        p[person] = None
        proposer = person
    else:
        assert person in a
        a.remove(person)
        proposer = p.get(person)
        if proposer is not None:
            p[proposer] = None
        p.pop(person)
    rejected = set()
    while proposer is not None:
        acceptor = None
        for candidate in ranking[proposer]:
            if candidate not in a or (proposer, candidate) in rejected:
                continue
            rejected.add((proposer, candidate))
            if proposer not in ranking[candidate]:
                continue
            current = p.get(candidate)
            if current is None or ranking[candidate].index(proposer) < ranking[candidate].index(current):
                acceptor = candidate
                break
        if acceptor is None:
            proposer = None
            continue
        displaced = p[acceptor]
        p[acceptor] = proposer
        p[proposer] = acceptor
        if displaced is not None:
            p[displaced] = None
        proposer = displaced
    assert stable(a, p, men, ranking)
    return frozenset(a), tuple(sorted(p.items()))


def verify_stable_set(n):
    people, men, women, _, ranking = market(n, False)
    exact = set()
    for perm in permutations(women):
        p = dict(zip(men, perm))
        p.update({w: m for m, w in zip(men, perm)})
        if stable(people, p, men, ranking):
            exact.add(tuple(w - n for w in perm))
    shifts = {tuple((i + r) % n for i in range(n)) for r in range(n)}
    assert exact == shifts, (n, exact, shifts)
    return len(exact)


def reachable(n, auxiliary):
    people, men, women, spare, ranking = market(n, auxiliary)
    initial = (frozenset(), ())
    queue = deque([initial])
    visited = {initial}
    full = frozenset(men + women)
    found = set()
    while queue:
        active, pairs = queue.popleft()
        p = dict(pairs)
        if active == full:
            found.add(tuple(p[m] - n for m in men))
        for x in people:
            nxt = event(active, pairs, x, x not in active, men + ((spare,) if auxiliary else ()), ranking)
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    return found, len(visited)


def verify_specific_history(n):
    people, men, women, spare, ranking = market(n, True)
    active, pairs = frozenset(), ()
    for x in women + (spare,) + men:
        active, pairs = event(active, pairs, x, True, men + (spare,), ranking)
    full = tuple((i + 1) % n for i in men)
    p = dict(pairs)
    assert tuple(p[m] - n for m in men) == full
    assert p[spare] is None
    active, pairs = event(active, pairs, spare, False, men + (spare,), ranking)
    assert active == frozenset(men + women)
    assert tuple(dict(pairs)[m] - n for m in men) == full


def main():
    checks = 0
    for n in range(2, 8):
        assert verify_stable_set(n) == n
        checks += 1
    for n in range(3, 7):
        out, states = reachable(n, False)
        expected = {tuple(i for i in range(n)), tuple((i + n - 1) % n for i in range(n))}
        assert out == expected, (n, out)
        print(f"terminal-only n={n}: {states} reachable intermediate states, 2 full outcomes")
        checks += states
    for n in range(3, 6):
        out, states = reachable(n, True)
        desired = tuple((i + 1) % n for i in range(n))
        assert desired in out
        print(f"one auxiliary man n={n}: {states} reachable intermediate states, shift-one reached")
        checks += states
    for n in range(3, 51):
        verify_specific_history(n)
        checks += n + 2
    print(f"PASS: {checks} enumerated states, stable-set counts and constructive steps; n=3..50 histories")


if __name__ == '__main__':
    main()
