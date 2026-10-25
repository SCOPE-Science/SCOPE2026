#!/usr/bin/env python3
"""Exact calculations for Ehrhart positivity of lattice polygon joins.

Uses only Python's standard library; finite range is bounded by normalized
volume 168 and not inferred from a numerical sample.
"""
from fractions import Fraction as F
from math import comb, factorial


def add(p, q):
    return [(p[k] if k < len(p) else 0) + (q[k] if k < len(q) else 0)
            for k in range(max(len(p), len(q)))]


def multiply(p, q):
    z = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            z[i+j] += a*b
    return z


def via_h_star(a, b, c, d):
    h = multiply([1, a, b], [1, c, d])
    total = [F(0)] * 6
    for j, hj in enumerate(h):
        fac = [F(1)]
        for u in range(1, 6):
            fac = multiply(fac, [F(u-j), F(1)])
        total = add(total, [F(hj)*co/factorial(5) for co in fac])
    return total


def via_convolution(a, b, c, d):
    # Pick coefficients recover polygon Ehrhart counts independently.
    B, C = a-b+3, c-d+3
    v, w = a+b+1, c+d+1
    def L(k, vol, boundary):
        return F(vol*k*k + boundary*k, 2) + 1
    y = [sum((L(k,v,B)*L(t-k,w,C) for k in range(t+1)), F(0))
         for t in range(6)]
    ans = [F(0)] * 6
    diffs = y
    for j in range(6):
        base = [F(1)]
        for u in range(j):
            base = multiply(base, [F(-u), F(1)])
        ans = add(ans, [diffs[0]*z/factorial(j) for z in base])
        diffs = [diffs[i+1]-diffs[i] for i in range(len(diffs)-1)]
        if not diffs:
            break
    return ans


def sign_numerators(a,b,c,d):
    U = 137+12*(a+c)-3*a*c+2*a*d+2*b*c-3*b*d-3*b-3*d
    V = 45+10*(a+c)-a*c+b*d-b-d
    return U, V


def parameter_states(bound):
    # All polygon Ehrhart-data are in this conservative finite superset:
    # normalized area N >=1, interior b >=0, and boundary B >=3,
    # so a=N-1-b and a>=b. Symmetry lets us require N<=M.
    for N in range(1, bound+1):
        for M in range(N, bound//N + 1):
            for b in range((N+1)//2):
                a=N-1-b
                for d in range((M+1)//2):
                    c=M-1-d
                    yield N, M, a, b, c, d


def main():
    # Algebraic derivation cross-checked by two different exact methods.
    samples = [(0,0,0,0), (11,0,13,0), (11,0,78,78),
               (2,1,1,1), (17,9,27,13), (42,0,3,1)]
    for a,b,c,d in samples:
        assert a>=b>=0 and c>=d>=0
        p=via_h_star(a,b,c,d)
        assert p==via_convolution(a,b,c,d), (a,b,c,d,p)
        U,V=sign_numerators(a,b,c,d)
        assert p[1]==F(U,60) and p[2]==F(V,24)
        assert p[3]==F((a-b)*(c-d)+7*(a+c)+b+d+17,24)
        assert p[4]==F(a*c-b*d+2*(a+c)+b+d+3,24)
        assert p[5]==F((a+b+1)*(c+d+1),120)
        assert p[0]==1
    checked=0
    min_U=(10**20,None)
    min_V=(10**20,None)
    for N,M,a,b,c,d in parameter_states(167):
        U,V=sign_numerators(a,b,c,d)
        checked+=1
        if U<min_U[0]: min_U=(U,(N,M,b,d))
        if V<min_V[0]: min_V=(V,(N,M,b,d))
        assert U>0 and V>0, (N,M,a,b,c,d,U,V)
    assert checked==14438,(checked,)
    assert min_U==(5,(11,15,0,0)), min_U
    assert min_V==(45,(1,1,0,0)), min_V
    bad=[]
    checked168=0
    for N,M,a,b,c,d in parameter_states(168):
        checked168+=1
        U,V=sign_numerators(a,b,c,d)
        if U<=0 or V<=0:
            bad.append((N,M,b,d,U,V))
    assert checked168==14838
    assert bad==[(12,14,0,0,-4,142)],bad
    # Realized by triangles (0,0),(12,0),(0,1) and (0,0),(14,0),(0,1).
    U,V=sign_numerators(11,0,13,0)
    assert (U,V)==(-4,142)
    assert via_h_star(11,0,13,0)[1]==F(-1,15)
    assert via_h_star(11,0,13,0)[2]==F(71,12)
    # Distinct quadratic-only sign pattern, realizable by a primitive-edge
    # 157-normalized-area triangle with (B,I)=(3,78).
    U,V=sign_numerators(11,0,78,78)
    assert (U,V)==(113,-1)
    pp=via_h_star(11,0,78,78)
    assert pp[1]==F(113,60) and pp[2]==F(-1,24)
    assert all(co>0 for j,co in enumerate(pp) if j not in (2,))
    print(f'EXACT_OK below_168_states={checked} min_U={min_U[0]} '
          f'min_V={min_V[0]} upto_168_states={checked168} '
          f'unique_bad={bad[0]} coeff_linear=-1/15 '
          f'quadratic_only=-1/24 independent_convolutions={len(samples)}')


if __name__ == '__main__':
    main()
