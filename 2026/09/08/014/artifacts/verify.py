#!/usr/bin/env python3
"""Lane-126: Fox-calculus cup + triple-Massey certificate for a balanced
presentation 2-complex K = <x,y,z | r1,r2,r3>. Stdlib only.
Replays: homology, cup vanishing, Massey defining system, indeterminacy
non-membership, full 8-triple table, controls. Writes results.json."""
import json, itertools

def W(s):
    out = []
    for tok in s.split():
        g = 'xyz'.index(tok.lower())
        out.append((g, -1 if tok.isupper() else +1))
    return out

def expvec(w):
    e = [0, 0, 0]
    for g, s in w:
        e[g] += s
    return e

def fox2(w):
    """A[i][j] = eps(d^2 w / dxi dxj). Cross-checked against independent
    recursion (prefix-product update); both agree on all words used."""
    a = [[0]*3 for _ in range(3)]
    for j in range(3):
        run = [0, 0, 0]
        for (g, s) in w:
            if g == j and s == +1:
                for i in range(3):
                    a[i][j] += run[i]
            if g == j and s == -1:
                run[g] += s
                for i in range(3):
                    a[i][j] -= run[i]
                continue
            run[g] += s
    return a

def fox2b(word):
    n = 3
    S = [[0]*n for _ in range(n)]
    e = [0]*n
    for (g, s) in word:
        f = [0]*n
        f[g] = s
        Sl = [[0]*n for _ in range(n)]
        if s == -1:
            Sl[g][g] = 1
        for i in range(n):
            for j in range(n):
                S[i][j] += e[i]*f[j] + Sl[i][j]
        for i in range(n):
            e[i] += f[i]
    return S

def snf_diag(A):
    M = [row[:] for row in A]
    m = len(M)
    n = len(M[0]) if m else 0
    k = 0
    guard = 0
    while k < min(m, n) and guard < 500:
        guard += 1
        piv = None
        for i in range(k, m):
            for j in range(k, n):
                if M[i][j] != 0 and (piv is None or abs(M[i][j]) < abs(M[piv[0]][piv[1]])):
                    piv = (i, j)
        if piv is None:
            break
        i, j = piv
        M[k], M[i] = M[i], M[k]
        for r in range(m):
            M[r][k], M[r][j] = M[r][j], M[r][k]
        changed = True
        inner = 0
        while changed and inner < 200:
            inner += 1
            changed = False
            for i in range(k+1, m):
                if M[i][k] != 0:
                    if M[k][k] == 0:
                        M[k], M[i] = M[i], M[k]
                        changed = True
                        continue
                    q = M[i][k] // M[k][k]
                    for t in range(n):
                        M[i][t] -= q*M[k][t]
                    if M[i][k] != 0:
                        M[k], M[i] = M[i], M[k]
                        changed = True
            for j in range(k+1, n):
                if M[k][j] != 0:
                    if M[k][k] == 0:
                        for r in range(m):
                            M[r][k], M[r][j] = M[r][j], M[r][k]
                        changed = True
                        continue
                    q = M[k][j] // M[k][k]
                    for t in range(m):
                        M[t][j] -= q*M[t][k]
                    if M[k][j] != 0:
                        for r in range(m):
                            M[r][k], M[r][j] = M[r][j], M[r][k]
                        changed = True
        bad = [(i, j) for i in range(k, m) for j in range(k, n)
               if M[i][j] != 0 and (M[k][k] == 0 or M[i][j] % M[k][k] != 0)]
        if bad:
            i, j = bad[0]
            for t in range(n):
                M[k][t] += M[i][t]
            continue
        k += 1
    return [abs(M[i][i]) if i < m and i < n else 0 for i in range(min(m, n))]

def solve_int_system(cols, rhs):
    """Integer linear solve sum_k t_k cols[k] = rhs. Exact: rational
    particular solution + nullspace search over bounded box (exact check).
    Returns one solution or None (None => provably outside lattice: rational
    inconsistency; box radius 40*den is exhaustive for our tiny systems since
    any integer solution differs from the particular one by ker elements and
    the check below verifies membership exactly -- failure means no small
    solution, and for the certificates we only assert None where a coordinate
    projection already proves non-membership, plus rational inconsistency)."""
    from fractions import Fraction
    n = len(rhs)
    k = len(cols)
    if k == 0:
        return [] if all(v == 0 for v in rhs) else None
    A = [[Fraction(cols[c][r]) for c in range(k)] for r in range(n)]
    b = [Fraction(v) for v in rhs]
    where = [-1]*k
    row = 0
    for c in range(k):
        sel = next((r for r in range(row, n) if A[r][c] != 0), None)
        if sel is None:
            continue
        A[row], A[sel] = A[sel], A[row]
        b[row], b[sel] = b[sel], b[row]
        where[c] = row
        for r in range(n):
            if r != row and A[r][c] != 0:
                f = A[r][c]/A[row][c]
                for t in range(c, k):
                    A[r][t] -= f*A[row][t]
                b[r] -= f*b[row]
        row += 1
    for r in range(n):
        if all(A[r][c] == 0 for c in range(k)) and b[r] != 0:
            return None
    t = [Fraction(0)]*k
    for c in range(k):
        if where[c] >= 0:
            t[c] = b[where[c]]/A[where[c]][c]
    free = [c for c in range(k) if where[c] < 0]
    ns = []
    for f in free:
        v = [Fraction(0)]*k
        v[f] = Fraction(1)
        for c in range(k):
            if where[c] >= 0:
                v[c] = -A[where[c]][f]/A[where[c]][c]
        ns.append(v)
    import math
    den = 1
    for v in [t]+ns:
        for x in v:
            den = den*x.denominator//math.gcd(den, x.denominator)
    if not ns:
        iv = [int(x) if x.denominator == 1 else None for x in t]
        if all(v is not None for v in iv) and \
           all(sum(iv[c]*cols[c][r] for c in range(k)) == rhs[r] for r in range(n)):
            return iv
        return None
    R = 40*den + 20
    for coef in itertools.product(range(-R, R+1), repeat=len(ns)):
        sol = [t[c]+sum(coef[q]*ns[q][c] for q in range(len(ns))) for c in range(k)]
        if all(x.denominator == 1 for x in sol):
            iv = [int(x) for x in sol]
            if all(sum(iv[c]*cols[c][r] for c in range(k)) == rhs[r] for r in range(n)):
                return iv
    return None

def cupval(u, v, A):
    return sum(u[i]*v[j]*A[i][j] for i in range(3) for j in range(3))

def main():
    r1 = W('x x y z Y Z y z Y Z')   # x^2 [y,z]^2, length 10
    r2 = W('x z X Z')               # [x,z], length 4
    r3 = W('x y X Y z y x Y X Z')   # [[x,y],z], length 10
    rels = [r1, r2, r3]
    E = [expvec(r) for r in rels]
    A = [fox2(r) for r in rels]
    for r in rels:
        assert fox2(r) == fox2b(r), 'Fox cross-check failed'
    assert E == [[2, 0, 0], [0, 0, 0], [0, 0, 0]], E
    Bcols = [[E[r][i] for r in range(3)] for i in range(3)]  # B^2 gens
    snf = snf_diag([row[:] for row in E])
    assert snf == [2, 0, 0], snf

    X, Y, Z = [1, 0, 0], [0, 1, 0], [0, 0, 1]
    cc = lambda u, v: [cupval(u, v, a) for a in A]
    cups = {}
    # canonical exact bounds: YZ = +2e1, ZY = -2e1, YY = ZZ = 0 (exact, no search noise)
    canon = {'YY': [0, 0, 0], 'YZ': [1, 0, 0], 'ZY': [-1, 0, 0], 'ZZ': [0, 0, 0]}
    for nm, u, v in [('YY', Y, Y), ('YZ', Y, Z), ('ZY', Z, Y), ('ZZ', Z, Z)]:
        c = cc(u, v)
        cups[nm] = {'cochain': c, 'bound': canon[nm], 'vanishes': True}
        assert [sum(E[r][i]*canon[nm][i] for i in range(3)) for r in range(3)] == c, (nm, c)
    assert all(v['vanishes'] for v in cups.values())
    assert cups['YZ']['cochain'] == [2, 0, 0]
    assert cups['ZY']['cochain'] == [-2, 0, 0]
    assert cups['YY']['cochain'] == [0, 0, 0]
    assert cups['ZZ']['cochain'] == [0, 0, 0]
    # graded-commutativity consistency at cochain level
    for u, v in [(Y, Z), (X, Y), (X, Z), (X, X)]:
        assert solve_int_system(Bcols, [a+b for a, b in zip(cc(u, v), cc(v, u))]) is not None

    # Massey <Y,Z,Z> with CANONICAL bounds (exact): s=(1,0,0), t=(0,0,0)
    s = [1, 0, 0]
    t = [0, 0, 0]
    assert s is not None and t is not None
    m = [a-b for a, b in zip(cc(s, Z), cc(Y, t))]
    assert m == [0, 1, 0], m
    Icols = Bcols + [cc(Y, h) for h in (Y, Z)] + [cc(h, Z) for h in (Y, Z)]
    assert solve_int_system(Icols, m) is None
    assert all(g[1] == 0 for g in Icols) and m[1] == 1  # coord-1 projection proof
    # bounding-choice robustness
    s2 = [s[0], s[1]+3, s[2]-2]
    assert [sum(E[r][i]*s2[i] for i in range(3)) for r in range(3)] == cups['YZ']['cochain']
    m2 = [a-b for a, b in zip(cc(s2, Z), cc(Y, t))]
    assert solve_int_system(Icols, [a-b for a, b in zip(m2, m)]) is not None

    # full 8-triple table with CANONICAL bounds (exact, search-noise-free)
    D = {'Y': Y, 'Z': Z}
    CB = {('Y', 'Y'): [0, 0, 0], ('Y', 'Z'): [1, 0, 0],
          ('Z', 'Y'): [-1, 0, 0], ('Z', 'Z'): [0, 0, 0]}
    tab = {}
    for abc in itertools.product('YZ', repeat=3):
        a, b, c = (D[ch] for ch in abc)
        co_ab, co_bc = cc(a, b), cc(b, c)
        assert [sum(E[r][i]*CB[(abc[0], abc[1])][i] for i in range(3))
                for r in range(3)] == co_ab
        assert [sum(E[r][i]*CB[(abc[1], abc[2])][i] for i in range(3))
                for r in range(3)] == co_bc
        sb, tb = CB[(abc[0], abc[1])], CB[(abc[1], abc[2])]
        key = ''.join(abc)
        if sb is None or tb is None:
            tab[key] = {'defined': False}
            continue
        mm = [x-y for x, y in zip(cc(sb, c), cc(a, tb))]
        I = Bcols + [cc(a, h) for h in (Y, Z)] + [cc(h, c) for h in (Y, Z)]
        tab[key] = {'defined': True, 'm': mm,
                    'zero_mod_indet': solve_int_system(I, mm) is not None}

    # controls: (i) [x,y] relator gives standard torus cup XY=+1, YX=-1
    At = fox2(W('x y X Y'))
    assert At == fox2b(W('x y X Y'))
    assert cupval(X, Y, At) == 1 and cupval(Y, X, At) == -1
    # (ii) all-commutator complex <x,y,z|[x,y],[y,z],[z,x]> has NONZERO cups
    Ac = [fox2(W(s)) for s in ['x y X Y', 'y z Y Z', 'z x Z X']]
    assert any(cupval(Y, Z, a) != 0 for a in Ac)

    res = {
        'presentation': ['x x y z Y Z y z Y Z', 'x z X Z',
                         'x y X Y z y x Y X Z'],
        'lengths': [10, 4, 10], 'E': E, 'snf_E': snf,
        'Fox2': A,
        'homology': {'H1': 'Z/2 x Z^2', 'H2': 'Z^2',
                     'H1cohom': 'Z^2 = span(Y,Z)', 'H2cohom': 'Z/2 x Z^2'},
        'cups': cups,
        'massey_YZZ': {'s': s, 't': t, 'm': m, 'indet_gens': Icols},
        'massey_table': tab,
        'controls': {'torus_XY': 1, 'torus_YX': -1,
                     'all_commutator_cups_nonzero': True},
    }
    with open('results.json', 'w') as f:
        json.dump(res, f, indent=2)
    print('E =', E, 'snf =', snf)
    print('cups =', json.dumps(cups))
    print('m(YZZ) =', m, '; non-membership certified by coord-1 projection')
    print('table =', json.dumps(tab))
    print('controls OK; wrote results.json')

main()
