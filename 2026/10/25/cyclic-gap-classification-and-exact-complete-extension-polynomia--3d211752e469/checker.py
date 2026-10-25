"""Independent finite check for a bidirected-cycle complete-extension census.

Run: python3 checker.py.  Only the Python standard library is required.
"""
from collections import Counter


def check_complete(mask, n):
    """Evaluate Dung's definition, without using the gap normal form."""
    chosen = {v for v in range(n) if (mask >> v) & 1}
    attacks = {(v - 1) % n for v in chosen} | {(v + 1) % n for v in chosen}
    if chosen & attacks:
        return False
    for v in range(n):
        attackers = {(v - 1) % n, (v + 1) % n}
        defended = attackers.issubset(attacks)
        if defended != (v in chosen):
            return False
    return True


def direct_profile(n):
    result = Counter()
    for mask in range(1 << n):
        if check_complete(mask, n):
            result[mask.bit_count()] += 1
    return result


def gap_profile(n):
    result = Counter({0: 1})
    for mask in range(1, 1 << n):
        v = [j for j in range(n) if (mask >> j) & 1]
        gaps = [(v[(j + 1) % len(v)] - v[j]) % n for j in range(len(v))]
        # For one selected world, the cyclic gap is n (not 0).
        if len(v) == 1:
            gaps = [n]
        if all(d in (2, 3) or d >= 5 for d in gaps):
            result[len(v)] += 1
    return result


def composition_profile(n):
    # Coefficient a(n,k)=[z^n] (z^2+z^3+z^5/(1-z))^k.
    old = [0] * (n + 1)
    old[0] = 1
    out = Counter({0: 1})
    for k in range(1, n // 2 + 1):
        nxt = [0] * (n + 1)
        for m in range(n + 1):
            if not old[m]:
                continue
            for gap in [2, 3] + list(range(5, n - m + 1)):
                if m + gap <= n:
                    nxt[m + gap] += old[m]
        old = nxt
        value = n * old[n]
        assert value % k == 0, (n, k, value)
        if value:
            out[k] = value // k
    return out


def stable_count(n):
    count = 0
    for mask in range(1 << n):
        chosen = {i for i in range(n) if (mask >> i) & 1}
        if not chosen:
            continue
        attacked = {(i + 1) % n for i in chosen} | {(i - 1) % n for i in chosen}
        if not (chosen & attacked) and len(chosen | attacked) == n:
            count += 1
    return count


def stable_compositions(n):
    old = [0] * (n + 1)
    old[0] = 1
    total = 0
    for k in range(1, n // 2 + 1):
        nxt = [0] * (n + 1)
        for j in range(n + 1):
            for d in (2, 3):
                if j + d <= n:
                    nxt[j + d] += old[j]
        old = nxt
        assert (n * old[n]) % k == 0
        total += n * old[n] // k
    return total


def G(t):
    return t*t+t*t*t+t**5/(1-t)


def main():
    count_masks = 0
    for n in range(3, 17):
        direct = direct_profile(n)
        gap = gap_profile(n)
        comp = composition_profile(n)
        assert direct == gap == comp, (n, direct, gap, comp)
        assert stable_count(n) == stable_compositions(n), n
        count_masks += 1 << n
        print('n=%2d complete=%6d stable=%5d profile=%s' %
              (n, sum(direct.values()), stable_count(n), sorted(direct.items())))
    low, high = 0.0, 1.0
    for _ in range(100):
        mid = (low+high)/2
        if G(mid) < 1:
            low = mid
        else:
            high = mid
    lam = 1/((low+high)/2)
    assert 1.54990 < lam < 1.54991
    assert G(1/lam) - 1 < 1e-12
    print('G-root growth base', format(lam,'.12f'))
    print('ALL_CHECKS_OK; masks=', count_masks)


if __name__ == '__main__':
    main()
