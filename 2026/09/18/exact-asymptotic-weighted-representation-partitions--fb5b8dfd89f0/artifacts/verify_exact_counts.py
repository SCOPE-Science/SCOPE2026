from collections import defaultdict
from itertools import product
from math import comb, exp, pi, sqrt


def boundary_data(k, T):
    r = T % k
    ns = [T + ((s - r) % k) for s in range(k)]
    qs = [(ns[s] - s) // k for s in range(k)]
    Q = max(qs)
    P = [
        [x for x in range(Q + 1, ns[s] + 1) if x % k == s]
        for s in range(k)
    ]
    C = [x for x in range(T + k) if not any(x in P_s for P_s in P)]
    return ns, qs, Q, [len(P_s) for P_s in P], C


def direct_boundary_count(k, T, c):
    ns, qs, _, _, _ = boundary_data(k, T)
    total = 0
    for signs in product((-1, 1), repeat=T + k):
        ok = True
        for s in range(k):
            lhs = sum(signs[j] for j in range(qs[s] + 1))
            lhs += sum(signs[k * j + s] for j in range(qs[s] + 1))
            if lhs != 2 * c:
                ok = False
                break
        total += int(ok)
    return total


def exact_count(k, T, c):
    _, qs, Q, M, C = boundary_data(k, T)
    assert C == list(range(Q + 1))
    dp = {(0,) * k: 1}
    for x in C:
        coeff = tuple(
            int(x <= qs[s]) + int(x % k == s)
            for s in range(k)
        )
        nxt = defaultdict(int)
        for state, multiplicity in dp.items():
            plus = tuple(state[s] + coeff[s] for s in range(k))
            minus = tuple(state[s] - coeff[s] for s in range(k))
            nxt[plus] += multiplicity
            nxt[minus] += multiplicity
        dp = nxt

    total = 0
    for state, multiplicity in dp.items():
        ways = 1
        for s in range(k):
            h = 2 * c - state[s]
            if abs(h) > M[s] or (M[s] + h) % 2:
                ways = 0
                break
            ways *= comb(M[s], (M[s] + h) // 2)
        total += multiplicity * ways
    return total


def fixed_c_constant(k):
    return (2 ** k) * (2 * k / pi) ** (k / 2) / sqrt(k + 3)


def diffusive_constant(k, gamma):
    return fixed_c_constant(k) * exp(-2 * k * k * gamma * gamma / (k + 3))


def scaled(total, k, T):
    return total * (T ** (k / 2)) / (2 ** T)


print("Small direct checks")
for k, T, c in ((2, 5, 0), (2, 7, 1), (3, 5, 0), (3, 6, 1)):
    direct = direct_boundary_count(k, T, c)
    reduced = exact_count(k, T, c)
    print(k, T, c, direct, reduced, direct == reduced)

print("Fixed-c checks")
for k in (2, 3, 4):
    for T in (50, 100, 200):
        total = exact_count(k, T, 0)
        value = scaled(total, k, T)
        predicted = fixed_c_constant(k)
        print(k, T, f"{value:.12f}", f"{predicted:.12f}", f"{value/predicted:.12f}")

print("Diffusive c_T checks")
for k in (2, 3):
    for T in (100, 200, 400):
        gamma = 0.5
        c = round(gamma * sqrt(T))
        total = exact_count(k, T, c)
        value = scaled(total, k, T)
        predicted = diffusive_constant(k, gamma)
        print(k, T, c, f"{value:.12f}", f"{predicted:.12f}", f"{value/predicted:.12f}")
