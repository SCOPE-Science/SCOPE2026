#!/usr/bin/env python3
"""Independent finite checks of the highest-simplex-boundary Laplacian metric formulas.
Only Python's standard library is required. These finite checks are not the all-m proof.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import sqrt, isclose


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def check(m):
    ss = [Q((-1)**i) for i in range(m)]
    ee = [tuple(Q(i == j) for i in range(m)) for j in range(m)]
    L = [[m*Q(i == j)-ss[i]*ss[j] for j in range(m)] for i in range(m)]
    # Independently reconstruct B^T B from oriented boundary faces.
    B = []
    for p, q in combinations(range(m), 2):
        row = [Q(0)]*m
        for j, missing in ((p, q), (q, p)):
            face = [t for t in range(m) if t != j]
            row[j] = Q((-1)**face.index(missing))
        B.append(row)
    for i in range(m):
        for j in range(m):
            assert sum(row[i]*row[j] for row in B) == L[i][j]
    vertices = [tuple(L[i][j] for i in range(m)) for j in range(m)]
    one = tuple([Q(1)]*m)
    if m % 2 == 0:
        k = m//2
        R2 = Q(m*(m-2))
        r2 = Q(2*m, m-2)
        plus = [i for i in range(m) if ss[i] == 1]
        minus = [i for i in range(m) if ss[i] == -1]
        vv = [tuple(vertices[i][j]-one[j] for j in range(m)) for i in range(m)]
        assert all(dot(v,v)==R2 for v in vv)
        assert all(sum(vv[i], Q(0))==0 for i in range(m))
        assert all(dot(vv[i],vv[j])==0 for i in plus for j in minus)
        for i in plus:
            for j in minus:
                normal=tuple(-Q(k-1,1)*(vv[i][h]+vv[j][h])/R2 for h in range(m))
                assert dot(normal, normal)==1/r2
                contacts=[t for t in range(m) if dot(normal,vv[t])==1]
                assert len(contacts)==m-2
                assert i not in contacts and j not in contacts
                assert all(dot(normal,vv[t])<=1 for t in range(m))
        return f'even m={m}: {k*k} facet planes, all {m} vertices on squared radius {R2}'
    else:
        eps=sum(ss)
        assert abs(eps)==1
        major=[i for i in range(m) if ss[i]==eps]
        minor=[i for i in range(m) if ss[i]!=eps]
        a=Q(len(major)); b=Q(len(minor))
        centroid=tuple(Q(1)-eps*t/m for t in ss)
        center_outer=tuple(sum(vertices[i][j] for i in major)/a for j in range(m))
        R2=Q(m*m*(m-1), m+1)
        for i in major:
            v=tuple(vertices[i][j]-center_outer[j] for j in range(m))
            assert dot(v,v)==R2
        for i in minor:
            v=tuple(vertices[i][j]-center_outer[j] for j in range(m))
            assert R2-dot(v,v)==Q(4*m,m+1)
        assert all(center_outer[j]==Q(m,m+1)*centroid[j] for j in range(m))
        for i in range(m):
            grad=tuple((ee[i][h]-eps*ss[i]*one[h])/m for h in range(m))
            assert dot(grad,ss)==0
            expected=Q(m-1,m*m) if i in major else Q(m+3,m*m)
            assert dot(grad,grad)==expected
            for j in range(m):
                dif=tuple(vertices[j][h]-centroid[h] for h in range(m))
                assert Q(1,m)+dot(grad,dif)==Q(i==j)
        r=2*m/((m+1)*sqrt(m-1)+(m-1)*sqrt(m+3))
        lam=[r*sqrt(m-1)/m if i in major else r*sqrt(m+3)/m for i in range(m)]
        assert isclose(sum(lam),1,rel_tol=1e-13)
        center_in=[sum(lam[i]*float(vertices[i][j]) for i in range(m)) for j in range(m)]
        theta=r*(sqrt(m-1)+sqrt(m+3))/2
        assert theta>1
        assert all(isclose(center_in[j],theta*float(centroid[j]),rel_tol=1e-12,abs_tol=1e-12) for j in range(m))
        return f'odd m={m}: {len(major)} of {m} outer contacts, squared radius {R2}, exact exclusion gap {Q(4*m,m+1)}'


if __name__ == '__main__':
    for m in range(3,18):
        print(check(m))
    print('PASS: finite exact-rational and floating point identities (m=3..17); universal claims use the separate proof.')
