#!/usr/bin/env python3
"""Standalone checks for a sharp two-state NFA square-root bound."""
from itertools import product

Q = (0, 1)
EXAMPLE = {
    'a': ((1, 0), (0, 0)),
    'b': ((0, 1), (1, 1)),
}
WITNESS = (('', 'b'), ('a', 'bb'), ('ab', 'babb'),
           ('abb', ''), ('b', 'bab'), ('bb', 'ab'))

def relation(w, transitions):
    M = ((1, 0), (0, 1))
    for ch in w:
        B = transitions[ch]
        M = tuple(tuple(int(any(M[i][r] and B[r][j] for r in Q))
                        for j in Q) for i in Q)
    return M

def square_root_accept(w, transitions, start, finish):
    M = relation(w, transitions)
    return int(any(M[start][r] and M[r][finish] for r in Q))

def pair_step(pairs, matrix):
    """Nondeterministic synchronous evolution of two unlabeled runs."""
    result = set()
    for u, v in pairs:
        for r, s in product(Q, repeat=2):
            if matrix[u][r] and matrix[v][s]:
                result.add(tuple(sorted((r, s))))
    return result

def compact_accept(w, transitions, start, finish):
    if start != finish:
        # Two disjoint three-state symmetric-square components.
        U = {(start, start)}
        V = {tuple(sorted((start, finish)))}
        for ch in w:
            U = pair_step(U, transitions[ch])
            V = pair_step(V, transitions[ch])
        return int(tuple(sorted((start, finish))) in U or
                   (finish, finish) in V)
    # One ordinary two-state component, plus one three-state
    # symmetric-square component.
    R = {start}
    P = {(0, 1)}
    for ch in w:
        B = transitions[ch]
        R = {j for i in R for j in Q if B[i][j]}
        P = pair_step(P, B)
    return int(start in R or (0, 1) in P)

def main():
    # The actual six-pair fooling certificate, including cross-products.
    H = [[square_root_accept(x+y, EXAMPLE, 0, 1)
          for _, y in WITNESS] for x, _ in WITNESS]
    for i in range(6):
        assert H[i][i] == 1
        for j in range(i+1, 6):
            assert not(H[i][j] and H[j][i]), (i, j)
    print('fooling_set_size=6')
    print('fooling_acceptance_matrix:')
    for row in H:
        print(''.join(map(str, row)))

    matrices = [tuple(tuple((i >> (2*r+c)) & 1 for c in Q)
                      for r in Q) for i in range(16)]
    tests = 0
    for A, B in product(matrices, repeat=2):
        delta = {'a': A, 'b': B}
        for start, finish in product(Q, repeat=2):
            for length in range(9):
                for letters in product('ab', repeat=length):
                    word = ''.join(letters)
                    assert compact_accept(word, delta, start, finish) == \
                        square_root_accept(word, delta, start, finish), \
                        (A, B, start, finish, word)
                    tests += 1
    print('binary_relation_pairs=256')
    print('endpoint_choices=4')
    print('word_length_range=0..8')
    print(f'word_equivalence_tests={tests}')
    print('ALL CHECKS PASS')

if __name__ == '__main__':
    main()
