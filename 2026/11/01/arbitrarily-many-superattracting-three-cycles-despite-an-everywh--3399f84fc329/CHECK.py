#!/usr/bin/env python3
"""Exact checks for polynomial nilpotent-Jacobian maps with multiple three-cycles.

Only Python's standard library is needed. This finite checker supplements the
all-N proof supplied in RESULT.md; finite tests do not prove the theorem.
"""
from fractions import Fraction as Q


def interpolate(n):
    """Solve P(0)=0, P(j*j)=j, P'(j*j)=0, 1<=j<=n, deg P<=2n."""
    m = 2*n + 1
    rows = []
    rows.append([Q(int(k == 0)) for k in range(m)] + [Q(0)])
    for j in range(1, n+1):
        s = Q(j*j)
        rows.append([s**k for k in range(m)] + [Q(j)])
        rows.append([Q(0) if k==0 else Q(k)*s**(k-1) for k in range(m)] + [Q(0)])
    for c in range(m):
        pivot = next((r for r in range(c, m) if rows[r][c]), None)
        assert pivot is not None
        rows[c], rows[pivot] = rows[pivot], rows[c]
        z = rows[c][c]
        rows[c] = [v/z for v in rows[c]]
        for r in range(m):
            if r == c: continue
            z = rows[r][c]
            if z:
                rows[r] = [a-z*b for a,b in zip(rows[r],rows[c])]
    return [row[-1] for row in rows]


def val(p, t):
    a = Q(0)
    for c in reversed(p):
        a = a*t + c
    return a


def der(p, t):
    return val([Q(k)*p[k] for k in range(1,len(p))],t)


def fmap(p, point):
    x,y,z=point
    u=val(p,y+x*x)
    return (u,z-2*x*u,u*u)


def jac(p,point):
    x,y,z=point
    u=val(p,y+x*x)
    v=der(p,y+x*x)
    return [[2*x*v,v,Q(0)],[-2*u-4*x*x*v,-2*x*v,Q(1)],
            [4*x*u*v,2*u*v,Q(0)]]


def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(3)),Q(0))
             for j in range(3)] for i in range(3)]


def zero(a):
    return all(x == 0 for row in a for x in row)


def run():
    checks = 0
    for n in range(1,7):
        p=interpolate(n)
        assert len(p)==2*n+1 and p[0]==0
        for j in range(1,n+1):
            s=Q(j*j)
            assert val(p,s)==j and der(p,s)==0
            cycle=[(Q(0),s,Q(0)), (Q(j),Q(0),s), (Q(j),-s,s)]
            for i,point in enumerate(cycle):
                assert fmap(p,point)==cycle[(i+1)%3]
                checks += 1
            j0=jac(p,cycle[0]); j1=jac(p,cycle[1]); j2=jac(p,cycle[2])
            assert zero(mm(j1,j0))
            assert zero(mm(j2,mm(j1,j0)))
            checks += 2
        for x in (-1,0,1):
            for y in (-1,0,1):
                for z in (-1,0,1):
                    matrix=jac(p,(Q(x),Q(y),Q(z)))
                    assert zero(mm(mm(matrix,matrix),matrix))
                    checks += 1
    print('PASS: N=1..6, exact interpolation, all 3-cycles, local two-step zero derivative,')
    print('and 162 sample pointwise nilpotency identities; checks:', checks)

if __name__=='__main__':
    run()
