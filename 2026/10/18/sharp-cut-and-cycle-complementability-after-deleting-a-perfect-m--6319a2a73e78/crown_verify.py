#!/usr/bin/env python3
"""Exact rational tests for crown-graph edge-space projections.

All calculations use the Python standard library; no numerical tolerances.
The proof for all dimensions is independent of this finite checker.
"""
from fractions import Fraction as F


def edges(n):
    return [(i, j) for i in range(n) for j in range(n) if i != j]


def entry(n, source, target):
    a, b = source
    k, l = target
    def s(x):
        return F(int(x == a) - int(x == b), 2*n)
    def c(x):
        return (F(int(x == a) + int(x == b), 2) - F(1, n)) / (n-2)
    g = F(1, 2*n*(n-1))
    return s(k)-s(l)+c(k)+c(l)+2*g


def test(n):
    ee = edges(n)
    for src in ee:
        col = {edge: entry(n, src, edge) for edge in ee}
        # Incidence: source vector minus its cut projection is divergence-free.
        for i in range(n):
            udiv = sum((int(edge == src)-val for edge,val in col.items() if edge[0] == i),F(0))
            vdiv = sum((int(edge == src)-val for edge,val in col.items() if edge[1] == i),F(0))
            assert udiv == 0 and vdiv == 0, (n, src, i)
        pnorm = sum(map(abs,col.values()),F(0))
        qnorm = sum((abs(F(int(e==src))-v) for e,v in col.items()),F(0))
        assert pnorm == F(3*n-4,n),(n,src,pnorm)
        assert qnorm == F(2*(2*n*n-6*n+3),n*(n-1)),(n,src,qnorm)
    # Check that P is the identity on the spanning row and column cuts.
    for idx in range(n):
        for target in ee:
            assert sum((entry(n,src,target) for src in ee if src[0]==idx),F(0)) == int(target[0]==idx)
            assert sum((entry(n,src,target) for src in ee if src[1]==idx),F(0)) == int(target[1]==idx)
    # Self-adjointness; the formula itself is explicitly row-plus-column.
    for a in ee:
        for b in ee:
            assert entry(n,a,b)==entry(n,b,a),(n,a,b)
    return len(ee)


if __name__=='__main__':
    counts=[(n,test(n)) for n in range(3,10)]
    for n,_ in counts:
        pc=F(3*n-4,n); qc=F(2*(2*n*n-6*n+3),n*(n-1))
        pb=F(3*n*n-4*n+2,n*n); qb=F(4*(n-1)**2,n*n)
        assert pc<pb and qc<qb
        assert (qc>pc)==(n>=5)
        assert (qb>pb)==(n>=4)
    print('PASS: exact incidence, self-adjointness, all-column norms and deletion/crossover comparisons')
    print('Dimensions:',' '.join(f'n={n}, edges={m}' for n,m in counts))
