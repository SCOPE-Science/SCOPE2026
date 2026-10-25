#!/usr/bin/env python3
"""Independent finite-field enumeration of weight-zero Rota--Baxter operators.
No optional packages or network access are required.
"""
from itertools import product
from collections import Counter


def fmul(a, b, q):
    if q == 2:
        return a & b
    if q == 4:
        p = 0
        for i in range(2):
            for j in range(2):
                if (a >> i) & 1 and (b >> j) & 1:
                    p ^= 1 << (i + j)
        if p & 8:
            p ^= 0b1110
        if p & 4:
            p ^= 0b111
        return p
    raise ValueError('Only q=2,4')


def prod(x, y, q):
    return (fmul(x[0], y[0], q),) + tuple(
        fmul(x[0], y[i], q) ^ fmul(y[0], x[i], q)
        for i in range(1, len(x)))


def act(cols, x, q):
    n = len(x)
    z = [0] * n
    for j, a in enumerate(x):
        if a:
            for i in range(n):
                z[i] ^= fmul(a, cols[j][i], q)
    return tuple(z)


def is_rb(cols, q):
    n = len(cols)
    images = cols
    for i in range(n):
        bi = tuple(int(k == i) for k in range(n))
        for j in range(i, n):
            bj = tuple(int(k == j) for k in range(n))
            rhs_arg1 = prod(images[i], bj, q)
            rhs_arg2 = prod(bi, images[j], q)
            rhs_arg = tuple(x ^ y for x, y in zip(rhs_arg1, rhs_arg2))
            if prod(images[i], images[j], q) != act(cols, rhs_arg, q):
                return False
    return True


def rank(matrix, q):
    a = [list(row) for row in matrix]
    rows, columns = len(a), len(a[0]) if a else 0
    p = 0
    for j in range(columns):
        k = next((k for k in range(p, rows) if a[k][j]), None)
        if k is None:
            continue
        a[p], a[k] = a[k], a[p]
        inverse = next(v for v in range(1, q) if fmul(v, a[p][j], q) == 1)
        a[p] = [fmul(inverse, x, q) for x in a[p]]
        for k in range(rows):
            if k != p and a[k][j]:
                c = a[k][j]
                a[k] = [x ^ fmul(c, y, q) for x, y in zip(a[k], a[p])]
        p += 1
        if p == rows:
            break
    return p


def gl_order(q, t):
    z = 1
    for j in range(t):
        z *= q**t - q**j
    return z


def gaussian(q, n, k):
    if k < 0 or k > n:
        return 0
    top, bottom = 1, 1
    for i in range(k):
        top *= q**(n-i) - 1
        bottom *= q**(k-i) - 1
    return top // bottom


def predicted(q, r, t):
    return gaussian(q, r, t)*gaussian(q, r-t, t)*gl_order(q, t)


def exhaustive(q, r):
    n = r + 1
    counts = Counter()
    count_rb = 0
    checked = 0
    for flat in product(range(q), repeat=n*n):
        cols = tuple(tuple(flat[j*n+i] for i in range(n)) for j in range(n))
        expected = all(col[0] == 0 for col in cols)
        if expected:
            T = tuple(tuple(cols[j+1][i+1] for j in range(r)) for i in range(r))
            for i in range(r):
                for j in range(r):
                    s = 0
                    for h in range(r):
                        s ^= fmul(T[i][h], T[h][j], q)
                    if s:
                        expected = False
                        break
                if not expected:
                    break
        actual = is_rb(cols, q)
        assert expected == actual, ('RB classification mismatch', q, r, cols, expected, actual)
        if actual:
            t = rank(T, q)
            u = tuple(cols[0][i+1] for i in range(r))
            v = []
            for i in range(r):
                s = 0
                for j in range(r):
                    s ^= fmul(T[i][j], u[j], q)
                v.append(s)
            index3 = any(v)
            counts[(t, index3)] += 1
            count_rb += 1
        checked += 1
    total_expected = 0
    for t in range(r//2+1):
        m = predicted(q,r,t)
        expected_three = m*(q**r - q**(r-t))
        expected_short = m*q**(r-t)
        assert counts[(t,True)] == expected_three,(q,r,t,'index3',counts[(t,True)],expected_three)
        assert counts[(t,False)] == expected_short,(q,r,t,'index≤2',counts[(t,False)],expected_short)
        total_expected += m*q**r
    assert count_rb == total_expected
    print('PASS', 'q=',q, 'radical_dimension=',r,'all_linear_maps=',checked,'RB_ops=',count_rb,'rank_index_counts=',dict(counts),flush=True)
    return checked


def orbit_test(q,r):
    n=r+1
    operators = []
    for flat in product(range(q), repeat=n*n):
        cols = tuple(tuple(flat[j*n+i] for i in range(n)) for j in range(n))
        if is_rb(cols,q):
            operators.append(cols)
    gls=[]
    for flat in product(range(q),repeat=r*r):
        rows=tuple(tuple(flat[i*r+j] for j in range(r)) for i in range(r))
        if rank(rows,q)==r:
            gls.append(rows)
    def apply_g(g,v):
        return tuple((sum(g[i][j]*v[j] for j in range(r))%2) for i in range(r))
    def transformed(cols,g):
        # Apply conjugation R' = G R G^-1 through its graph: R'(1)=G R(1);
        # matrix T' determined by T'(G b_j)=G T b_j.
        u=tuple(cols[0][i+1] for i in range(r))
        tcols=[tuple(cols[j+1][i+1] for i in range(r)) for j in range(r)]
        # Direct conjugation in binary, via inverse G using linear solver by searching domain.
        tprime=[]
        for j in range(r):
            basis=tuple(int(i==j) for i in range(r))
            inv_basis=next(v for v in product(range(2),repeat=r) if apply_g(g,v)==basis)
            y=[0]*r
            for h in range(r):
                if inv_basis[h]:
                    y=[a^b for a,b in zip(y,tcols[h])]
            tprime.append(apply_g(g,tuple(y)))
        uprime=apply_g(g,u)
        return (tuple([0]+list(uprime)),)+tuple(tuple([0]+list(col)) for col in tprime)
    seen=set()
    orbits=[]
    for op in operators:
        if op in seen:
            continue
        this={transformed(op,g) for g in gls}
        seen.update(this)
        T=tuple(tuple(op[j+1][i+1] for j in range(r)) for i in range(r))
        t=rank(T,q)
        u=tuple(op[0][i+1] for i in range(r))
        if not any(u): cat='zero'
        else:
            columns=[tuple(op[j+1][i+1] for i in range(r)) for j in range(r)]
            image={tuple((sum(x[j]*columns[j][i] for j in range(r))%2) for i in range(r)) for x in product(range(2),repeat=r)}
            Tu=tuple((sum(T[i][j]*u[j] for j in range(r))%2) for i in range(r))
            cat=('image' if u in image else ('kernel_outside_image' if not any(Tu) else 'outside_kernel'))
        orbits.append((t,cat,len(this)))
    expected_classes=2 if r==1 else (2*r + (r%2==0))
    assert len(orbits)==expected_classes, (r,orbits,expected_classes)
    assert len(seen)==len(operators)
    print('PASS_GL_ORBITS',q,r,len(orbits),sorted(orbits),flush=True)


def main():
    total=0
    for q,r in [(2,1),(2,2),(2,3),(4,1),(4,2)]:
        total+=exhaustive(q,r)
    for r in [1,2,3]:
        orbit_test(2,r)
    print('ALL_SQUARE_ZERO_RB_CHECKS_PASSED',total,flush=True)

if __name__ == '__main__':
    main()
