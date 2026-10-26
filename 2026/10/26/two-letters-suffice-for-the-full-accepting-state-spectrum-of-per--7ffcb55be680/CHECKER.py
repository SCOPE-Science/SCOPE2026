"""Finite consistency checks for a binary right-quotient witness construction.

Requires only Python's standard library. Infinite correctness is established by
an algebraic proof rather than by these finite computations.
"""
from collections import deque
from itertools import permutations
from math import factorial


def minimization_classes(states, transitions, final):
    classes = {q: (int(q in final)) for q in states}
    while True:
        signatures = {q: (classes[q], tuple(classes[transitions[c][q]] for c in 'ab')) for q in states}
        ids = {s: i for i, s in enumerate(sorted(set(signatures.values())))}
        new = {q: ids[signatures[q]] for q in states}
        if all(new[q] == new[r] for q in states for r in states if classes[q] == classes[r]) and len(set(new.values())) == len(set(classes.values())):
            return len(set(new.values()))
        classes = new


def check(k, h, m):
    assert k >= 2 and h >= 2 and 1 <= m < k
    # Zero-based indexing. a is the k-cycle; b swaps 0 and 1.
    a = tuple((q + 1) % k for q in range(k))
    b = tuple(1 if q == 0 else 0 if q == 1 else q for q in range(k))
    delta = {'a': a, 'b': b}
    qa = tuple(range(k))
    start = (qa, 0)
    seen = {start}
    todo = deque([start])
    while todo:
        perm, t = todo.popleft()
        for c in 'ab':
            nxt = (tuple(delta[c][perm[q]] for q in range(k)), (t + (c == 'a')) % h)
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    assert len(seen) == factorial(k) * h
    assert len({p for p, r in seen if p[k-1] == k-1 and r != h-1}) == factorial(k-1)
    assert {p for p, r in seen if p[k-1] == k-1 and r != h-1} == {
        p for p in permutations(range(k)) if p[k-1] == k-1}

    states_b = tuple((q, i) for q in range(k) for i in range(h))
    tb = {
        'a': {(q,i): (a[q], (i+1)%h) for q,i in states_b},
        'b': {(q,i): (b[q], i) for q,i in states_b},
    }
    fb = {(k-1, i) for i in range(h-1)}
    assert minimization_classes(states_b, tb, fb) == k*h
    fa = set(range(m))
    states_a = tuple(range(k))
    ta = {'a': {q: a[q] for q in states_a}, 'b': {q: b[q] for q in states_a}}
    assert minimization_classes(states_a, ta, fa) == k
    quotient_final = set()
    for p, r in seen:
        if p[k-1] == k-1 and r != h-1:
            quotient_final.update(q for q in states_a if p[q] in fa)
    assert quotient_final == set(range(k-1))
    assert minimization_classes(states_a, ta, quotient_final) == k
    return len(seen)


def main():
    cases = 0
    total_pair_states = 0
    for k in range(2, 7):
        for h in range(2, 7):
            for m in range(1, k):
                total_pair_states += check(k, h, m)
                cases += 1
    print('PASS', cases, 'witness parameter triples;', total_pair_states, 'permutation-counter group elements checked (with repetitions).')
    print('Checked exact reachability, stabilizer image, full DFA minimality, and quotient accepting set.')

if __name__ == '__main__':
    main()
