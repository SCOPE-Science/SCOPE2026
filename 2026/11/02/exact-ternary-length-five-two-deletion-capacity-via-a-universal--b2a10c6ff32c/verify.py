#!/usr/bin/env python3
"""Self-contained finite-pattern and witness checks for a two-deletion bound."""
from collections import Counter
from itertools import combinations, product

WITNESS = ("00000", "11111", "22222", "00112", "10221", "21100")


def descendants(word):
    return {"".join(word[i] for i in ix) for ix in combinations(range(5), 3)}


def weight5(triple):
    """Five times the shadow weight: integers avoid floating point."""
    if triple[0] == triple[1] == triple[2]:
        return 5
    if triple[0] == triple[2]:
        return 0
    return 1


def restricted_growth_words(n):
    """One representative for each equality partition of n positions."""
    def extend(prefix, upper):
        if len(prefix) == n:
            yield "".join(str(i) for i in prefix)
            return
        for symbol in range(upper + 2):
            yield from extend(prefix + (symbol,), max(upper, symbol))
    yield from extend((0,), 0)


patterns = tuple(restricted_growth_words(5))
assert len(patterns) == 52
mass = [sum(map(weight5, descendants(w))) for w in patterns]
assert min(mass) >= 5
print("exhaustive equality types (Bell number B_5):", len(patterns))
print("minimum universal shadow weight (in fifths):", min(mass))
for q in range(2, 7):
    words = tuple("".join(x) for x in product("012345"[:q], repeat=5))
    assert all(sum(map(weight5, descendants(w))) >= 5 for w in words)
    print("alphabet", q, "checked words", len(words))
seen = set()
for w in WITNESS:
    shadow = descendants(w)
    assert not (seen & shadow), (w, seen & shadow)
    seen |= shadow
    print("codeword", w, "descendants", ",".join(sorted(shadow)))
assert len(seen) == 20
assert len(WITNESS) == 6
print("ternary shadow union:", len(seen), "out of 27")
print("weighted upper bound: floor(3 + (27 - 9)/5) =", (3 * 5 + 27 - 9) // 5)
print("ternary exact optimum: 6")
print("All checks passed.")
