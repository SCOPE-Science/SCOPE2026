"""Standalone small-state test for the power-versus-product evolutionary-game theorem.
This is a finite sanity check, not a proof of the all-hypergraph assertion.
"""
import math
from itertools import product

N = 4
triads = ((0, 1, 2), (0, 1, 3))
alpha, r, mu = 0.2, 3.0, 0.25
states = list(product((0, 1), repeat=N))
index = {s: k for k, s in enumerate(states)}
neighbors = {i: set() for i in range(N)}
tri_inc = {i: [] for i in range(N)}
for e in triads:
    for i in e:
        tri_inc[i].append(e)
        neighbors[i].update(j for j in e if j != i)
assert all(neighbors.values())

def utility(s, gamma):
    u = [0.0] * N
    for i in range(N):
        for tri in tri_inc[i]:
            total = sum(s[j] for j in tri)
            benefit = float(total == 3) if gamma is None else (total / 3.0) ** gamma
            u[i] += 3 * alpha * r * benefit - s[i]
        u[i] /= len(tri_inc[i])
    return u

def kernel(gamma):
    rows = []
    for s in states:
        u = utility(s, gamma)
        row = [0.0] * len(states)
        for i in range(N):
            for j in neighbors[i]:
                p_pair = 1.0 / (N * len(neighbors[i]))
                p_copy = 1.0 / (1.0 + math.exp(u[i] - u[j]))
                pbit = p_copy * s[j] + (1 - p_copy) * s[i]
                pbit = mu + (1 - 2 * mu) * pbit
                new = list(s)
                new[i] = 1
                row[index[tuple(new)]] += p_pair * pbit
                new[i] = 0
                row[index[tuple(new)]] += p_pair * (1 - pbit)
        assert abs(sum(row) - 1) < 1e-13
        rows.append(row)
    return rows

def tv(a,b):
    return 0.5 * sum(abs(x-y) for x,y in zip(a,b))

def relative_entropy(a,b):
    assert all(x == 0 or y > 0 for x,y in zip(a,b))
    return sum(x * math.log(x/y) for x,y in zip(a,b) if x>0)

def matmul(a,b):
    m=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(m)) for j in range(m)] for i in range(m)]

p_infty=kernel(None)
q=2/3
for gamma in (1, 2, 4, 8, 16):
    p=kernel(gamma)
    theta=1.0
    delta=1.5*alpha*r*theta*(1-2*mu)*q**gamma
    max_tv=max(tv(a,b) for a,b in zip(p,p_infty))
    assert max_tv <= delta+1e-12, (gamma,max_tv,delta)
    eta=delta/2
    assert max_tv <= eta+1e-12, (gamma,max_tv,eta)
    max_kl=max(relative_entropy(a,b) for a,b in zip(p,p_infty))
    assert max_kl <= eta*eta/(mu*(1-mu))+1e-12, (gamma,max_kl)
    for s in states:
        u=utility(s,gamma)
        v=utility(s,None)
        assert max(abs(x-y) for x,y in zip(u,v)) <= 3*alpha*r*q**gamma+1e-12
    # The witness state (C,C,D,C) gives matching exponential order.
    s=(1,1,0,1)
    assert tv(p[index[s]], p_infty[index[s]]) > 0

# Explicit N-step minorization lower bound for mu in (0,1/2].
p4=p_infty
for _ in range(N-1):
    p4=matmul(p4,p_infty)
lower=(mu/N)**N
assert min(x for row in p4 for x in row) >= lower-1e-15

# Check the asymptotic rate for the witness, not only positivity.
ref=index[(1,1,0,1)]
ratio=[]
for gamma in (12,18,24):
    ratio.append(tv(kernel(gamma)[ref],p_infty[ref])/q**gamma)
assert max(ratio)-min(ratio)<0.01
assert min(ratio)>0.001
print('VERIFY_OK', 'N=',N,'asymptotic_row_TV_coefficient=',ratio[-1])
