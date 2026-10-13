"""Independent finite checks for an exact cyclic-automaton reset formula.

Run with Python 3: python verify.py
No external packages are required. Finite tests corroborate the proof, not replace it.
"""
from collections import deque


def moves(n):
    return (tuple((i + 1) % n for i in range(n)),
            tuple((i + 1) % n if i % 2 == 0 else i for i in range(n)))


def upper_word(n):
    assert n % 2 == 1 and n >= 3
    k = (n - 1) // 2
    if n == 3:
        return "bb"
    chunks = ["bb"]
    for j in range(1, k - 1):
        chunks.extend(["a" * (n - 2 * j), "b", "a" * (2 * j), "b"])
    chunks.extend(["aaa", "bb"])
    return "".join(chunks)


def expected(n):
    if n % 2 == 0:
        return None
    k = (n - 1) // 2
    return 2 * k * k - k + 1


def potential(n, length, start):
    assert n >= 5 and n % 2 == 1
    k = (n - 1) // 2
    if length == n:
        return 2 * k * k - k + 1
    if length == 1:
        return 0
    if length == 2:
        return 1
    if length % 2:
        j = (length - 1) // 2
        return j * n + 1 - start
    j = length // 2
    return ((j - 1) * n + 1 - start
            if start <= n - length - 1 else j * n + 1 - start)


def apply_mask(mask, n, action):
    out = 0
    for s in range(n):
        if mask & (1 << s):
            out |= 1 << action[s]
    return out


def shortest(n):
    a, b = moves(n)
    full = (1 << n) - 1
    q = deque([full])
    distance = {full: 0}
    while q:
        mask = q.popleft()
        if mask.bit_count() == 1:
            return distance[mask]
        for action in (a, b):
            nxt = apply_mask(mask, n, action)
            if nxt not in distance:
                distance[nxt] = distance[mask] + 1
                q.append(nxt)
    return None


def main():
    bfs_count = 0
    for n in range(2, 20):
        actual = shortest(n)
        assert actual == (1 if n == 2 else expected(n)), (n, actual, expected(n))
        bfs_count += 1
    word_count = 0
    for n in range(3, 152, 2):
        a, b = moves(n)
        word = upper_word(n)
        assert len(word) == expected(n)
        states = set(range(n))
        for letter in word:
            action = a if letter == "a" else b
            states = {action[s] for s in states}
        assert states == {1}, (n, states)
        word_count += 1
    transitions = 0
    # Check independently computed inverse images and the lower-bound potential.
    for n in range(5, 102, 2):
        a, b = moves(n)
        for length in range(1, n):
            for start in range(n):
                source = {(start + t) % n for t in range(length)}
                inva = {i for i in range(n) if a[i] in source}
                invb = {i for i in range(n) if b[i] in source}
                assert inva == {(start - 1 + t) % n for t in range(length)}
                e = (start + length - 1) % n
                alpha = int(start == 0 or start % 2 == 1)
                beta = int(e % 2 == 0)
                nxtlength = length + alpha - beta
                nxtstart = (start - alpha) % n
                predicted = {(nxtstart + t) % n for t in range(nxtlength)}
                assert invb == predicted, (n, length, start)
                assert potential(n, length, start) + 1 >= potential(n, length, (start - 1) % n)
                transitions += 1
                if nxtlength:
                    assert potential(n, length, start) + 1 >= potential(n, nxtlength, nxtstart), (n, length, start, nxtlength, nxtstart)
                    transitions += 1
        assert potential(n, n, 0) == expected(n)
    print("VERIFY_OK", "bfs_n=2..19", f"bfs_cases={bfs_count}",
          f"witness_odd_n=3..151_count={word_count}",
          f"inverse_potential_edges={transitions}")


if __name__ == "__main__":
    main()
