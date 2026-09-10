"""Jones polynomial via Temperley-Lieb (clean implementation).
rho(s_i) = A*I + A^{-1}*E_i over R=Z[A,A^{-1},delta]/(delta+A^2+A^{-2}).
E_i as matchings; composition counted with loop exponents; substitute delta at end.
Markov trace via closure caps; writhe normalization; validate trefoil/fig8/unknot.
"""
import sympy as sp

A = sp.Symbol('A')
t = sp.Symbol('t')

def all_matchings(n):
    # Rectangular geometry: cyclic order around the box is
    # top L->R: 0..n-1, then bottom R->L: 2n-1..n. Crossing tests use this order.
    cyc = list(range(n)) + list(range(2 * n - 1, n - 1, -1))
    pos = {p: k for k, p in enumerate(cyc)}
    pts = list(range(2 * n))
    out = []
    def rec(remaining, pairs):
        if not remaining:
            out.append(frozenset(pairs))
            return
        a = remaining[0]
        for j in range(1, len(remaining)):
            b = remaining[j]
            # chord (a,b): #points strictly between along cycle must be even
            ia, ib = pos[a], pos[b]
            if ia > ib:
                ia, ib = ib, ia
            inside = ib - ia - 1
            if inside % 2 == 1:
                continue
            ok = True
            for (c, d) in pairs:
                def between(x, y, z):
                    px, py, pz = pos[x], pos[y], pos[z]
                    if px < pz:
                        return px < py < pz
                    return py > px or py < pz
                if (between(a, c, b) != between(a, d, b)) and (between(c, a, d) != between(c, b, d)):
                    ok = False
                    break
            if not ok:
                continue
            rest = [x for k, x in enumerate(remaining) if k != 0 and k != j]
            rec(rest, pairs + [(a, b)])
    rec(pts, [])
    # double-check count = Catalan(n)
    from math import comb
    assert len(out) == comb(2 * n, n) // (n + 1), (n, len(out))
    return out

def compose(n, X, Y):
    """Stack X on top of Y. Returns (loops, Z) as matchings on 2n points."""
    N = 3 * n
    parent = list(range(N))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[a] = b
    TOP = list(range(n)); MID = list(range(n, 2 * n)); BOT = list(range(2 * n, 3 * n))
    for (a, b) in X:
        U = TOP[a] if a < n else MID[a - n]
        V = TOP[b] if b < n else MID[b - n]
        union(U, V)
    for (a, b) in Y:
        U = MID[a] if a < n else BOT[a - n]
        V = MID[b] if b < n else BOT[b - n]
        union(U, V)
    comps = {}
    for v in range(N):
        comps.setdefault(find(v), []).append(v)
    loops = 0
    pairs = []
    for vs in comps.values():
        ext = [v for v in vs if v < n or v >= 2 * n]
        if not ext:
            loops += 1
        else:
            assert len(ext) == 2
            a, b = ext
            ia = a if a < n else n + (a - 2 * n)
            ib = b if b < n else n + (b - 2 * n)
            pairs.append((ia, ib))
    return loops, frozenset(pairs)

def tl_E(n, i):
    a, b = i - 1, i
    E = {(a, b), (n + a, n + b)}
    for j in range(n):
        if j != a and j != b:
            E.add((j, n + j))
    return frozenset(E)

def op_compose_table(n, basis, idx, X):
    """Table for left multiplication by fixed diagram X: col m -> (loops, row)."""
    tab = []
    for m in basis:
        lp, z = compose(n, X, m)
        tab.append((lp, idx[z]))
    return tab

def braid_matrix(n, basis, idx, word):
    """Matrix of rho(word) as dict-of-dict {(r,c): (poly in delta as dict exp->coefclass, A-poly sympy)}.
    Simpler: entries are sympy expressions in A and D (delta symbol); substitute D at end."""
    D = sp.Symbol('D')
    d = len(basis)
    M = [[(sp.Integer(1) if r == c else sp.Integer(0)) for c in range(d)] for r in range(d)]
    tables = {}
    for i in range(1, n):
        tables[i] = op_compose_table(n, basis, idx, tl_E(n, i))
    for i in word:
        if i < 0:
            raise NotImplementedError("inverses not needed (positive braid)")
        tab = tables[i]
        # R = A*I + A^{-1}*E ; E_{rc} = D^{lp} if tab[c]=(lp,r) else 0
        N = [[sp.Integer(0)] * d for _ in range(d)]
        for c in range(d):
            for r in range(d):
                # (R@M)[r][c] = A*M[r][c] + A^{-1}*sum_k E[r][k] M[k][c]
                # E[r][k] nonzero iff tab[k] = (lp, r)
                pass
        # do full matmul directly:
        NN = [[sp.Integer(0)] * d for _ in range(d)]
        for r in range(d):
            for c in range(d):
                val = A * M[r][c]
                s = sp.Integer(0)
                for k in range(d):
                    lp, rr = tab[k]
                    if rr == r:
                        s += (D**lp) * M[k][c]
                val += A**(-1) * s
                NN[r][c] = sp.expand(val)
        M = NN
    return M, D

def closure_loops(n, X, Y):
    """Markov trace pairing T(X,Y): loops of the closed diagram formed by taking
    the TOP half of X (pairs with both ends in 0..n-1, i.e. caps) plus the BOTTOM
    half of Y (pairs with both ends in n..2n-1, i.e. cups), with through-strands
    of X glued to through-strands of Y, closed by n arcs top_i <-> bottom_i.
    Implementation: nodes XT (n, top boundary), YB (n, bottom boundary).
    - cap (a,b) in X, a,b<n: union(XT[a],XT[b]).
    - cup (a,b) in Y, a,b>=n: union(YB[a-n],YB[b-n]).
    - through strand a->a' in X (a<n, a'>=n) continues into Y: track exit port.
      Build wiring: for X, map each top t to exit (either top t' via cap chain or
      bottom port p). Simplest: union-find over XT + MIDports... Use explicit:
      nodes: XT(n) + XBm(n, X-bottom ports) + YTp(n, Y-top ports) + YB(n).
      X pairs -> unions on XT/XBm; Y pairs -> unions on YTp/YB; glue XBm[i]-YTp[i];
      close XT[i]-YB[i]. Count components.
    Checks: T(E,E)=1 (unknot); T(I2,I2)=2 (2-unlink); T(I,E)=1."""
    N = 4 * n
    parent = list(range(N))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[a] = b
    XT = list(range(n)); XBm = list(range(n, 2 * n))
    YTp = list(range(2 * n, 3 * n)); YB = list(range(3 * n, 4 * n))
    # ONLY: X caps (both ends on top), Y cups (both ends on bottom),
    # and through-strand connections X-top-to-X-bottom glued to Y-top-to-Y-bottom.
    for (a, b) in X:
        if a < n and b < n:
            union(XT[a], XT[b])
    for (a, b) in Y:
        if a >= n and b >= n:
            union(YB[a - n], YB[b - n])
    # through strands: X-top t exits at X-bottom port p(t); Y-top port q(s) exits at Y-bottom s.
    def exit_port(matching, top_idx):
        # follow pairing from top point top_idx to bottom port (or back to top)
        cur = top_idx
        seen = set()
        while True:
            if cur in seen:
                return None  # returned to top: capped, no exit
            seen.add(cur)
            nxt = None
            for (a, b) in matching:
                if a == cur:
                    nxt = b
                    break
                if b == cur:
                    nxt = a
                    break
            if nxt is None:
                raise RuntimeError("unpaired point")
            if cur < n and nxt >= n:
                return nxt - n  # exited at bottom port
            if cur >= n and nxt < n:
                return None  # re-entered top region -> capped path; signal
            cur = nxt
    # simpler: pair exit ports directly: for each X-bottom port p, find which X-top(s) reach it;
    # for each Y-top port q, find which Y-bottom(s) it reaches; glue p<->q then check connectivity via unions.
    # Build reachability: bottom port p of X connects to top t iff t's path exits at p.
    for i in range(n):
        union(XBm[i], YTp[i])
    # connect through paths: for X, union XT[t] with XBm[exit(t)] when exit exists
    for t0 in range(n):
        # walk from top t0 within X
        cur = t0
        seen = set()
        while True:
            if cur in seen:
                break
            seen.add(cur)
            nxt = next((b if a == cur else a) for (a, b) in X if a == cur or b == cur)
            if cur < n and nxt >= n:
                union(XT[t0], XBm[nxt - n])
                break
            if cur >= n and nxt < n:
                break  # capped
            cur = nxt
    for s0 in range(n):
        # walk from bottom of Y upward: start at Y-bottom s0
        cur = n + s0
        seen = set()
        while True:
            if cur in seen:
                break
            seen.add(cur)
            nxt = next((b if a == cur else a) for (a, b) in Y if a == cur or b == cur)
            if cur >= n and nxt < n:
                union(YB[s0], YTp[nxt])
                break
            if cur < n and nxt >= n:
                break  # cupped
            cur = nxt
    for i in range(n):
        union(XT[i], YB[i])
    comps = {}
    for v in range(N):
        comps.setdefault(find(v), []).append(v)
    # only components meeting the closed loop (XT or YB nodes) count;
    # isolated middle-port components are artifacts of unused cups/caps halves.
    nloops = 0
    for vs in comps.values():
        if any(v < n or v >= 3 * n for v in vs):
            nloops += 1
    return nloops

def jones(n, word):
    basis = all_matchings(n)
    idx = {m: k for k, m in enumerate(basis)}
    M, D = braid_matrix(n, basis, idx, word)
    d = len(basis)
    # trace: tr(M) = sum_{r,c} M[r][c] * T[r][c], T[r][c] = D^{closure_loops(basis_r, basis_c)}
    tr = sp.Integer(0)
    for r in range(d):
        for c in range(d):
            if M[r][c] != 0:
                tr += M[r][c] * D**closure_loops(n, basis[r], basis[c])
    tr = sp.expand(tr)
    delta = -A**2 - A**(-2)
    tr = sp.expand(tr.subs(D, delta))
    w = sum(1 if i > 0 else -1 for i in word)
    V_A = sp.simplify(((-A**3)**(-w)) * tr / delta)
    # convert A -> t^{-1/4}: V should be Laurent in t^{1/2}; for knots Laurent in t
    V = sp.simplify(V_A.subs(A, t**(-sp.Rational(1, 4))))
    return sp.simplify(V), {'dim': d}

if __name__ == '__main__':
    for (n, w, name) in [(2, [1, 1, 1], 'trefoil'), (2, [1], 'unknot-Hopf? s1 in B2 (Hopf link)'),
                         (1, [], 'unknot B1')]:
        V, info = jones(n, w)
        print(name, 'dim', info['dim'], 'V =', V, '; V(1) =', sp.simplify(V.subs(t, 1)))
