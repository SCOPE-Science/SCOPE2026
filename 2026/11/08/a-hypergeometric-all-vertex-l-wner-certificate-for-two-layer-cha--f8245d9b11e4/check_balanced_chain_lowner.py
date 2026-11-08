#!/usr/bin/env python3
"""Exact contact and Löwner-certificate checks for balanced two-layer chain polytopes.

Uses only Python standard library. Checks each vertex, mean, covariance,
and all three positive quadratic-form eigenspaces for m = 1,...,8.
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def dot(u, v):
    return sum(a*b for a, b in zip(u, v))


def run(m):
    d = 2*m
    den = comb(2*m+1, m)
    t = F(m+1, 2*(2*m+1))
    qc = F(m*(m+1), 2*(2*m+1))
    qp = F(m*(m+1)**2, 2*(2*m+1)**2)
    qm = F(m*(m+1)**2, 2*(2*m+1))
    s = [1]*m + [-1]*m
    ones = [1]*d
    def Pcontrast(i,j):
        return (F(int(i == j),1) - F(1,m)) if (i//m == j//m) else F(0,1)
    def Pplus(i,j): return F(1,d)
    def Pminus(i,j): return F(s[i]*s[j],d)
    Q = [[qc*Pcontrast(i,j)+qp*Pplus(i,j)+qm*Pminus(i,j)
          for j in range(d)] for i in range(d)]
    Qinverse = [[Pcontrast(i,j)/qc+Pplus(i,j)/qp+Pminus(i,j)/qm
                 for j in range(d)] for i in range(d)]
    # Count the origin once. Every other vertex has exactly one nonzero part.
    vertices = [(tuple([0]*d), F(1,den))]
    for side in (0,1):
        for bits in product((0,1),repeat=m):
            k = sum(bits)
            if k == 0:
                continue
            v = tuple((bits+((0,)*m)) if side == 0 else (((0,)*m)+bits))
            vertices.append((v,F(comb(m+1,k),2*den)))
    assert len(vertices) == 2**(m+1)-1
    assert sum(w for v,w in vertices) == 1
    mean = [sum(w*v[i] for v,w in vertices) for i in range(d)]
    assert mean == [t]*d, (m,'mean')
    cov = [[sum(w*(v[i]-t)*(v[j]-t) for v,w in vertices)
            for j in range(d)] for i in range(d)]
    assert cov == [[Q[i][j]/d for j in range(d)] for i in range(d)], (m,'covariance')
    assert qc>0 and qp>0 and qm>0
    for v,w in vertices:
        diff=[F(z)-t for z in v]
        norm=sum(diff[i]*sum(Qinverse[i][j]*diff[j] for j in range(d)) for i in range(d))
        assert norm == 1, (m,v,norm)
    assert qm/qp == 2*m+1
    return len(vertices)


def main():
    for m in range(1,9):
        print(f'm={m}: {run(m)} exact vertices/contact points, mean and covariance verified')
    print('BALANCED_CHAIN_LOEWNER_EXACT_CHECKS_PASSED')

if __name__=='__main__':
    main()
