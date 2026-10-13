#!/usr/bin/env python3
"""Exact rational checks for quantum average mixing on subdivided bicliques.

Requires Python 3 and SymPy. This is a finite cross-check, not a proof for
unbounded graph orders. No datasets or network access are required.
"""
import sympy as sp


def subdivided_biclique(a, b):
    n = a + b + a*b
    h = sp.zeros(n)
    for i in range(a):
        for j in range(b):
            e = a + b + i*b + j
            h[i, e] = h[e, i] = 1
            h[a+j, e] = h[e, a+j] = 1
    return h


def direct_average(h, a, b):
    n = h.rows
    ident = sp.eye(n)
    square = h*h
    squared_eigenvalues = sorted(set([a+b] + ([b] if a>1 else []) + ([a] if b>1 else [])))
    p0 = ident
    for lam in squared_eigenvalues:
        p0 = p0*(ident-square/sp.Integer(lam))
    mixing = p0.multiply_elementwise(p0)
    for lam in squared_eigenvalues:
        p = square/sp.Integer(lam)
        for mu in squared_eigenvalues:
            if mu != lam:
                p = p*(square-sp.Integer(mu)*ident)/sp.Integer(lam-mu)
        # Projector construction is independently checked through the final matrix.
        hp = h*p
        mixing += (p.multiply_elementwise(p) + hp.multiply_elementwise(hp)/sp.Integer(lam))/2
    return mixing


def closed_average(a, b):
    ab = a*b
    n = a+b+ab
    da = sp.eye(a)-sp.ones(a)/a
    db = sp.eye(b)-sp.ones(b)/b
    sa = da.multiply_elementwise(da)
    sb = db.multiply_elementwise(db)
    result = sp.zeros(n)
    for i in range(a+b):
        for j in range(a+b):
            result[i,j] = sp.Rational(1,(a+b)**2)
    result[a+b:n,a+b:n] += sp.kronecker_product(sa,sb)
    z = sp.Matrix([sp.Rational(b,a*(a+b))]*a+[sp.Rational(a,b*(a+b))]*b+[sp.Rational(1,ab)]*ab)
    result += z*z.T/2
    ca = sp.zeros(n,a)
    cb = sp.zeros(n,b)
    for i in range(a):
        ca[i,i] = 1
        for j in range(b):
            ca[a+b+i*b+j,i] = sp.Rational(1,b)
    for j in range(b):
        cb[a+j,j] = 1
        for i in range(a):
            cb[a+b+i*b+j,j] = sp.Rational(1,a)
    result += ca*sa*ca.T/2 + cb*sb*cb.T/2
    if a==b:
        result[a+b:n,a+b:n] += sp.kronecker_product(da,db)/ab
    return result


def expected_nullity(a,b):
    a,b=sorted((a,b))
    if a>=3: return 0
    if a==2: return b+1 if b>2 else 4
    if b==1: return 1
    if b==2: return 2
    return b-1


def main():
    pairs=[(a,b) for a in range(1,5) for b in range(a,5) if a+b+a*b<=20]
    entries=0
    for a,b in pairs:
        h=subdivided_biclique(a,b)
        calc=direct_average(h,a,b)
        closed=closed_average(a,b)
        assert calc==closed, ('matrix_mismatch',a,b)
        assert closed*sp.ones(closed.rows,1)==sp.ones(closed.rows,1), ('not_stochastic',a,b)
        if closed.rows<=15:
            assert closed.rank()==closed.rows-expected_nullity(a,b), ('rank_mismatch',a,b)
        entries += closed.rows**2
    print('VERIFY_OK exact_pairs=%d exact_entries=%d 3_3_order=%d 2_3_rank=%d 1_3_rank=%d' %
          (len(pairs),entries, closed_average(3,3).rows,
           closed_average(2,3).rank(),closed_average(1,3).rank()))


if __name__=='__main__':
    main()
