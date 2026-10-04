from functools import lru_cache
from itertools import combinations

def partitions(n, lo=2):
    if n == 0:
        yield ()
        return
    for x in range(lo, n + 1):
        for rest in partitions(n - x, x):
            yield (x,) + rest

def distances(parts):
    part_of = []
    for i, size in enumerate(parts):
        part_of.extend([i] * size)
    n = len(part_of)
    d = [[0 if i == j else (1 if part_of[i] != part_of[j] else 2)
          for j in range(n)] for i in range(n)]
    return d

def is_gp(mask, n, d):
    vs = [i for i in range(n) if (mask >> i) & 1]
    for a, b, c in combinations(vs, 3):
        for x, y, z in ((a,b,c), (a,c,b), (b,a,c)):
            if d[x][z] == d[x][y] + d[y][z]:
                return False
    return True

def first_player_wins(parts, misere=False):
    d = distances(parts)
    n = sum(parts)
    @lru_cache(None)
    def win(mask):
        moves = [v for v in range(n)
                 if not ((mask >> v) & 1) and is_gp(mask | (1 << v), n, d)]
        if not moves:
            return True if misere else False
        return any(not win(mask | (1 << v)) for v in moves)
    return win(0)

count = 0
for order in range(4, 11):
    for parts in partitions(order):
        if len(parts) < 2:
            continue
        k = len(parts)
        achievement = (k % 2 == 1 and any(x % 2 == 1 for x in parts))
        avoidance = (k % 2 == 0 and any(x % 2 == 0 for x in parts))
        got = (first_player_wins(parts, False), first_player_wins(parts, True))
        assert got == (achievement, avoidance), (parts, got, achievement, avoidance)
        count += 1

assert first_player_wins((3,3), False) is False
assert first_player_wins((3,3), True) is False
assert first_player_wins((2,2,2), False) is False
assert first_player_wins((2,2,2), True) is False

print("VERIFY_OK")
print("checked", count, "complete multipartite isomorphism types of order at most 10")
print("K_{3,3}: B wins both games")
print("K_{2,2,2}: B wins both games")
