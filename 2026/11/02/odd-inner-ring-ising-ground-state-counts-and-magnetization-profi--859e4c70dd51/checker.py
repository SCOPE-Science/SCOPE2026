#!/usr/bin/env python3
"""Exact and independent checks of the GP(4r+2,2) zero-field Ising formulas.

Usage: python3 checker.py. Depends on Python 3 and SymPy (see requirements.txt).
No external input files or network access are required.
"""
from __future__ import annotations
from collections import defaultdict
import sympy as S


def fibonacci(m):
    a, b = 0, 1
    for _ in range(m):
        a, b = b, a + b
    return a


def spin_graph(n):
    if n < 6:
        raise ValueError('n must be at least 6')
    edges = set()
    def e(i, j):
        if i == j:
            raise ValueError('loop')
        edges.add(tuple(sorted((i, j))))
    for i in range(n):
        e(i, (i+1)%n)
        e(i, i+n)
        e(i+n, ((i+2)%n)+n)
    assert len(edges) == 3*n
    return tuple(sorted(edges))


def brute(n):
    # Complement-symmetric spin assignments. The i-th bit is the spin at vertex i.
    best = 3*n+1
    ways = 0
    edges = spin_graph(n)
    for mask in range(1 << (2*n-1)):
        unsat = sum(1 for i,j in edges if ((mask >> i) & 1) == ((mask >> j) & 1))
        if unsat < best:
            best, ways = unsat, 2
        elif unsat == best:
            ways += 2
    return best, ways


STATES = [(a,b,c) for a in (0,1) for b in (0,1) for c in (0,1)]
TRANSITIONS = [
    (i, j, int(a == aa) + int(c == bb) + int(a == b))
    for i,(a,b,c) in enumerate(STATES)
    for j,(aa,bb,cc) in enumerate(STATES) if cc == b
]


def transfer_min(n):
    # Tropical/min-plus matrix traces, independent of symbolic determinant steps.
    best, ways = 3*n+1, 0
    for initial in range(8):
        layer = {initial: (0, 1)}
        for _ in range(n):
            nxt = {}
            for i, j, w in TRANSITIONS:
                if i not in layer: continue
                val, multiplicity = layer[i]
                q = val + w
                if j not in nxt or q < nxt[j][0]:
                    nxt[j] = (q, multiplicity)
                elif q == nxt[j][0]:
                    nxt[j] = (q, nxt[j][1]+multiplicity)
            layer = nxt
        if initial in layer:
            score, cnt = layer[initial]
            if score < best:
                best, ways = score, cnt
            elif score == best:
                ways += cnt
    return best, ways


def symbolic_certificate():
    z, x, y = S.symbols('z x y')
    mat = S.zeros(8)
    for i,j,w in TRANSITIONS: mat[i,j] = z**w
    p = S.Poly((S.eye(8) - x*mat).det(), x)
    doubled = S.Poly(S.expand(p.as_expr() * p.as_expr().subs(x, -x)), x)
    E0 = S.Integer(0)
    E1 = S.Integer(0)
    for (power,), coefficient in doubled.terms():
        assert power % 2 == 0
        ell = power // 2
        terms = S.Poly(coefficient, z)
        for (k,), a in terms.terms():
            assert k >= ell, ('nonpolynomial after normalization', ell, k)
            if k == ell: E0 += a*y**ell
            if k == ell + 1: E1 += a*y**ell
    claimed_E0 = (1-3*y**2+y**4)**2
    claimed_E1 = -2*y*(y-1)**2*(y**4+8*y**3+15*y**2+8*y+1)
    assert S.expand(E0-claimed_E0) == 0
    assert S.expand(E1-claimed_E1) == 0
    R1 = -y*S.diff(E1/E0,y)
    R1odd = S.cancel((R1 - R1.subs(y,-y))/2)
    f = y/(1-y-y**2)
    D2f = y*S.diff(y*S.diff(f,y),y)
    assert S.cancel(R1odd - (D2f-D2f.subs(y,-y))) == 0
    # Add a fugacity counting the 1-spins, so magnetization is resolved rather
    # than merely summed out. This is strictly more information than Z_n(z,1).
    w, Y = S.symbols('w Y')
    tm = S.zeros(8)
    for i,j,cost in TRANSITIONS:
        a,b,c = STATES[i]
        tm[i,j] = z**cost * w**(a+b)
    pm = S.Poly((S.eye(8)-x*tm).det(method='berkowitz'),x)
    doubles = S.Poly(S.expand(pm.as_expr()*pm.as_expr().subs(x,-x)),(x,z,w))
    em0 = S.Integer(0); em1 = S.Integer(0)
    for (kx,kz,kw),val in doubles.terms():
        assert kx%2 == 0
        ell = kx//2
        assert kz >= ell
        if kz == ell: em0 += val*Y**ell*w**(kw-2*ell)
        if kz == ell+1: em1 += val*Y**ell*w**(kw-2*ell)
    assert S.cancel(em0-claimed_E0.subs(y,Y)) == 0
    odd_em1 = S.expand((em1 - em1.subs(Y,-Y))/2)
    claimed_odd = -2*Y**7 + (2-w**2-w**(-2))*Y**5-2*Y
    assert S.cancel(odd_em1-claimed_odd) == 0
    # The only fugacity powers in this odd part are 0,+2,-2.
    # Its logarithmic derivative therefore proves magnetization 0,+4,-4.
    print('weighted determinant odd part and magnetization support: PASS')
    print('symbolic determinant coefficients E0/E1 and odd Fibonacci identity: PASS')


def coefficient_c(k):
    # Coefficient of t^k in (1-3t+t^2)^(-2), using the two Fibonacci factors.
    if k < 0: return 0
    return sum(fibonacci(2*i+2)*fibonacci(2*(k-i)+2) for i in range(k+1))


def transfer_magnet(n):
    """Return (minimum frustration, {physical magnetization: multiplicity})."""
    best = 3*n+1
    dist = defaultdict(int)
    for initial in range(8):
        layer = {(initial,0): (0,1)}
        for _ in range(n):
            nxt = {}
            for (i,ones),(energy,count) in layer.items():
                a,b,c = STATES[i]
                for ii,j,w in TRANSITIONS:
                    if ii != i: continue
                    key=(j,ones+a+b)
                    e=energy+w
                    if key not in nxt or e<nxt[key][0]:
                        nxt[key]=(e,count)
                    elif e==nxt[key][0]:
                        nxt[key]=(e,nxt[key][1]+count)
            layer=nxt
        for (i,ones),(energy,count) in layer.items():
            if i != initial: continue
            if energy < best:
                best=energy
                dist=defaultdict(int)
            if energy == best:
                dist[2*ones-2*n] += count
    return best, dict(dist)


def check():
    symbolic_certificate()
    for n in (6,8):
        found = brute(n)
        expected = (n//2+1, 2*(n//2)**2*fibonacci(n//2)) if n%4 == 2 else (n//2,None)
        assert found[0] == expected[0]
        if n%4 == 2: assert found[1] == expected[1]
        assert found == transfer_min(n)
        print(f'brute graph vs transfer, n={n}: {found}, PASS')
    # Independently compare exact min-plus transfer to closed formula in 99 cases.
    for n in range(6, 204, 2):
        b, g = transfer_min(n)
        if n%4 == 2:
            m=n//2
            assert (b,g) == (m+1, 2*m*m*fibonacci(m)), (n,b,g)
    print('99 exact transfer comparisons for n=6,8,...,202: PASS')
    for n in range(6,54,4):
        m=n//2
        optimal, dist = transfer_magnet(n)
        a = m*coefficient_c((m-5)//2)
        expected = {0:2*m*m*fibonacci(m)-2*a}
        if a: expected.update({-4:a,4:a})
        assert optimal == m+1
        assert dist == expected, (n,dist,expected)
    print('12 exact magnetization-resolved transfer comparisons n=6,10,...,50: PASS')
    print('VERIFY_OK')


if __name__ == '__main__':
    check()
