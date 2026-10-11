#!/usr/bin/env python3
"""Finite corroboration for Euclidean minimum spheres of matroid independence polytopes.

Requires NumPy and SciPy. Proof for every matroid is in RESULT.md.
"""
from fractions import Fraction
import itertools
import math
import numpy as np
from scipy.optimize import minimize, LinearConstraint, Bounds

count = 0
epigraph_count = 0

def check_matroid(m, r, rank, independent_epigraph=False):
    global count, epigraph_count
    masks = list(range(1 << m))
    rank_values = [rank(mask) for mask in masks]
    assert rank_values[0] == 0
    assert rank_values[-1] == r
    independent_masks = [mask for mask in masks if rank_values[mask] == mask.bit_count()]
    V = np.array([[(mask >> e) & 1 for e in range(m)] for mask in independent_masks], dtype=float)
    A = np.array([[(mask >> e) & 1 for e in range(m)] for mask in masks if mask], dtype=float)
    b = np.array([rank_values[mask] for mask in masks if mask], dtype=float)
    t = min(r/m, 0.5)
    q = np.full(m, t)

    opt = minimize(
        lambda x: 0.5 * float(np.sum((x-0.5)**2)),
        q, jac=lambda x: x-0.5,
        bounds=Bounds(0, 1),
        constraints=[LinearConstraint(A, -np.inf, b)],
        method='SLSQP', options={'ftol': 1e-12, 'maxiter': 500},
    )
    assert opt.success, (m, r, opt.message)
    c = opt.x
    assert np.max(A @ c-b) <= 1e-8
    assert np.min(c) >= -1e-8 and np.max(c) <= 0.5+1e-8

    R2 = m/4 - float(np.sum((c-0.5)**2))
    d2 = np.sum((V-c)**2, axis=1)
    assert abs(float(np.max(d2))-R2) < 2e-7, (m, r, R2, np.max(d2))
    w = 1-2*c
    scores = V @ w
    contacts = np.where(np.abs(scores-np.max(scores)) < 1e-8)[0]
    assert set(contacts) == set(np.where(np.abs(d2-R2) < 1e-8)[0])

    envelope = m/4 - m*(0.5-t)**2
    assert R2 <= envelope+2e-8
    feasible_q = (np.max(A@q-b) < 1e-8)
    assert (abs(R2-envelope) < 2e-7) == feasible_q
    defects = []
    for mask in masks[1:]:
        deficit = max(0, t*mask.bit_count()-rank_values[mask])
        defects.append(deficit*deficit/mask.bit_count())
    assert envelope-R2+2e-7 >= max(defects)

    if feasible_q:
        assert np.max(np.abs(c-q)) < 2e-7
        if 2*r < m:
            assert set(contacts) == {j for j,mask in enumerate(independent_masks) if mask.bit_count()==r}
        else:
            assert len(contacts) == len(independent_masks)

    if independent_epigraph:
        # An independent direct Euclidean minimax computation.
        def ineq(z):
            return z[m]-np.sum((V-z[:m])**2, axis=1)
        def jac(z):
            return np.column_stack((2*(V-z[:m]), np.ones(len(V))))
        opt2 = minimize(
            lambda z: z[-1], np.r_[np.full(m, 0.37), float(m+2)],
            jac=lambda z: np.r_[np.zeros(m), 1],
            constraints=[{'type':'ineq','fun':ineq,'jac':jac}],
            method='SLSQP',
            options={'ftol':1e-11, 'maxiter':1500},
        )
        assert opt2.success, (m,r,opt2.message)
        assert abs(opt2.fun-R2) < 3e-6
        assert np.max(np.abs(opt2.x[:m]-c)) < 4e-5
        epigraph_count += 1
    count += 1

# All uniform ranks in dimensions 2 through 8.
for m in range(2,9):
    for r in range(1,m+1):
        check_matroid(m,r,lambda mask,r=r: min(mask.bit_count(),r), m<=5)

# Nonuniform partition/direct-sum matroids; each block has a rank cap.
examples = [
    ([3,2],[1,2]), ([2,2],[1,1]), ([4,1],[1,1]),
    ([2,2,2],[1,1,1]), ([1,3,2],[1,1,2]),
    ([1,1,2,3],[1,1,1,2]), ([3,3],[1,2]),
    ([2,3,2],[1,1,2]), ([4,2],[1,1]),
]
for sizes, caps in examples:
    first=0
    block_masks=[]
    for s in sizes:
        block_masks.append(((1<<s)-1)<<first)
        first+=s
    rank=lambda mask, bm=block_masks, c=caps: sum(min((mask&bb).bit_count(), cc) for bb,cc in zip(bm,c))
    check_matroid(sum(sizes),sum(caps),rank,sum(sizes)<=6)

# Graphic matroids with the independent sets being forests.
def graphic_rank(n,edges):
    def rank(mask):
        parent=list(range(n))
        def root(v):
            while parent[v]!=v:
                v=parent[v]
            return v
        for j,(a,b) in enumerate(edges):
            if (mask>>j)&1:
                ra,rb=root(a),root(b)
                if ra!=rb:
                    parent[ra]=rb
        return n-len(set(root(x) for x in range(n)))
    return rank

graphs=[
    (3, [(0,1),(1,2),(0,2)]),
    (4, [(0,1),(1,2),(2,3),(3,0)]),
    (4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]),
    (5, [(0,1),(1,2),(2,3),(3,4),(4,0)]),
    (5, [(0,1),(0,2),(0,3),(0,4),(1,2),(2,3),(3,4)]),
]
for n,edges in graphs:
    mask_all=(1<<len(edges))-1
    rank=graphic_rank(n,edges)
    check_matroid(len(edges),rank(mask_all),rank,len(edges)<=6)

# Exact rational sharpness certificate for the direct sum U_{1,3} + U_{2,2}.
m=5
center=[Fraction(1,3)]*3+[Fraction(1,2)]*2
half=Fraction(1,2)
R2=Fraction(m,4)-sum((x-half)**2 for x in center)
envelope=Fraction(m,4)
delta=Fraction(1,2)
assert R2==Fraction(7,6)
assert envelope-R2==Fraction(1,12)==delta**2/3
contacts=0
for mask in range(1<<m):
    if (mask&7).bit_count()<=1:
        v=[Fraction((mask>>i)&1) for i in range(m)]
        d=sum((x-y)**2 for x,y in zip(v,center))
        assert d<=R2
        if d==R2: contacts+=1
assert contacts==12

print(f'VERIFY_OK matroid-independence-min-spheres profiles={count} direct_minimax={epigraph_count} rank_defects=yes exact_sharpness=yes')
