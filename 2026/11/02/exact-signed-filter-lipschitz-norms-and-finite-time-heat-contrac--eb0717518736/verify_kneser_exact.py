"""Exact arithmetic checks for two-subset Kneser Lipschitz operator formulas.

This finite certificate supplements the all-dimension proof in RESULT.md.
Run with Python 3: python verify_kneser_exact.py
"""
from fractions import Fraction as F
from itertools import combinations, product


def vertices(n):
    return list(combinations(range(n), 2))


def adjacency(n):
    vs = vertices(n)
    return vs, [[int(set(x).isdisjoint(y)) for y in vs] for x in vs]


def check_quad(n):
    vs, adj = adjacency(n)
    N = len(vs)
    k = (n-2)*(n-3)//2
    mu = (n-3)*(n-4)//2
    for i in range(N):
        assert sum(adj[i]) == k
        for j in range(N):
            lhs = sum(adj[i][h]*adj[h][j] for h in range(N))
            rhs = (n-3)*int(i==j)-(n-4)*adj[i][j]+mu
            assert lhs == rhs, (n, i, j)
    return N*N


def signed_certificate(n, alpha, beta):
    vs, adj = adjacency(n)
    idx = {v: i for i, v in enumerate(vs)}
    u, v = (0, 1), (2, 3)
    out = [j for j in range(4, n)]
    U = [(i, j) for i in (0, 1) for j in out]
    V = [(i, j) for i in (2, 3) for j in out]
    assert adj[idx[u]][idx[v]] == 1
    if n >= 6:
        for i in (0, 1):
            for a, b in zip(out, out[1:]+out[:1]):
                assert adj[idx[(i,a)]][idx[(i+2,b)]] == 1
        value = abs(alpha-beta) + 2*(n-4)*abs(beta)
        positive = [u if alpha-beta>0 else v] if alpha!=beta else []
        negative = [v if alpha-beta>0 else u] if alpha!=beta else []
        positive += V if beta>0 else (U if beta<0 else [])
        negative += U if beta>0 else (V if beta<0 else [])
        assert set(positive).isdisjoint(negative)
        f = [F(1,2) if x in positive else -F(1,2) if x in negative else F(0) for x in vs]
        assert all(abs(f[i]-f[j]) <= 1 for i in range(len(vs)) for j in range(i+1,len(vs)) if adj[i][j])
        dual = (alpha-beta)*(f[idx[u]]-f[idx[v]]) + beta*(sum(f[idx[w]] for w in V)-sum(f[idx[w]] for w in U))
        assert dual == value
        return 1
    assert len(U)==len(V)==2
    # Vertex potentials at the corners (x,y)=(0,4),(1,3),(1,-3), and negatives.
    anchors = [
        (F(0),F(0),F(-1),F(1)),
        (F(0),F(-1),F(-1),F(1)),
        (F(0),F(-1),F(0),F(-1)),
    ]
    extrema = []
    # All pairs of support vertices are at distance 1 if disjoint, else 2.
    ss = [u,v]+U+V
    for a,b,c,d in anchors:
        for sign in (1,-1):
            anchor = {u:sign*a,v:sign*b,**{w:sign*c for w in U},**{w:sign*d for w in V}}
            for p,q in combinations(ss,2):
                dist = 1 if set(p).isdisjoint(q) else 2
                assert abs(anchor[p]-anchor[q]) <= dist,(p,q)
            # McShane inf-extension to every graph vertex.
            f = {w:min(anchor[s]+(0 if s==w else 1 if set(s).isdisjoint(w) else 2) for s in anchor) for w in vs}
            assert all(f[s]==anchor[s] for s in anchor)
            assert all(abs(f[vs[i]]-f[vs[j]])<=1 for i in range(len(vs)) for j in range(i+1,len(vs)) if adj[i][j])
            val=(alpha-beta)*(f[u]-f[v])+beta*(sum(f[w] for w in V)-sum(f[w] for w in U))
            extrema.append(val)
    return int(max(extrema)==max(abs(alpha)+3*abs(beta),4*abs(beta)))


def check_heat_formulas(n):
    # Algebraically independent rational spectral multipliers for exact heat-factor identities.
    k=(n-2)*(n-3)//2
    tests=0
    for a,b in product([F(0),F(1,7),F(1,3),F(1,2),F(1)],repeat=2):
        if b > a: continue
        alpha=((n-3)*a+b)/(n-2)
        beta=(a-b)/(n-2)
        norm = max(abs(alpha)+3*abs(beta),4*abs(beta)) if n==5 else abs(alpha-beta)+2*(n-4)*abs(beta)
        formula=(5*a-2*b)/3 if n==5 else (3*(n-4)*a-2*(n-5)*b)/(n-2)
        assert norm==formula,(n,alpha,beta,norm,formula)
        assert alpha+beta*k >=0
        tests+=1
    return tests


if __name__ == '__main__':
    assert all(signed_certificate(5,F(a),F(b)) for a,b in product(range(-4,5),repeat=2))
    quad=0; signed=81; heat=0
    for n in range(5,20):
        quad += check_quad(n)
        heat += check_heat_formulas(n)
        if n>=6:
            for a,b in product(range(-3,4),repeat=2):
                signed+=signed_certificate(n,F(a),F(b))
    print('CHECK_OK adjacency_matrix_entries=',quad,'exact_signed_certificates=',signed,'rational_spectral_heat_tests=',heat)
