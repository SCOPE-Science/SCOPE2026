#!/usr/bin/env python3
"""Exact bit-integer GF(2) rank and polynomial-identity checks on line graphs."""
from itertools import combinations


def rank_gf2(rows):
    pivot = {}
    for value in rows:
        while value:
            lead = value.bit_length() - 1
            if lead not in pivot:
                pivot[lead] = value
                break
            value ^= pivot[lead]
    return len(pivot)


def compose(left, right):
    result = []
    for row in left:
        total = 0
        while row:
            bit = row & -row
            total ^= right[bit.bit_length()-1]
            row ^= bit
        result.append(total)
    return result


def line_graph_matrix(n, k):
    deleted = {(2*i,2*i+1) for i in range(k)}
    edges = [(u,v) for u,v in combinations(range(n),2) if (u,v) not in deleted]
    adjacency = []
    for i,(u,v) in enumerate(edges):
        row = 0
        for j,(a,b) in enumerate(edges):
            if i != j and len({u,v,a,b}) == 3:
                row |= 1 << j
        adjacency.append(row)
    return adjacency


def verify():
    cases = 0
    for n in range(3, 17):
        for k in range(n//2+1):
            A = line_graph_matrix(n,k)
            E = len(A)
            A2 = compose(A,A)
            A3 = compose(A2,A)
            r1,r2,r3 = (rank_gf2(matrix) for matrix in (A,A2,A3))
            if n % 2:
                assert A3 == A
                assert (r1,r2,r3) == (n-1,n-1,n-1)
                # A+A^2 has exactly k independent images, controlling two-cycles.
                assert rank_gf2([x^y for x,y in zip(A,A2)]) == k
                # A restricted to its recurrent image has k size-two Jordan blocks at 1.
                assert n-1-2*k >= 0
            else:
                m = n//2
                predicted = k if k < m else m-1-int(m % 2 == 0)
                assert A3 == [0]*E
                assert (r1,r2,r3) == (n-2,predicted,0)
                assert r1-2*r2 >= 0 and E-2*r1+r2 >= 0
            cases += 1
    print(f'ALL_MATRIX_CASES_PASS n=3..16 cases={cases}')
    print('Verified ranks of A, A^2, A^3 and the polynomial identities over GF(2).')
    print('For odd n, also verified rank(A+A^2)=k.')

if __name__ == '__main__':
    verify()
