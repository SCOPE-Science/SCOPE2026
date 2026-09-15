"""Reproducible verification for lane-20320 target (pure sympy).
Checks: critical point rho of PT (5.6), Newton simplex vertices,
normalized volume k^{k-1}(n+1), affine edge lengths, Markov exclusion.
"""
import sympy as sp
import itertools

def W_expr(n, k):
    xs = sp.symbols('x1:%d' % (n + 1))  # x1..xn
    xs = list(xs)
    P = sp.Integer(1)
    for x in xs:
        P *= x
    xk = xs[k - 1]
    Q = 1 + sum(xk / xs[i] for i in range(k - 1))
    rest = sum(1 / xs[i] for i in range(k - 1, n))
    return xs, rest + P * Q**k

def check_crit(n, k):
    xs, W = W_expr(n, k)
    rho = {xs[i]: sp.Rational(1, k) for i in range(k)}
    for i in range(k, n):
        rho[xs[i]] = sp.Integer(1)
    grads = [sp.simplify(g.subs(rho)) for g in [sp.diff(W, x) for x in xs]]
    assert all(g == 0 for g in grads), (n, k, grads)
    val = sp.simplify(W.subs(rho))
    assert val == n + 1, (n, k, val)
    print(f"crit n={n} k={k}: rho=(1/{k} x{k},1 x{n-k}) grad=0 value={val} OK")

def verts(n, k):
    C = tuple([1] * n)
    V = []
    for i in range(k - 1):
        v = [1] * n
        v[i] -= k
        v[k - 1] += k
        V.append(tuple(v))
    D = []
    for j in range(k - 1, n):
        d = [0] * n
        d[j] = -1
        D.append(tuple(d))
    return C, V, D

def det_vol(n, k):
    C, V, D = verts(n, k)
    pts = V + [C] + D
    assert len(pts) == n + 1
    M = sp.Matrix([[p[i] - pts[0][i] for p in pts[1:]] for i in range(n)])
    # edge matrix from V_0: columns V_i-V_0, C-V_0, D_j-V_0
    return abs(int(M.det()))

def gcd_len(a, b):
    import math
    d = 0
    for u, v in zip(a, b):
        d = math.gcd(d, u - v)
    return d

def check_poly(n, k):
    C, V, D = verts(n, k)
    S = V + [C] + D
    vol = det_vol(n, k)
    assert vol == k**(k - 1) * (n + 1), (n, k, vol)
    # long edges: C-V_i and V_i-V_j have length k
    for v in V:
        assert gcd_len(C, v) == k, (n, k, C, v)
    for a, b in itertools.combinations(V, 2):
        assert gcd_len(a, b) == k, (n, k, a, b)
    # all edges incident to D plus C-D have length 1
    for d in D:
        assert gcd_len(C, d) == 1, (n, k)
        for v in V:
            assert gcd_len(v, d) == 1, (n, k, v, d)
    for a, b in itertools.combinations(D, 2):
        assert gcd_len(a, b) == 1
    # count vertices incident to a long edge
    long_inc = sum(1 for p in S if any(gcd_len(p, q) > 1 for q in S if q != p))
    assert long_inc == k, (n, k, long_inc)
    print(f"poly n={n} k={k}: vol={vol}=k^(k-1)(n+1), long-inc={long_inc} OK")

def check_markov():
    assert 3**2 + 3**2 + 3**2 != 3 * 3 * 3 * 3, "sanity"
    print("(3,3,3) is NOT Markov: 27 != 81 OK")

if __name__ == "__main__":
    for n in range(3, 8):
        for k in range(3, n + 1):
            check_crit(n, k)
            check_poly(n, k)
    check_markov()
    print("ALL CHECKS PASSED")
