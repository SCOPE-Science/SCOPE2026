"""Exact verification of the Mallows four-person stable-roommates probability.

Run with Python 3 standard library: python3 verify.py
Each agent independently draws a four-name Mallows permutation, then deletes self.
"""
from collections import Counter, defaultdict
from itertools import permutations, product

AGENTS = tuple(range(4))
MATCHINGS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))


def inversions(order):
    return sum(order[i] > order[j] for i in range(len(order)) for j in range(i+1, len(order)))


def number_stable(profile):
    ranks = [{j: k for k, j in enumerate(row)} for row in profile]
    total = 0
    for edges in MATCHINGS:
        partner = [0]*4
        for a, b in edges:
            partner[a], partner[b] = b, a
        if all(not(ranks[a][b] < ranks[a][partner[a]] and
                   ranks[b][a] < ranks[b][partner[b]])
               for a in AGENTS for b in range(a+1, 4) if partner[a] != b):
            total += 1
    return total


def orbit(profile):
    result = set()
    for sigma in permutations(AGENTS):
        remapped = [None]*4
        for i, row in enumerate(profile):
            remapped[sigma[i]] = tuple(sigma[j] for j in row)
        result.add(tuple(remapped))
    return result


def mult(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def powpoly(a, n):
    out = [1]
    for _ in range(n):
        out = mult(out, a)
    return out


def deriv(a):
    return [i*a[i] for i in range(1, len(a))]


def sub(a, b):
    return [(a[i] if i<len(a) else 0) - (b[i] if i<len(b) else 0)
            for i in range(max(len(a),len(b)))]


def normal(a):
    while len(a)>1 and a[-1]==0:
        a=a[:-1]
    return a


def check():
    # Exhaustive direct stability test on all 6^4 ordered three-name profiles.
    menus = [list(permutations(j for j in AGENTS if j != i)) for i in AGENTS]
    categories = {k:set() for k in range(4)}
    for profile in product(*menus):
        categories[number_stable(profile)].add(profile)
    assert tuple(len(categories[k]) for k in range(4)) == (48, 1098, 150, 0)

    # Construct the complete unsolvable set again from two relabeling orbits.
    representative_a = ((1,2,3),(2,0,3),(0,1,3),(0,1,2))
    representative_b = ((1,2,3),(2,0,3),(0,1,3),(0,2,1))
    orbit_a, orbit_b = orbit(representative_a), orbit(representative_b)
    assert len(orbit_a)==24 and len(orbit_b)==24
    assert not orbit_a & orbit_b and orbit_a|orbit_b == categories[0]

    # Four-entry Mallows permutations drawn before the agent's own name is deleted.
    # The unnormalized law of each three-name order depends on which name is deleted.
    all_orders = list(permutations(AGENTS))
    collapsed = [defaultdict(Counter) for _ in AGENTS]
    for p in all_orders:
        inv = inversions(p)
        for i in AGENTS:
            reduced = tuple(j for j in p if j != i)
            collapsed[i][reduced][inv] += 1
    Z = normal(mult(powpoly([1,1],2), mult([1,0,1], [1,1,1])))
    for i in AGENTS:
        assert sum(sum(c.values()) for c in collapsed[i].values()) == 24
        assert [sum(c.get(e,0) for c in collapsed[i].values()) for e in range(len(Z))] == Z

    # Enumerate exactly the 48 unsolvable three-name profiles with their
    # four independent collapsed full-ranking weights, a polynomial operation.
    num = [0]*25
    for profile in categories[0]:
        weight = [1]
        for agent, row in enumerate(profile):
            coefficients = collapsed[agent][row]
            weights = [coefficients.get(i,0) for i in range(7)]
            weight = mult(weight, weights)
        for e, c in enumerate(weight):
            num[e] += c
    expected = [0,0,3,22,82,208,404,642,870,1038,1129,1162,1168,
                1162,1129,1038,870,642,404,208,82,22,3,0,0]
    assert num == expected
    assert sum(num)==12288 and sum(powpoly(Z,4))==24**4

    # Simplify the rational law and check its derivative by integer arithmetic.
    A = [3,1,3,-2,6,-2,3,1,3]  # coefficient order: constant first
    B = normal(mult(powpoly([1,1],2), mult(powpoly([1,0,1],2), powpoly([1,1,1],3))))
    N = mult([0,0,1], A)
    assert normal(mult(num,B)) == normal(mult(N,powpoly(Z,4)))

    H = [3,3,-4,-30,-50,-71,-74,-71,-50,-30,-4,3,3]
    left = normal(sub(mult(deriv(N),B),mult(N,deriv(B))))
    right = normal(mult(mult([0,2,-2],H),
                        mult(mult([1,1],[1,0,1]),powpoly([1,1,1],2))))
    assert left == right
    assert H==H[::-1] and sum(H)==-372 and H[0]>0
    assert sum(1 for a,b in zip(H,H[1:]) if a*b<0)==2
    print('VERIFY_OK')
    print('Four-person ordered profiles: 1296; no stable matching: 48 (two disjoint relabeling orbits)')
    print('Full Mallows four-rank numerator coefficients:',num)
    print('Full permutation count:',24**4,'No-solution total at q=1:',sum(num))
    print('Exact rational function and derivative factorizations verified over integers')

if __name__=='__main__':
    check()
