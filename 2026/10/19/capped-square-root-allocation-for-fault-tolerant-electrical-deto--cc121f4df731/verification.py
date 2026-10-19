"""Reproduce finite checks for priced electrical-detour design on bridgeless cacti.

Requires Python 3, numpy, scipy and networkx. The theorem for arbitrary sizes
rests on the analytic KKT proof; these computations are supplementary.
"""
import math
import itertools
import numpy as np
import networkx as nx
from scipy.optimize import minimize

COUNT = 0

def verify(cond, msg):
    global COUNT
    COUNT += 1
    if not cond:
        raise AssertionError(msg)

def cycle_solution(costs, budget):
    c = np.asarray(costs, dtype=float)
    assert len(c) >= 3 and np.all(c > 0) and budget > 0
    order = sorted(range(len(c)), key=lambda j: c[j])
    sorted_c = c[order]
    n = len(c)
    good = []
    for k in range(2, n + 1):
        C = float(sum(sorted_c[:k]) / (k - 1))
        if sorted_c[k-1] <= C + 1e-10 and (k == n or C <= sorted_c[k] + 1e-10):
            good.append((k, C))
    assert good
    k, C = good[-1]
    H = (k-1)*math.sqrt(C) + sum(math.sqrt(v) for v in sorted_c[k:])
    r = H*np.sqrt(np.maximum(c, C))/budget
    w = 1/r
    optimum = H*H/budget
    return w, optimum, C, k, H

def detour_value_cycle(w):
    r = 1 / np.asarray(w)
    return max(sum(r) - r)

def full_resistance_after_deleting(G, edge, weights):
    g = G.copy()
    g.remove_edge(*edge)
    v = list(g.nodes())
    mapping = {x:i for i,x in enumerate(v)}
    L = np.zeros((len(v),len(v)))
    for e in g.edges():
        wt = weights[frozenset(e)]
        a,b = [mapping[x] for x in e]
        L[a,a] += wt;L[b,b] += wt
        L[a,b] -= wt;L[b,a] -= wt
    if not nx.has_path(g, *edge):
        return float('inf')
    d = np.zeros(len(v))
    d[mapping[edge[0]]] = 1
    d[mapping[edge[1]]] = -1
    return float(d @ np.linalg.solve(L + np.ones_like(L)/len(v), d))

def build_cactus(lengths):
    # A bouquet is a cactus, but the theorem also allows arbitrary block trees.
    G = nx.Graph()
    top = 0
    pos = 1
    cycles=[]
    for q, length in enumerate(lengths):
        parent = 0 if q % 2 == 0 else (cycles[-1][1][0][1] if cycles else 0)
        vertices = [parent] + list(range(pos, pos+length-1))
        pos += length - 1
        edges = [tuple(sorted((vertices[i],vertices[(i+1)%length]))) for i in range(length)]
        G.add_edges_from(edges)
        cycles.append((length,edges))
    return G, cycles

rng = np.random.default_rng(33132)
for n in range(3, 10):
    for case in range(18):
        c = np.exp(rng.uniform(-2.2, 2.2, n))
        budget = float(rng.uniform(.1, 20))
        w, val, C, k, H = cycle_solution(c, budget)
        verify(abs(np.dot(c,w)-budget) < 1e-8*budget, 'budget')
        verify(abs(detour_value_cycle(w)-val) < 1e-8*val, 'analytic objective')
        verify(min(c) < C and C <= max(c) * n/(n-1), 'threshold range')
        verify(k >= 2, 'two-or-more equal maximal allocations')
        # Independent numerical constrained optimizer in resistance coordinates.
        # For fixed maximum detour 1, minimize strictly convex sum c_i/r_i.
        x0 = 1/(val*w)
        n_ = len(c)
        constraints = [{'type':'ineq','fun':lambda x,i=i:1 - np.sum(x) + x[i]} for i in range(n_)]
        res = minimize(lambda x: np.sum(c/x), x0*0.9,
                       jac=lambda x:-c/x**2,
                       bounds=[(1e-9, None)]*n_, constraints=constraints,
                       method='SLSQP',options={'ftol':1e-10,'maxiter':400})
        verify(res.success or (max(np.sum(res.x)-res.x) <= 1+1e-7 and abs(res.fun-H*H) <= 1e-7*H*H), f'optimizer residual {res.message}')
        verify(np.sum(c/res.x) >= H*H - 1e-6*H*H, 'global value numeric')
        # An arbitrary feasible perturbation cannot beat the analytic bound.
        raw = np.exp(rng.normal(size=n))
        candidate = budget*raw/np.dot(c,raw)
        verify(detour_value_cycle(candidate) >= val*(1-1e-10), 'competitor')

for prices in ([1,1,1],[1,1,2],[1,1,3],[1,4,25,64],[1,2,3,4,5]):
    c = np.array(prices, dtype=float)
    w, val, C, k, H = cycle_solution(c, 10)
    verify(abs(val - detour_value_cycle(w)) < 1e-10,'worked example')

for lengths in ([3,3],[3,4],[3,4,5],[4,5,6,3]):
    G, blocks = build_cactus(lengths)
    raw_costs=[];Hs=[]
    for n, edges in blocks:
        c=np.exp(rng.uniform(-1,2,len(edges)))
        raw_costs.append(c)
        Hs.append(cycle_solution(c,1)[4])
    total = sum(H*H for H in Hs)
    budget = 19.
    weights = {}
    for (n,edges),c,H in zip(blocks,raw_costs,Hs):
        local_budget=budget*H*H/total
        w,val,C,k,h = cycle_solution(c,local_budget)
        verify(abs(val-total/budget)<1e-8,'equalized block outage')
        for e,v in zip(edges,w):weights[frozenset(e)]=v
    for n,edges in blocks:
        for e in edges:
            r=full_resistance_after_deleting(G,e,weights)
            verify(abs(r-total/budget)<1e-7*total/budget or r<total/budget*(1+1e-7),'electrical matrix compared with closed form')
    verify(abs(sum(c[i]*weights[frozenset(e)] for (n,edges),c in zip(blocks,raw_costs)
               for i,e in enumerate(edges))-budget)<1e-8,'global budget')

print(f'PASS {COUNT} assertions; independent numerical optimization and Laplacian inversion checks')
