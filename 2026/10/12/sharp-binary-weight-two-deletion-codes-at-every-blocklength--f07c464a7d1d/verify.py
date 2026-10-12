"""Direct finite cross-checks for a binary weight-two single-deletion theorem.
The all-length upper bound is mathematical; no finite computation substitutes for it.
Run: python3 verify.py
"""
from itertools import combinations


def deletion_shadow(n, pair):
    bits = [int(i in pair) for i in range(n)]
    return {tuple(bits[:d] + bits[d+1:]) for d in range(n)}


def construction(n):
    return ([(i, i+1) for i in range(0, n-1, 2)] +
            [(i, i+3) for i in range(1, n-3, 4)])


def max_clique(n):
    """Pure-Python exact Bron-Kerbosch-style maximum clique in compatibility graph.
    Tests n<=9 only; no extrapolation from search.
    """
    vertices = list(combinations(range(n), 2))
    shadows = [deletion_shadow(n, v) for v in vertices]
    N = len(vertices)
    neigh = [0]*N
    for i in range(N):
        for j in range(i+1, N):
            if shadows[i].isdisjoint(shadows[j]):
                neigh[i] |= 1 << j
                neigh[j] |= 1 << i

    best = 0
    def expand(P, depth):
        nonlocal best
        if depth + P.bit_count() <= best:
            return
        if P == 0:
            best = max(best, depth)
            return
        # Include-exclude with a high-degree pivot, for independent exactness.
        while P:
            if depth + P.bit_count() <= best:
                return
            pivot = max((i for i in range(N) if P >> i & 1),
                        key=lambda i: (P & neigh[i]).bit_count())
            expand(P & neigh[pivot], depth+1)
            P &= ~(1 << pivot)
    expand((1<<N)-1, 0)
    return best


def main():
    for n in range(2, 65):
        C = construction(n)
        predicted = (3*n-2)//4
        assert len(C) == len(set(C)) == predicted
        assert all(0 <= a < b < n and b-a in (1,3) for a,b in C)
        shadows = [deletion_shadow(n, pair) for pair in C]
        for i in range(len(C)):
            for j in range(i+1,len(C)):
                assert shadows[i].isdisjoint(shadows[j]), (n, C[i], C[j])
        t = len([1 for a,b in C if b == a+1])
        s = len(C)-t
        assert t + 2*s <= n-1
        assert t <= (n//2)
        assert ((n-1 + (n//2))//2) == predicted
        if n <= 9:
            assert max_clique(n) == predicted, (n, predicted)
    for n in range(4, 65):
        color_counts = {}
        for a,b in combinations(range(n),2):
            r = (a+b+2) % (n-1)
            color_counts[r] = color_counts.get(r,0)+1
        assert max(color_counts.values()) == (n+1)//2
    print('VERIFY_OK construction n=2..64; exhaustive maxima n=2..9; modified VT classes n=4..64')


if __name__ == '__main__':
    main()
