"""Exact rational checks for a quadratic metric-graph projection bound.

Run: python3 verify.py
The universal theorem and limiting sharpness are proved analytically in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product

Q0 = (F(1), -F(7, 2), F(5, 2))
Q1 = (F(0), -F(3, 2), F(5, 2))
B = (F(0), F(4), -F(4))
L0 = (F(1), F(-3), F(2))
L1 = (F(0), F(-1), F(2))
C = F(79, 25)
checks = 0


def check(condition, msg):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(msg)


def polyadd(a, b):
    return tuple((a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b))))


def polyscale(a, x):
    return tuple(x * z for z in a)


def polydot(a, b):
    return sum(a[i] * b[j] / F(i+j+1)
               for i in range(len(a)) for j in range(len(b)))


def inteval(a, x):
    return sum(t * x**(i+1) / (i+1) for i, t in enumerate(a))


def evaluate(a, x):
    return sum(t * x**i for i, t in enumerate(a))


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def inverse(matrix):
    n = len(matrix)
    m = [list(row)+idrow for row, idrow in zip(matrix, identity(n))]
    for k in range(n):
        pivot = next((i for i in range(k, n) if m[i][k]), None)
        check(pivot is not None, 'singular Gram matrix')
        m[k], m[pivot] = m[pivot], m[k]
        t = m[k][k]
        m[k] = [z/t for z in m[k]]
        for i in range(n):
            if i != k:
                t = m[i][k]
                if t:
                    m[i] = [a-t*b for a,b in zip(m[i], m[k])]
    result = [row[n:] for row in m]
    for i in range(n):
        for j in range(n):
            check(sum(matrix[i][k]*result[k][j] for k in range(n)) == F(i == j),
                  'failed exact inverse verification')
    return result


def gram_orthogonal(n, edges):
    m = len(edges)
    out = [[F(0) for _ in range(n+m)] for _ in range(n+m)]
    for k,(u,v,w) in enumerate(edges):
        out[u][u] += w*F(1,8)
        out[v][v] += w*F(1,8)
        out[u][v] -= w*F(1,24)
        out[v][u] -= w*F(1,24)
        out[n+k][n+k] = w*F(8,15)
    return out


def gram_lagrange(n, edges):
    m = len(edges)
    out = [[F(0) for _ in range(n+m)] for _ in range(n+m)]
    for k,(u,v,w) in enumerate(edges):
        ids = [u,v,n+k]
        funcs = [L0,L1,B]
        for i in range(3):
            for j in range(3):
                out[ids[i]][ids[j]] += w*polydot(funcs[i],funcs[j])
    return out


def edge_kernel(z, invh, n, edges, edge_idx=None, s=None):
    # Return each quadratic kernel's coefficients in the variable x on an edge.
    if edge_idx is None:
        row = invh[z]
        bubble_e = None
    else:
        u,v,w = edges[edge_idx]
        row = [evaluate(Q0,s)*invh[u][j] + evaluate(Q1,s)*invh[v][j]
               for j in range(n)]
        bubble_e = edge_idx
    arr = []
    for k,(u,v,w) in enumerate(edges):
        pol = polyadd(polyscale(Q0,row[u]), polyscale(Q1,row[v]))
        if bubble_e == k:
            pol = polyadd(pol, polyscale(B, evaluate(B,s)/(F(8,15)*w)))
        arr.append(pol)
    return arr


def direct_kernel(z, invb, n, edges, edge_idx=None, s=None):
    ev = [F(0) for _ in range(n+len(edges))]
    if edge_idx is None:
        ev[z] = 1
    else:
        u,v,w = edges[edge_idx]
        ev[u] = evaluate(L0,s)
        ev[v] = evaluate(L1,s)
        ev[n+edge_idx] = evaluate(B,s)
    co = [sum(ev[i]*invb[i][j] for i in range(len(ev))) for j in range(len(ev))]
    return [polyadd(polyadd(polyscale(L0,co[u]), polyscale(L1,co[v])),
                    polyscale(B,co[n+k]))
            for k,(u,v,w) in enumerate(edges)]

# Local polynomial and integral identities; roots of Q0, Q1 are 2/5,3/5.
check(polyadd(Q0, polyscale(B,F(1,8))) == L0, 'basis transform 0')
check(polyadd(Q1, polyscale(B,F(1,8))) == L1, 'basis transform 1')
for pair, expect in [((Q0,Q0),F(1,8)), ((Q1,Q1),F(1,8)),
                     ((Q0,Q1),F(-1,24)), ((Q0,B),F(0)),
                     ((Q1,B),F(0)), ((B,B),F(8,15))]:
    check(polydot(*pair) == expect, 'local Gram identity')
check(2*inteval(Q0,F(2,5))-inteval(Q0,F(1)) == F(79,300),
      'absolute value of Q0')
check(2*inteval(Q1,F(1))-2*inteval(Q1,F(3,5))-inteval(Q1,F(1))
      == F(79,300), 'absolute value of Q1')
check(F(12)*F(79,300) == C, 'universal constant')
check((C+5)/4 == F(51,25), 'interior secondary envelope')
check(C > F(5,2), 'strict derivative envelope')

# Explicit weighted connected graphs with unequal weights and cycles.
graphs = [
    (2, [(0,1,F(3,2))]),
    (3, [(0,1,F(2,3)),(1,2,F(5,7))]),
    (3, [(0,1,F(1,3)),(1,2,F(7,5)),(2,0,F(6,5))]),
    (5, [(0,1,F(1,2)),(0,2,F(3,5)),(0,3,F(5,4)),(0,4,F(7,8))]),
    (5, [(0,1,F(2,3)),(1,2,F(1,7)),(2,3,F(13,11)),
         (3,4,F(2,5)),(4,0,F(9,8)),(1,4,F(3,4))]),
]
for d in (2,3,4):
    verts = list(product((0,1),repeat=d))
    idx = {v:i for i,v in enumerate(verts)}
    edges = [(idx[u],idx[tuple(u[:j]+(1,)+u[j+1:])],F(1))
             for u in verts for j in range(d) if u[j] == 0]
    graphs.append((2**d,edges))

for n,edges in graphs:
    h = gram_orthogonal(n,edges)
    a = inverse([r[:n] for r in h[:n]])
    g = gram_lagrange(n,edges)
    ginv = inverse(g)
    weights = [F(0) for _ in range(n)]
    for u,v,w in edges:
        weights[u] += w
        weights[v] += w
    for z in range(n):
        check(all(x>0 for x in a[z]), 'strict inverse positivity')
        check(sum(weights[j]*a[z][j] for j in range(n)) == F(12),
              'mass sum')
        for left,right in zip(edge_kernel(z,a,n,edges),
                              direct_kernel(z,ginv,n,edges)):
            check(left == right, 'vertex reproducing kernel')
    for e in range(len(edges)):
        for s in [F(1,5),F(1,2),F(4,5)]:
            for left,right in zip(edge_kernel(None,a,n,edges,e,s),
                                  direct_kernel(None,ginv,n,edges,e,s)):
                check(left == right, 'interior reproducing kernel')

# Exact hypercube radial moment estimates for finite d.
for d in (1,2,3,4):
    verts = list(product((0,1),repeat=d))
    idx = {v:i for i,v in enumerate(verts)}
    edges = [(idx[u],idx[tuple(u[:j]+(1,)+u[j+1:])],F(1))
             for u in verts for j in range(d) if u[j] == 0]
    a = inverse([r[:2**d] for r in gram_orthogonal(2**d,edges)[:2**d]])[0]
    shell = sum(a[i]*sum(v) for i,v in enumerate(verts))
    check(shell <= F(6,d), 'shell moment upper bound')
    check(sum(min(a[u],a[v]) for u,v,w in edges) <= shell,
          'edge min shell bound')
print('PASS:',checks,'exact-rational assertions;'
      ' independent quadratic Gram/kernel checks on',len(graphs),'graphs')
