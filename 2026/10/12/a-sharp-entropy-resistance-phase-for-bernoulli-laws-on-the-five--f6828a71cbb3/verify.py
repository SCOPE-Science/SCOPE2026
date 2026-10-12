"""Exact rational checks for finite cyclic Bernoulli symmetrizer vertices.

Only Python 3 standard library is required. The global entropy minimum
follows analytically from strict concavity and the vertex table in RESULT.md;
finite sample checks here corroborate the algebra, not the universal proof.
"""
from fractions import Fraction as F
from itertools import combinations
from math import log


def det3(a):
    return (a[0][0] * (a[1][1]*a[2][2]-a[1][2]*a[2][1])
            - a[0][1] * (a[1][0]*a[2][2]-a[1][2]*a[2][0])
            + a[0][2] * (a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def solve(a, b):
    d = det3(a)
    if d == 0:
        return None
    out = []
    for i in range(3):
        x = [list(row) for row in a]
        for j in range(3):
            x[j][i] = b[j]
        out.append(det3(x)/d)
    return out


def all_vertices(p):
    q = 1-p
    matrix = [[F(1)]*5, [q,p,F(0),-q,-p],
              [F(0),q,2*p-1,-p,F(0)]]
    vertices = set()
    for idx in combinations(range(5),3):
        vals = solve([[row[i] for i in idx] for row in matrix],
                     [F(1),F(0),F(0)])
        if vals is None or min(vals) < 0:
            continue
        y = [F(0)]*5
        for i,t in zip(idx,vals):
            y[i] = t
        vertices.add(tuple(y))
    return vertices


def expected_vertices(p):
    q = 1-p
    a = (p,F(0),F(0),F(0),q)
    b = ((1-2*p)/(2-3*p),p*q/(2-3*p),F(0),q*q/(2-3*p),F(0))
    c = (F(0),q/2,F(1,2),p/2,F(0))
    r = (1-2*p)/(3-5*p)
    d = (F(0),r,q/(3-5*p),F(0),r)
    return {a,b,c,d}


def conv(p,y):
    q=1-p
    return tuple(p*y[i]+q*y[(i-1)%5] for i in range(5))


def entropy(y):
    return -sum(float(t)*log(float(t)) for t in y if t>0)


def run():
    checks=0
    samples = [F(1,100), F(1,17), F(1,8), F(1,5),F(1,4),
               F(1,3),F(2,5),F(9,20),F(23,50),F(49,100),F(499,1000)]
    for p in samples:
        q=1-p
        a=all_vertices(p)
        b=expected_vertices(p)
        assert a==b, (p,a,b)
        checks+=1
        for y in a:
            assert sum(y)==1 and min(y)>=0
            z=conv(p,y)
            assert z[1]==z[4] and z[2]==z[3]
            checks+=3
        dominated_b=((1-2*p)/(2-3*p),p*q/(2-3*p),F(0),q*q/(2-3*p),F(0))
        dominated_c=(F(0),q/2,F(1,2),p/2,F(0))
        assert max(dominated_b)<=q and max(dominated_c)<=q
        assert entropy(dominated_b)>entropy((p,q))
        assert entropy(dominated_c)>entropy((p,q))
        checks+=3
        assert min(entropy(y) for y in a)>=min(entropy(y) for y in b)-1e-12
        checks+=1
    low=F(46,100)
    high=F(47,100)
    def gap(p):
        vs=expected_vertices(p)
        e=entropy((p,1-p))
        d=next(y for y in vs if y[0]==0 and y[3]==0 and y[4]>0)
        return entropy(d)-e
    assert gap(low)>0 and gap(high)<0
    checks+=2
    for _ in range(70):
        m=(low+high)/2
        if gap(m)>0: low=m
        else: high=m
    print('CHECKS_PASS',checks,'phase_boundary_midpoint',float((low+high)/2))


if __name__=='__main__':
    run()
