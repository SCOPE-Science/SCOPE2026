"""Exact finite checks for a three-summand point-concentration theorem.

The infinite-support theorem is proved analytically; these finite tests are
not a substitute for that proof.
"""
from collections import Counter
from itertools import combinations, product


def pmf(weights):
    return {j: w for j, w in enumerate(weights) if w}


def convolve(a, b):
    result = Counter()
    for x, p in a.items():
        for y, q in b.items():
            result[x+y] += p*q
    return result


def all_checks():
    parameters = [(1, 3), (7, 20), (19, 50), (2, 5), (21, 50), (9, 20), (1, 2)]
    checked = 0
    supports = list(combinations(range(8), 3))
    for a, d in parameters:
        b = d - 2*a
        if not 0 <= b <= a:
            raise AssertionError('invalid boundary')
        bound_num = a * (7*a*a - 6*a*d + 2*d*d) if 5*a <= 2*d else 3*a*a*(d-a)
        mu = pmf([b, a, a])
        nu = pmf([a, a, b])
        mixed = convolve(convolve(mu,mu),nu)
        same = convolve(convolve(mu,mu),mu)
        assert mixed[3] == a*(7*a*a-6*a*d+2*d*d)
        assert same[4] == 3*a*a*(d-a)
        assert max(mixed[3], same[4]) == bound_num
        measures = []
        for s in supports:
            for light in range(3):
                measures.append({t:(b if j == light else a) for j,t in enumerate(s) if (b if j == light else a)})
        maximum = -1
        for u in measures:
            for v in measures:
                pair = Counter()
                for x,p in u.items():
                    for y,q in v.items():
                        pair[x+y] += p*q
                largest = sorted(pair.values(), reverse=True)[:3]
                largest += [0] * (3-len(largest))
                # Given pair, any third extremal 3-point law is optimized
                # by assigning the two heavy masses to its two largest atoms.
                third_optimum = a*(largest[0]+largest[1]) + b*largest[2]
                if third_optimum > maximum:
                    maximum = third_optimum
                assert third_optimum <= bound_num, (a,d,u,v,third_optimum,bound_num)
                checked += 1
        assert maximum == bound_num, (a,d,maximum,bound_num)
        print(f'alpha={a}/{d}, exact max={maximum}/{d**3}, bound={bound_num}/{d**3}')
    exceptional = 0
    for gap in (1,2,4):
        s = [0,gap,2*gap]
        for heavy_indices in product(combinations(s,2), repeat=3):
            r = []
            for i,j,k in ((0,1,2),(0,2,1),(1,2,0)):
                count = sum((3*gap - x - y) in s for x in heavy_indices[i] for y in heavy_indices[j])
                r.append(count)
            assert min(r) <= 3, (gap,heavy_indices,r)
            exceptional += 1
    print(f'PASS: {checked} exact bounded-support convolution maxima; all seven sharp.')
    print(f'PASS: {exceptional} independent discrete checks of the simultaneous-heavy-set obstruction.')

if __name__ == '__main__':
    all_checks()
