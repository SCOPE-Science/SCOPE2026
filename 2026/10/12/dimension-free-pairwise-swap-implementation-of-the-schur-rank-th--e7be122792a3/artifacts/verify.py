from fractions import Fraction


def harmonic(r):
    return sum((Fraction(1, j) for j in range(1, r + 1)), Fraction(0, 1))


def A(r):
    return (r + 2) * harmonic(r) - r


def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for first in range(max_part, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def exact_waiting_mean(partition, r):
    n = sum(partition)
    h = len(partition)
    if h <= r:
        last_growth_row = h - 1
    else:
        last_growth_row = r
    total = Fraction(0, 1)
    for k in range(1, last_growth_row + 1):
        below_mass = sum(partition[k:])
        p = Fraction(below_mass, (n - k) * (k + 1))
        total += 1 / p
    return total


def first_column_bound(n, r):
    return n * A(r)


def main():
    # Exact algebraic identity for the comparison geometric variables.
    for r in range(1, 20):
        lhs = sum(Fraction(k + 1, r + 1 - k) for k in range(1, r + 1))
        assert lhs == A(r)

    # The auxiliary low-column expression is strictly increasing in the height.
    previous = Fraction(0, 1)
    for h in range(2, 20):
        g = (h + 1) * harmonic(h - 1) - (h - 1)
        assert g > previous
        previous = g

    # Exhaustive finite corroboration of the deterministic mean inequality.
    for n in range(2, 13):
        for r in range(1, n):
            bound = first_column_bound(n, r)
            for partition in partitions(n):
                mean = exact_waiting_mean(partition, r)
                assert mean <= bound, (n, r, partition, mean, bound)

    print("VERIFY_OK")


if __name__ == "__main__":
    main()
