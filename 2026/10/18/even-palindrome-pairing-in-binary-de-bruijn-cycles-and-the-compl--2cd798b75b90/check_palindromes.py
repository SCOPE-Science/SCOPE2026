"""Exact, standalone verification of first-unforced palindrome profiles in binary order-five de Bruijn cycles."""
from collections import Counter

K = 5
EDGE_COUNT = 1 << K
VERTEX_COUNT = 1 << (K - 1)
VERTEX_MASK = VERTEX_COUNT - 1


def length_six_palindromes(word):
    twice = word + word[:5]
    return frozenset(twice[i:i+6] for i in range(32) if twice[i:i+6] == twice[i:i+6][::-1])


def profile(palindromes):
    a = frozenset(('001100', '101101'))
    b = frozenset(('010010', '110011'))
    if palindromes not in (frozenset(), a, b, a | b):
        raise AssertionError(('unexpected palindrome profile', palindromes))
    return ('A' if a <= palindromes else '') + ('B' if b <= palindromes else '') or 'none'


def local_assignment_census():
    hist = Counter()
    total = 0
    for setting in range(1 << VERTEX_COUNT):
        # For each four-bit vertex v, incoming five-bit edge a:v
        # is followed by outgoing five-bit edge v:b, where b=a XOR bit(setting,v).
        succ = [0] * EDGE_COUNT
        for e in range(EDGE_COUNT):
            v = e & VERTEX_MASK
            a = e >> (K - 1)
            b = a ^ ((setting >> v) & 1)
            succ[e] = (v << 1) | b
        assert len(set(succ)) == EDGE_COUNT
        used = set()
        current = 0  # edge 00000 exists in every Euler tour, unique rotation anchor
        for _ in range(EDGE_COUNT):
            if current in used:
                break
            used.add(current)
            current = succ[current]
        if len(used) != EDGE_COUNT or current != 0:
            continue
        total += 1
        # Each edge represents the unique order-five factor at its position.
        orbit = [0]
        for i in range(31):
            orbit.append(succ[orbit[-1]])
        word = ''.join(str(e >> 4) for e in orbit)
        assert len({(word + word[:4])[i:i+5] for i in range(32)}) == 32
        pals = length_six_palindromes(word)
        hist[profile(pals)] += 1
        assert (('A' in profile(pals)) == (((setting >> 6)&1)==0))
        assert (('B' in profile(pals)) == (((setting >> 9)&1)==0))
    assert total == 2048
    assert hist == Counter({'none':768, 'A':512,'B':512,'AB':256}), hist
    return hist


def independent_euler_census():
    hist = Counter()
    total = 0
    def dfs(v, used, sequence):
        nonlocal total
        if len(sequence) == EDGE_COUNT:
            if v != 0:
                return
            # `sequence` records successive edge bits, first edge 00000.
            w = ''.join(map(str,sequence))
            assert len({(w + w[:4])[i:i+5] for i in range(32)}) == 32
            total += 1
            hist[profile(length_six_palindromes(w))] += 1
            return
        for b in (0,1):
            e = (v<<1)|b
            if not (used>>e)&1:
                dfs(e & VERTEX_MASK,used | (1 << e),sequence+[b])
    # Fix edge 00000. Every Euler tour contains it exactly once.
    # The corresponding edge outputs 0; other edges append their final bit.
    dfs(0,1,[0])
    assert total == 2048
    assert hist == Counter({'none':768, 'A':512,'B':512,'AB':256}), hist
    return hist

if __name__ == '__main__':
    a = local_assignment_census()
    b = independent_euler_census()
    assert a == b
    print('ORDER5_PALINDROME_PROFILE_PASS local_assignments=65536 cycles=2048 independent_euler_cycles=2048 profiles=',dict(sorted(a.items())))
