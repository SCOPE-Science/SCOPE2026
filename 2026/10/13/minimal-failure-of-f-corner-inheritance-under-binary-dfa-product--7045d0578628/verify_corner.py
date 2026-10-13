"""Independent finite checker for the binary f-corner product obstruction.

The positive words are the empty word and nonempty words beginning with 'a'.
The function positive_distance uses a two-phase breadth-first search that
tracks whether the compulsory initial a has been consumed. All comparisons
are exact integer comparisons, with None denoting an unreachable target.
"""
from collections import deque
from itertools import product


def positive_distance(maps, origin, target):
    if origin == target:
        return 0
    n = len(maps[0])
    # Stage 0 enforces the first letter a; stage 1 permits either letter.
    pending = deque([(origin, 0, 0)])
    visited = {(origin, 0)}
    while pending:
        x, stage, distance = pending.popleft()
        letters = (0,) if stage == 0 else (0, 1)
        for letter in letters:
            y = maps[letter][x]
            if y == target:
                return distance + 1
            node = (y, 1)
            if node not in visited:
                visited.add(node)
                pending.append((y, 1, distance + 1))
    return None


def corner(maps):
    n = len(maps[0])
    for q in range(1, n):
        forward = positive_distance(maps, q, 0)
        backward = positive_distance(maps, 0, q)
        if forward is None or (backward is not None and forward >= backward):
            return False
    return True


def direct_product(A, B):
    n, m = len(A[0]), len(B[0])
    return tuple(tuple(A[c][i] * m + B[c][j]
                       for i in range(n) for j in range(m))
                 for c in (0, 1))


def act(maps, state, word):
    for letter in word:
        state = maps[0 if letter == 'a' else 1][state]
    return state


def reachable_all(maps):
    n = len(maps[0])
    for source in range(n):
        reached = {source}
        todo = [source]
        for state in todo:
            for trans in maps:
                j = trans[state]
                if j not in reached:
                    reached.add(j)
                    todo.append(j)
        if len(reached) != n:
            return False
    return True


def main():
    M = [maps for a in product(range(2), repeat=2)
         for b in product(range(2), repeat=2)
         if corner(maps := (a, b))]
    assert len(M) == 5, M
    assert all(corner(direct_product(A, B)) for A in M for B in M)
    A = ((0, 0), (1, 0))
    B = ((0, 0, 2), (1, 2, 0))
    assert reachable_all(A) and reachable_all(B)
    assert corner(A) and corner(B)
    P = direct_product(A, B)
    target, witness_state = 0, 2  # (0,0) and (0,2) in lexicographic order
    assert positive_distance(P, target, witness_state) == 3
    assert positive_distance(P, witness_state, target) == 3
    assert not corner(P)
    assert [act(P, s, 'aba') for s in range(6)] == [0]*6
    assert act(P, 0, 'abb') == 2
    assert act(P, 2, 'aba') == 0
    print('VERIFY_OK individual_corners=5 two_by_two_products=25 '
          'minimal_total_states=5 strong_factor_sizes=2,3 '
          'forward_positive_distance=3 reverse_positive_distance=3 '
          'joint_reset=aba')


if __name__ == '__main__':
    main()
