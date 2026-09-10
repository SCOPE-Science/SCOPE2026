"""Generators for Gog / Magog triangles (Biane-Cheballah 1401.6516, Secs 2-4).
Encoding: X[i][j], i=0..n-1 (row i has i+1 entries), values positive ints.
GT interlacing: X[i][j] in [X[i+1][j], X[i+1][j+1]] (below row bounds above row).
  This forces every row weakly increasing by induction (bottom row constrained
  explicitly to be weakly increasing for Magog).
Gog: bottom row fixed 1..n; all rows strictly increasing.
Magog: bottom row weakly increasing in 1..n; diagonal caps X[j][j]<=j+1 (1-idx).
Audit: counts must equal ASM numbers 1,2,7,42,429,7436 (MRR/Zeilberger).
"""
import sys

def gen_gog(n):
    X = [None]*n
    X[n-1] = list(range(1, n+1))
    out = []
    def rec(i):
        if i < 0:
            out.append([list(r) for r in X]); return
        below = X[i+1]
        cur = [0]*(i+1)
        def inner(j, lo):
            if j > i:
                X[i] = list(cur); rec(i-1); X[i] = None; return
            for v in range(max(below[j], lo), below[j+1]+1):
                cur[j] = v; inner(j+1, v+1)
        inner(0, 1)
    rec(n-2)
    return out

def gen_magog(n):
    out = []
    X = [None]*n
    def rec(i):
        if i < 0:
            out.append([list(r) for r in X]); return
        if i == n-1:
            # bottom row: weakly increasing, values 1..n
            cur = [0]*n
            def binner(j, lo):
                if j > n-1:
                    X[i] = list(cur); rec(i-1); X[i] = None; return
                for v in range(lo, n+1):
                    cur[j] = v; binner(j+1, v)
            binner(0, 1)
        else:
            below = X[i+1]
            cap = i+1  # X[i][i] <= i+1 (1-indexed j=i+1 -> cap i+1)
            cur = [0]*(i+1)
            def inner(j, lo):
                if j > i:
                    if cur[i] > cap: return
                    X[i] = list(cur); rec(i-1); X[i] = None; return
                for v in range(max(below[j], lo), below[j+1]+1):
                    cur[j] = v; inner(j+1, v)
            inner(0, 1)
    rec(n-1)
    return out

def is_gog(X):
    n = len(X)
    if X[n-1] != list(range(1, n+1)): return False
    for i in range(n):
        if len(X[i]) != i+1: return False
        for j in range(i):
            if not (X[i][j] < X[i][j+1]): return False
        if i < n-1:
            for j in range(i+1):
                if not (X[i+1][j] <= X[i][j] <= X[i+1][j+1]): return False
    return True

def is_magog(X):
    n = len(X)
    for i in range(n):
        if len(X[i]) != i+1: return False
        for j in range(i):
            if not (X[i][j] <= X[i][j+1]): return False
        if X[i][i] > i+1: return False
        if i < n-1:
            for j in range(i+1):
                if not (X[i+1][j] <= X[i][j] <= X[i+1][j+1]): return False
    for v in X[n-1]:
        if not (1 <= v <= n): return False
    return True

if __name__ == "__main__":
    asm = {1:1,2:2,3:7,4:42,5:429,6:7436}
    N = int(sys.argv[1]) if len(sys.argv)>1 else 5
    which = sys.argv[2] if len(sys.argv)>2 else "both"
    if which in ("both","gog"):
        for n in range(1, N+1):
            g = gen_gog(n)
            ok = all(is_gog(t) for t in g)
            print(f"gog n={n}: {len(g)} (expect {asm[n]}) valid={ok}", flush=True)
    if which in ("both","magog"):
        for n in range(1, N+1):
            m = gen_magog(n)
            ok = all(is_magog(t) for t in m)
            print(f"magog n={n}: {len(m)} (expect {asm[n]}) valid={ok}", flush=True)
