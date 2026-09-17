"""Finite-torus sanity check for the unequal-prime axis-periodicity theorem.

Example: A={0,1}, B={0,1,5}; |A|=2, |B|=3,
gcd(A-A)=gcd(B-B)=1. Enumerate exact A×B-tilings of Z_6×Z_6
and verify each translation set has period (2,0) or (0,3).
"""


def torus_tilings(W, H, A, B, limit=100000):
    cells = [(x, y) for y in range(H) for x in range(W)]
    idx = {c: i for i, c in enumerate(cells)}
    placements = []
    for tx in range(W):
        for ty in range(H):
            s = {((tx + a) % W, (ty + b) % H) for a in A for b in B}
            if len(s) != len(A) * len(B):
                continue
            mask = 0
            for c in s:
                mask |= 1 << idx[c]
            placements.append(((tx, ty), mask))

    bycell = [[] for _ in cells]
    for j, (_, mask) in enumerate(placements):
        for i in range(W * H):
            if (mask >> i) & 1:
                bycell[i].append(j)

    full = (1 << (W * H)) - 1
    sols = []

    def rec(covered, chosen):
        if len(sols) >= limit:
            return
        if covered == full:
            sols.append({placements[j][0] for j in chosen})
            return

        best = None
        for i in range(W * H):
            if not ((covered >> i) & 1):
                opts = [j for j in bycell[i] if placements[j][1] & covered == 0]
                if not opts:
                    return
                if best is None or len(opts) < len(best):
                    best = opts
                    if len(best) == 1:
                        break

        for j in best:
            rec(covered | placements[j][1], chosen + [j])

    rec(0, [])
    return sols


def has_period(S, W, H, dx, dy):
    shifted = {((x + dx) % W, (y + dy) % H) for x, y in S}
    return shifted == S


if __name__ == "__main__":
    W = H = 6
    A = [0, 1]
    B = [0, 1, 5]
    sols = torus_tilings(W, H, A, B)
    bad = [
        S
        for S in sols
        if not (has_period(S, W, H, 2, 0) or has_period(S, W, H, 0, 3))
    ]
    print(f"tilings enumerated: {len(sols)}")
    print(f"violations of predicted axis-periodicity: {len(bad)}")
    assert len(sols) == 60
    assert not bad
