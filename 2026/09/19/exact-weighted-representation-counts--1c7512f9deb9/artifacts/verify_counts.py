from collections import defaultdict
from math import pi, sqrt, exp


def boundary_columns(k, T):
    ns = [T + ((s - T) % k) for s in range(k)]
    qs = [(ns[s] - s) // k for s in range(k)]
    columns = []
    for x in range(T + k):
        columns.append(tuple(
            int(x <= qs[s]) + int(x % k == s and x <= ns[s])
            for s in range(k)
        ))
    return qs, columns


def exact_count(k, T, cvec):
    qs, columns = boundary_columns(k, T)
    target = tuple(qs[s] + 1 - cvec[s] for s in range(k))
    zero = (0,) * k
    dp = {zero: 1}
    for col in columns:
        nxt = dict(dp)
        for state, multiplicity in dp.items():
            new_state = tuple(state[s] + col[s] for s in range(k))
            if all(new_state[s] <= target[s] for s in range(k)):
                nxt[new_state] = nxt.get(new_state, 0) + multiplicity
        dp = nxt
    return dp.get(target, 0)


def constant(k):
    return (8 * k / pi) ** (k / 2) / sqrt(k + 3)


def scalar_profile(k, lam):
    return exp(-2 * k * k * lam * lam / (k + 3))


def normalized_ratio(k, T, c):
    count = exact_count(k, T, (c,) * k)
    base = constant(k) * (2 ** T) / (T ** (k / 2))
    lam = c / sqrt(T)
    prediction = base * scalar_profile(k, lam)
    return count, count / prediction


def main():
    print("Exact-count checks for the weighted-representation local-limit formula")
    for k in (2, 3):
        print(f"C_{k} = {constant(k):.15f}")
    tests = [
        (2, 40, 0),
        (2, 80, 0),
        (2, 120, 0),
        (2, 200, 0),
        (3, 25, 0),
        (3, 40, 0),
        (3, 60, 0),
        (2, 80, 4),
        (2, 120, 5),
        (2, 200, 7),
    ]
    for k, T, c in tests:
        count, ratio = normalized_ratio(k, T, c)
        print(f"k={k:1d} T={T:3d} c={c:2d} count={count} actual/predicted={ratio:.12f}")


if __name__ == "__main__":
    main()
