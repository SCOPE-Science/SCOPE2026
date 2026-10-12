"""Independent finite checks for the fixed-letter binary morphism theorem.

Enumerates *pairs of nonunit morphisms* rather than using the gap criterion
as an oracle. This is a finite test, not a proof for arbitrary word lengths.
"""
from itertools import product
from math import comb


def words_up_to(bound):
    return ["".join(bits) for length in range(1, bound + 1)
            for bits in product("ab", repeat=length)]


def factor_pair(w):
    n = len(w)
    pool = words_up_to(n)
    for v in pool:
        if "a" not in v or v == "a":
            continue
        c = v.count("a")
        if w.count("a") % c:
            continue
        for u in pool:
            if "a" not in u or u == "a":
                continue
            if u.count("a") * c != w.count("a"):
                continue
            if sum(len(v) if letter == "a" else 1 for letter in u) != n:
                continue
            if "".join(v if letter == "a" else "b" for letter in u) == w:
                return (u, v)
    return None


def criterion(w):
    m = w.count("a")
    assert m >= 1
    if m == 1:
        return w.count("b") >= 2
    if w.startswith("b") or w.endswith("b"):
        return True
    interior = [len(run) for run in w.split("a")[1:-1]]
    assert len(interior) == m - 1
    for c in range(2, m):
        if m % c:
            continue
        d = m // c
        if all(interior[k * c + (j - 1)] == interior[j - 1]
               for k in range(1, d) for j in range(1, c)):
            return True
    return False


def all_boundary_free(m, beta):
    # Exactly m copies of a, beta copies of b, first and last letters a.
    # Generate the m-1 interior nonnegative gaps independently.
    def gap_vectors(n, total):
        if n == 0:
            if total == 0:
                yield ()
            return
        for value in range(total + 1):
            for rest in gap_vectors(n - 1, total - value):
                yield (value,) + rest

    for gaps in gap_vectors(m - 1, beta):
        yield "a" + "".join("b" * g + "a" for g in gaps)


def main():
    for n in range(1, 10):
        nwords = 0
        reducible = 0
        for bits in product("ab", repeat=n):
            w = "".join(bits)
            if "a" not in w:
                continue
            pair = factor_pair(w)
            predicted = criterion(w)
            assert bool(pair) == predicted, (w, pair, predicted)
            if pair:
                u, v = pair
                assert (u != "a" and v != "a" and
                        "".join(v if t == "a" else "b" for t in u) == w)
            nwords += 1
            reducible += bool(pair)
        print("word_length", n, "tested", nwords, "reducible", reducible)
    for beta in range(0, 10):
        words = list(all_boundary_free(4, beta))
        observed = sum(not criterion(w) for w in words)
        expected = comb(beta + 2, 2) - (beta // 2 + 1)
        assert observed == expected, (beta, observed, expected)
    for m in (2, 3, 5, 7):
        for beta in range(0, 7):
            words = list(all_boundary_free(m, beta))
            assert len(words) == comb(beta + m - 2, m - 2)
            assert all(not criterion(w) for w in words)
    for m in range(2, 21):
        w = "ab" + "a" * (m - 1)
        assert w.count("a") == m and w.count("b") == 1
        assert not criterion(w), (m, w)
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
