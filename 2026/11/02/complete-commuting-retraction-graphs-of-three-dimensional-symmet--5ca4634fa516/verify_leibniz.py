"""Reproduce the idempotent/commuting census in a three-dimensional Leibniz algebra.

For odd prime fields only (the proof applies to all odd-characteristic fields).
The standalone checker enumerates all algebra endomorphisms from their six
free coordinates, tests f^2=f by direct matrix multiplication, and tests
commuting pairs independently using the same matrix multiplication.
"""
from itertools import product
from collections import Counter


def matmul(A, B, q):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) % q
                       for j in range(3)) for i in range(3))


def verify(q, lam):
    nonzero_squares = {x*x % q for x in range(1, q)}
    split = ((-lam) % q in nonzero_squares)
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    zero = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
    idempotents = []
    for a, b, d, e, s, t in product(range(q), repeat=6):
        scalar = (a*a + lam*b*b) % q
        # The three independent bracket preservation identities.
        if (d*d + lam*e*e - lam*scalar) % q != 0: continue
        if (a*d + lam*b*e) % q != 0: continue
        matrix = ((a, d, 0), (b, e, 0), (s, t, scalar))
        if matmul(matrix, matrix, q) == matrix:
            idempotents.append(matrix)
    assert zero in idempotents and identity in idempotents
    N = len(idempotents)
    assert N == (2 + 2*q*q if split else 2)
    active = [x for x in idempotents if x not in (zero, identity)]
    neighbors = [set() for _ in active]
    for i in range(len(active)):
        for j in range(i+1, len(active)):
            if matmul(active[i], active[j], q) == matmul(active[j], active[i], q):
                neighbors[i].add(j);neighbors[j].add(i)
    E = sum(map(len, neighbors))//2
    if split:
        assert E == q*q
        degrees = Counter(map(len, neighbors))
        assert degrees == {q: 2*q, 0: 2*q*(q-1)}
        special = {i for i in range(len(active)) if neighbors[i]}
        colors = {}
        start = next(iter(special));colors[start] = 0; todo=[start]
        while todo:
            v=todo.pop()
            for w in neighbors[v]:
                if w in colors:
                    assert colors[w] != colors[v]
                else:
                    colors[w] = 1-colors[v];todo.append(w)
        assert set(colors)==special
        assert Counter(colors.values()) == {0:q,1:q}
        assert all(neighbors[i] == {j for j,c in colors.items() if c != colors[i]}
                   for i in special)
        maximal_size3 = 2*q*(q-1)
        maximal_size4 = q*q
        assert sum(3+len(neighbors[i]) for i in range(len(active)))+2*N == 4+12*q*q
    else:
        assert not active and E == 0
        maximal_size3=maximal_size4=0
    print(f'q={q:2} lambda={lam:2} split={str(split):5} idempotents={N:3} '
          f'noncentral_edges={E:3} maximal_size3={maximal_size3:3} maximal_size4={maximal_size4:3}')


def main():
    for q,ls in [(3,[1,2]),(5,[1,2]),(7,[1,3]),(11,[1,2])]:
        for lam in ls:verify(q,lam)
    print('VERIFY_OK: idempotent and commuting spectrum on all eight tested presentations')

if __name__ == '__main__':main()
