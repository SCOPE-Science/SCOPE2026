"""Schutzenberger involution (Berenstein-Kirillov s_k) + GOGAm inequality (5.1).
Conventions: X[i][j], i=0..n-1, row i has i+1 entries. All 1-indexed paper
formulas converted. s_k acts on row k (1-idx), k<=n-1.
"""
from gen import gen_gog, gen_magog

def sk(X, k):
    """Apply s_k (1-indexed k, 1<=k<=n-1). Returns new triangle."""
    n = len(X)
    Y = [list(r) for r in X]
    r = k-1
    for j in range(k):  # j=0..k-1 <-> paper j=1..k
        jp = j+1
        below_lo = X[r+1][j]
        below_hi = X[r+1][j+1]
        if jp == 1:
            mx = below_lo
        else:
            mx = max(below_lo, X[r-1][j-1])
        if jp == k:
            mn = below_hi
        else:
            mn = min(below_hi, X[r-1][j])
        Y[r][j] = mx + mn - X[r][j]
    return Y

def schutzenberger(X):
    """S = w1 w2 ... w_{n-1}, w_j = s_j ... s_1 (operators compose right-to-left)."""
    n = len(X)
    Y = [list(r) for r in X]
    for j in range(n-1, 0, -1):
        for k in range(1, j+1):
            Y = sk(Y, k)
    return Y

def chains(n, k):
    """All chains n=j0>j1>...>j_{n-k}>=1 (1-indexed)."""
    from itertools import combinations
    out = []
    for combo in combinations(range(1, n), n-k):
        js = (n,) + tuple(sorted(combo, reverse=True))
        out.append(js)
    return out

def is_gogam(X):
    """Check inequality (5.1) for all k and chains, plus X[n][n]<=n."""
    n = len(X)
    if X[n-1][n-1] > n: return False
    for k in range(1, n):
        for js in chains(n, k):
            s = 0
            for i in range(n-k):
                s += X[js[i]+i-1][js[i]-1] - X[js[i+1]+i-1][js[i+1]-1]
            s += X[js[n-k]+n-k-1][js[n-k]-1]
            if s > k: return False
    return True

def left_trap(X, k):
    """Project to left (n,k) trapezoid: entries with 1-indexed j<=k."""
    return tuple(tuple(row[:min(len(row), k)]) for row in X)

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    # S involution check on Gog triangles
    g = gen_gog(n)
    ok_inv = all(schutzenberger(schutzenberger(t)) == t for t in g)
    print(f"n={n}: S involutive on {len(g)} Gog triangles: {ok_inv}", flush=True)
    # Magog -> GOGAm
    m = gen_magog(n)
    G = [schutzenberger(t) for t in m]
    ok_g = all(is_gogam(t) for t in G)
    print(f"n={n}: S(Magog) all satisfy (5.1): {ok_g} ({len(G)} triangles)", flush=True)
    ok_inv_m = all(schutzenberger(schutzenberger(t)) == t for t in m)
    print(f"n={n}: S involutive on Magog: {ok_inv_m}", flush=True)
    # left trapezoid census k=1,2,3
    for k in (1, 2, 3):
        pg = set(left_trap(t, k) for t in g)
        pm = set(left_trap(t, k) for t in G)
        print(f"n={n} k={k}: |Gleft|={len(pg)} |Mleft|={len(pm)} equal={len(pg)==len(pm)}", flush=True)
