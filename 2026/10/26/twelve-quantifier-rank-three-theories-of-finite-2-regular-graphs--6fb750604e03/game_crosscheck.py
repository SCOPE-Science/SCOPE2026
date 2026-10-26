#!/usr/bin/env python3
"""Small independent minimax EF-game check for the twelve 3-round types."""
from functools import lru_cache
from checker import graph, rank_three_type

def duplicator_wins(left, right, rounds):
    """Direct alternating Spoiler/Duplicator minimax, no Hintikka recursion."""
    G, H = graph(left), graph(right)
    @lru_cache(None)
    def solve(a, b, remaining):
        if remaining == 0:
            return True
        for reverse in (False, True):
            source, target = (H, G) if reverse else (G, H)
            source_moves, target_moves = (b, a) if reverse else (a, b)
            for u in range(len(source)):
                answered = False
                for v in range(len(target)):
                    if any((u == x) != (v == y) or
                           bool(source[u] & (1 << x)) !=
                           bool(target[v] & (1 << y))
                           for x, y in zip(source_moves, target_moves)):
                        continue
                    next_a, next_b = ((a + (v,), b + (u,)) if reverse
                                      else (a + (u,), b + (v,)))
                    if solve(next_a, next_b, remaining - 1):
                        answered = True
                        break
                if not answered:
                    return False
        return True
    return solve((), (), rounds)

REPS = ((3,), (4,), (5,), (3,3), (6,), (3,4), (7,), (3,5),
        (4,4), (3,3,3), (4,5), (3,4,5))

if __name__ == '__main__':
    for i, p in enumerate(REPS):
        for j, q in enumerate(REPS):
            win = duplicator_wins(p, q, 3)
            assert win == (i == j)
            assert win == (rank_three_type(graph(p)) == rank_three_type(graph(q)))
    extra_pairs = [((7,), (8,)), ((7,), (5,5)),
                   ((3,4), (3,3,4,4)), ((4,5), (4,4,6)),
                   ((3,4,5), (3,3,4,4,5,6))]
    for p, q in extra_pairs:
        assert duplicator_wins(p, q, 3)
    print('PASS: 144 ordered representative games and 5 extra comparisons.')
