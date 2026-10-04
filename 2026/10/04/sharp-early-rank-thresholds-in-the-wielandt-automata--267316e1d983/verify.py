#!/usr/bin/env python3
from collections import deque


def transitions(n):
    b = [(i + 1) % n for i in range(n)]
    c = [2 if i in (0, 1) else (i + 1) % n for i in range(n)]
    return b, c


def apply(mask, trans):
    out = 0
    for i, j in enumerate(trans):
        if (mask >> i) & 1:
            out |= 1 << j
    return out


def power_bfs(n):
    b, c = transitions(n)
    full = (1 << n) - 1
    dist = {full: 0}
    count = {full: 1}
    first = {full: ""}
    q = deque([full])
    while q:
        x = q.popleft()
        for letter, trans in (("b", b), ("c", c)):
            y = apply(x, trans)
            nd = dist[x] + 1
            if y not in dist:
                dist[y] = nd
                count[y] = count[x]
                first[y] = first[x] + letter
                q.append(y)
            elif dist[y] == nd:
                count[y] += count[x]
    return dist, count, first


def threshold_data(n, s, dist, count, first):
    target_rank = n - s
    best = min(d for mask, d in dist.items() if mask.bit_count() <= target_rank)
    targets = [mask for mask, d in dist.items() if d == best and mask.bit_count() <= target_rank]
    number_of_words = sum(count[mask] for mask in targets)
    witness = min(first[mask] for mask in targets)
    return best, number_of_words, witness


def direct_image(n, word):
    b, c = transitions(n)
    mask = (1 << n) - 1
    for letter in word:
        mask = apply(mask, b if letter == "b" else c)
    return mask


def main():
    lines = []
    for n in range(3, 15):
        dist, count, first = power_bfs(n)
        s0 = (n + 1) // 2
        profile = []
        for s in range(1, n):
            best, number, witness = threshold_data(n, s, dist, count, first)
            profile.append(best)
            if s <= s0:
                expected = "c" + "bc" * (s - 1)
                assert best == 2 * s - 1, (n, s, best)
                assert number == 1, (n, s, number)
                assert witness == expected, (n, s, witness, expected)
                mask = direct_image(n, expected)
                assert mask.bit_count() == n - s, (n, s, mask.bit_count())
        if s0 + 1 <= n - 1:
            next_best = profile[s0]
            assert next_best > 2 * (s0 + 1) - 1, (n, s0 + 1, next_best)
        lines.append("n=%d profile=%s" % (n, ",".join(map(str, profile))))
    print("VERIFY_OK")
    print("checked_n=3..14")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
