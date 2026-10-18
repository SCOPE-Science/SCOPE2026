#!/usr/bin/env python3
"""Finite reproducibility checks for the tree equilibrium response identity.
Uses only the Python standard library; not a proof of the infinite/all-parameter theorem.
"""
import math
import random


def linear_solve(matrix, rhs):
    n = len(rhs)
    a = [list(matrix[i]) + [float(rhs[i])] for i in range(n)]
    for i in range(n):
        k = max(range(i, n), key=lambda j: abs(a[j][i]))
        assert abs(a[k][i]) > 1e-14
        a[i], a[k] = a[k], a[i]
        p = a[i][i]
        for j in range(i + 1, n):
            t = a[j][i] / p
            for h in range(i + 1, n + 1):
                a[j][h] -= t * a[i][h]
            a[j][i] = 0.0
    x = [0.0] * n
    for i in reversed(range(n)):
        x[i] = (a[i][n] - sum(a[i][j] * x[j] for j in range(i + 1, n))) / a[i][i]
    return x


def derivatives(edges, rates, alpha, z):
    vertices = len(rates)
    inc = [[] for _ in range(vertices)]
    for j, (u, v) in enumerate(edges):
        inc[u].append(j)
        inc[v].append(j)
    s = [sum(z[j] for j in inc[v]) for v in range(vertices)]
    if min(s) <= 0 or min(z) <= 0:
        raise ValueError('positive domain required')
    grad = [z[j] ** (1 / alpha - 1) - rates[u] / s[u] - rates[v] / s[v]
            for j, (u, v) in enumerate(edges)]
    m = len(edges)
    h = [[0.0] * m for _ in range(m)]
    for j in range(m):
        h[j][j] = (1 - alpha) / alpha * z[j] ** (1 / alpha - 2)
    for v in range(vertices):
        w = rates[v] / s[v] ** 2
        for i in inc[v]:
            for j in inc[v]:
                h[i][j] += w
    phi = alpha * sum(x ** (1 / alpha) for x in z) - sum(rates[v] * math.log(s[v]) for v in range(vertices))
    return phi, grad, h, s, inc


def equilibrium(edges, rates, alpha, start=None):
    m = len(edges)
    z = [1.0] * m if start is None else list(start)
    for iteration in range(170):
        val, grad, h, _, _ = derivatives(edges, rates, alpha, z)
        if max(abs(t) for t in grad) < 2e-8:
            return z
        step = linear_solve(h, [-v for v in grad])
        armijo = sum(g * d for g, d in zip(grad, step))
        assert armijo < 1e-10
        a = 1.0
        while a > 2**(-46):
            zz = [zi + a * di for zi, di in zip(z, step)]
            if min(zz) > 0:
                v2 = derivatives(edges, rates, alpha, zz)[0]
                if v2 <= val + 1e-4 * a * armijo:
                    z = zz
                    break
            a *= .5
        else:
            raise AssertionError('Newton line search stalled')
    raise AssertionError('Newton iteration limit: '+str((z,grad,rates,alpha)))


def tree_response(edges, rates, alpha, z, root=0):
    n = len(rates)
    _, _, h, s, inc = derivatives(edges, rates, alpha, z)
    assert len(inc[root]) == 1
    neighbors = [[] for _ in range(n)]
    for e, (a, b) in enumerate(edges):
        neighbors[a].append((b, e))
        neighbors[b].append((a, e))
    parent = [-2] * n
    pedge = [-1] * n
    parent[root] = -1
    order = [root]
    for u in order:
        for v, e in neighbors[u]:
            if parent[v] == -2:
                parent[v] = u
                pedge[v] = e
                order.append(v)
    assert len(order) == n
    ds = [(1-alpha)/alpha * z[e] ** (1/alpha - 2) for e in range(len(edges))]
    w = [rates[v] / s[v] ** 2 for v in range(n)]
    c = [0.0] * len(edges)
    factor = [0.0] * len(edges)
    for v in reversed(order[1:]):
        e = pedge[v]
        kids = [edge for child, edge in neighbors[v] if parent[child] == v]
        a = 1.0 + w[v] * sum(1.0 / c[f] for f in kids)
        c[e] = ds[e] + w[v] / a
        for f in kids:
            factor[f] = w[v] / (c[f] * a)
    x = [0.0] * len(edges)
    e0 = pedge[order[1]]
    x[e0] = 1.0 / (w[root] + c[e0])
    for v in order[1:]:
        e = pedge[v]
        for child, f in neighbors[v]:
            if parent[child] == v:
                x[f] = -factor[f] * x[e]
    b = [0.0] * len(edges)
    b[e0] = 1.0
    direct = linear_solve(h, b)
    for a, v in zip(x, direct):
        assert abs(a-v) <= 1e-8 * max(1, abs(v)), (a, v)
    for v in order[1:]:
        e = pedge[v]
        sign = (-1)**(len(tuple(path_to_root(parent, v))) - 2)
        assert sign*x[e] > 0
    return [z[e] ** (1/alpha-1) * x[e] / (alpha*z[e0]) for e in range(len(edges))]


def path_to_root(parent, v):
    while v != -1:
        yield v
        v = parent[v]


def test():
    rng = random.Random(310831)
    checks = 0
    for nv in range(2, 11):
        for kind in range(4):
            for rep in range(5):
                if kind == 0:
                    parent = [0] + [i-1 for i in range(1, nv)]
                elif kind == 1:
                    parent = [0] + [0 for i in range(1, nv)]
                elif kind == 2:
                    parent = [0] + [(i-1)//2 for i in range(1, nv)]
                else:
                    parent = [0] + [rng.randrange(i) for i in range(1, nv)]
                raw = [(i, parent[i]) for i in range(1, nv)]
                # Reindex so the distinguished root is an original leaf.
                deg = [0]*nv
                for u, v in raw: deg[u]+=1; deg[v]+=1
                root = next(i for i, d in enumerate(deg) if d == 1)
                rates = [math.exp(rng.uniform(-.7, .7)) for _ in range(nv)]
                alpha = rng.choice([.12, .32, .56, .79, .94])
                z = equilibrium(raw, rates, alpha)
                response = tree_response(raw, rates, alpha, z, root)
                assert abs(sum(response)-1) < 1e-7
                eps = 2e-5 * rates[root]
                more = list(rates); less = list(rates)
                more[root] += eps
                less[root] -= eps
                zp = equilibrium(raw, more, alpha, start=z)
                zm = equilibrium(raw, less, alpha, start=z)
                actual = [(zp[j]**(1/alpha)-zm[j]**(1/alpha))/(2*eps) for j in range(len(raw))]
                for a, b in zip(response, actual):
                    assert abs(a-b) < 4e-5 * max(1, abs(a), abs(b)), (nv,kind,rep,a,b)
                    checks += 1
                # Check a finite (not infinitesimal) change as well.
                jumped = list(rates)
                jumped[root] *= 1.3
                zj = equilibrium(raw, jumped, alpha, start=z)
                assert all((zj[j]**(1/alpha)-z[j]**(1/alpha))*a > 0
                           for j, a in enumerate(response))
                assert abs(sum(e**(1/alpha) for e in z)-sum(rates)) < 1e-7
                checks += 3
    print('PASS: {} independent derivative, conservation and tree-response checks'.format(checks))

if __name__ == '__main__':
    test()
