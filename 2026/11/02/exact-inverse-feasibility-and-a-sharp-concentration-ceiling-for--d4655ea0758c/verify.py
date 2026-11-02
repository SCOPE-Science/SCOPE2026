#!/usr/bin/env python3
"""Exact-rational checks for inverse fractional delegation, with no external packages."""
from fractions import Fraction as F
from itertools import combinations
import random


def invert_linear(M, b):
    n = len(M)
    a = [[F(v) for v in row] + [F(b[i])] for i, row in enumerate(M)]
    for k in range(n):
        piv = next(i for i in range(k, n) if a[i][k])
        a[k], a[piv] = a[piv], a[k]
        scale = a[k][k]
        a[k] = [v / scale for v in a[k]]
        for i in range(n):
            if i != k:
                z = a[i][k]
                if z:
                    a[i] = [v - z*u for v, u in zip(a[i], a[k])]
    return [row[-1] for row in a]


def weight(Q, tau):
    n = len(tau)
    M = [[F(int(i == j)) - Q[i][j] * (1 - tau[j]) for j in range(n)] for i in range(n)]
    visits = invert_linear(M, [1]*n)
    return [tau[i] * visits[i] for i in range(n)]


def hall(G, tau, w):
    n = len(tau)
    if sum(w) != n or any(w[i] < tau[i] for i in range(n)):
        return False
    r = [w[i]/tau[i] - 1 for i in range(n)]
    c = [(1-tau[j])*w[j]/tau[j] for j in range(n)]
    if sum(r) != sum(c):
        return False
    for mask in range(1 << n):
        incoming = [j for j in range(n) if any((j,i) in G for i in range(n) if mask >> i & 1)]
        if sum(r[i] for i in range(n) if mask >> i & 1) > sum(c[j] for j in incoming):
            return False
    return True


def realize_by_flow(G, tau, w):
    """Separate augmenting-path exact-rational max-flow on source -> donors -> receivers -> sink."""
    n = len(tau)
    if sum(w) != n or any(w[i] < tau[i] for i in range(n)):
        return None
    r = [w[i]/tau[i]-1 for i in range(n)]
    c = [(1-tau[j])*w[j]/tau[j] for j in range(n)]
    source, sink = 2*n, 2*n+1
    cap = [[F(0) for _ in range(2*n+2)] for __ in range(2*n+2)]
    total = sum(c)
    for j in range(n):
        cap[source][j] = c[j]
    for i in range(n):
        cap[n+i][sink] = r[i]
    for j,i in G:
        cap[j][n+i] = total
    initial = [row[:] for row in cap]
    sent = F(0)
    while True:
        pred = {source: None}
        queue = [source]
        for x in queue:
            for y in range(2*n+2):
                if y not in pred and cap[x][y] > 0:
                    pred[y] = x
                    queue.append(y)
            if sink in pred:
                break
        if sink not in pred:
            break
        path = []
        v = sink
        while v != source:
            u = pred[v]
            path.append((u,v))
            v = u
        f = min(cap[u][v] for u,v in path)
        for u,v in path:
            cap[u][v] -= f
            cap[v][u] += f
        sent += f
    if sent != total:
        return None
    flows = [[initial[j][n+i]-cap[j][n+i] for j in range(n)] for i in range(n)]
    assert all(sum(flows[i][j] for j in range(n)) == r[i] for i in range(n))
    assert all(sum(flows[i][j] for i in range(n)) == c[j] for j in range(n))
    Q = [[flows[i][j]/c[j] for j in range(n)] for i in range(n)]
    assert weight(Q, tau) == list(w)
    return Q


def random_Q(G, n, rng):
    M = [[F(0) for j in range(n)] for i in range(n)]
    for j in range(n):
        targets = [i for i in range(n) if (j,i) in G]
        counts = [rng.randint(1,4) for _ in targets]
        for i,z in zip(targets, counts):
            M[i][j] = F(z, sum(counts))
    return M


def go():
    rng = random.Random(5023891)
    checks = 0
    for n in range(2, 6):
        for _ in range(100):
            G = {(j,i) for j in range(n) for i in range(n) if i != j and rng.randint(0,1)}
            for j in range(n):
                if not any(jj == j for jj,ii in G):
                    i=(j+1)%n
                    G.add((j,i))
            tau = [F(rng.randint(1,4), rng.randint(5,10)) for _ in range(n)]
            Q = random_Q(G, n, rng)
            w = weight(Q,tau)
            assert sum(w) == n
            assert hall(G,tau,w)
            realized=realize_by_flow(G,tau,w)
            assert realized is not None and weight(realized,tau)==w
            checks += 1
            # A deliberately perturbed target may or may not be feasible, but Hall and maxflow must agree.
            a,b=rng.sample(range(n),2)
            p=w[:]
            delta=F(rng.randint(-8,8),10)
            p[a]+=delta
            p[b]-=delta
            assert hall(G,tau,p) == (realize_by_flow(G,tau,p) is not None)
            checks+=1
    for n in range(2, 9):
        G = {(j,i) for j in range(n) for i in range(n) if j != i}
        for t in (F(1,5),F(1,3),F(1,2),F(4,5)):
            tau = [t]*n
            U = (n*(1-t)+t)/(2-t)
            # Uniform target is feasible, max hub target sharp.
            uni=[F(1)]*n
            assert hall(G,tau,uni)
            star=[(n-U)/F(n-1)]*n
            star[0]=U
            assert sum(star)==n
            assert hall(G,tau,star)
            realized=realize_by_flow(G,tau,star)
            assert realized is not None and weight(realized,tau)==star
            for i in range(n):
                for k in range(5):
                    w=[F(1)]*n
                    delta=F(k,10)
                    if i != 0:
                        w[i] += delta
                        w[0] -= delta
                    assert hall(G,tau,w) == (all(z >= t and z <= U for z in w))
                    checks += 1
            checks += 1
    print('EXACT_RATIONAL_TESTS_PASSED',checks)
    print('Graphs: 400 random sparse loopless trust networks, n=2..5, heterogeneous retention,')
    print('800 realizable and perturbed-target cut-vs-flow tests, 28 complete-digraph sharp-cap checks.')

if __name__=='__main__':
    go()
