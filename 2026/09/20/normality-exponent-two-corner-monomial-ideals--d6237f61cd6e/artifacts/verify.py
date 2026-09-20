from math import gcd


def semigroup_table(limit, b, c):
    hit = [False] * (limit + 1)
    for r in range(limit // b + 1):
        rem = limit - r * b
        for s in range(rem // c + 1):
            hit[r * b + s * c] = True
    return hit


def interval_criterion(b, c):
    """Exact criterion obtained from the proof for possible x-degree-one holes."""
    bc = b * c
    S = semigroup_table(bc, b, c)
    lower = (bc + 1) // 2
    for u in range(1, b + 1):
        for v in range(1, c + 1):
            q = c * u + b * v
            if 2 * q <= bc:
                upper = bc - q
                if not any(S[t] for t in range(lower, upper + 1)):
                    return False
    return True


def theorem_criterion(b, c):
    if b % 2 == 0 or c % 2 == 0:
        return True
    if gcd(b, c) > 1:
        return True
    T = (b * c + 1) // 2
    S = semigroup_table(T, b, c)
    return S[T]


def main():
    mismatches = []
    for b in range(2, 101):
        for c in range(2, 151):
            direct = interval_criterion(b, c)
            closed = theorem_criterion(b, c)
            if direct != closed:
                mismatches.append((b, c, direct, closed))
    print(f"pairs_checked={99 * 149}")
    print(f"mismatches={len(mismatches)}")
    if mismatches:
        print(mismatches[:20])
        raise SystemExit(1)


if __name__ == "__main__":
    main()
