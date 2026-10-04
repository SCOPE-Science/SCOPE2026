#!/usr/bin/env python3

def C(S, X, full):
    return (S | (full ^ X)) if (S & ~X) == 0 else S

# Exhaustive algebra check on all triples through seven worlds.
for N in range(1, 8):
    full = (1 << N) - 1
    for X in range(1 << N):
        for S in range(1 << N):
            assert C(C(S, X, full), X, full) == C(S, X, full)
    for X in range(1 << N):
        for Y in range(1 << N):
            expected = (X == Y) or ((X | Y) == full)
            actual = True
            for S in range(1 << N):
                if C(C(S, Y, full), X, full) != C(C(S, X, full), Y, full):
                    actual = False
                    break
            assert actual == expected, (N, X, Y)

# Exact commuting-pair census through eight worlds.
for N in range(1, 9):
    full = (1 << N) - 1
    count = 0
    for X in range(1 << N):
        for Y in range(1 << N):
            if X == Y or (X | Y) == full:
                count += 1
    assert count == (2 ** N) + (3 ** N) - 1

expected = {1: 12, 2: 96, 3: 6816}
for n, want in expected.items():
    N = 2 ** n
    got = (2 ** N) + (3 ** N) - 1
    assert got == want

print("VERIFY_OK")
