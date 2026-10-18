"""Independent finite checks for optimal zero-forcing reconfiguration after two matching-edge deletions.
Run: python3 verify_two_deleted.py
"""
from collections import Counter, deque
from itertools import combinations


def neighbors(a, b):
    # G = K_(a,b) minus cross-edges a_0 b_0 and a_1 b_1.
    out = []
    for i in range(a):
        out.append(sum(1 << (a+j) for j in range(b) if i != j or i >= 2))
    for j in range(b):
        out.append(sum(1 << i for i in range(a) if i != j or j >= 2))
    return out


def force(black, adj, n):
    full = (1 << n) - 1
    while black != full:
        new = 0
        for i in range(n):
            if black >> i & 1:
                white_neighbors = adj[i] & (full ^ black)
                if white_neighbors and (white_neighbors & (white_neighbors-1)) == 0:
                    new |= white_neighbors
        if new == 0:
            return False
        black |= new
    return True


def profile(a, b, white):
    A = frozenset(i for i in range(a) if white >> i & 1)
    B = frozenset(j for j in range(b) if white >> (a+j) & 1)
    return A, B


def expected_min(a, b, A, B):
    T = frozenset((0, 1))
    return len(A) == len(B) == 2 and A & T and B & T and (A & T) != (B & T)


def graph(V, n):
    adj = [set() for _ in V]
    for i, x in enumerate(V):
        for j in range(i+1, len(V)):
            d = (x ^ V[j]).bit_count()
            if d == 2:
                adj[i].add(j)
                adj[j].add(i)
    return adj


def diameter(adj):
    answer = 0
    for i in range(len(adj)):
        distances = [-1] * len(adj)
        distances[i] = 0
        work = deque([i])
        while work:
            u = work.popleft()
            for v in adj[u]:
                if distances[v] == -1:
                    distances[v] = distances[u] + 1
                    work.append(v)
        assert min(distances) >= 0, 'disconnected'
        answer = max(answer, max(distances))
    return answer


def run():
    checked = 0
    cases = 0
    min_total = 0
    for a in range(3, 9):
        for b in range(3, 9):
            n = a+b
            adj = neighbors(a, b)
            found = []
            for white in range(1 << n):
                black = ((1 << n)-1) ^ white
                ok = force(black, adj, n)
                A, B = profile(a, b, white)
                if len(A)+len(B) == 4:
                    assert ok == bool(expected_min(a, b, A, B)), (a,b,white)
                    if ok:
                        found.append(white)
                if len(A)+len(B) >= 5:
                    assert not ok, (a,b,white,'oversized white')
                checked += 1
            found.sort()
            expected_count = 2*(a*b-a-b)
            assert len(found) == expected_count, (a,b,len(found),expected_count)
            rg = graph(found, n)
            assert all(len(v) == a+b-4 for v in rg), (a,b,Counter(map(len,rg)))
            assert sum(map(len,rg))//2 == (a*b-a-b)*(a+b-4)
            diam = diameter(rg)
            assert diam == (3 if min(a,b) == 3 else 4), (a,b,diam)
            cases += 1
            min_total += len(found)
    print(f'VERIFICATION_OK graph_cases={cases} zero_forcing_initial_sets={checked} minimum_supports={min_total} a,b=3..8')


if __name__ == '__main__':
    run()
