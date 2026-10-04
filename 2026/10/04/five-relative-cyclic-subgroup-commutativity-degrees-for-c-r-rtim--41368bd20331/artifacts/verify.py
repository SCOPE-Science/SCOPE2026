from fractions import Fraction

def find_action(r, m):
    for t in range(2, r):
        x = 1
        for k in range(1, m + 1):
            x = (x * t) % r
            if x == 1:
                if k == m:
                    return t
                break
    raise AssertionError("no action of required order")

def check_case(p, q, r):
    m = p * q
    assert (r - 1) % m == 0
    t = find_action(r, m)
    E = [(a, b) for a in range(r) for b in range(m)]
    e = (0, 0)

    def mul(g, h):
        a, b = g
        c, d = h
        return ((a + pow(t, b, r) * c) % r, (b + d) % m)

    def inv(g):
        a, b = g
        scale = pow(pow(t, b, r), -1, r)
        return ((-scale * a) % r, (-b) % m)

    def cyclic(g):
        H = {e}
        x = e
        while True:
            x = mul(x, g)
            if x == e:
                break
            H.add(x)
        return frozenset(H)

    def generated(gens):
        H = {e}
        changed = True
        while changed:
            changed = False
            current = list(H)
            for x in list(gens) + current:
                if x not in H:
                    H.add(x)
                    changed = True
                y = inv(x)
                if y not in H:
                    H.add(y)
                    changed = True
            current = list(H)
            for x in current:
                for y in current:
                    z = mul(x, y)
                    if z not in H:
                        H.add(z)
                        changed = True
        return frozenset(H)

    def set_product(H, K):
        return frozenset(mul(h, k) for h in H for k in K)

    def permutes(H, K):
        return set_product(H, K) == set_product(K, H)

    cyclic_subgroups = {cyclic(g) for g in E}
    L = len(cyclic_subgroups)
    assert L == 3 * r + 2

    one = frozenset({e})
    A = cyclic((1, 0))
    B = cyclic((0, 1))
    P = cyclic((0, q))
    Q = cyclic((0, p))
    Kp = generated([(1, 0), (0, q)])
    Kq = generated([(1, 0), (0, p)])
    G = frozenset(E)

    partners = {
        H: sum(1 for K in cyclic_subgroups if permutes(H, K))
        for H in cyclic_subgroups
    }
    assert partners[one] == L
    assert partners[A] == L
    assert set(
        partners[H]
        for H in cyclic_subgroups
        if H not in (one, A)
    ) == {5}

    def csd(H):
        LH = [K for K in cyclic_subgroups if K.issubset(H)]
        numerator = sum(partners[K] for K in LH)
        return Fraction(numerator, len(LH) * L)

    expected = {
        "one": Fraction(1, 1),
        "A": Fraction(1, 1),
        "P": Fraction(3 * r + 7, 2 * (3 * r + 2)),
        "Q": Fraction(3 * r + 7, 2 * (3 * r + 2)),
        "B": Fraction(3 * r + 17, 4 * (3 * r + 2)),
        "Kp": Fraction(11 * r + 4, (r + 2) * (3 * r + 2)),
        "Kq": Fraction(11 * r + 4, (r + 2) * (3 * r + 2)),
        "G": Fraction(21 * r + 4, (3 * r + 2) ** 2),
    }
    got = {
        "one": csd(one),
        "A": csd(A),
        "P": csd(P),
        "Q": csd(Q),
        "B": csd(B),
        "Kp": csd(Kp),
        "Kq": csd(Kq),
        "G": csd(G),
    }
    assert got == expected, (p, q, r, got, expected)
    assert len(set(got.values())) == 5

for case in [(2, 3, 7), (2, 5, 11), (2, 3, 13)]:
    check_case(*case)

print("VERIFY_OK")
