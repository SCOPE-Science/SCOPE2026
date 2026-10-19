"""Reproducible checks for a three-parameter household-final-size inverse theorem.

Run with `python verify.py` (Python 3.9+; standard library only).
Analytical proofs of global uniqueness and nonidentifiability appear in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import log, log1p, sqrt, isclose


def laplace(a, s):
    return (1 + s / a) ** (-a)


def two_contact_probabilities(a, lam):
    p = laplace(a, lam)
    q = laplace(a, 2 * lam)
    return q, 2 * p * (p - q), 1 - q - 2 * p * (p - q)


def exact_graph_probabilities(a, lam):
    """Independent directed-graph enumeration; a is a positive integer.

    Each infective has correlated outgoing-edge indicators, but different
    infectives have independent infectious periods. Integrate each pair of
    outgoing arcs first, then enumerate all 64 directed edge sets.
    """
    a = int(a)
    lam = F(lam)
    p = (1 + lam / a) ** (-a)
    q = (1 + 2 * lam / a) ** (-a)
    arc_pairs = [[(i, j) for j in range(3) if j != i] for i in range(3)]
    result = [F(0), F(0), F(0)]
    mass = F(0)
    for bits in product([0, 1], repeat=6):
        adj = {i: [] for i in range(3)}
        pr = F(1)
        for src in range(3):
            two_bits = bits[2*src:2*src+2]
            successes = sum(two_bits)
            pr *= (q if successes == 0 else p-q if successes == 1 else 1-2*p+q)
            for bit, (_, dst) in zip(two_bits, arc_pairs[src]):
                if bit:
                    adj[src].append(dst)
        reached = {0}
        changed = True
        while changed:
            nxt = reached | {y for x in reached for y in adj[x]}
            changed = nxt != reached
            reached = nxt
        result[len(reached)-1] += pr
        mass += pr
    assert mass == 1
    return tuple(result)


def invert(h1, q, r):
    """Invert household sizes two and three for shape, transmission, mixing."""
    p = (q + sqrt(q*q + 2*r)) / 2
    R = log(q) / log(p)
    assert 1 < R < 2, (p, q, R)

    def f(u):
        if u == 0:
            return 2
        return log1p(2*u)/log1p(u)
    hi = 1.0
    while f(hi) > R:
        hi *= 2
    lo = 0.0
    for _ in range(100):
        mid = (lo+hi)/2
        if f(mid) > R:
            lo = mid
        else:
            hi = mid
    u = (lo+hi)/2
    a = -log(p)/log1p(u)
    lam = a*u
    beta = a*(h1 ** (-1/a) - 1)
    eta = log(beta/lam)/log(2)
    return a, beta, eta, lam, p


def sar2(a, lam):
    q, r, z = two_contact_probabilities(a, lam)
    return (r + 2*z)/2


def check():
    # Fully independent exact enumeration of 64 possible directed graphs.
    for a, beta, lam in [(1, F(1), F(2,3)),
                          (2, F(2), F(4,3)),
                          (3, F(9,4), F(3,2)),
                          (4, F(3), F(2))]:
        direct = two_contact_probabilities(F(a), lam)
        graph = exact_graph_probabilities(a, lam)
        assert graph == direct, (a, graph, direct)
        assert graph[0] + graph[1] + graph[2] == 1
        assert 1 <= beta/lam <= 2
    # Exact rational worked example.
    assert exact_graph_probabilities(1, F(2,3)) == (F(3,7), F(36,175), F(64,175))
    assert sar2(F(1), F(2,3)) == F(82,175)
    # Global inverse, tested over interior and allowed endpoint values.
    for a, beta, eta in [(1,1,log(1.5,2)), (2,2,log(1.5,2)),
                          (3,1.2,0.27), (0.8,2.1,0.72),
                          (4,3,0), (2,0.7,1), (1.4,0.47,0.5)]:
        lam = beta * 2**(-eta)
        h1 = laplace(a, beta)
        q, r, _ = two_contact_probabilities(a, lam)
        aa, bb, ee, ll, pp = invert(h1, q, r)
        for v, w in [(aa,a),(bb,beta),(ee,eta),(ll,lam)]:
            assert isclose(v,w,rel_tol=2e-9,abs_tol=2e-9), (a,beta,eta,v,w)
        assert q > pp*pp and q < pp
    # Same two stratum means admit distinct Gamma shapes within 0<eta<1.
    target = F(82,175)
    a = 2.0
    beta = a * (2**(1/a)-1)  # n=1 no-transmission chance remains 1/2
    lo,hi = 0.0, beta
    for _ in range(100):
        mid = (lo+hi)/2
        if sar2(a,mid) < float(target): lo=mid
        else: hi=mid
    lam = (lo+hi)/2
    eta = log(beta/lam)/log(2)
    assert 0 < eta < 1
    assert isclose(laplace(a,beta),0.5,abs_tol=1e-14)
    assert isclose(sar2(a,lam),float(target),abs_tol=1e-14)
    assert not isclose(a,1.0)
    # Nonzero shape signal, second-order in contact intensity.
    for a in (0.8, 1.0, 2.0, 4.0):
        for lam in (.01, .001, .0001):
            p, q = laplace(a,lam), laplace(a,2*lam)
            assert q-p*p > 0
            if lam == .0001:
                assert isclose((q-p*p)/(lam*lam),1/a,rel_tol=.001)
    print('PASS: 64-graph exact enumeration, shape/scale inverse,')
    print('      medium-summary ambiguity, and weak-transmission asymptotics.')
    print('Rational test: size-2 P0=1/2; size-3 (P0,P1,P2)=(3/7,36/175,64/175).')


if __name__ == '__main__':
    check()
