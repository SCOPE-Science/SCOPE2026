#!/usr/bin/env python3
"""Literal independent checks of Cantor first-repeat complexity."""
from itertools import product


def cantork(k):
    w = "1"
    for _ in range(k):
        w = "".join("101" if c == "1" else "000" for c in w)
    return w


def first_repeat(w, n):
    seen = {}
    for i in range(len(w) - n + 1):
        subword = w[i:i+n]
        if subword in seen:
            return seen[subword], i
        seen[subword] = i
    raise AssertionError("Need a longer iterate")


def formula(n):
    if n == 1:
        return 2
    m = 1
    while n > 3*m:
        m *= 3
    if n == 3*m:
        return 5*m
    if n <= 2*m:
        return 2*m
    return 3*m+1


def block_checks():
    cases = 0
    for m in range(1, 9):
        for interior in product("01", repeat=max(0, m-2)):
            A = "1" + "".join(interior) + "1" if m > 1 else "1"
            w = A + "0"*m + A + "0"*(3*m) + A + "0"*m
            for n, end in ((2*m+1, 3*m+1), (3*m, 5*m)):
                factors = [w[i:i+n] for i in range(end)]
                assert len(set(factors)) == len(factors), (m, A, n)
                cases += 1
    return cases


def run():
    w = cantork(8)
    assert len(w) == 6561
    for n in range(1, 730):
        earlier, observed = first_repeat(w, n)
        assert observed == formula(n), (n, observed, formula(n), earlier)
    cases = block_checks()
    print(f"PASS 729 full first-repeat scans; {cases} generic block tests; word length {len(w)}")

if __name__ == "__main__":
    run()
