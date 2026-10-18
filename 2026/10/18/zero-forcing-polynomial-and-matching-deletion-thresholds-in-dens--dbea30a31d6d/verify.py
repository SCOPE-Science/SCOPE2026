"""Independent finite checks for the zero-forcing-set classification.

Run: python3 verify.py. No external dependencies. Enumeration does not
replace the proof for arbitrary side sizes.
"""
from itertools import combinations
from math import comb


def expected(a, b, t):
    x = comb(a, 2) - comb(a-t, 2)
    y = comb(b, 2) - comb(b-t, 2)
    return (1, a+b, a*b+x+y, b*x+a*y,
            x*y-t*(a-t)*(b-t)-comb(t, 2))


def prediction(a, b, t, U, V):
    u, v = len(U), len(V)
    if u > 2 or v > 2:
        return False
    A = set(U).intersection(range(t))
    B = set(V).intersection(range(t))
    if (u == 2 and not A) or (v == 2 and not B):
        return False
    return not (u == 2 and v == 2 and A == B)


def graph_adjacency(a, b, t):
    nbr = [0] * (a+b)
    for i in range(a):
        for j in range(b):
            if i == j and i < t:
                continue
            nbr[i] |= 1 << (a+j)
            nbr[a+j] |= 1 << i
    return nbr


def actually_zero_forcing(nbr, white):
    """Iteratively apply *all* currently legal forces in a graph."""
    count = len(nbr)
    full = (1 << count)-1
    while white:
        blue = full ^ white
        newly_blue = 0
        for i in range(count):
            if not (blue & (1 << i)):
                continue
            white_nbr = nbr[i] & white
            if white_nbr and white_nbr & (white_nbr-1) == 0:
                newly_blue |= white_nbr
        if not newly_blue:
            return False
        white &= ~newly_blue
    return True


def run():
    profiles = 0
    full_sets = 0
    for a in range(3, 8):
        for b in range(3, 8):
            for t in range(min(a, b) + 1):
                nbr = graph_adjacency(a, b, t)
                coeff = [0] * 5
                for white in range(1 << (a+b)):
                    full_sets += 1
                    U = tuple(i for i in range(a) if white >> i & 1)
                    V = tuple(j for j in range(b) if white >> (a+j) & 1)
                    actual = actually_zero_forcing(nbr, white)
                    model = prediction(a, b, t, U, V)
                    assert actual == model, (a, b, t, white, actual, model)
                    if actual:
                        assert len(U)+len(V) <= 4
                        coeff[len(U)+len(V)] += 1
                assert tuple(coeff) == expected(a, b, t), (a,b,t,coeff,expected(a,b,t))
                profiles += 1
    restricted_sets = 0
    for a, b in ((8, 9), (10, 11), (13, 14)):
        for t in sorted(set((0, 1, 2, min(a,b)))):
            nbr = graph_adjacency(a, b, t)
            cnt = [0] * 5
            for i in range(3):
                for j in range(3):
                    for U in combinations(range(a), i):
                        for V in combinations(range(b), j):
                            restricted_sets += 1
                            white = sum(1 << u for u in U) | sum(1 << (a+v) for v in V)
                            actual = actually_zero_forcing(nbr, white)
                            model = prediction(a, b, t, U, V)
                            assert actual == model, (a,b,t,U,V)
                            if actual: cnt[i+j] += 1
            assert tuple(cnt) == expected(a,b,t), (a,b,t,cnt)
    print('VERIFICATION_OK')
    print('exhaustive_profiles',profiles)
    print('all_subsets_checked',full_sets)
    print('large_board_restricted_subsets_checked',restricted_sets)
    for a,b,t in ((4,4,0),(4,4,1),(4,4,2),(4,4,4),(5,6,2),(7,7,7)):
        print('coeff',a,b,t,expected(a,b,t))

if __name__ == '__main__':
    run()
