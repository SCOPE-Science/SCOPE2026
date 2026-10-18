"""Independent iterative relation-wise counting-colour-refinement checks for cyclic Latin cell structures."""
from collections import Counter
from math import gcd


def expected_partition(n, g):
    h = n // gcd(n, g)
    step = n // h
    H = set(range(0, n, step))
    ans = []
    for x in range(n):
        for y in range(n):
            z = (x + y) % n
            if x in H and y in H:
                s = ("point", x, y)
            elif x in H:
                s = ("row", x)
            elif y in H:
                s = ("column", y)
            elif z in H:
                s = ("symbol", z)
            else:
                s = ("outside",)
            ans.append(s)
    return ans


def refine(n, g):
    colors = [0] * (n * n)
    colors[0] = 1
    colors[g] = 2
    rounds = 0
    while True:
        profiles = [[Counter() for _ in range(n)] for _ in range(3)]
        for x in range(n):
            for y in range(n):
                v = colors[n * x + y]
                profiles[0][x][v] += 1
                profiles[1][y][v] += 1
                profiles[2][(x + y) % n][v] += 1
        signatures = []
        for x in range(n):
            for y in range(n):
                typ = (colors[n * x + y],) + tuple(
                    tuple(sorted(profiles[k][t].items()))
                    for k, t in enumerate((x, y, (x + y) % n))
                )
                signatures.append(typ)
        unique = {s: i for i, s in enumerate(sorted(set(signatures)))}
        updated = [unique[s] for s in signatures]
        rounds += 1
        if len(set(updated)) == len(set(colors)):
            return updated, rounds
        colors = updated


def same_partition(a, b):
    da, db = {}, {}
    for p, q in zip(a, b):
        if p in da and da[p] != q:
            return False
        if q in db and db[q] != p:
            return False
        da[p] = q
        db[q] = p
    return True


def main():
    pairs = 0
    all_cells = 0
    maximum_rounds = 0
    for n in range(2, 23):
        for g in range(1, n):
            predicted = expected_partition(n, g)
            computed, rounds = refine(n, g)
            assert same_partition(predicted, computed), (n, g)
            h = n // gcd(n, g)
            k = n // h
            counts = Counter(predicted)
            formula = h * h + (3 * h if k > 1 else 0) + (1 if k > 2 else 0)
            assert len(counts) == formula, (n, g, len(counts), formula)
            pairs += 1
            all_cells += n * n
            maximum_rounds = max(maximum_rounds, rounds)
    print(f"PASS: {pairs} cyclic parameters 2<=n<=22, 1<=g<n")
    print(f"PASS: {all_cells} total cells analysed over those parameter pairs")
    print(f"PASS: stable partition equals the subgroup-coordinate partition in every case")
    print(f"PASS: class-count formula in every case; maximum observed refinement rounds={maximum_rounds}")

if __name__ == '__main__':
    main()
