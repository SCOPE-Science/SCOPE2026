from math import gcd

def phi(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)

def Phi(n):
    return sum(phi(m) for m in range(1, n + 1))

for r in range(2, 201):
    can = {}
    for d in range(0, r + 1):
        for a in range(1, r + d + 1):
            b = a + d
            g = gcd(a, b)
            can[g] = can.get(g, 0) + 1

    term = {}
    for d in range(0, r):
        for a in range(1, r + d):
            b = a + d
            g = gcd(a, b)
            term[g] = term.get(g, 0) + 1

    for g in range(1, r + 1):
        assert can.get(g, 0) == 3 * Phi(r // g)
        assert term.get(g, 0) == 3 * Phi((r - 1) // g)

    assert sum(can.values()) == 3 * r * (r + 1) // 2
    assert sum(term.values()) == 3 * r * (r - 1) // 2

print("VERIFY_OK")
