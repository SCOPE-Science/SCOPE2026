#!/usr/bin/env python3
"""Exact computations for the three-row periodic Spiral kinetic model.

Requires Python 3.10+ and SymPy 1.12+.  Run: python verify.py.
All edges and states are reconstructed from the printed local rule.
"""
from collections import defaultdict, deque
from itertools import product
from math import isclose, log
import sympy as S


def occupied(m, y):
    return (m >> (y % 3)) & 1


def locally_frozen(a, b, c):
    for y in range(3):
        if not occupied(b, y):
            continue
        ne = occupied(b, y + 1) or occupied(c, y + 1)
        sw = occupied(b, y - 1) or occupied(a, y - 1)
        nw = occupied(a, y) or occupied(a, y + 1)
        se = occupied(c, y) or occupied(c, y - 1)
        if not ((ne and sw) or (nw and se)):
            return False
    return True


def physical_frozen(word):
    # Independent implementation on site coordinates, rather than the local
    # three-column predicate used to construct the transfer matrix.
    n = len(word)
    if n < 4:
        raise ValueError('Physical check requires at least four columns.')
    def occ(x, y):
        return (word[x % n] >> (y % 3)) & 1
    for x in range(n):
        for y in range(3):
            if not occ(x, y):
                continue
            ne = occ(x, y + 1) or occ(x + 1, y + 1)
            sw = occ(x, y - 1) or occ(x - 1, y - 1)
            nw = occ(x - 1, y) or occ(x - 1, y + 1)
            se = occ(x + 1, y) or occ(x + 1, y - 1)
            if not ((ne and sw) or (nw and se)):
                return False
    return True


def build_matrix(z):
    states = [(a, b) for a in range(8) for b in range(8)]
    ix = {s: j for j, s in enumerate(states)}
    T = S.zeros(64)
    E = [[] for _ in states]
    for k, (a, b) in enumerate(states):
        for c in range(8):
            if locally_frozen(a, b, c):
                j = ix[(b, c)]
                T[k, j] = z**b.bit_count()
                E[k].append(j)
    return T, E


def critical_polynomial(lam, z):
    return S.expand(
        lam**8 - (z+1)**3 * lam**7
        + z*(3*z**2+5*z+3)*lam**6
        - z**2*(3*z**4+3*z**3+3*z+2)*lam**5
        + z**4*(z**4+5*z**3+10*z**2+10*z+3)*lam**4
        + z**5*(z**5+2*z**4+6*z**3-10*z-6)*lam**3
        - z**7*(5*z**3+8*z**2+9*z+2)*lam**2
        - z**9*(z**3-2)*lam + 3*z**12
    )


def cyclic_component_sizes(E):
    # Kosaraju decomposition, independent of symbolic linear algebra.
    V = len(E)
    reverse = [[] for _ in range(V)]
    for s, tlist in enumerate(E):
        for t in tlist:
            reverse[t].append(s)
    seen, order = set(), []
    def dfs(s):
        seen.add(s)
        for t in E[s]:
            if t not in seen:
                dfs(t)
        order.append(s)
    for s in range(V):
        if s not in seen:
            dfs(s)
    seen, sizes = set(), []
    def back(s):
        seen.add(s)
        count = 1
        for t in reverse[s]:
            if t not in seen:
                count += back(t)
        return count
    for s in reversed(order):
        if s not in seen:
            sizes.append(back(s))
    return sorted(sizes, reverse=True)


def direct_histogram(n):
    counts = defaultdict(int)
    for word in product(range(8), repeat=n):
        if physical_frozen(word):
            counts[sum(v.bit_count() for v in word)] += 1
    return dict(counts)


def transfer_histogram(n):
    # Each closed walk contributes z^(number of occupied sites).
    _, adj = build_matrix(S.Integer(1))
    count = defaultdict(int)
    for a in range(8):
        for b in range(8):
            start = 8*a+b
            cur = {(start, 0):1}
            for _ in range(n):
                new = defaultdict(int)
                for (state, occupancy), ways in cur.items():
                    for nxt in adj[state]:
                        middle_mask = state % 8
                        new[(nxt, occupancy + middle_mask.bit_count())] += ways
                cur = new
            for (state, weight), val in cur.items():
                if state == start:
                    count[weight] += val
    return dict(count)


def run():
    lam, z = S.symbols('lambda z')
    T, E = build_matrix(z)
    assert len(E) == 64
    assert cyclic_component_sizes(E) == [52] + [1]*12
    assert T[63,63] == z**3  # all occupied self-loop ensures aperiodicity
    cp = T.charpoly(lam).as_expr()
    p8 = critical_polynomial(lam,z)
    assert S.rem(cp, p8, lam) == 0
    q12 = S.cancel(cp/(lam**44*p8))
    assert S.degree(q12,lam) == 12
    assert S.simplify(cp - lam**44*p8*q12) == 0
    p1 = lam**8-8*lam**7+11*lam**6-11*lam**5+29*lam**4-7*lam**3-24*lam**2+lam+3
    q1 = lam**12+4*lam**10+lam**9+13*lam**8-9*lam**7+6*lam**6+17*lam**5+15*lam**4-2*lam**3+4*lam**2+lam+1
    pz = -12*lam**7+22*lam**6-46*lam**5+165*lam**4-14*lam**3-208*lam**2+6*lam+36
    assert S.expand(p8.subs(z,1)-p1) == 0
    assert S.expand(q12.subs(z,1)-q1) == 0
    assert S.expand(S.diff(p8,z).subs(z,1)-pz)==0
    # Independent physical local-rule enumeration vs weighted transfer walks.
    for n,total in [(4,1738),(5,11303),(6,72790)]:
        physical=direct_histogram(n)
        transfer=transfer_histogram(n)
        assert physical == transfer, (n,physical,transfer)
        assert sum(physical.values()) == total
        print('physical-vs-transfer',n,total,len(physical),'occupation classes')
    roots = S.nroots(p1,n=30,maxsteps=300)
    R=max(float(S.re(x)) for x in roots if abs(float(S.im(x)))<1e-15)
    rho = float((-pz/S.diff(p1,lam)).subs(lam,R))/(3*R)
    assert isclose(R,6.45917521976858,rel_tol=1e-12)
    assert isclose(rho,.6089266973105203,rel_tol=1e-12)
    print('Perron root',R,'entropy per site',log(R)/3,'occupation fraction',rho)
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
