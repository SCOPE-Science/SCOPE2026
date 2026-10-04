#!/usr/bin/env python3

TABLE = {
    2: (13, 7),
    3: (149, 75),
    4: (2641, 1321),
    5: (6261, 3175),
    6: (711649, 355825),
    7: (249077, 127839),
    8: (1890241, 945121),
    9: (6464397, 3438463),
}

def reachability(limit, generators):
    r = bytearray(limit + 1)
    r[0] = 1
    generators = sorted(set(generators))
    for x in range(limit + 1):
        if r[x]:
            for g in generators:
                y = x + g
                if y > limit:
                    break
                r[y] = 1
    return r

def check_S(k, expected_F, expected_g):
    A = 2**k - 1
    limit = expected_F + A
    gens = []
    n = 2
    while n**k - 1 <= limit:
        gens.append(n**k - 1)
        n += 1
    r = reachability(limit, gens)
    gaps = [x for x in range(1, expected_F + 1) if not r[x]]
    assert gaps[-1] == expected_F
    assert len(gaps) == expected_g
    assert all(r[expected_F + 1: expected_F + A + 1])
    return A

def check_T(k, A, expected_F, expected_g):
    F_T_num = expected_F - A
    assert F_T_num % 2 == 0
    F_T = F_T_num // 2
    limit = F_T + A
    gens = [A]
    u = 3
    while (u**k - 1)//2 <= limit:
        gens.append((u**k - 1)//2)
        u += 2
    r = reachability(limit, gens)
    gaps = [x for x in range(1, F_T + 1) if not r[x]]
    assert gaps[-1] == F_T
    g_T = len(gaps)
    assert all(r[F_T + 1: F_T + A + 1])
    assert expected_F == A + 2*F_T
    assert expected_g == 2*g_T + (A - 1)//2
    return F_T, g_T

def main():
    rows = []
    for k, (a, b) in TABLE.items():
        A = check_S(k, a, b)
        F_T, g_T = check_T(k, A, a, b)
        assert a % 2 == 1 and b % 2 == 1
        rows.append((k, A, F_T, g_T, a, b))
    print("VERIFY_OK")
    print("k A_k F(T_k) g(T_k) a_k b_k")
    for row in rows:
        print(*row)

if __name__ == "__main__":
    main()
