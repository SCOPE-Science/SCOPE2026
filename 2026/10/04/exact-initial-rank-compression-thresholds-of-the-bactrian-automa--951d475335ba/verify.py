from collections import deque


def step(n, subset, letter):
    if letter == "b":
        return frozenset(1 if q == n else q + 1 for q in subset)
    if letter == "a":
        return frozenset(1 if q == n - 1 else 2 if q == n else q for q in subset)
    raise ValueError(letter)


def apply(n, word):
    s = frozenset(range(1, n + 1))
    for c in word:
        s = step(n, s, c)
    return s


def expected(s):
    if s == 1:
        return 1
    if s % 2 == 0:
        k = (s - 2) // 2
        return 5 * k + 1
    k = (s - 1) // 2
    return 5 * k


def witness(s):
    if s == 1:
        return "a"
    if s % 2 == 0:
        k = (s - 2) // 2
        return "a" + "bbbba" * k
    k = (s - 1) // 2
    return "abbba" + "bbbba" * (k - 1)


def bfs_thresholds(n):
    start = frozenset(range(1, n + 1))
    dist = {start: 0}
    queue = deque([start])
    while queue:
        s = queue.popleft()
        for c in "ab":
            t = step(n, s, c)
            if t not in dist:
                dist[t] = dist[s] + 1
                queue.append(t)
    out = {}
    for deficiency in range(1, (n + 1) // 2 + 1):
        target = n - deficiency
        out[deficiency] = min(d for subset, d in dist.items() if len(subset) <= target)
    return out


def main():
    for n in range(5, 18, 2):
        got = bfs_thresholds(n)
        want = {s: expected(s) for s in got}
        assert got == want, (n, got, want)

    for n in range(5, 102, 2):
        for s in range(1, (n + 1) // 2 + 1):
            w = witness(s)
            image = apply(n, w)
            assert len(w) == expected(s), (n, s, w)
            assert n - len(image) >= s, (n, s, w, sorted(image))
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
