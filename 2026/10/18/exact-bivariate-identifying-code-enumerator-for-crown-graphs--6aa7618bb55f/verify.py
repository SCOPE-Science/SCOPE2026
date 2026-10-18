"""Direct independent test of identifying codes in matching-deleted bicliques.

Run: python3 verify.py
Only Python standard library is needed.
"""
from collections import Counter


def expand(n):
    coeff = Counter({(0, 0): 1})
    for _ in range(n):
        next_coeff = Counter()
        for (a, b), c in coeff.items():
            next_coeff[a + 1, b] += c
            next_coeff[a, b + 1] += c
            next_coeff[a + 1, b + 1] += c
        coeff = next_coeff
    return coeff


def exact_bivariate(n):
    coeff = expand(n)
    for key, val in expand(n - 1).items():
        coeff[key] += n * val
    for a, b, val in (
        (n - 1, 0, n), (0, n - 1, n),
        (n - 1, 1, n), (1, n - 1, n),
        (n - 2, 1, n * (n - 1)), (1, n - 2, n * (n - 1)),
    ):
        coeff[a, b] -= val
    return Counter({key: value for key, value in coeff.items() if value})


def closed_neighborhoods(n):
    result = []
    for v in range(2 * n):
        neighbors = 1 << v
        for w in range(2 * n):
            if v != w and ((v < n) != (w < n)) and v % n != w % n:
                neighbors |= 1 << w
        result.append(neighbors)
    return result


def actual_identifying(mask, neighborhoods):
    signatures = [mask & neighbor_mask for neighbor_mask in neighborhoods]
    return 0 not in signatures and len(set(signatures)) == len(neighborhoods)


def predicted_identifying(x, y, n):
    if (x | y).bit_count() < n - 1:
        return False
    both = (x & y).bit_count()
    if y.bit_count() == 0 and x.bit_count() != n:
        return False
    if y.bit_count() == 1 and both == 0:
        return False
    if x.bit_count() == 0 and y.bit_count() != n:
        return False
    if x.bit_count() == 1 and both == 0:
        return False
    return True


def main():
    profiles = 0
    subsets = 0
    for n in range(4, 11):
        counts = Counter()
        neighborhoods = closed_neighborhoods(n)
        for mask in range(1 << (2 * n)):
            x = mask & ((1 << n) - 1)
            y = mask >> n
            actual = actual_identifying(mask, neighborhoods)
            predicted = predicted_identifying(x, y, n)
            assert actual == predicted, (n, x, y, actual, predicted)
            if actual:
                counts[(x.bit_count(), y.bit_count())] += 1
        expected = exact_bivariate(n)
        assert counts == expected, (n, counts - expected, expected - counts)
        univariate = Counter()
        for (a, b), value in counts.items():
            univariate[a + b] += value
        least = min(univariate)
        assert least == (4 if n == 4 else n - 1)
        assert univariate[least] == (56 if n == 4 else n * (2 ** (n - 1) - 2 * n))
        assert sum(counts.values()) == 3 ** n + n * 3 ** (n - 1) - 2 * n * n - 2 * n
        profiles += 1
        subsets += 1 << (2 * n)
        print(f"n={n} subsets={1 << (2 * n)} minimum={least} minimum_count={univariate[least]}")
    for n in range(11, 51):
        coeff = exact_bivariate(n)
        assert all(v > 0 for v in coeff.values())
        assert sum(coeff.values()) == 3 ** n + n * 3 ** (n - 1) - 2 * n * n - 2 * n
        for (a, b), val in coeff.items():
            assert coeff[(b, a)] == val
        assert coeff[(n, n)] == 1
    print(f"VERIFICATION_OK profiles={profiles} graph_subsets={subsets} symbolic_n=11..50")


if __name__ == '__main__':
    main()
