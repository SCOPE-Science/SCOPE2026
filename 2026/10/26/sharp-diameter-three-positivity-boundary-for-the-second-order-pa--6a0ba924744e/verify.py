#!/usr/bin/env python3
"""Exact algebraic verifier of the [0/2] Padé tree-positivity classification.

Requires Python 3.9+ and SymPy. In the same directory run:
    python verify.py --check
Certificate entries store exact rational monomial coefficients.
"""
import argparse
import json
from pathlib import Path
import sympy as sp

A, B, H = sp.symbols('a b h')
M = sp.Matrix([[A + 1, -1, -A, 0],
               [-1, B + 1, 0, -B],
               [-1, 0, 1, 0],
               [0, -1, 0, 1]])
Q = sp.eye(4) + H * M + sp.Rational(1, 2) * H**2 * M**2
DET = sp.Poly(Q.det(method='domain-ge'), A, B, H).as_expr()
ADJ = Q.adjugate()


def polynomials():
    results = {}
    for i, j in ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)):
        results[f'adj_{i}{j}'] = sp.Poly(sp.expand(ADJ[i, j]), A, B, H)
    scale = H**2 + 2 * H + 2
    results['same_leaf_a'] = sp.Poly(sp.cancel((ADJ[2, 2] * scale - 2 * DET) / A), A, B, H)
    results['same_leaf_b'] = sp.Poly(sp.cancel((ADJ[3, 3] * scale - 2 * DET) / B), A, B, H)
    return results


def encoded(poly):
    return [[*powers, int(coef.p), int(coef.q)] for powers, coef in poly.terms()]


def check_certificate(filename):
    raw = json.loads(Path(filename).read_text(encoding='utf8'))
    assert raw['variables'] == ['a', 'b', 'h']
    assert raw['meaning'] == 'coefficients of eight numerator polynomials for the two-hub equitable quotient'
    expected = {name: encoded(poly) for name, poly in polynomials().items()}
    assert raw['coefficients'] == expected, 'Certificate does not match the declared exact quotient matrices'
    for name, terms in expected.items():
        assert terms, name
        assert all(p > 0 and q > 0 and ha >= 1 for _, _, ha, p, q in terms), name
        print(f'{name}: {len(terms)} strictly positive coefficients; smallest h-power {min(t[2] for t in terms)}')
    print('certificate identities and coefficient signs: PASS')


def graph_laplacian(num_vertices, edges):
    L = sp.zeros(num_vertices)
    for u, v in edges:
        L[u, u] += 1
        L[v, v] += 1
        L[u, v] -= 1
        L[v, u] -= 1
    return L


def direct_examples():
    # Construct all leaf-leaf, hub-leaf, and hub-hub entries independently of the quotient.
    for a, b in ((1, 1), (1, 4), (3, 2), (7, 8)):
        N = a + b + 2
        edges = [(0, 1)] + [(0, k) for k in range(2, 2+a)] + [(1, k) for k in range(2+a, N)]
        L = graph_laplacian(N, edges)
        for h in (sp.Rational(1, 10), sp.Rational(1, 1), sp.Rational(7, 3)):
            Z = (sp.eye(N) + h * L + h**2 * L**2 / 2).inv()
            assert all(z > 0 for z in Z), f'Failed direct positivity for {(a, b, h)}'
            assert all(sum(Z.row(i)) == 1 for i in range(N))
    print('twelve independent exact-rational double-star inverses: PASS')

    # An induced five-vertex path gives the sharp negative fourth-distance sign.
    L = graph_laplacian(5, [(i, i+1) for i in range(4)])
    z = sp.symbols('z')
    E = (sp.eye(5) + z*L + z**2*L**2/2).inv()
    coeff = sp.expand(sp.series(E[0, 4], z, 0, 5).removeO()).coeff(z, 4)
    assert coeff == -sp.Rational(1, 4)
    assert E[0, 4].subs(z, sp.Rational(1, 100)) < 0
    print('path of length four: exact fourth-order negative coefficient: PASS')

    z = sp.symbols('z')
    R = 1 / (1 + z + z**2/2)
    assert sp.series(R, z, 0, 5).removeO().expand().coeff(z, 4) == -sp.Rational(1, 4)
    assert sp.simplify(sp.diff(R, z, 2) - (1+3*z+sp.Rational(3,2)*z*z)/(1+z+z*z/2)**3) == 0
    print('Padé expansion and scalar strict convexity: PASS')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--emit-certificate', action='store_true')
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    source = Path(__file__).with_name('certificate.json')
    if args.emit_certificate:
        source.write_text(json.dumps({
            'variables': ['a', 'b', 'h'],
            'meaning': 'coefficients of eight numerator polynomials for the two-hub equitable quotient',
            'coefficients': {name: encoded(poly) for name, poly in polynomials().items()},
        }, indent=2) + '\n', encoding='utf8')
        print('Certificate written:', source.name)
    if args.check or not args.emit_certificate:
        check_certificate(source)
        direct_examples()
        print('ALL CHECKS PASS')


if __name__ == '__main__':
    main()
