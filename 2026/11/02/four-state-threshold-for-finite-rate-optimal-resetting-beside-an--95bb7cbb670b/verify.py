"""Exact-rational independent checks for the weighted-graph resetting theorem.

Run with: python3 verify.py
No third-party dependencies are required. Finite checks supplement, not replace,
the analytic hazard and minimization proofs.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt

checks = 0

def eq(a, b):
    global checks
    assert a == b, (a, b)
    checks += 1

def solve(A, b):
    """Gaussian elimination over exact rational numbers."""
    n = len(b)
    R = [[F(q) for q in row] + [F(y)] for row, y in zip(A, b)]
    for i in range(n):
        j = next(k for k in range(i,n) if R[k][i])
        R[i], R[j] = R[j], R[i]
        v = R[i][i]
        R[i] = [q/v for q in R[i]]
        for k in range(n):
            if k == i: continue
            v = R[k][i]
            R[k] = [x-v*y for x,y in zip(R[k],R[i])]
    return [row[-1] for row in R]

def reset_mean(edges, r, n, source=0, target=None):
    """Target is n by default; edges include ordered or undirected rates."""
    if target is None: target = n
    Q = [[F(0) for _ in range(n)] for _ in range(n)]
    for (i,j),w in edges.items():
        w = F(w)
        if i == target or i >= n: continue
        Q[i][i] += w
        if j != target: Q[i][j] -= w
    for i in range(n):
        if i != source:
            Q[i][i] += F(r)
            Q[i][source] -= F(r)
    return solve(Q, [1]*n)[source]

# Three-vertex classification, allowing directed rates (target state 2).
for a,b,c,d,r in product([F(1,2),F(1),F(3)], [F(1,2),F(2)],
                          [F(0),F(1),F(4)], [F(0),F(1)],
                          [F(1,3),F(1),F(5)]):
    edges = {(0,2):a,(0,1):b,(1,2):c,(1,0):d}
    actual = reset_mean(edges,r,2,target=2)
    claimed = (r+b+c+d)/(a*r+a*(c+d)+b*c)
    eq(actual, claimed)

# Four-vertex symmetric weighted graph. Target 3; source 0;
# edges 0-3 weight 1, 0-1 weight 1, 1-3 weight 3, 0-2 weight 1.
edges = {(0,3):1,(3,0):1,(0,1):1,(1,0):1,
         (1,3):3,(3,1):3,(0,2):1,(2,0):1}
for k in range(0,101):
    r = F(k,5)
    actual = reset_mean(edges,r,3,target=3)
    claimed = (r*r+7*r+9)/(r*r+8*r+7)
    eq(actual, claimed)

# Unreset first-passage renewal identity at rational reset rates.
# f(s) is the Laplace transform from the killed-chain resolvent.
for k in range(1,71):
    s = F(k,6)
    # Solve (s I - Q)u=1 for the unreset killed network.
    Q = [[F(0) for _ in range(3)] for _ in range(3)]
    for (i,j),w in edges.items():
        if i == 3: continue
        Q[i][i] += F(w)
        if j != 3: Q[i][j] -= F(w)
    for i in range(3): Q[i][i] += s
    u = solve(Q,[1,1,1])[0]
    f = 1-s*u
    eq((1-f)/(s*f), (s*s+7*s+9)/(s*s+8*s+7))

# Exact polynomial identity N'D - ND' = r^2 - 4r - 23.
# Arrays are ascending coefficient order, so no symbolic package needed.
def multiply(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j]+=a*b
    return out
N=[9,7,1]; D=[7,8,1]
A=multiply([N[1],2*N[2]],D)
B=multiply(N,[D[1],2*D[2]])
eq([x-y for x,y in zip(A,B)],[-23,-4,1,0])

# Exact checks for the hazard-maximal theorem on connected 4-vertex graphs.
# All edges take values 0, 1 or 2, and the reset site's absorption
# edge dominates other direct absorption edges.
edge_pairs=[(0,1),(0,2),(1,2),(0,3),(1,3),(2,3)]
for weights in product([0,1,2], repeat=6):
    ws=dict(zip(edge_pairs,weights))
    a=ws[(0,3)]
    if a==0 or ws[(1,3)]>a or ws[(2,3)]>a: continue
    # Check undirected connectivity via reachability from vertex 0.
    reached={0}
    while True:
        more={j for (i,j),w in ws.items() if w and i in reached}
        more|={i for (i,j),w in ws.items() if w and j in reached}
        if more <= reached: break
        reached|=more
    if len(reached)<4: continue
    directed={}
    for (i,j),w in ws.items():
        if w: directed[(i,j)]=directed[(j,i)]=w
    for r in [F(0),F(1,2),F(2),F(8)]:
        actual=reset_mean(directed,r,3,target=3)
        assert actual >= F(1,a)
        checks += 1

# The unique positive derivative root and exact optimum.
root = 2 + 3*sqrt(3)
assert 0 < root and abs(root*root-4*root-23)<1e-12
checks += 1
minimum = (root*root+7*root+9)/(root*root+8*root+7)
assert abs(minimum-(2/3+sqrt(3)/6))<1e-12
checks += 1
assert minimum < 1 and F(9,7)>minimum
checks += 1
print(f"PASS: {checks} independent rational and root checks")
