"""Independent exhaustive tests of zero forcing and forts on two matched cliques.

Run with Python 3.8 or later. This file uses only the standard library.
"""
from collections import Counter
from itertools import combinations
from math import comb


def neighbor_masks(n):
    """Vertex identifiers are 0,...,n-1 in A and n,...,2n-1 in B."""
    out = []
    for layer in (0, 1):
        for i in range(n):
            out.append(sum(1 << (layer * n + j) for j in range(n) if j != i)
                       | (1 << ((1 - layer) * n + i)))
    return out


def graph_forces_everything(blue, adjacency):
    full = (1 << len(adjacency)) - 1
    while blue != full:
        selected = 0
        for i, neighbors in enumerate(adjacency):
            if (blue >> i) & 1:
                white_neighbors = neighbors & ~blue
                if white_neighbors and not white_neighbors & (white_neighbors - 1):
                    selected |= white_neighbors
        if not selected:
            return False
        blue |= selected
    return True


def is_fort(mask, adjacency):
    if not mask:
        return False
    for i, neighbors in enumerate(adjacency):
        if not (mask >> i) & 1:
            overlap = neighbors & mask
            if overlap and not overlap & (overlap - 1):
                return False
    return True


def described_zero_forcing(n, white):
    left = {i for i in range(n) if white & (1 << i)}
    right = {i for i in range(n) if white & (1 << (n+i))}
    if not left or not right:
        return True
    return (len(left) == 1 and
            any(i not in left and i not in right for i in range(n))) or (
            len(right) == 1 and
            any(i not in right and i not in left for i in range(n)))


def described_minimal_forts(n):
    result = set()
    if n == 2:
        for i in range(2):
            j = 1-i
            result.add((1 << i) | (1 << (n+j)))
        return result
    if n == 3:
        for j in range(n):
            other = [i for i in range(n) if i != j]
            result.add((1 << j) | sum(1 << (n+i) for i in other))
            result.add((1 << (n+j)) | sum(1 << i for i in other))
            result.add(sum((1 << i) | (1 << (n+i)) for i in other))
        return result
    for L in combinations(range(n), 2):
        for R in combinations(range(n), 2):
            result.add(sum(1 << i for i in L) | sum(1 << (n+i) for i in R))
    for j in range(n):
        result.add((1 << j) | sum(1 << (n+i) for i in range(n) if i != j))
        result.add((1 << (n+j)) | sum(1 << i for i in range(n) if i != j))
    return result


def proposed_polynomial(n):
    """Coefficient dictionary in number of initially white vertices."""
    c = Counter()
    for b in range(n+1):
        c[b] += 2*comb(n,b)
    c[0] -= 1
    if n == 2:
        c[2] += 2
    else:
        c[2] += n*n
        for b in range(2,n-1):
            c[b+1] += 2*n*comb(n,b)
        c[n] += 2*n*(n-1)
    return +c


def test_one(n, check_minimal=True):
    adjacency = neighbor_masks(n)
    full = (1 << (2*n))-1
    white_polynomial = Counter()
    fort_flags = bytearray(1 << (2*n))
    for white in range(1 << (2*n)):
        blue = full ^ white
        actual = graph_forces_everything(blue,adjacency)
        assert actual == described_zero_forcing(n,white), ('zero forcing',n,white)
        if actual:
            white_polynomial[white.bit_count()] += 1
        if check_minimal:
            fort_flags[white] = is_fort(white, adjacency)
    assert white_polynomial == proposed_polynomial(n), ('polynomial',n,white_polynomial,proposed_polynomial(n))
    if n >= 3:
        assert sum(white_polynomial.values()) == (n+1)*2**(n+1)-n*n-6*n-1
        assert white_polynomial[n] == 2*n*(n-1)+2
    if check_minimal:
        observed = set()
        for fort in range(1,len(fort_flags)):
            if not fort_flags[fort]:
                continue
            proper = (fort - 1) & fort
            minimal = True
            while proper:
                if fort_flags[proper]:
                    minimal = False
                    break
                proper = (proper-1)&fort
            if minimal:
                observed.add(fort)
        assert observed == described_minimal_forts(n), ('minimal forts',n,observed ^ described_minimal_forts(n))
        assert all(fort_flags[s] for s in observed)
    return len(fort_flags), sum(white_polynomial.values()), len(described_minimal_forts(n))


if __name__ == '__main__':
    count = 0
    for n in range(2,8):
        size, successful, forts = test_one(n, True)
        count += size
        print('n=%d subsets=%d success=%d minimal_forts=%d' %
              (n,size,successful,forts))
    size, successful, forts = test_one(8,False)
    count += size
    print('n=8 subsets=%d success=%d minimal_forts=unexamined' % (size,successful))
    print('VERIFY_OK direct_subsets=%d complete_polynomial_orders=7 exact_minimal_fort_orders=6' % count)
