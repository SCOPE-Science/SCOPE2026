from collections import deque


def step_subset(S, n, letter):
    if letter == "a":
        return frozenset((q + 1) % n for q in S)
    if letter == "b":
        return frozenset(0 if q == n - 1 else q for q in S)
    raise ValueError(letter)


def apply_word(S, n, word):
    for letter in word:
        S = step_subset(S, n, letter)
    return S


def shortest_to_rank(n, target_rank):
    start = frozenset(range(n))
    queue = deque([(start, 0)])
    seen = {start}
    while queue:
        S, dist = queue.popleft()
        if len(S) <= target_rank:
            return dist
        for letter in "ab":
            T = step_subset(S, n, letter)
            if T not in seen:
                seen.add(T)
                queue.append((T, dist + 1))
    raise AssertionError("target rank unreachable")


def witness(s):
    return "b" + "aab" * (s - 1)


def expected_missing(n, s):
    if s == 1:
        return {n - 1}
    return set(range(1, 2 * s - 2, 2)) | {n - 1}


def main():
    checked = 0
    for n in range(3, 13):
        max_s = (n + 1) // 2
        row = []
        for s in range(1, max_s + 1):
            w = witness(s)
            image = apply_word(frozenset(range(n)), n, w)
            missing = set(range(n)) - set(image)
            assert len(w) == 3 * s - 2
            assert len(image) == n - s
            assert missing == expected_missing(n, s)
            exact = shortest_to_rank(n, n - s)
            assert exact == 3 * s - 2
            row.append(f"s={s}:L={exact}")
            checked += 1
        print(f"n={n} " + " ".join(row))
    print(f"BFS_CASES={checked}")
    print("FORMULA_CHECK=PASS")
    print("NOTE=Finite BFS is a check only; the all-n proof is the counting argument in RESULT.md.")


if __name__ == "__main__":
    main()
