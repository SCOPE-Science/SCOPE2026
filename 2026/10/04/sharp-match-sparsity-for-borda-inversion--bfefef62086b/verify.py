from math import comb


def construction(n):
    wins = [0] * n
    reduced_wins = [0] * (n - 1)
    games = [0] * n
    total = 0

    # One decisive match for each pair among the surviving players;
    # the higher index wins.
    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            wins[j] += 1
            reduced_wins[j] += 1
            games[i] += 1
            games[j] += 1
            total += 1

    # Extra decisive matches against the deleted player P_n.
    for i in range(n - 1):
        q = 2 * (n - 1 - (i + 1))
        wins[i] += q
        games[i] += q
        games[n - 1] += q
        total += q

    return wins, reduced_wins, games, total


def check(n):
    wins, reduced, games, total = construction(n)
    assert wins == [2 * n - 4 - i for i in range(n - 1)] + [0]
    assert reduced == list(range(n - 1))
    assert all(wins[i] > wins[i + 1] for i in range(n - 1))
    assert all(reduced[i] < reduced[i + 1] for i in range(n - 2))
    assert total == 3 * comb(n - 1, 2)

    q = [2 * (n - 1 - (i + 1)) for i in range(n - 1)]
    assert sum(q) == (n - 1) * (n - 2)
    for i in range(n - 2):
        assert q[i] - q[i + 1] == 2

    expected_delta = 3 if n == 3 else (n - 1) * (n - 2)
    assert max(games) == expected_delta

    # Arithmetic identity used in the total-match lower bound.
    lower_sum = sum(2 * n - 3 - i for i in range(1, n))
    assert lower_sum == 3 * comb(n - 1, 2)


for n in range(3, 101):
    check(n)

# Named small cases.
assert construction(3)[3] == 3
assert max(construction(3)[2]) == 3
assert construction(5)[3] == 18
assert max(construction(5)[2]) == 12
print('VERIFY_OK')
