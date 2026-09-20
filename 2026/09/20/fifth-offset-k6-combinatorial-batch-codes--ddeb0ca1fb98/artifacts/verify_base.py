from itertools import combinations

# Dual representation of a (15,28,6,10)-CBC:
# each entry is the set of servers storing one item.
SUPPORTS = [
    {3},
    {1, 4},
    {2, 4},
    {4, 5},
    {5, 6},
    {1, 7},
    {2, 7},
    {6, 7},
    {1, 8},
    {6, 8},
    {9},
    {5, 9},
    {2, 10},
    {3, 10},
    {8, 10},
]

def main():
    assert len(SUPPORTS) == 15
    assert sum(map(len, SUPPORTS)) == 28

    checked = 0
    minima = {}
    witnesses = {}
    for r in range(1, 7):
        minimum = 11
        witness = None
        for idxs in combinations(range(len(SUPPORTS)), r):
            checked += 1
            union = set().union(*(SUPPORTS[i] for i in idxs))
            if len(union) < r:
                raise AssertionError(
                    f"Hall violation for {tuple(i + 1 for i in idxs)}: {sorted(union)}"
                )
            if len(union) < minimum:
                minimum = len(union)
                witness = tuple(i + 1 for i in idxs)
        minima[r] = minimum
        witnesses[r] = witness

    print("items =", len(SUPPORTS))
    print("servers = 10")
    print("storage =", sum(map(len, SUPPORTS)))
    print("request subsets checked =", checked)
    for r in range(1, 7):
        print(f"minimum union size for {r} requested items = {minima[r]}")
    print("CBC(15,28,6,10) Hall condition: PASS")

if __name__ == "__main__":
    main()
