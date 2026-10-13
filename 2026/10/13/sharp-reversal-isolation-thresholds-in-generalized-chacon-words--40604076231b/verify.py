"""Reproducible finite consistency checks for the generalized Chacon cutoff.

The symbolic gap-grammar argument in RESULT.md, not this bounded test,
proves the infinite parameter statement.
"""
from pathlib import Path
import json


def words(a, levels):
    w = "0"
    result = [w]
    for _ in range(levels):
        w = w * a + "1" + w
        result.append(w)
    return result


def gaps(word):
    bits = [j for j, symbol in enumerate(word) if symbol == "1"]
    return tuple(bits[j + 1] - bits[j] - 1 for j in range(len(bits) - 1))


def factors(word, n):
    return {word[j:j + n] for j in range(len(word) - n + 1)}


def reversible(fset):
    return {z for z in fset if z[::-1] in fset}


def main():
    gap_cases = 0
    for a in range(2, 15):
        w = words(a, 4)
        gs = [gaps(v) for v in w]
        A, B, C = a + 1, a, 1
        assert gs[2] == (A,) * (a - 1) + (C, B)
        for j in range(2, 4):
            assert gs[j + 1] == ((gs[j] + (A,)) * (a - 1)
                                  + gs[j] + (C, B) + gs[j])
            assert gs[j][:a] == (A,) * (a - 1) + (C,)
            assert gs[j][-2:] == (C, B)
        pairs = set(zip(gs[4], gs[4][1:]))
        assert pairs == {(A, A), (A, C), (B, A), (B, C), (C, B)}
        for i in range(len(gs[4])):
            if gs[4][i] != A:
                continue
            j = i
            while j < len(gs[4]) and gs[4][j] == A:
                j += 1
            assert j - i <= a
            if j - i == a:
                assert i and j < len(gs[4])
                assert gs[4][i - 1] == B and gs[4][j] == C
        alt_max = 0
        for i in range(len(gs[4])):
            j = i
            while (j < len(gs[4]) and gs[4][j] in (B, C)
                   and (j == i or gs[4][j] != gs[4][j - 1])):
                j += 1
            alt_max = max(alt_max, j - i)
        assert alt_max == 4
        gap_cases += 1
    a = 3
    ws = words(a, 3)
    assert len(ws[2]) == 21
    assert len(ws[3]) == 85
    f19 = factors(ws[3], 19)
    cert = json.loads(Path(__file__).with_name("a3_certificate.json").read_text(encoding="utf8"))
    assert cert["parameter"] == 3 and cert["level"] == 3 and cert["window_length"] == 19
    assert cert["iterated_word"] == ws[3]
    assert cert["distinct_factors_sorted"] == sorted(f19)
    assert len(f19) == 37
    assert not reversible(f19)
    f18 = factors(ws[3], 18)
    pal18 = {z for z in f18 if z == z[::-1]}
    assert pal18 == {"010000100001000010"}
    assert cert["palindrome_length_18"] in pal18
    cutoff_cases = 0
    for a in range(2, 11):
        T = 13 if a == 2 else 19 if a == 3 else a * a + 3 * a
        w = words(a, 4)[-1]
        assert not reversible(factors(w, T)), a
        assert any(z == z[::-1] for z in factors(w, T - 1)), a
        cutoff_cases += 1
    for a in range(4, 101):
        A, B, C = a + 1, a, 1
        contexts = [(B, C), (B, A), (A, C)]
        assert max(min(P, Q2) + min(Q, P2)
                   for P, Q in contexts for P2, Q2 in contexts) == 2 * a
        assert 4 * a + 9 <= a * a + 3 * a - 1
        assert a * a + 2 * a + 3 <= a * a + 3 * a - 1
    print("VERIFY_OK gap_recursion_parameters=13 localized_a3_factors_n19=37 "
          "a3_palindromes_n18=1 sampled_cutoffs=9 context_bounds=97")


if __name__ == "__main__":
    main()
