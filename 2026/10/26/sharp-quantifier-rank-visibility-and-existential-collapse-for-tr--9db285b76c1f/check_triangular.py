"""Reproducible finite checks for the quantifier-rank profile of triangular graphs.

Only supplementary small-instance checks; all-rank proof is mathematical.
Uses the Python standard library.
"""
from itertools import combinations, permutations


def adjacency_matrix(n):
    edges = list(combinations(range(n), 2))
    return edges, [[bool(set(a) & set(b)) if a != b else False
                    for b in edges] for a in edges]


def canonical_pattern(items, matrix):
    k = len(items)
    def code(order):
        return tuple(int(matrix[items[order[i]]][items[order[j]]])
                     for i in range(k) for j in range(i+1,k))
    return min(code(p) for p in permutations(range(k)))


def finite_patterns(n, max_q):
    vertices, mat = adjacency_matrix(n)
    result = {0:{()}}
    for k in range(1, max_q+1):
        result[k] = set(canonical_pattern(c,mat)
                        for c in combinations(range(len(vertices)),k))
    return result


def check():
    cache={}
    for q in range(1,5):
        for n in range(2,2*q+2):
            if n not in cache or max(cache[n])<q:
                cache[n]=finite_patterns(n,q)
        for n in range(2,2*q+1):
            left,right=cache[n],cache[n+1]
            new = [(k,p) for k in range(1,q+1) for p in right[k]-left[k]]
            if n<2*q:
                assert new,(q,n,'no separating existential pattern')
            else:
                assert not new,(q,n,'unexpected existential separation')
        print('q=',q,' visible exact orders 2..',2*q-1,
              '; first tail order=',2*q,
              '; finite existential-pattern checks PASS',sep='')
    print('All tested adjacent-order predictions PASS. Finite checks are not a proof.')


if __name__=='__main__':
    check()
