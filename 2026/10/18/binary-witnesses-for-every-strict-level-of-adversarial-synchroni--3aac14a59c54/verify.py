#!/usr/bin/env python3
"""Finite-state checks for a binary adversarial-synchronization theorem.

The exhaustive game solver independently constructs the subset game, allowing
all response words shorter than k, and computes Alice's least worst-case number
of turns by monotone attractor iteration. This finite check supplements, but
is not a substitute for, the theorem's proof for arbitrary n.
"""
from itertools import combinations


def actions(n):
    return {'b': tuple((s + 1) % n for s in range(n)),
            'c': tuple(0 if s == 0 else 1 for s in range(n))}


def move(S, mapping):
    return frozenset(mapping[s] for s in S)


def fixed_point_game(n, k):
    letters = actions(n)
    subsets = [frozenset(c) for j in range(1, n + 1)
               for c in combinations(range(n), j)]
    nontrivial = [p for p in subsets if len(p) > 1]
    responses = {}
    for p in nontrivial:
        seen = {p}
        frontier = {p}
        for _ in range(k - 1):
            frontier = {move(s, a) for s in frontier for a in letters.values()}
            seen.update(frontier)
        responses[p] = seen
    least_turns = {p: 0 for p in subsets if len(p) == 1}
    for _ in range(len(nontrivial) + 1):
        new = {}
        for p in nontrivial:
            if p in least_turns:
                continue
            guarantees = []
            for a in letters.values():
                q = move(p, a)
                if len(q) == 1:
                    guarantees.append(1)
                elif all(r in least_turns for r in responses[q]):
                    guarantees.append(1 + max(least_turns[r] for r in responses[q]))
            if guarantees:
                new[p] = min(guarantees)
        if not new:
            break
        least_turns.update(new)
    return least_turns.get(frozenset(range(n)))


def check_strategy(n):
    a = actions(n)
    full = frozenset(range(n))
    assert move(full, a['c']) == frozenset((0, 1))
    assert move(move(move(full, a['c']), a['b']), a['c']) == frozenset((1,))
    for j in range(1, n):
        pair = frozenset((0, j))
        assert move(pair, a['c']) == frozenset((0, 1))
        bpair = move(pair, a['b'])
        response = (n - 1 - j) if j < n - 1 else 0
        assert 0 <= response <= n - 2
        for _ in range(response):
            bpair = move(bpair, a['b'])
        assert len(bpair) == 2 and 0 in bpair
    # Check Alice's three-turn policy against every Bob response word
    # of length at most n-3 at both of her nonfinal turns.
    reachable = {frozenset((0, 1))}
    for _ in range(n - 3):
        reachable |= {move(s, x) for s in list(reachable) for x in a.values()}
    for pair in reachable:
        if len(pair) == 1:
            continue
        if 0 not in pair:
            assert len(move(pair, a['c'])) == 1
            continue
        assert pair == frozenset((0, 1))
        after_b = move(pair, a['b'])
        reachable2 = {after_b}
        for _ in range(n - 3):
            reachable2 |= {move(s, x) for s in list(reachable2) for x in a.values()}
        for q in reachable2:
            assert len(q) == 1 or 0 not in q
    # Exhaustively check short words cannot reset; three-letter witness does.
    for x in a.values():
        assert len(move(full, x)) > 1
        for y in a.values():
            assert len(move(move(full, x), y)) > 1


def main():
    total = 0
    for n in range(3, 11):
        check_strategy(n)
        row = []
        for k in range(1, n + 2):
            actual = fixed_point_game(n, k)
            expected = 3 if k <= n - 2 else None
            assert actual == expected, (n, k, actual, expected)
            total += 1
            row.append('3' if actual == 3 else 'B')
        print(f'n={n}: ' + ' '.join(f'k={k}:{v}' for k, v in enumerate(row, 1)))
    print(f'PASS: {total} complete subset-game outcomes, n=3..10, k=1..n+1')
    print('PASS: exact three-letter reset bound and explicit Bob/Alice strategy checks')
    print('NOTE: infinite-n validity established by a separate mathematical proof')

if __name__ == '__main__':
    main()
