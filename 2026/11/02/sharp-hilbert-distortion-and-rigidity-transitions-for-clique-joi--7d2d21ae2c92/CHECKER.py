"""Reproducible exact-arithmetic checks for the clique-joined rook-graph formula.

Uses rational Gram matrices for actual Euclidean configurations. Finite tests
support, but do not replace, the universal Hilbert-space proof.
Run: python CHECKER.py
"""
from fractions import Fraction as F


def formula(m, n, h):
    assert m >= 2 and n >= 2 and h >= 1
    M, N = max(m, n), min(m, n)
    eta = F(h-1, 2*h)
    L = (4*N*(M-1) + M*N*F(h-1, h)) / (2*M*N + M-N)
    D2 = max(F(2), L)
    assert L < F(5, 2)
    assert (L <= 2) == (eta <= F(1, M)+F(1, N))
    return M, N, L, D2


def gram_value(core, m, n, h, u, v, i, j):
    # core is a list of (coordinate_i, coordinate_j), then h hub indices.
    if i < len(core):
        a, b = core[i]
        if j < len(core):
            c, d = core[j]
            return u/F(2) * (F(int(a == c))-F(1,m)) + v/F(2) * (F(int(b == d))-F(1,n))
        return F(0)
    if j < len(core):
        return F(0)
    return F(1,2) * (F(int(i == j)) - F(1,h))


def verify_embedding(m, n, h, u, v, D2):
    core = [(a,b) for a in range(m) for b in range(n)]
    nn = len(core)+h
    gs = [gram_value(core,m,n,h,u,v,i,i) for i in range(nn)]
    upper_observed = F(0)
    lower_observed = None
    pairs = 0
    for i in range(nn):
        for j in range(i+1,nn):
            sq = gs[i]+gs[j]-2*gram_value(core,m,n,h,u,v,i,j)
            if i < len(core) and j < len(core):
                a,b=core[i];c,d=core[j]
                graph_sq = 1 if int(a!=c)+int(b!=d)==1 else 4
            else:
                graph_sq = 1
            ratio = sq/F(graph_sq)
            assert ratio >= 1, (m,n,h,i,j,ratio)
            assert ratio <= D2, (m,n,h,i,j,ratio,D2)
            upper_observed = max(upper_observed, ratio)
            lower_observed = ratio if lower_observed is None else min(lower_observed,ratio)
            pairs+=1
    assert lower_observed == 1
    assert upper_observed == D2, (m,n,h, upper_observed, D2)
    return pairs


def main():
    total = 0
    case_count = 0
    strict = boundary = below = 0
    rigidity_sample = 0
    for m in range(2,9):
        for n in range(2,m+1):
            for h in range(1,9):
                M,N,L,D2 = formula(m,n,h)
                if L > 2:
                    strict += 1
                    u,v = 4-L,L
                    assert 1 < u < 2 < v < F(5,2)
                else:
                    if L == 2: boundary += 1
                    else: below += 1
                    u=v=F(2)
                core_r = F(m-1,2*m)*u+F(n-1,2*n)*v
                hub_r=F(h-1,2*h)
                if L>2:
                    assert core_r+hub_r==L
                else:
                    assert F(1)<=core_r+hub_r<=2
                total+=verify_embedding(m,n,h,u,v,D2)
                case_count+=1
                if L>2 and m==n:
                    alternate_u=(L+2)/2
                    alternate_v=4-alternate_u
                    assert alternate_u != u
                    assert F(1) <=alternate_u<=D2
                    assert F(1) <=alternate_v<=D2
                    assert F(m-1,2*m)*alternate_u+F(n-1,2*n)*alternate_v+hub_r==D2
                    total+=verify_embedding(m,n,h,alternate_u,alternate_v,D2)
                    rigidity_sample+=1
    print('CHECK_OK parameter_triples=',case_count,
          'exact_pairwise_checks=',total,
          'strict=',strict,'boundary=',boundary,'below=',below,
          'balanced_nonrigid_alternate=',rigidity_sample)

if __name__=='__main__':
    main()
