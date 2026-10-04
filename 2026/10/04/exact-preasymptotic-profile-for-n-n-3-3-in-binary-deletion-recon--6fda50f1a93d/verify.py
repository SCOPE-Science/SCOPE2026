#!/usr/bin/env python3
from itertools import combinations

EXPECTED = {4: 2, 5: 4, 6: 6, 7: 8, 8: 11, 9: 15}
WITNESSES = {
    4: ("0001", "1110"),
    5: ("01110", "10001"),
    6: ("001110", "101001"),
    7: ("0011010", "1010011"),
    8: ("00110101", "10100110"),
    9: ("010100110", "100110101"),
}

def subsequences_after_deletions(word, d):
    n = len(word)
    return {
        ''.join(word[i] for i in keep)
        for keep in combinations(range(n), n - d)
    }

def lcs_length(a, b):
    prev = [0] * (len(b) + 1)
    for ca in a:
        cur = [0]
        for j, cb in enumerate(b, 1):
            if ca == cb:
                cur.append(prev[j - 1] + 1)
            else:
                cur.append(max(prev[j], cur[-1]))
        prev = cur
    return prev[-1]

def exhaustive_value(n):
    words = [format(i, f'0{n}b') for i in range(1 << n)]
    d2 = [subsequences_after_deletions(w, 2) for w in words]
    d3 = [subsequences_after_deletions(w, 3) for w in words]
    best = -1
    best_pairs = []
    eligible = 0
    pair_checks = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            pair_checks += 1
            # For equal length n, d_L(x,y) >= 3 iff the length-(n-2)
            # deletion balls are disjoint. Cross-check this against LCS.
            eligible_by_ball = d2[i].isdisjoint(d2[j])
            eligible_by_lcs = lcs_length(words[i], words[j]) <= n - 3
            assert eligible_by_ball == eligible_by_lcs
            if not eligible_by_ball:
                continue
            eligible += 1
            inter = len(d3[i] & d3[j])
            if inter > best:
                best = inter
                best_pairs = [(words[i], words[j])]
            elif inter == best:
                best_pairs.append((words[i], words[j]))
    return best, best_pairs, eligible, pair_checks

def main():
    total_pairs = 0
    total_eligible = 0
    total_maximizers = 0
    for n in range(4, 10):
        best, pairs, eligible, checked = exhaustive_value(n)
        assert best == EXPECTED[n], (n, best, EXPECTED[n])
        assert WITNESSES[n] in pairs, (n, WITNESSES[n], pairs[:10])
        total_pairs += checked
        total_eligible += eligible
        total_maximizers += len(pairs)

    # The published all-n upper bound specializes to 20. As a direct
    # corroborative boundary check, the stated length-10 construction has
    # deletion distance at least 3 and exactly 20 common 3-deletion outputs.
    a = "1010101010"
    b = "0110011001"
    assert subsequences_after_deletions(a, 2).isdisjoint(
        subsequences_after_deletions(b, 2)
    )
    assert len(
        subsequences_after_deletions(a, 3)
        & subsequences_after_deletions(b, 3)
    ) == 20

    print(
        "VERIFY_OK "
        f"n=4..9 pair_checks={total_pairs} eligible_pairs={total_eligible} "
        f"maximizing_pairs={total_maximizers} boundary_n10=20"
    )

if __name__ == "__main__":
    main()
