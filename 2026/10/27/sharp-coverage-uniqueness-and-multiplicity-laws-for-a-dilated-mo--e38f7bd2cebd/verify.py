"""Finite direct checks of singleton and adjacent-pair counts."""


def check(k):
    limit = 4**k
    members = [0]
    for j in range(k):
        members += [a + 4**j for a in members]
    counts = [0] * limit
    for a in members:
        for b in members:
            n = a + 3*b
            if n < limit:
                counts[n] += 1
    singleton = counts.count(1)
    adjacent = sum(x + y == 1 for x, y in zip(counts, [0] + counts[:-1]))
    assert singleton == adjacent == 3**k, (k, singleton, adjacent)


if __name__ == "__main__":
    for exponent in range(8):
        check(exponent)
    print("Checked exact singleton and adjacent-pair counts for k=0,...,7.")
