#!/usr/bin/env python3
from collections import defaultdict

CODES = {
    "5.40": "O1- O2- U1- U2- O3+ O4- U5- U4- O5- U3+",
    "5.107": "O1- O2- U1- U2- U3+ O4- U5- U4- O5- O3+",
    "5.880": "O1- O2- U1- O3+ O4- U5- U4- O5- U3+ U2-",
    "5.1238": "O1- O2- U1- O3+ U4- O5- O4- U5- U3+ U2-",
}
EXPECTED_PATHS = {
    "5.40": [("R2", 4, 5), ("R1", 3), ("R2", 1, 2)],
    "5.107": [("R2", 4, 5), ("R1", 3), ("R2", 1, 2)],
    "5.880": [("R2", 1, 2), ("R1", 3), ("R2", 4, 5)],
    "5.1238": [("R2", 1, 2), ("R1", 3), ("R2", 4, 5)],
}

def parse(text):
    out = []
    for token in text.split():
        out.append((token[0], int(token[1:-1]), 1 if token[-1] == "+" else -1))
    return out

def positions(code):
    out = defaultdict(list)
    for i, (_, crossing, _) in enumerate(code):
        out[crossing].append(i)
    return out

def signs(code):
    out = {}
    for _, crossing, sign in code:
        if crossing in out:
            assert out[crossing] == sign
        out[crossing] = sign
    return out

def odd_crossings(code):
    out = []
    for crossing, (i, j) in sorted(positions(code).items()):
        assert i < j
        if (j - i - 1) % 2 == 1:
            out.append(crossing)
    return out

def odd_writhe(code):
    s = signs(code)
    return sum(s[c] for c in odd_crossings(code))

def crossing_change(code, labels):
    labels = set(labels)
    return [
        (("U" if ou == "O" else "O") if crossing in labels else ou,
         crossing,
         -sign if crossing in labels else sign)
        for ou, crossing, sign in code
    ]

def cyclic_adjacent(i, j, n):
    return (i - j) % n in (1, n - 1)

def r1(code, crossing):
    p = positions(code)[crossing]
    assert len(p) == 2 and cyclic_adjacent(p[0], p[1], len(code))
    assert {code[p[0]][0], code[p[1]][0]} == {"O", "U"}
    return [t for t in code if t[1] != crossing]

def r2(code, a, b):
    s = signs(code)
    assert s[a] == -s[b]
    n = len(code)
    endpoint = {a: {}, b: {}}
    for i, (ou, crossing, _) in enumerate(code):
        if crossing in endpoint:
            endpoint[crossing][ou] = i
    assert set(endpoint[a]) == {"O", "U"} and set(endpoint[b]) == {"O", "U"}
    assert cyclic_adjacent(endpoint[a]["O"], endpoint[b]["O"], n)
    assert cyclic_adjacent(endpoint[a]["U"], endpoint[b]["U"], n)
    return [t for t in code if t[1] not in (a, b)]

for name, text in CODES.items():
    code = parse(text)
    assert odd_crossings(code) == [1, 2, 4, 5]
    assert odd_writhe(code) == -4
    lower_bound = abs(odd_writhe(code)) // 2
    assert lower_bound == 2
    code = crossing_change(code, {1, 4})
    for move in EXPECTED_PATHS[name]:
        if move[0] == "R1":
            code = r1(code, move[1])
        else:
            code = r2(code, move[1], move[2])
    assert code == []

print("VERIFY_OK knots=5.40,5.107,5.880,5.1238 odd_writhe=-4 lower_bound=2 upper_bound=2")
