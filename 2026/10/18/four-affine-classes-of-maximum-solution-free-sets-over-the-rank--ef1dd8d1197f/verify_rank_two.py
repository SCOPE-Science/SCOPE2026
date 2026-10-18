"""Exact finite enumeration for x+5y=3z+3u on (Z/8Z)^2.

Uses only Python's integer arithmetic, bitsets and set operations.
"""
from itertools import permutations, product

MOD = 8
V = tuple((a, b) for a in range(MOD) for b in range(MOD))
N = len(V)
assert N == 64

def idx(a, b):
    return ((a % MOD) * MOD) + (b % MOD)

# The coefficient 3 is its own inverse modulo 8.
# The equation is equivalent to u = 3*x + 7*y - z.
forbidden = set()
for x in range(N):
    a, b = V[x]
    for y in range(N):
        c, d = V[y]
        for z in range(N):
            e, f = V[z]
            u = idx(3*a + 7*c - e, 3*b + 7*d - f)
            edge = tuple(sorted({x, y, z, u}))
            if len(edge) > 1:
                forbidden.add(edge)

F2 = [0] * N
F3 = [[0] * N for _ in range(N)]
F4 = [[[0] * N for _ in range(N)] for _ in range(N)]
for edge in forbidden:
    if len(edge) == 2:
        a,b = edge
        F2[a] |= 1 << b
        F2[b] |= 1 << a
    elif len(edge) == 3:
        for a,b in permutations(edge, 2):
            c = next(v for v in edge if v != a and v != b)
            F3[a][b] |= 1 << c
    elif len(edge) == 4:
        for a,b,c in permutations(edge, 3):
            d = next(v for v in edge if v not in (a,b,c))
            F4[a][b][c] |= 1 << d

# Any nonempty admissible set may be translated to contain the origin.
# Increasing-label depth-first search enumerates each rooted set once.
def census(target, collect=False):
    nodes = 0
    solutions = set() if collect else 0
    def explore(chosen, allowed):
        nonlocal nodes, solutions
        nodes += 1
        if len(chosen) == target:
            if collect:
                solutions.add(chosen)
            else:
                solutions += 1
            return
        if len(chosen) + allowed.bit_count() < target:
            return
        while allowed:
            if len(chosen) + allowed.bit_count() < target:
                return
            bit = allowed & -allowed
            v = bit.bit_length() - 1
            allowed ^= bit
            nxt = allowed & ~F2[v]
            for u in chosen:
                nxt &= ~F3[v][u]
            for i,u in enumerate(chosen):
                for w in chosen[i+1:]:
                    nxt &= ~F4[v][u][w]
            if len(chosen)+1+nxt.bit_count() >= target:
                explore(chosen+(v,), nxt)
    explore((0,), ((1 << N)-1) & ~1 & ~F2[0])
    return solutions, nodes

rooted, nodes8 = census(8, True)
nonexist9, nodes9 = census(9)
assert len(rooted) == 12288 and nonexist9 == 0
assert (0,1,8,9,20,21,28,29) in rooted
assert nodes8 == 57143 and nodes9 == 16096, (nodes8,nodes9)

matrices = [(a,b,c,d) for a,b,c,d in product(range(8),repeat=4)
            if (a*d-b*c)%2]
assert len(matrices) == 1536

def rooted_affine_orbit(seed):
    out = set()
    for a,b,c,d in matrices:
        transformed = [idx(a*V[t][0]+b*V[t][1],
                           c*V[t][0]+d*V[t][1]) for t in seed]
        for anchor in transformed:
            A,B = V[anchor]
            out.add(tuple(sorted(idx(V[t][0]-A,V[t][1]-B)
                                 for t in transformed)))
    return out

remaining = set(rooted)
orbit_data = []
while remaining:
    representative = min(remaining)
    orbit = rooted_affine_orbit(representative)
    assert orbit <= remaining
    orbit_data.append((representative,len(orbit)))
    remaining -= orbit
assert len(orbit_data) == 4
assert all(length == 3072 for _,length in orbit_data)
assert [rep for rep,_ in orbit_data] == [
    (0,1,8,9,20,21,28,29),
    (0,1,8,9,20,21,28,61),
    (0,1,8,9,20,28,29,53),
    (0,1,8,9,20,29,53,60),
]
# Double counting incidences between extremal sets and their elements.
all_extremizers = (N*len(rooted))//8
assert all_extremizers == 98304
print('VERIFY_OK forbidden_edges=%d rooted_eight=%d size_nine=%d nodes8=%d nodes9=%d affine_orbits=%s total_extremizers=%d' % (
    len(forbidden),len(rooted),nonexist9,nodes8,nodes9,
    [n for _,n in orbit_data],all_extremizers))
