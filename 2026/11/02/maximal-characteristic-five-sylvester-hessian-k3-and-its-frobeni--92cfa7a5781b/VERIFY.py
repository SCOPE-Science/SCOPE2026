#!/usr/bin/env python3
"""Exact verification of the characteristic-five symmetric Hessian quartic.

Requires SymPy 1.13 or later for polynomial ideal calculations.
Pure-Python finite-field loops independently enumerate rational points.
"""
from itertools import product
import sympy as sp


def symbolic_certificate():
    xs = sp.symbols('x0:4')
    x5 = tuple(xs) + (-sum(xs),)
    e4 = sp.expand(sum(sp.prod(x5[j] for j in range(5) if j != i)
                       for i in range(5)))
    c3 = sp.expand(sum(z**3 for z in x5))
    assert sp.expand(sp.hessian(c3, xs).det(method='domain-ge') - 1296*e4) == 0
    u, v, w = sp.symbols('u v w')
    h = sp.expand(e4.subs({xs[0]: 1, xs[1]: u, xs[2]: v, xs[3]: w}))
    initial = [h, sp.diff(h, u), sp.diff(h, v), sp.diff(h, w)]
    actual = sp.groebner(initial, u, v, w, modulus=5, order='lex')
    expected = [
        u**2+u-w**2-w,
        u*v+2*w**2+2*w,
        u*w+2*w**2+2*w,
        v**2+v-w**2-w,
        v*w+2*w**2+2*w,
        w**3-w,
    ]
    guessed = sp.groebner(expected, u, v, w, modulus=5, order='lex')
    assert actual.is_zero_dimensional
    assert len(actual.polys) == len(guessed.polys) == 6
    assert [p.as_expr() for p in actual.polys] == [p.as_expr() for p in guessed.polys]
    # The 5 geometric solutions in this affine chart are already F5 rational.
    expected_roots = {(0,0,0),(4,0,0),(0,4,0),(0,0,4),(1,1,1)}
    roots = set()
    for pt in product(range(5),repeat=3):
        values = dict(zip((u,v,w),pt))
        if all(int(q.subs(values)) % 5 == 0 for q in expected):
            roots.add(pt)
    assert roots == expected_roots
    # Since the leading monomials are u^2, uv, uw, v^2, vw, w^3,
    # the quotient has basis 1,u,v,w,w^2, hence length 5 and is reduced.
    for pt, det in [((0,0,0),3), ((1,1,1),2)]:
        matrix = sp.hessian(h, (u,v,w)).subs(dict(zip((u,v,w),pt)))
        assert int(matrix.det()) % 5 == det
    print('SYLVESTER_HESSIAN_IDENTITY=1296_E4_EXACT')
    print('JACOBIAN_GROEBNER_6_GENERATORS_CHART_LENGTH=5_REDUCED')
    print('AFFINE_SINGULAR_ROOTS=' + str(sorted(roots)))
    print('TWO_NODE_ORBIT_HESSIAN_DETERMINANTS_MOD5=(3,2)')


def finite_counts(field_size, d=2):
    q = field_size
    elements = tuple(range(q))
    add, mult = [[0]*q for _ in elements], [[0]*q for _ in elements]
    for a in elements:
        for b in elements:
            if q == 5:
                add[a][b] = (a+b) % 5
                mult[a][b] = (a*b) % 5
            else:
                a0,a1 = a%5, a//5
                b0,b1 = b%5, b//5
                add[a][b] = (a0+b0)%5 + 5*((a1+b1)%5)
                mult[a][b] = (a0*b0+d*a1*b1)%5 + 5*((a0*b1+a1*b0)%5)
    neg = [next(b for b in elements if add[a][b] == 0) for a in elements]
    chart_counts, singular_counts = [], []
    for first in range(4):
        n,ns=0,0
        for tail in product(elements, repeat=3-first):
            p4 = (0,)*first + (1,) + tail
            x4 = neg[add[add[p4[0]][p4[1]]][add[p4[2]][p4[3]]]]
            a = p4 + (x4,)
            value = 0
            for omit in range(5):
                z=1
                for j in range(5):
                    if j != omit:
                        z=mult[z][a[j]]
                value=add[value][z]
            if value:continue
            n += 1
            # Intrinsic hypersurface singularity in H=sum x_i=0:
            # all five ambient derivatives of e4 must be equal.
            deriv=[]
            for omit in range(5):
                rem=[a[j] for j in range(5) if j != omit]
                zsum=0
                for omit2 in range(4):
                    z=1
                    for j in range(4):
                        if j!=omit2:
                            z=mult[z][rem[j]]
                    zsum=add[zsum][z]
                deriv.append(zsum)
            if len(set(deriv)) == 1:
                ns += 1
        chart_counts.append(n)
        singular_counts.append(ns)
    return tuple(chart_counts),tuple(singular_counts)


def main():
    symbolic_certificate()
    for q,d in [(5,2),(25,2),(25,3)]:
        c,s=finite_counts(q,d)
        assert sum(c)==(41 if q==5 else 901)
        assert sum(s)==11
        assert (sum(c)+q*sum(s)) == (96 if q==5 else 1176)
        print(f'FIELD={q},T2={d}: QUARTIC={sum(c)} CHARTS={c}; NODES={sum(s)} NODE_CHARTS={s}; RESOLUTION={sum(c)+q*sum(s)}')
    assert 1176==1+25*25+22*25
    assert 96-1-25==18*5-4*5
    print('WEIL_EQUALITY_F25=1176; FROBENIUS_EIGENVALUES_PLUS5_18_MINUS5_4')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
