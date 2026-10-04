#!/usr/bin/env python3
import math

def properties(n, relation):
    def le(a, b):
        return a <= b

    doxastic = all(le(a, b) for a, b in relation)

    ap = True
    for s in range(n):
        for t in range(n):
            if any(le(s, u) and (u, t) in relation for u in range(n)):
                if (s, t) not in relation:
                    ap = False
                    break
        if not ap:
            break

    basic = all(
        any(
            le(s, u) and le(v, u) and (v, t) in relation
            for u in range(n)
            for v in range(n)
            for t in range(n)
        )
        for s in range(n)
    )

    visionary = all(
        any(le(s, u) and (u, t) in relation for u in range(n) for t in range(n))
        for s in range(n)
    )

    futuristic = all(
        any(
            le(s, t)
            and any(le(s, u) and (u, v) in relation and le(v, t)
                    for u in range(n) for v in range(n))
            for t in range(n)
        )
        for s in range(n)
    )

    return doxastic, ap, basic, visionary, futuristic

for n in range(1, 5):
    pairs = [(i, j) for i in range(n) for j in range(n)]
    counts = [0, 0, 0, 0]
    for mask in range(1 << len(pairs)):
        relation = {pairs[k] for k in range(len(pairs)) if (mask >> k) & 1}
        dox, ap, basic, visionary, futuristic = properties(n, relation)
        if dox and ap:
            counts[0] += 1
            counts[1] += int(basic)
            counts[2] += int(visionary)
            counts[3] += int(futuristic)
            assert visionary == futuristic

    expected = [
        math.factorial(n + 1),
        math.factorial(n + 1) - 1,
        math.factorial(n),
        math.factorial(n),
    ]
    assert counts == expected, (n, counts, expected)

print("VERIFY_OK")
