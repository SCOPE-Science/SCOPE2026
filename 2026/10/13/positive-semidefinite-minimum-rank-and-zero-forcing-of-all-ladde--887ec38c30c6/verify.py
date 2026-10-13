"""Integer Gram certificate and independent graph checks for powers of two-row grids.
Run with Python 3 (standard library only): python3 verify.py
"""
from collections import deque
from itertools import combinations


def graph_power(length, power):
    """Power graph from BFS on the original ladder, independent of matrix design."""
    count = 2 * length
    original = [set() for _ in range(count)]
    def index(row, column):
        return row * length + column
    for column in range(length):
        a, b = index(0, column), index(1, column)
        original[a].add(b)
        original[b].add(a)
    for row in range(2):
        for column in range(length - 1):
            a, b = index(row, column), index(row, column + 1)
            original[a].add(b)
            original[b].add(a)
    answer = []
    for start in range(count):
        dist = [-1] * count
        dist[start] = 0
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            for nxt in original[vertex]:
                if dist[nxt] == -1:
                    dist[nxt] = dist[vertex] + 1
                    queue.append(nxt)
        answer.append({other for other in range(count)
                       if other != start and dist[other] <= power})
    return answer


def gram_factor(length, power):
    """An integer factor with exactly 2(length-power) rows and 2length columns."""
    windows = length - power
    u = [(1, 3) for _ in range(power + 1)]
    v = [(3, 7) for _ in range(power + 1)]
    u[0], u[power] = (1, 0), (1, 1)
    v[0], v[power] = (1, -1), (0, 1)
    x = [[0] * (2 * length) for _ in range(2 * windows)]
    for row in range(2):
        for column in range(length):
            for window in range(windows):
                offset = column - window
                if 0 <= offset <= power:
                    a, b = (u if row == 0 else v)[offset]
                    x[2 * window][row * length + column] = a
                    x[2 * window + 1][row * length + column] = b
    return x


def rank_mod(matrix, prime=1000003):
    a = [[int(z) % prime for z in row] for row in matrix]
    if not a:
        return 0
    height, width = len(a), len(a[0])
    rank = 0
    for col in range(width):
        pivot = next((r for r in range(rank, height) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, prime)
        a[rank] = [(z * inv) % prime for z in a[rank]]
        for r in range(rank + 1, height):
            if a[r][col]:
                factor = a[r][col]
                a[r] = [(u - factor * v) % prime for u, v in zip(a[r], a[rank])]
        rank += 1
        if rank == height:
            break
    return rank


def force_closure(neighbors, initial):
    colored = set(initial)
    forces = []
    while True:
        found = None
        for vertex in sorted(colored):
            white = neighbors[vertex] - colored
            if len(white) == 1:
                found = (vertex, next(iter(white)))
                break
        if found is None:
            break
        colored.add(found[1])
        forces.append(found)
    return colored, forces


def verify(length, power, check_minimal=False):
    assert length >= power + 1 and power >= 1
    neighbors = graph_power(length, power)
    factor = gram_factor(length, power)
    n = 2 * length
    for i in range(n):
        for j in range(i + 1, n):
            dot = sum(row[i] * row[j] for row in factor)
            assert (dot != 0) == (j in neighbors[i]), (length, power, i, j, dot)
    windows = length - power
    pivot_columns = [row * length + column
                     for column in range(windows) for row in range(2)]
    pivot_matrix = [[line[j] for j in pivot_columns] for line in factor]
    assert rank_mod(pivot_matrix) == 2 * windows
    starting = {row * length + column
                for row in range(2) for column in range(power)}
    closure, forces = force_closure(neighbors, starting)
    assert len(starting) == 2 * power
    assert len(closure) == n
    assert len(forces) == 2 * windows
    if check_minimal:
        for cardinality in range(2 * power):
            for subset in combinations(range(n), cardinality):
                assert len(force_closure(neighbors, subset)[0]) != n, (length, power, subset)
    return len(forces)


def main():
    profiles = 0
    for power in range(1, 11):
        for length in range(power + 1, power + 14):
            verify(length, power)
            profiles += 1
    brute = 0
    for power in range(1, 4):
        for length in range(power + 1, 7):
            verify(length, power, check_minimal=True)
            brute += 1
    print('ALL CHECKS PASSED')
    print('gram_support_rank_and_forcing_profiles=', profiles)
    print('independent_brute_force_minimum_profiles=', brute)
    print('factor_rank=', '2*(length-power)')
    print('demonstration_length_8_power_3_forces=', verify(8, 3))


if __name__ == '__main__':
    main()
