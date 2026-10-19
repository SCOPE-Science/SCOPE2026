#!/usr/bin/env python3
"""Exact palindromic-factor spectrum of the Baum--Sweet word for 1 <= n <= 8192.

Uses only the Python standard library. Run: python3 verify.py
"""
from collections import defaultdict
from hashlib import sha256

MORPHISM = {"A": "AB", "B": "CB", "C": "BD", "D": "DD"}
OUTPUT = {"A": "1", "B": "1", "C": "0", "D": "0"}
MAX_LENGTH = 8192
SMALL_COUNTS = (
    2, 2, 3, 3, 4, 3, 4, 3, 4, 4, 4, 4, 4, 3, 4, 2,
    4, 2, 4, 2, 4, 1, 4, 1, 3, 1, 2, 1, 2, 1, 2, 1,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2,
)


def language_pairs():
    # Starts at AB, a factor of the fixed point mu^omega(A).
    pairs = {"AB"}
    while True:
        new = set(pairs)
        for pair in pairs:
            stretched = MORPHISM[pair[0]] + MORPHISM[pair[1]]
            new.update(stretched[i : i + 2] for i in range(len(stretched) - 1))
        if new == pairs:
            return sorted(pairs)
        pairs = new


def inflated_letters(level):
    blocks = {c: c for c in MORPHISM}
    for _ in range(level):
        blocks = {c: "".join(MORPHISM[a] for a in old) for c, old in blocks.items()}
    assert all(len(w) == (1 << level) for w in blocks.values())
    return blocks


def coded_pair_blocks(level, pairs):
    blocks = inflated_letters(level)
    return ["".join(OUTPUT[c] for c in blocks[p[0]] + blocks[p[1]]) for p in pairs]


def nonzero_palindromes_via_eertree(string, cap):
    """Yield each distinct palindrome containing '1' in the given string.

    A newly read symbol creates at most one new distinct palindrome:
    its longest palindromic suffix. Odd/even root nodes are -1 and 0.
    """
    sizes = [-1, 0]
    suffix = [0, 0]
    trans = [{}, {}]
    last = 1
    for i, ch in enumerate(string):
        u = last
        while i - 1 - sizes[u] < 0 or string[i - 1 - sizes[u]] != ch:
            u = suffix[u]
        if ch in trans[u]:
            last = trans[u][ch]
            continue
        v = len(sizes)
        sizes.append(sizes[u] + 2)
        suffix.append(0)
        trans.append({})
        trans[u][ch] = v
        if sizes[v] == 1:
            suffix[v] = 1
        else:
            j = suffix[u]
            while i - 1 - sizes[j] < 0 or string[i - 1 - sizes[j]] != ch:
                j = suffix[j]
            suffix[v] = trans[j][ch]
        last = v
        if sizes[v] <= cap:
            p = string[i + 1 - sizes[v] : i + 1]
            if "1" in p:
                assert p == p[::-1]
                yield p


def expected_nonzero_count(n):
    if n <= 44:
        return SMALL_COUNTS[n - 1] - 1
    for exponent in range(6, 13):
        delta = n - (1 << exponent)
        if exponent % 2 == 0 and 3 <= delta <= 25 and delta % 2 == 1:
            return 1
        if exponent % 2 == 1 and 2 <= delta <= 12 and delta % 2 == 0:
            return 1
    return 0


def brute_palindromes(words, cap):
    """Independent center-expansion enumeration on smaller complete factor blocks."""
    found = defaultdict(set)
    for string in words:
        for center in range(len(string)):
            for left, right in ((center, center), (center, center + 1)):
                while left >= 0 and right < len(string) and string[left] == string[right]:
                    length = right - left + 1
                    if length > cap:
                        break
                    substring = string[left : right + 1]
                    if "1" in substring:
                        found[length].add(substring)
                    left -= 1
                    right += 1
    return found


def direct_baum_sweet(n):
    if n == 0:
        return "1"
    return "1" if all(len(run) % 2 == 0 for run in bin(n)[2:].split("1") if run) else "0"


def main():
    pairs = language_pairs()
    assert pairs == ["AB", "BB", "BC", "BD", "CB", "DB", "DC", "DD"]

    level = 13
    large = coded_pair_blocks(level, pairs)
    assert len(large) == 8 and all(len(w) == 2 * MAX_LENGTH for w in large)
    # D is an absorbing zero letter, so 0^n occurs for all 1 <= n <= 8192.
    assert "0" * (2 * MAX_LENGTH) in large
    # Independent check that the substituted fixed point is Baum--Sweet.
    first_block = "".join(OUTPUT[c] for c in inflated_letters(level)["A"])
    assert first_block == "".join(direct_baum_sweet(i) for i in range(MAX_LENGTH))

    from_eertree = defaultdict(set)
    for string in large:
        for palindrome in nonzero_palindromes_via_eertree(string, MAX_LENGTH):
            from_eertree[len(palindrome)].add(palindrome)
    counts = [1 + len(from_eertree[n]) for n in range(1, MAX_LENGTH + 1)]
    assert all(len(from_eertree[n]) == expected_nonzero_count(n)
               for n in range(1, MAX_LENGTH + 1))
    assert tuple(counts[:44]) == SMALL_COUNTS

    exceptional = [n for n in range(45, MAX_LENGTH + 1) if counts[n - 1] == 2]
    assert len(exceptional) == 66
    assert sum(1 for n in range(45, MAX_LENGTH + 1) if counts[n - 1] == 1) == 8082

    # A separate enumeration using center expansions for every length <= 128.
    # The same pair-cover lemma applies with level 8, so this independently
    # enumerates factors of the infinite word in this smaller range.
    small = coded_pair_blocks(8, pairs)
    check = brute_palindromes(small, 128)
    for n in range(1, 129):
        assert check[n] == from_eertree[n], (n, len(check[n]), len(from_eertree[n]))

    line_data = "".join(f"{n},{c}\n" for n, c in enumerate(counts, 1)).encode("utf-8")
    digest = sha256(line_data).hexdigest()
    assert digest == "c94eac15fdef31d2b90ccd14121e0782788a316c05a5c80f9d7bde100ff05e55"
    print("VERIFIED_PAIR_SET=" + ",".join(pairs))
    print("VERIFIED_LENGTHS=1..8192")
    print("EXCEPTIONAL_LENGTHS_45..8192=66")
    print("ZERO_ONLY_LENGTHS_45..8192=8082")
    print("PROFILE_SHA256=" + digest)
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
