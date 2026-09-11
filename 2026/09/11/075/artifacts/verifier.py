"""Independent verifier for witness.json. Separate code path from search."""
import json

SIG = [1, 2, 0, 4, 5, 3, 7, 8, 6, 9]

def cycle_profile(p):
    seen = [False] * 10
    lens = []
    for i in range(10):
        if not seen[i]:
            j = i
            L = 0
            while not seen[j]:
                seen[j] = True
                j = p[j]
                L += 1
            lens.append(L)
    return sorted(lens)

def main():
    d = json.load(open("output/artifacts/witness.json"))
    A, B = d["A"], d["B"]
    assert cycle_profile(SIG) == [1, 3, 3, 3], cycle_profile(SIG)
    for name, G in (("A", A), ("B", B)):
        assert len(G) == 10 and all(len(r) == 10 for r in G)
        for i in range(10):
            assert sorted(G[i]) == list(range(10)), f"{name} row {i}"
            assert sorted(G[r][i] for r in range(10)) == list(range(10)), f"{name} col {i}"
        for r in range(10):
            for c in range(10):
                assert G[SIG[r]][SIG[c]] == SIG[G[r][c]], f"{name} equiv at {(r, c)}"
    pairs = set()
    for r in range(10):
        for c in range(10):
            pairs.add((A[r][c], B[r][c]))
    assert len(pairs) == 100, len(pairs)
    print("INDEPENDENT_VERIFY_OK: Latin A,B; orth 100/100; diag-sigma autotopism; profile 3+3+3+1")

if __name__ == "__main__":
    main()
