#!/usr/bin/env python3
"""Independent finite-field linear algebra checks for quiver annihilator spectra."""
from itertools import product
from collections import Counter

def rank_mod(mat, p):
    a = [row[:] for row in mat]
    n, piv = len(a), 0
    for j in range(len(a[0]) if a else 0):
        lead = next((i for i in range(piv, n) if a[i][j] % p), None)
        if lead is None:
            continue
        a[piv], a[lead] = a[lead], a[piv]
        inv = pow(a[piv][j], -1, p)
        a[piv] = [inv * x % p for x in a[piv]]
        for i in range(n):
            if i != piv:
                factor = a[i][j]
                if factor:
                    a[i] = [(x - factor * y) % p for x, y in zip(a[i], a[piv])]
        piv += 1
    return piv

def direct_spectrum(vertices, arrows, p):
    dim = vertices + len(arrows)
    spectrum = Counter()
    for a in product(range(p), repeat=dim):
        mat = [[0] * dim for _ in range(dim)]
        for i in range(vertices):
            mat[i][i] = a[i]
            for e, (u, v) in enumerate(arrows):
                if v == i:
                    mat[vertices + e][i] = a[vertices + e]
        for e, (u, v) in enumerate(arrows):
            mat[vertices + e][vertices + e] = a[u]
        spectrum[dim - rank_mod(mat, p)] += 1
    return spectrum

def predicted_spectrum(vertices, arrows, q):
    m = len(arrows)
    out = Counter()
    for bits in range(1 << vertices):
        S = {i for i in range(vertices) if bits >> i & 1}
        out_S = sum(u in S for u, v in arrows)
        base = Counter({out_S: (q-1)**(vertices-len(S)) * q**(m-out_S)})
        for j in range(vertices):
            d = sum(u in S and v == j for u, v in arrows)
            if j in S:
                nxt = Counter()
                for k, z in base.items():
                    nxt[k] += z * (q**d - 1)
                    nxt[k + 1] += z
                base = nxt
            else:
                base = Counter({k: z * q**d for k,z in base.items()})
        out.update({})
        for k, z in base.items():
            out[k] += z
    return out

def height_two_pair_count(lower, upper, arrows, q):
    # Independent vertex-subset expression, valid for all q as a polynomial.
    vertices = lower + upper
    total = 0
    for bits in range(1 << vertices):
        z = bits.bit_count()
        induced = sum(bool(bits >> i & 1) and bool(bits >> (lower+j) & 1)
                      for i,j in arrows)
        total += q**(z+induced)*(q-1)**(vertices-z)
    return q**len(arrows)*total

def main():
    cases = [
       ('edgeless', 2, []),
       ('one_arrow', 2, [(0,1)]),
       ('one_loop', 1, [(0,0)]),
       ('two_loops', 1, [(0,0),(0,0)]),
       ('parallel', 2, [(0,1),(0,1)]),
       ('two_cycle', 2, [(0,1),(1,0)]),
       ('line', 3, [(0,1),(1,2)]),
       ('inward_fork', 3, [(0,2),(1,2)]),
       ('outward_fork', 3, [(0,1),(0,2)]),
       ('oriented_triangle', 3, [(0,1),(1,2),(0,2)]),
       ('star_lower', 4, [(0,1),(0,2),(0,3)]),
       ('star_upper', 4, [(1,0),(2,0),(3,0)]),
       ('four_path', 4, [(0,2),(1,2),(1,3)]),
       ('four_cycle', 4, [(0,2),(0,3),(1,2),(1,3)]),
    ]
    checks, elements = 0, 0
    for p in (2,3,5):
        for name, vertices, arrows in cases:
            dim = vertices+len(arrows)
            if p**dim > 7000:
                continue
            actual = direct_spectrum(vertices, arrows, p)
            expected = predicted_spectrum(vertices, arrows, p)
            assert actual == expected, (name,p,actual,expected)
            assert sum(actual.values()) == p**dim
            checks += 1; elements += p**dim
            print('PASS',name,'q=',p,'elements=',p**dim)
    for p in (2,3,5):
        for name,lower,upper,edges in [
            ('star_lower',1,3,[(0,0),(0,1),(0,2)]),
            ('star_upper',3,1,[(0,0),(1,0),(2,0)]),
            ('path4',2,2,[(0,0),(1,0),(1,1)]),
        ]:
            Q = [(i,lower+j) for i,j in edges]
            ann = predicted_spectrum(lower+upper,Q,p)
            zeros = sum(cnt*p**d for d,cnt in ann.items())
            assert zeros == height_two_pair_count(lower,upper,edges,p)
    a = predicted_spectrum(4,[(0,1),(0,2),(0,3)],2)
    b = predicted_spectrum(4,[(1,0),(2,0),(3,0)],2)
    c = predicted_spectrum(4,[(0,2),(1,2),(1,3)],2)
    assert a != b
    assert sum(c0 * 2**k for k,c0 in a.items()) == sum(c0 * 2**k for k,c0 in b.items()) == 2216
    assert sum(c0 * 2**k for k,c0 in c.items()) == 2152
    # A degree-at-most-ten difference polynomial is determined by 11 values.
    for x in range(11):
        left = height_two_pair_count(1,3,[(0,0),(0,1),(0,2)],x)
        path = height_two_pair_count(2,2,[(0,0),(1,0),(1,1)],x)
        assert left-path == x**6*(x-1)**3
    print('STAR_LOWER_q2',sorted(a.items()))
    print('STAR_UPPER_q2',sorted(b.items()))
    print('PATH4_q2',sorted(c.items()))
    print('STAR_VS_PATH_POLYNOMIAL_IDENTITY_CHECKED')
    print('ALL_QUIVER_ANNIHILATOR_CHECKS_PASSED',checks,elements)

if __name__ == '__main__':
    main()
