"""Independent finite checks for the minimum double vertex-edge dominating sets of cycles.

Run: python verify.py. Uses only the Python standard library.
"""
from itertools import combinations


def predicted(n):
    if n % 2:
        return n * ((n + 3) // 4)
    return 6 if n % 4 == 0 else 2


def gap_profile(n, chosen):
    points = sorted(chosen)
    gaps = [(points[(i + 1) % len(points)] - points[i]) % n
            for i in range(len(points))]
    k = len(points)
    if n < 5:
        return True
    if any(a + b > 4 for a, b in zip(gaps, gaps[1:] + gaps[:1])):
        return False
    if n % 2 == 0:
        return (all(d == 2 for d in gaps) or
                (n % 4 == 0 and all(gaps[i] == gaps[i % 2]
                                      for i in range(k)) and
                 set(gaps) == {1, 3}))
    for r in range((k - 1) // 2 + 1):
        core = [1, 3] * r + [1]
        rest = [2] * (k - len(core))
        target = core + rest
        if any(gaps == target[j:] + target[:j] for j in range(k)):
            return True
    return False


def direct(n):
    # Test the original closed-edge-neighborhood definition, not the four-window reformulation.
    edge_covers = []
    for i in range(n):
        u, v = i, (i + 1) % n
        cover = set()
        for w in (u, v):
            cover.update((w, (w - 1) % n, (w + 1) % n))
        edge_covers.append(cover)
    k = (n + 1) // 2
    good = []
    for chosen in combinations(range(n), k):
        ss = set(chosen)
        if all(len(ss & cov) >= 2 for cov in edge_covers):
            assert gap_profile(n, chosen), (n, chosen)
            good.append(chosen)
    assert len(good) == predicted(n), (n, len(good), predicted(n))
    for t in range(k):
        assert not any(all(len(set(chosen) & cov) >= 2 for cov in edge_covers)
                       for chosen in combinations(range(n), t)), (n, t)
    return len(good)


def transfer(n):
    # Weighted 8-state transfer: state is a binary 3-word; each allowed 4-window has >=2 ones.
    # Trace of length-n transfer walks counts all valid named cyclic 0/1 words by weight.
    k = (n + 1) // 2
    total = 0
    for start in range(8):
        dp = {(start, 0): 1}
        for _ in range(n):
            nxt = {}
            for (state, weight), count in dp.items():
                a, b, c = (state >> 2) & 1, (state >> 1) & 1, state & 1
                for bit in (0, 1):
                    if a + b + c + bit < 2 or weight + bit > k:
                        continue
                    new_state = ((state << 1) & 7) | bit
                    key = (new_state, weight + bit)
                    nxt[key] = nxt.get(key, 0) + count
            dp = nxt
        total += dp.get((start, k), 0)
    return total


if __name__ == "__main__":
    for n in range(3, 19):
        print("direct", n, direct(n))
    for n in range(5, 81):
        result = transfer(n)
        assert result == predicted(n), (n, result, predicted(n))
    print("all transfer counts for 5 <= n <= 80 match closed formula")
    print("PASS")
