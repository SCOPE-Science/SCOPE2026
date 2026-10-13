"""Exact finite certificate for paired one-probe trace-estimator coupling."""
from itertools import permutations, product
from fractions import Fraction


def reps(n):
    return [(1,) + t for t in product((-1, 1), repeat=n-1)]


def action_maps(n):
    states = reps(n)
    by_state = {r: i for i, r in enumerate(states)}
    maps = set()
    for perm in permutations(range(n)):
        for signs in product((-1, 1), repeat=n-1):
            signed = (1,) + signs
            image = []
            for r in states:
                s = tuple(signed[i]*r[perm[i]] for i in range(n))
                if s[0] == -1:
                    s = tuple(-a for a in s)
                image.append(by_state[s])
            maps.add(tuple(image))
    return sorted(maps)


def error_values(n, coeff):
    edges = list(__import__('itertools').combinations(range(n), 2))
    assert len(coeff) == len(edges)
    return [sum(w*r[i]*r[j] for (i, j), w in zip(edges, coeff)) for r in reps(n)]


def squared_matching_cost(qa, qb, mp):
    return sum((qa[i] - qb[mp[i]])**2 for i in range(len(qa)))


def certificate():
    import math
    for n in (1, 2, 3, 4):
        G = action_maps(n)
        expected = {1:1, 2:2, 3:24, 4:192}[n]
        assert len(G) == expected, (n, len(G), expected)
        assert len(G) == math.factorial(2**(n-1)) if n <= 3 else len(G) < math.factorial(8)
        print('dim', n, 'signed permutation actions', len(G), 'classes', 2**(n-1))
    a = (-2, 2, -3, 2, 2, 2)
    b = (-1, 2, 2, 3, -3, 3)
    qa, qb = error_values(4, a), error_values(4, b)
    assert qa == [9, -5, 5, -1, -3, -9, 1, 3]
    assert qb == [0, 4, -8, 8, -2, -10, 2, 6]
    assert len(set(qa)) == len(set(qb)) == 8
    all_couplings_cost = sum((x-y)**2 for x,y in zip(sorted(qa), sorted(qb)))
    signed_permutation_cost = min(squared_matching_cost(qa,qb,m) for m in action_maps(4))
    assert (all_couplings_cost, signed_permutation_cost) == (16, 24)
    delta = Fraction(1,16)
    assert delta**2 * all_couplings_cost / 2 == Fraction(1,32)
    assert delta**2 * signed_permutation_cost / 2 == Fraction(3,64)
    # Row absolute sums: 7 and 8, giving strict diagonal dominance when delta < 1/8.
    from itertools import combinations
    for coeff in (a,b):
        sums=[0]*4
        for (i,j),v in zip(combinations(range(4),2),coeff):
            sums[i]+=abs(v)
            sums[j]+=abs(v)
        assert max(sums)<=8
    # A simple n=3 zero-cost relabeling example, while same-probe cost is nonzero.
    p = error_values(3,(1,0,0))
    q = error_values(3,(0,1,0))
    assert sorted(p) == sorted(q)
    assert min(squared_matching_cost(p,q,m) for m in action_maps(3)) == 0
    print('n4 sorted squared cost', all_couplings_cost, 'best signed squared cost', signed_permutation_cost)
    print('n4 optimal MSE', Fraction(1,32), 'signed-permutation minimum', Fraction(3,64))
    print('verification complete')


if __name__ == '__main__':
    certificate()
