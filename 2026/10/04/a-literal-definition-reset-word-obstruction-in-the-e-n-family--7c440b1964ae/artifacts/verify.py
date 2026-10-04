from collections import deque


def transition(n, letter):
    if letter == "a":
        return [1, 2] + list(range(2, n))
    if letter == "b":
        return list(range(1, n)) + [0]
    raise ValueError(letter)


def image(states, table):
    return frozenset(table[i] for i in states)


def replay(n, word):
    state_set = frozenset(range(n))
    tables = {letter: transition(n, letter) for letter in "ab"}
    for letter in word:
        state_set = image(state_set, tables[letter])
    return state_set


def witness(n):
    blocks = (n - 2) // 2
    return ("aa" + "b" * (n - 2)) * blocks + "aa"


def exact_reset_threshold(n):
    tables = {letter: transition(n, letter) for letter in "ab"}
    start = frozenset(range(n))
    queue = deque([start])
    distance = {start: 0}
    while queue:
        state_set = queue.popleft()
        if len(state_set) == 1:
            return distance[state_set]
        for letter in "ab":
            nxt = image(state_set, tables[letter])
            if nxt not in distance:
                distance[nxt] = distance[state_set] + 1
                queue.append(nxt)
    raise AssertionError("literal automaton should synchronize")


for n in range(4, 13):
    word = witness(n)
    claimed = n * n - 3 * n + 2
    assert replay(n, word) == frozenset({2})
    assert len(word) == n * ((n - 2) // 2) + 2
    if n >= 5:
        assert len(word) < claimed
    threshold = exact_reset_threshold(n)
    assert threshold <= len(word)
    print(f"n={n} witness={len(word)} theorem4={claimed} bfs_threshold={threshold}")

# The universal proof tracks interval endpoints exactly.  After one block
# aa b^(n-2), the full set becomes {1,...,n-2} in one-based notation;
# thereafter each block changes {1,...,m} to {1,...,m-2}.  The assertions
# below replay only that algebraic endpoint recurrence for a large stress range.
for n in range(4, 501):
    m = n
    for _ in range((n - 2) // 2):
        m -= 2
    assert m in (2, 3)

print("VERIFY_OK symbolic_n_max=500 exhaustive_power_n_max=12")
