"""Finite linear-program checks for ultrametric-capped semimetric polytopes.

Requires scipy. These examples check a general symbolic theorem but do not prove it.
"""
from itertools import combinations, permutations
from math import isclose
import numpy as np
from scipy.optimize import linprog


def fixture(n, distances):
    edges = list(combinations(range(n), 2))
    w = {tuple(sorted(k)): float(v) for k, v in distances.items()}
    assert len(w) == len(edges) and all(w[e] > 0 for e in edges)
    for i, j, k in permutations(range(n), 3):
        assert w[tuple(sorted((i, j)))] <= max(w[tuple(sorted((i, k)))], w[tuple(sorted((k, j)))])
    return edges, w


def run_case(name, n, distances):
    edges, w = fixture(n, distances)
    idx = {edge: e for e, edge in enumerate(edges)}
    e_idx = lambda i, j: idx[tuple(sorted((i,j)))]
    w_ij = lambda i, j: w[tuple(sorted((i,j)))]
    m = len(edges)
    A, b = [], []
    tri_rows = []
    for i, j, k in permutations(range(n), 3):
        row = np.zeros(m)
        row[e_idx(i,j)] = 1.0
        row[e_idx(i,k)] = -1.0
        row[e_idx(j,k)] = -1.0
        A.append(row)
        b.append(0.0)
        tri_rows.append((i,j,k,row.copy()))
    for p, e in enumerate(edges):
        row = np.zeros(m)
        row[p] = 1
        A.append(row)
        b.append(w[e])
    # Independently check all directional support values using optimization.
    for i, j, k, row in tri_rows:
        lp = linprog(row, A_ub=A, b_ub=b, bounds=[(None,None)]*m, method='highs')
        assert lp.success, lp.message
        expected = -2 * min(w_ij(i,k), w_ij(j,k))
        assert isclose(lp.fun, expected, abs_tol=2e-7), (name, (i,j,k), lp.fun, expected)
    # Asymmetry LP in z=(s+1)c. z_(ik)+z_(jk)-z_(ij)>=2min(...).
    Ap, bp = [], []
    for p, e in enumerate(edges):
        row = np.zeros(m+1)
        row[p] = 1
        row[m] = -w[e]
        Ap.append(row); bp.append(0)
    for i, j, k, _ in tri_rows:
        row = np.zeros(m+1)
        row[e_idx(i,j)] = 1
        row[e_idx(i,k)] = -1
        row[e_idx(j,k)] = -1
        Ap.append(row)
        bp.append(-2*min(w_ij(i,k),w_ij(j,k)))
    obj = np.zeros(m+1); obj[m]=1
    result = linprog(obj, A_ub=Ap, b_ub=bp, bounds=[(None,None)]*m+[(1,None)],method='highs')
    assert result.success and isclose(result.fun,2,abs_tol=2e-7), (name,result)
    # Determine root clusters directly, predict coordinate-wise ranges of all centers.
    R = max(w.values())
    comps=[]
    unseen=set(range(n))
    while unseen:
        seed=unseen.pop()
        cls={seed} | {j for j in unseen if w_ij(seed,j)<R}
        unseen-=cls
        comps.append(cls)
    hbound=0.0
    if len(comps)==2:
        L=max(w[e] for e in edges if any(e[0] in cls and e[1] in cls for cls in comps))
        hbound=R-L
    for p, e in enumerate(edges):
        root_cross = (w[e]==R and len(comps)==2)
        z_high=2*w[e]
        z_low=z_high-hbound if root_cross else z_high
        for sign,expected in [(-1,-z_high),(1,z_low)]:
            objective = np.zeros(m+1)
            objective[p]=sign
            bounds=[(None,None)]*m+[(2,2)]
            sol=linprog(objective,A_ub=Ap,b_ub=bp,bounds=bounds,method='highs')
            assert sol.success and isclose(sol.fun,expected,abs_tol=2e-7), (name,e,sign,sol.fun,expected)
    print(f'{name}: n={n}, edges={m}, root_clusters={len(comps)}, center_dim={int(hbound>0)}, h_interval=[0,{hbound:g}], s=2')


if __name__=='__main__':
    run_case('equilateral 3',3,{(0,1):3,(0,2):3,(1,2):3})
    run_case('cherry 3',3,{(0,1):1,(0,2):5,(1,2):5})
    run_case('paired 4',4,{(0,1):2,(2,3):3,**{(i,j):5 for i in (0,1) for j in (2,3)}})
    run_case('star 4',4,{e:4 for e in combinations(range(4),2)})
    run_case('three clusters 5',5,{e:(2 if e==(0,1) else 3 if e==(2,3) else 5) for e in combinations(range(5),2)})
    run_case('nested 5',5,{e:(1 if e==(0,1) else 2 if set(e)<={0,1,2} else 3 if e==(3,4) else 7) for e in combinations(range(5),2)})

    # Further hierarchical instances: a seeded sequence of genuinely ultrametric caps.
    from random import Random
    rng = Random(71)
    for n in range(3, 7):
        for k in range(8):
            components = [{i} for i in range(n)]
            caps = {}
            height = 0
            while len(components) > 1:
                height += rng.randint(1, 3)
                count = rng.randint(2, min(len(components), 4))
                selected_indices = sorted(rng.sample(range(len(components)), count), reverse=True)
                selected = [components.pop(j) for j in selected_indices]
                for aa, bb in combinations(selected, 2):
                    for i in aa:
                        for j in bb:
                            caps[tuple(sorted((i, j)))] = height
                components.append(set.union(*selected))
            run_case(f'seeded n={n} case={k}', n, caps)
