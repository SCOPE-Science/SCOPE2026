"""Reproduce the complete order-five binary de Bruijn shortest-border census.
All arithmetic and enumerations are exact; Python standard library only.
"""
from collections import Counter

ORDER = 5
N = 1 << ORDER
V = 1 << (ORDER - 1)

def normalize(word):
    """Rotate to the unique circular occurrence of 00000."""
    i = (word + word[:ORDER-1]).find('0' * ORDER)
    assert 0 <= i < N
    return word[i:] + word[:i]

def local_pairing_cycles():
    """Enumerate the 2^16 bijections from incoming to outgoing edges."""
    results = set()
    for bits in range(1 << V):
        successor = [0] * N
        for v in range(V):
            incoming0, incoming1 = v, v + V
            outgoing0, outgoing1 = 2 * v, 2 * v + 1
            if (bits >> v) & 1:
                outgoing0, outgoing1 = outgoing1, outgoing0
            successor[incoming0] = outgoing0
            successor[incoming1] = outgoing1
        e = 0
        visited = set()
        path = []
        while e not in visited:
            visited.add(e)
            path.append(e)
            e = successor[e]
        if e != 0 or len(path) != N:
            continue
        word = ''.join(str(e >> (ORDER - 1)) for e in path)
        assert normalize(word) == word
        results.add(word)
    return results

def eulerian_dfs_cycles():
    """Directly visit every Euler circuit in the 4-bit de Bruijn digraph."""
    ans = set()
    used = [False] * N
    used[0] = True
    path = [0]
    def explore(vertex):
        if len(path) == N:
            if vertex == 0:
                word = ''.join(str(edge >> (ORDER - 1)) for edge in path)
                ans.add(word)
            return
        for bit in (0, 1):
            edge = 2 * vertex + bit
            if not used[edge]:
                used[edge] = True
                path.append(edge)
                explore(edge & (V-1))
                path.pop()
                used[edge] = False
    explore(0)
    return ans

def all_shortest_borders(word):
    """Direct prefix/suffix comparison; 0 denotes unbordered."""
    roots = [word[i:] + word[:i] for i in range(N)]
    return [next((j for j in range(1, N) if rot[:j] == rot[-j:]), 0)
            for rot in roots]

def square_center_minimal_period(word):
    """Independent circular-square check at each join; 0 means no short square."""
    answer = []
    for cut in range(N):
        minimum = 0
        for half in range(1, ORDER):
            if all(word[(cut - half + t) % N] == word[(cut + t) % N]
                   for t in range(half)):
                minimum = half
                break
        answer.append(minimum)
    return answer

def orbit(word):
    opposite = word.translate(str.maketrans('01','10'))
    return {normalize(x) for x in (word, word[::-1], opposite, opposite[::-1])}

def main():
    direct = eulerian_dfs_cycles()
    matched = local_pairing_cycles()
    assert direct == matched and len(direct) == 2048
    hist = Counter()
    orbit_hist = Counter()
    seen = set()
    group = {}
    for word in sorted(direct):
        circular = word + word[:ORDER - 1]
        assert len({circular[i:i + ORDER] for i in range(N)}) == N
        shortest = all_shortest_borders(word)
        centered = square_center_minimal_period(word)
        assert shortest == centered
        count = Counter(shortest)
        assert count[1] == 16 and count[2] == 4
        assert not any(k > 4 for k in count)
        signature = (count[0], count[3], count[4])
        hist[signature] += 1
        group[word] = signature
    for word in sorted(direct):
        if word in seen:
            continue
        eq = orbit(word)
        assert eq <= direct and len(eq) in (2,4)
        assert len({group[w] for w in eq}) == 1
        seen.update(eq)
        orbit_hist[(group[word],len(eq))] += 1
    assert seen == direct
    target = {
        (8,4,0):48, (9,3,0):448,(9,2,1):256, (9,1,2):64,
        (10,2,0):800,(10,1,1):384,(10,0,2):48
    }
    assert hist == target
    assert sum(hist.values()) == 2048
    assert sum(hist[sig]*sig[0] for sig in hist) == 8*48+9*768+10*1232
    assert sum(orbit_hist.values()) == 528
    assert sum(v for (sig,sz),v in orbit_hist.items() if sz == 2) == 32
    assert sum(v for (sig,sz),v in orbit_hist.items() if sz == 4) == 496
    for sig in sorted(hist):
        assert sum(sz*v for (s,sz),v in orbit_hist.items() if s == sig) == hist[sig]
    print('VERIFY_OK', 'local_pairings=65536','direct_eulerian_cycles=2048',
          'distinct_order5_cycles=2048','roots=65536',
          'independent_border_and_square_center_algorithms=2',
          'full_signatures='+repr(sorted(target.items())),
          'symmetry_orbits='+repr(sorted(orbit_hist.items())))

if __name__ == '__main__':
    main()
