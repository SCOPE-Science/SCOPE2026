#!/usr/bin/env python3
"""Reproduce finite-state identities for a bounded-confidence voter process.

All stationary and detailed-balance checks use exact rational arithmetic.
The analytic graph-uniform assertion is proved separately, not by enumeration.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, isclose, log


def rate(state, i, new, p, q, neighbors, compatible):
    old = state[i]
    if old == new:
        return F(0)
    u = p / len(compatible)
    if new not in compatible[old]:
        return u
    deg = len(neighbors[i])
    present = sum(state[j] == new for j in neighbors[i])
    return u + (1-p) * F(comb(present, q), comb(deg, q)) if present >= q else u


def generator(states, p, q, neighbors, compatible):
    lookup = {s: i for i, s in enumerate(states)}
    matrix = [[F(0) for _ in states] for _ in states]
    for index, state in enumerate(states):
        for i in range(len(state)):
            for new in range(len(compatible)):
                if new == state[i]:
                    continue
                nxt = list(state)
                nxt[i] = new
                j = lookup[tuple(nxt)]
                matrix[index][j] += rate(state, i, new, p, q, neighbors, compatible)
        matrix[index][index] = -sum(matrix[index])
    return matrix


def q_audit():
    checks = 0
    path = [frozenset((1,)), frozenset((0, 2)), frozenset((1,))]
    pvalues = [F(1, 7), F(2, 5), F(5, 6)]
    graphs = [
        (([1], [0]), [1]),
        (([1,2], [0,2], [0,1]), [1,2]),
        (([1,3], [0,2], [1,3], [0,2]), [1,2]),
        (([1,2,3], [0,2,3], [0,1,3], [0,1,2]), [1,2,3])
    ]
    for neighbors, sizes in graphs:
        n = len(neighbors)
        for q in sizes:
            for p in pvalues:
                a = (0,) * n
                b = (1,) + (0,) * (n-1)
                c = (2,) + (0,) * (n-1)
                uv = p / 3
                assert rate(a,0,2,p,q,neighbors,path) == uv
                assert rate(c,0,1,p,q,neighbors,path) == uv
                assert rate(b,0,0,p,q,neighbors,path) == uv + 1-p
                assert rate(a,0,1,p,q,neighbors,path) == uv
                assert rate(b,0,2,p,q,neighbors,path) == uv
                assert rate(c,0,0,p,q,neighbors,path) == uv
                checks += 6
    # For q=1 and complete social contacts, all-compatible confidence admits
    # the explicit detailed-balance weight product_j (theta)_{n_j}.
    all_conf = [frozenset(set(range(3)) - {i}) for i in range(3)]
    for n in range(2, 5):
        neigh = [list(set(range(n)) - {i}) for i in range(n)]
        for p in pvalues:
            states = list(product(range(3), repeat=n))
            Q = generator(states,p,1,neigh,all_conf)
            theta = F(n-1)*p / (3*(1-p))
            weights = []
            for s in states:
                w = F(1)
                for j in range(3):
                    for k in range(s.count(j)):
                        w *= theta+k
                weights.append(w)
            for i in range(len(states)):
                for j in range(i+1,len(states)):
                    if Q[i][j]:
                        assert weights[i]*Q[i][j] == weights[j]*Q[j][i]
                        checks += 1
    # Exact two-person, three-opinion count-chain stationary weights.
    count_states = [(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)]
    for p in pvalues:
        Q = [[F(0) for _ in count_states] for _ in count_states]
        for k, count in enumerate(count_states):
            for old in range(3):
                if count[old] == 0:
                    continue
                for new in range(3):
                    if old == new:
                        continue
                    c = list(count)
                    c[old] -= 1
                    c[new] += 1
                    nbr = count[new]
                    r = count[old]*(p/3 + (1-p)*nbr*int(new in path[old]))
                    Q[k][count_states.index(tuple(c))] += r
            Q[k][k] = -sum(Q[k])
        pi = [(2-p)/9,2*p/9,F(2,9),(3-2*p)/9,2*p/9,(2-p)/9]
        assert sum(pi) == 1
        for j in range(len(Q)):
            assert sum(pi[i]*Q[i][j] for i in range(len(Q))) == 0
            checks += 1
        J = 2*p*(1-p)/27
        directed = [(0,2),(2,1),(1,0),(5,2),(2,4),(4,5)]
        for i,j in directed:
            assert pi[i]*Q[i][j]-pi[j]*Q[j][i] == J
            checks += 1
        chosen = {frozenset((i,j)) for i,j in directed}
        for i in range(len(Q)):
            for j in range(i+1,len(Q)):
                if frozenset((i,j)) not in chosen:
                    assert pi[i]*Q[i][j]-pi[j]*Q[j][i] == 0
                    checks += 1
        entropy = 0.0
        for i in range(len(Q)):
            for j in range(i+1,len(Q)):
                if Q[i][j] and Q[j][i]:
                    fwd = float(pi[i]*Q[i][j])
                    bwd = float(pi[j]*Q[j][i])
                    entropy += (fwd-bwd)*log(fwd/bwd)
        expected = float(4*p*(1-p)/27)*log(float((3-2*p)/p))
        assert isclose(entropy,expected,rel_tol=1e-12,abs_tol=1e-13)
        checks += 1
    def derivative(p):
        return (1-2*p)*log((3-2*p)/p)-3*(1-p)/(3-2*p)
    left,right=1e-8,0.49999999
    for _ in range(80):
        mid=(left+right)/2
        if derivative(mid)>0:
            left=mid
        else:
            right=mid
    peak=(left+right)/2
    assert abs(peak-0.29198479714179526)<1e-12
    print('PASS:',checks,'exact graph, detailed-balance, stationary-flow checks')
    print('Peak independence probability:',format(peak,'.15f'))
    print('Peak entropy production:',format(4*peak*(1-peak)/27*log((3-2*peak)/peak),'.15f'))

if __name__ == '__main__':
    q_audit()
