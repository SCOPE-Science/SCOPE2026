"""Independent finite checks for the fixed-up-degree polynomial theorem.
Run: python3 verify.py (Python 3, standard library only).
"""
from itertools import permutations
from collections import Counter, defaultdict
from math import comb


def box_degree(p):
    n = len(p)
    answer = 0
    for i in range(n):
        ceiling = n + 1
        for j in range(i + 1, n):
            if p[i] < p[j] < ceiling:
                answer += 1
                ceiling = p[j]
    return answer


def direct_degree(p):
    return sum(p[i] < p[j] and not any(p[i] < p[t] < p[j]
               for t in range(i + 1, j))
               for i in range(len(p)) for j in range(i + 1, len(p)))


def is_skew_indecomp(p):
    return all(min(p[:k]) < max(p[k:]) for k in range(1, len(p)))


def connected_cover_graph(p):
    n = len(p)
    parent = list(range(n))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] < p[j] and not any(p[i] < p[t] < p[j] for t in range(i+1, j)):
                parent[root(i)] = root(j)
    return len({root(i) for i in range(n)}) == 1


def coefficient_from_blocks(C, r, n):
    # Formal series R^k, retaining only q-degrees <= r.
    pieces = [(s, b, count) for s, counter in C.items() if s > 1
              for b, count in counter.items() if b <= r]
    result = 0
    powers = {(0, 0): 1}
    for k in range(1, r + 1):
        new = defaultdict(int)
        for (degree, length), count in powers.items():
            for s, b, multiplicity in pieces:
                if degree + b <= r:
                    new[(degree+b, length+s)] += count*multiplicity
        powers = new
        for (degree, length), count in powers.items():
            if degree == r and n >= length:
                result += count * comb(n-length+k, k)
    return result


def main():
    D = {0: Counter({0: 1})}
    C = {}
    explicit_count = 0
    for n in range(1, 10):
        d = Counter()
        if n <= 6:
            c = Counter()
        for p in permutations(range(1, n + 1)):
            b = box_degree(p)
            d[b] += 1
            explicit_count += 1
            if n <= 7:
                assert b == direct_degree(p), (n, p)
            if n <= 7:
                assert is_skew_indecomp(p) == connected_cover_graph(p), (n, p)
            if n <= 6 and is_skew_indecomp(p):
                c[b] += 1
        D[n] = d
        assert sum(d.values()) == __import__('math').factorial(n)
        if n <= 6:
            C[n] = c
            assert not c or min(c) >= n-1, (n,c)
    assert C[2] == {1: 1}
    assert C[3] == {2: 3}
    assert C[4][3] == 11
    for n in range(1, 10):
        for r in range(1, min(5, n*n//4) + 1):
            calculated = coefficient_from_blocks(C, r, n)
            assert calculated == D[n][r], (n, r, calculated, D[n][r])
        if n >= 3:
            assert D[n][2] == (n-2)*(n+3)//2
        if n >= 4:
            assert D[n][3] == (n**3+6*n*n-13*n-42)//6
    print('EXPLICIT_PERMUTATIONS_OK', explicit_count)
    print('DIRECT_TRIPLE_AND_CONNECTIVITY_OK lengths_1_to_7')
    print('ALL_Q_SLICES_OK r_1_to_5 lengths_1_to_9')
    print('EXACT_Q2_Q3_POLYNOMIALS_OK')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
