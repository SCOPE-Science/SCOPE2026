#!/usr/bin/env python3
"""Exact rational checks for rectangular normalized Monge-polytope asymmetry.

Run: python3 verify_monge_asymmetry.py
All arithmetic uses Python's standard-library fractions.Fraction.
"""
from fractions import Fraction as F


def ray(p, q, typ, a, b=None):
    v = [[F(0) for _ in range(q)] for _ in range(p)]
    if typ == 'NE':
        for i in range(a):
            for j in range(q - b, q):
                v[i][j] = F(1, a*b)
    elif typ == 'SW':
        for i in range(p-a,p):
            for j in range(b):
                v[i][j] = F(1, a*b)
    elif typ == 'ROW':
        for j in range(q):
            v[a][j] = F(1, q)
    elif typ == 'COL':
        for i in range(p):
            v[i][a] = F(1, p)
    else:
        raise ValueError(typ)
    return v


def vertices(p, q):
    out = []
    for i in range(1,p):
        for j in range(1,q):
            out += [ray(p,q,'NE',i,q-j),ray(p,q,'SW',p-i,j)]
    out += [ray(p,q,'ROW',i) for i in range(p)]
    out += [ray(p,q,'COL',j) for j in range(q)]
    return out


def h(z, i, j):
    return z[i][j+1]+z[i+1][j]-z[i][j]-z[i+1][j+1]


def certificate(p, q):
    # q >= p; the transpose supplies all other cases.
    z = [[F(1,p) for _ in range(q)] for _ in range(p)]
    w = [[0]*(q+1) for _ in range(p+1)]
    for i in range(1,p):
        for j in range(1,q):
            aa = i*(q-j)
            bb = (p-i)*j
            ww = min(aa,bb)
            w[i][j] = ww
            # Equal-area pairs contribute half of each normalized rectangle.
            ne = F(1) if aa < bb else F(0) if aa > bb else F(1,2)
            sw = 1-ne
            for r in range(p):
                for s in range(q):
                    if r < i and s >= j:
                        z[r][s] += ne/F(ww)
                    if r >= i and s < j:
                        z[r][s] += sw/F(ww)
    lam = [[F(1+w[r+1][s+1]-w[r+1][s]-w[r][s+1]+w[r][s])
            for s in range(q)] for r in range(p)]
    return z,w,lam


def inspect(p,q):
    v = vertices(p,q)
    z,w,lam = certificate(p,q)
    t = p*(q-1)+1
    assert sum(map(sum,z)) == t
    assert sum(map(sum,lam)) == p*q
    assert all(x>=0 for row in lam for x in row)
    assert all(z[i][j]>=max(x[i][j] for x in v)
               for i in range(p) for j in range(q))
    assert all(h(z,i,j) == F(1,w[i+1][j+1]) and
               h(z,i,j)>=max(h(x,i,j) for x in v)
               for i in range(p-1) for j in range(q-1))
    # Exact dual coefficient identity, first on every ambient basis vector,
    # then on the primal certificate itself.
    for r in range(p):
        for s in range(q):
            e = [[F(int(i==r and j==s)) for j in range(q)] for i in range(p)]
            rhs = sum(lam[i][j]*e[i][j] for i in range(p) for j in range(q))
            rhs += sum(w[i+1][j+1]*h(e,i,j)
                       for i in range(p-1) for j in range(q-1))
            assert rhs==1
    lower = sum(lam[i][j]*F(1,p) for i in range(p) for j in range(q))
    lower += sum(w[i+1][j+1]*max(h(x,i,j) for x in v)
                 for i in range(p-1) for j in range(q-1))
    assert lower == t
    return len(v),p*q+(p-1)*(q-1)


def main():
    cases=nv=nf=0
    for p in range(2,10):
        for q in range(p,13):
            a,b=inspect(p,q)
            cases+=1;nv+=a;nf+=b
    print('PASS exact Monge asymmetry certificates:',cases,'parameter pairs;',
          nv,'vertices and',nf,'facet inequalities checked;',
          'basis coefficient identities independently verified.')


if __name__=='__main__':
    main()
