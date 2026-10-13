#!/usr/bin/env python3
"""Exact terminal-code exploration for two-colour spread-before-ignition on positive cycles.
Python 3.10+, standard library only. State 0=unburned, 1/-1=permanent colours.
"""
from collections import Counter, deque


def terminal_code(n):
    root = (0,)*n
    queue = deque([root])
    seen = {root}
    output = set()
    transitions = 0
    while queue:
        old = queue.popleft()
        if all(old):
            output.add(old)
            continue
        new = list(old)
        for i in range(n):
            if old[i] == 0:
                influence = old[(i-1)%n] + old[(i+1)%n]
                new[i] = (influence > 0) - (influence < 0)
        if all(new):
            options = [tuple(new)]
        else:
            options = []
            for i in range(n):
                if new[i] == 0:
                    for colour in (-1, 1):
                        candidate = new.copy()
                        candidate[i] = colour
                        options.append(tuple(candidate))
        for nxt in options:
            transitions += 1
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return output, len(seen), transitions


def boundary_count(word):
    return sum(word[i] != word[(i+1) % len(word)] for i in range(len(word)))


def cyclic_run_type(word):
    n = len(word)
    anchor = next(i for i in range(n) if word[i] != word[(i-1) % n])
    runs = []
    length = 1
    for k in range(1, n):
        if word[(anchor+k) % n] == word[(anchor+k-1) % n]:
            length += 1
        else:
            runs.append(length)
            length = 1
    runs.append(length)
    return min(tuple(runs[i:] + runs[:i]) for i in range(len(runs)))


def covering_radius(words, n):
    bits = [sum((v == -1) << j for j, v in enumerate(w)) for w in words]
    profile = Counter()
    for u in range(1 << n):
        profile[min((u ^ v).bit_count() for v in bits)] += 1
    return max(profile), [profile[t] for t in range(max(profile)+1)]


def main():
    print('n | reachable | spread+ignition states | transitions | walls | covering radius | distance histogram')
    for n in range(3, 11):
        words, states, transitions = terminal_code(n)
        walls = sorted(Counter(boundary_count(w) for w in words).items())
        radius, dist = covering_radius(words, n)
        print(f'{n} | {len(words)} | {states} | {transitions} | {walls} | {radius} | {dist}')
        expected = (2 if n==3 else 10 if n==4 else n*(n-1)+2 if n<=9 else 172)
        assert len(words) == expected
        if n <= 9:
            assert all(boundary_count(w) <= 2 for w in words)
            if n>=4:
                assert all(boundary_count(w) in (0,2) for w in words)
        if n == 10:
            assert Counter(boundary_count(w) for w in words) == {0:2, 2:90, 4:80}
            types=Counter(cyclic_run_type(w) for w in words if boundary_count(w)==4)
            expected_types={(1,2,2,5):20,(1,5,2,2):20,(1,2,4,3):20,(1,3,4,2):20}
            assert types==expected_types, types
            print('n10 four-boundary run types:',sorted(types.items()))
    print('BFS_CERTIFIED')

if __name__ == '__main__':
    main()
