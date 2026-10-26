"""Exact finite-state proof certificate for two forest-pattern expectation counts.

For a binary code L w R of a tree permutation, with w arbitrary, the
inversion adjacency between positions i<j occurs exactly when letter_i=L,
letter_j=R, and the intervening letters form L* or R* or R+L+.
Track four marked positions and their induced inversion pattern.
"""
from collections import defaultdict, deque
from itertools import permutations

PATTERNS = ((1, 2, 4, 3), (1, 3, 2, 4))
Q = (1, -8, 25, -38, 28, -8)

def advance_gap(s, c):
    if s == 0 or s == 5:
        return s
    if s == 1:
        return 2 if c == 'L' else 3
    if s == 2:
        return 2 if c == 'L' else 5
    if s == 3:
        return 4 if c == 'L' else 3
    if s == 4:
        return 4 if c == 'L' else 5
    raise AssertionError(s)

def transition(state, c, marked, pattern):
    k = len(state)
    if marked:
        if k == 4:
            return None
        for i, s in enumerate(state):
            actual = c == 'R' and s not in (0, 5)
            expected = pattern[i] > pattern[k]
            if actual != expected:
                return None
    result = tuple(advance_gap(s, c) for s in state)
    if marked:
        result += (1 if c == 'L' else 0,)
    return result

def automaton(pattern):
    starts = ((), (1,))  # first letter is obligatorily L, marked or unmarked
    visited = set(starts)
    todo = deque(starts)
    edges = {}
    finish = {}
    while todo:
        state = todo.popleft()
        edges[state] = []
        for c in 'LR':
            for marked in (False, True):
                other = transition(state, c, marked, pattern)
                if other is not None:
                    edges[state].append(other)
                    if other not in visited:
                        visited.add(other)
                        todo.append(other)
        finish[state] = sum(
            len(other) == 4 for marked in (False, True)
            if (other := transition(state, 'R', marked, pattern)) is not None
        )
    return starts, edges, finish

def totals(pattern, upper):
    starts, edges, finish = automaton(pattern)
    distribution = defaultdict(int)
    for s in starts:
        distribution[s] += 1
    answer = [0] * (upper + 1)
    for n in range(2, upper + 1):
        if n > 2:
            nd = defaultdict(int)
            for s, weight in distribution.items():
                for t in edges[s]:
                    nd[t] += weight
            distribution = nd
        answer[n] = sum(weight * finish[s] for s, weight in distribution.items())
    return answer, len(edges)

def inversion_graph_from_binary(code):
    n = len(code)
    matrix = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            middle = ''.join(code[i+1:j])
            admissible = (set(middle) <= {'L'} or set(middle) <= {'R'}
                          or (middle.count('R') > 0 and middle.count('L') > 0
                              and middle == 'R' * middle.count('R') + 'L' * middle.count('L')))
            if code[i] == 'L' and code[j] == 'R' and admissible:
                matrix[i][j] = matrix[j][i] = True
    return matrix

def pattern_count(matrix, pattern):
    from itertools import combinations
    return sum(all(matrix[sites[i]][sites[j]] == (pattern[i] > pattern[j])
                   for i in range(4) for j in range(i + 1, 4))
               for sites in combinations(range(len(matrix)), 4))

def check():
    upper = 122
    a, size_a = totals(PATTERNS[0], upper)
    b, size_b = totals(PATTERNS[1], upper)
    assert (size_a, size_b) == (71, 45), (size_a, size_b)
    difference = [x - y for x, y in zip(a, b)]
    assert difference[5:10] == [2, 16, 78, 300, 1002], difference[5:10]
    # The numerator of Q*(G_1243-G_1324)-2z^5 has degree <=122.
    # Both generating functions are rational using automata of respective
    # dimensions 71 and 45, and both start with an obligatory initial and
    # final letter. Therefore exact vanishing of coefficients 0..122 proves
    # the entire formal rational identity (no extrapolation).
    for n in range(upper + 1):
        lhs = sum(Q[j] * difference[n-j] for j in range(min(n, 5)+1))
        assert lhs == (2 if n == 5 else 0), (n, lhs)
    # Distinct check using direct binary words, and no reuse of DP counts.
    from itertools import product
    for n in range(2, 10):
        checks = [0, 0]
        for middle in product('LR', repeat=n-2):
            graph = inversion_graph_from_binary('L' + ''.join(middle) + 'R')
            for i, pattern in enumerate(PATTERNS):
                checks[i] += pattern_count(graph, pattern)
        assert checks == [a[n], b[n]], (n, checks, a[n], b[n])
    # Independently reconstruct tree permutations from all n! permutations,
    # rather than relying on the binary-word inversion graph rule.
    from itertools import combinations
    for n in range(2, 8):
        brute = [0, 0]
        trees = 0
        for permutation in permutations(range(1, n+1)):
            edges = [(i,j) for i in range(n) for j in range(i+1,n)
                     if permutation[i] > permutation[j]]
            if len(edges) != n-1:
                continue
            parent = list(range(n))
            def root(i):
                while parent[i] != i:
                    i = parent[i]
                return i
            for i,j in edges:
                parent[root(i)] = root(j)
            if len({root(i) for i in range(n)}) != 1:
                continue
            trees += 1
            for sites in combinations(range(n),4):
                v = [permutation[i] for i in sites]
                order = tuple(1+sum(w < x for w in v) for x in v)
                for k, pattern in enumerate(PATTERNS):
                    if order == pattern:
                        brute[k] += 1
        assert trees == 2**(n-2), (n,trees)
        assert brute == [a[n],b[n]], (n,brute,a[n],b[n])
    print('PASS: exhaustive unrelated permutation-graph enumeration n=2..7')
    print('PASS: 71-state and 45-state exact automata; 123 polynomial coefficient identities;')
    print('PASS: direct binary-word reconstruction and occurrence enumeration, n=2..9;')
    print('PASS: G_1243(z)-G_1324(z) = 2*z^5/((1-z)^2*(1-2*z)^3).')
    print('n=5..9 difference counts:', difference[5:10])

if __name__ == '__main__':
    check()
