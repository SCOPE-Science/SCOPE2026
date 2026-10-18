#!/usr/bin/env python3
"""Exact census of longest circular palindromic factors in binary order-five de Bruijn cycles.
Only Python's standard library is required. All indexes and loops are finite.
"""
from collections import Counter

ORDER = 5
N = 1 << ORDER
VERTICES = 1 << (ORDER - 1)
EXPECTED = {7: 200, 8: 192, 9: 856, 10: 128, 11: 392, 12: 32, 13: 200, 15: 48}
EXPECTED_ORBITS = {7: {2: 14, 4: 43}, 8: {2: 4, 4: 46},
                   9: {2: 6, 4: 211}, 10: {4: 32},
                   11: {2: 6, 4: 95}, 12: {4: 8},
                   13: {2: 2, 4: 49}, 15: {4: 12}}


def switch_cycles():
    """Enumerate all local binary predecessor/successor matchings on (n-1)-factors."""
    for mask in range(1 << VERTICES):
        nxt = [0] * N
        for u in range(N):
            v = u & (VERTICES - 1)
            initial = u >> (ORDER - 1)
            last = initial ^ ((mask >> v) & 1)
            nxt[u] = ((v << 1) | last) & (N - 1)
        seen = 0
        orbit = []
        u = 0
        while not ((seen >> u) & 1):
            seen |= (1 << u)
            orbit.append(u)
            u = nxt[u]
        if u == 0 and len(orbit) == N:
            word = ''.join(str(x >> (ORDER - 1)) for x in orbit)
            assert word.startswith('0' * ORDER)
            yield word


def euler_cycles():
    """Independently enumerate Eulerian circuits of the order-four overlap graph."""
    initial = '0' * ORDER
    start_vertex = 0
    used = {0}
    appended = []
    mask = VERTICES - 1
    def dfs(vertex):
        if len(used) == N:
            if vertex == start_vertex:
                word = initial + ''.join(appended)
                assert len(word) == N + ORDER - 1
                yield word[:N]
            return
        for bit in (0, 1):
            edge = (vertex << 1) | bit
            if edge not in used:
                used.add(edge)
                appended.append(str(bit))
                yield from dfs(edge & mask)
                appended.pop()
                used.remove(edge)
    yield from dfs(start_vertex)


def circular_palindrome_center(s):
    """Expand about each of the 2*N centers on the infinite periodic extension."""
    n = len(s)
    best = 0
    for center in range(n):
        odd = 1
        while odd + 2 <= n and s[(center-(odd+1)//2) % n] == s[(center+(odd+1)//2) % n]:
            odd += 2
        best = max(best, odd)
        even = 0
        while even + 2 <= n and s[(center-even//2) % n] == s[(center+1+even//2) % n]:
            even += 2
        best = max(best, even)
    return best


def circular_palindrome_windows(s):
    """Enumerate circular windows in a different representation and direction."""
    n=len(s)
    ss=s+s
    for k in range(n,0,-1):
        for i in range(n):
            p=ss[i:i+k]
            if p==p[::-1]:
                return k
    assert False


def check_debruijn(s):
    assert len(s) == N
    ss=s+s
    vals={ss[i:i+ORDER] for i in range(N)}
    assert len(vals)==N
    assert s.startswith('0'*ORDER)


def canonical(s):
    """The unique rotation beginning with the all-zero order-five factor."""
    i = (s + s).index('0' * ORDER)
    return s[i:] + s[:i]


def dihedral_binary_orbit(s):
    """Rotation is already factored out; apply reversal and bit complement."""
    comp = ''.join('1' if c == '0' else '0' for c in s)
    return {canonical(z) for z in (s, s[::-1], comp, comp[::-1])}


def main():
    a={}
    b={}
    for s in switch_cycles():
        check_debruijn(s)
        a[s]=circular_palindrome_center(s)
    for s in euler_cycles():
        check_debruijn(s)
        assert s not in b
        b[s]=circular_palindrome_windows(s)
    assert len(a)==len(b)==2048, (len(a),len(b))
    assert a == b
    hist=dict(sorted(Counter(a.values()).items()))
    assert hist == EXPECTED,(hist,EXPECTED)
    assert sum(hist.values()) == 2048
    assert min(hist)==7 and max(hist)==15
    assert hist.get(14,0)==0
    remaining = set(a)
    orbit_hist = {length: Counter() for length in EXPECTED}
    while remaining:
        w = min(remaining)
        orbit = dihedral_binary_orbit(w)
        assert orbit.issubset(remaining)
        assert 1 <= len(orbit) <= 4
        assert len({a[z] for z in orbit}) == 1
        orbit_hist[a[w]][len(orbit)] += 1
        remaining.difference_update(orbit)
    got_orbits = {length: dict(counts) for length, counts in orbit_hist.items()}
    assert got_orbits == EXPECTED_ORBITS, (got_orbits, EXPECTED_ORBITS)
    assert sum(sum(counts.values()) for counts in orbit_hist.values()) == 528
    print('VERIFY_OK binary_order5_cycles=2048 local_switch_assignments=65536 independent_euler_and_switch_sets_identical=2048 circular_max_palindrome_distribution='+','.join(f'{k}:{v}' for k,v in hist.items())+' symmetry_orbits=528 size2=32 size4=496')

if __name__=='__main__':main()
