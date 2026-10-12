"""Exact finite-case checks for the ordered one-tree Schur-clique sampling theorem.

Only Python standard library required. These finite checks supplement, but do not
replace, the symbolic induction that applies to every neighborhood size.
"""
from fractions import Fraction
from itertools import product
from math import factorial


def tree_distance(a, b, parent, n):
    """Return series resistance on the unique tree path, exactly."""
    ancestor_dist = {a: Fraction(0)}
    p = a
    value = Fraction(0)
    while p != n:
        value += Fraction(n, n-p)
        p = parent[p]
        ancestor_dist[p] = value
    p = b
    value_b = Fraction(0)
    while p not in ancestor_dist:
        value_b += Fraction(n, n-p)
        p = parent[p]
    return ancestor_dist[p] + value_b


def check(n):
    assert n >= 2
    counts = factorial(n-1)
    vertices = range(1, n+1)
    pair_sum = {(i,j):Fraction(0) for i in vertices for j in vertices if i<j}
    edge_sum = {(i,j):Fraction(0) for i in vertices for j in vertices if i<j}
    configurations = 0
    # Each index i chooses its parent j independently and uniformly from i+1..n.
    for chosen in product(*(tuple(range(i+1,n+1)) for i in range(1,n))):
        parent = {i:chosen[i-1] for i in range(1,n)}
        configurations += 1
        for i, j in parent.items():
            edge_sum[i,j] += Fraction(n-i, n)
        for i,j in pair_sum:
            r = tree_distance(i,j,parent,n)
            pair_sum[i,j] += r
        assert tree_distance(n-1,n,parent,n) == n
    assert configurations == counts
    for (i,j),v in pair_sum.items():
        assert v == n*counts, ('mean resistance', n, i,j,v, counts)
    for (i,j),v in edge_sum.items():
        assert v == Fraction(counts,n), ('unbiasedness',n,i,j,v,counts)
    # On a centered Laplacian the resistance matrix determines the
    # pseudoinverse uniquely by double centering D -> -P D P / 2.
    # Here averaged D has off-diagonal entries n, hence E[T^+] = nP/2.
    D = [[Fraction(0) if i==j else Fraction(n) for j in range(n)] for i in range(n)]
    rowmean = [sum(row, Fraction(0))/n for row in D]
    grandmean = sum(rowmean, Fraction(0))/n
    for i in range(n):
        for j in range(n):
            mean_inverse_ij = -Fraction(1,2)*(D[i][j]-rowmean[i]-rowmean[j]+grandmean)
            expected = Fraction(n,2)*(Fraction(int(i==j))-Fraction(1,n))
            assert mean_inverse_ij == expected, ('inverse', n,i,j)
    return configurations,len(pair_sum),len(edge_sum)


def main():
    total=0
    for n in range(2,9):
        configs,npairs,nedges=check(n)
        total+=configs
        print(f'n={n}: {configs} trees; {npairs} exact mean pair resistances; '
              f'{nedges} exact mean conductances; pseudoinverse identity')
    print(f'PASS: {total} trees enumerated; all finite exact identities confirmed.')
    print('Unbounded n is established by the mathematical induction, not this enumeration.')

if __name__=='__main__':
    main()
