from itertools import combinations
N = 6
V = range(1 << N)
FULL = (1 << N) - 1

def bit(x, i):
    return (x >> (N - 1 - i)) & 1

def grain_ball(x):
    out = {x}
    for i in range(1, N):
        if bit(x, i) != bit(x, i - 1):
            out.add(x ^ (1 << (N - 1 - i)))
    return frozenset(out)

balls = [grain_ball(x) for x in V]
adj = [set() for _ in V]
for a, b in combinations(V, 2):
    if balls[a].isdisjoint(balls[b]):
        adj[a].add(b)
        adj[b].add(a)

max_size = 0
max_cliques = []

def bron_kerbosch(R, P, X):
    global max_size, max_cliques
    if not P and not X:
        s = len(R)
        if s > max_size:
            max_size = s
            max_cliques = [tuple(sorted(R))]
        elif s == max_size:
            max_cliques.append(tuple(sorted(R)))
        return
    if len(R) + len(P) < max_size:
        return
    U = P | X
    pivot = max(U, key=lambda z: len(P & adj[z])) if U else None
    candidates = sorted(P - (adj[pivot] if pivot is not None else set()))
    for v in candidates:
        bron_kerbosch(R | {v}, P & adj[v], X & adj[v])
        P.remove(v)
        X.add(v)

bron_kerbosch(set(), set(V), set())
max_cliques = sorted(set(max_cliques))

def is_linear(C):
    S = set(C)
    return 0 in S and all((a ^ b) in S for a in S for b in S)

def complement_closed(C):
    S = set(C)
    return all((x ^ FULL) in S for x in S)

expected = [
('000000','000011','001100','001111','010010','010101','011000','011011','100011','100100','101010','101101','110001','110110','111000','111111'),
('000000','000011','001100','001111','010010','010101','011000','011011','100100','100111','101010','101101','110000','110011','111100','111111'),
('000000','000111','001001','001110','010010','010101','011011','011100','100011','100100','101010','101101','110001','110110','111000','111111'),
('000000','000111','001001','001110','010010','010101','011011','011100','100100','100111','101010','101101','110000','110011','111100','111111'),
]
expected_int = sorted(tuple(int(w, 2) for w in C) for C in expected)
assert max_size == 16
assert max_cliques == expected_int
assert len(max_cliques) == 4
assert sum(is_linear(C) for C in max_cliques) == 1
assert sum(complement_closed(C) for C in max_cliques) == 2
index = {C:i for i,C in enumerate(max_cliques)}
comp = []
for C in max_cliques:
    D = tuple(sorted(x ^ FULL for x in C))
    assert D in index
    comp.append(index[D])
assert comp == [3,1,2,0]
for C in max_cliques:
    for a,b in combinations(C,2):
        assert balls[a].isdisjoint(balls[b])
print('VERIFY_OK maximum=16 labeled_maxima=4 linear_maxima=1 complement_closed=2 complement_map=3,1,2,0')
