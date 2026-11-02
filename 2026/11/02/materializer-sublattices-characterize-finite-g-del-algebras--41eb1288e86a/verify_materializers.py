"""Exact finite checks for the materializer join criterion (standard Python only)."""
from itertools import combinations


def naturally_labeled_posets(n):
    pairs = list(combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        up = [1 << i for i in range(n)]
        for t, (i, j) in enumerate(pairs):
            if mask & (1 << t):
                up[i] |= 1 << j
        if all(not (up[i] & (1 << j)) or not (up[j] & ~up[i])
               for i in range(n) for j in range(n)):
            yield up


def check(up):
    n = len(up)
    lower = [sum(1 << i for i in range(n) if up[i] & (1 << p))
             for p in range(n)]
    ideals = [s for s in range(1 << n) if all(
        not (s & (1 << p)) or (s & lower[p]) == lower[p]
        for p in range(n))]
    is_ideal = set(ideals)

    def arrow(a, b):
        return sum(1 << p for p in range(n) if not (a & lower[p] & ~b))

    global_sublattices = True
    for antecedent in ideals:
        neg = arrow(antecedent, 0)
        materializers = {b for b in ideals if arrow(antecedent, b) == (neg | b)}
        assert 0 in materializers and (1 << n)-1 in materializers
        assert all((b & c) in materializers
                   for b in materializers for c in materializers)
        for j in ideals:
            added = [p for p in range(n) if
                     (antecedent & lower[p]) != 0 and
                     ((antecedent & lower[p]) & ~j) == 0]
            closure = j
            for p in added:
                closure |= lower[p]
            assert closure in is_ideal
            assert closure in materializers
            assert closure & antecedent == j & antecedent
            assert all((j & ~m) or not (closure & ~m)
                       for m in materializers)
            assert (j in materializers) == (j == closure)
        is_join_closed = all((b | c) in materializers
                             for b in materializers for c in materializers)
        global_sublattices &= is_join_closed
        condition = True
        for p in range(n):
            d = antecedent & lower[p]
            if d == 0:
                continue
            max_d = [q for q in range(n) if d & (1 << q) and not any(
                q != r and (d & (1 << r)) and (up[q] & (1 << r))
                for r in range(n))]
            if len(max_d) > 1:
                condition = False
                break
        assert condition == is_join_closed

    prelinear = all((arrow(a, b) | arrow(b, a)) == (1 << n) - 1
                    for a in ideals for b in ideals)
    forest = all((up[q] & (1 << r)) or (up[r] & (1 << q))
                 for p in range(n) for q in range(n) for r in range(n)
                 if (lower[p] & (1 << q)) and (lower[p] & (1 << r)))
    assert prelinear == global_sublattices == forest
    return len(ideals)


def main():
    for n in range(1, 7):
        count = 0
        for up in naturally_labeled_posets(n):
            check(up)
            count += 1
        print(f"NATURALLY_LABELED_POSETS_PASS n={n} count={count}")
    print("MATERIALIZER_HORN_AND_FOREST_CRITERIA_PASS")


if __name__ == '__main__':
    main()
