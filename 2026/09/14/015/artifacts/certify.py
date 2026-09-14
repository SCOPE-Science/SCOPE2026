"""Reproducible certificate for lane-1856 target:
phi1 in Out(F4), Phi1: a->bc, b->c, c->d, d->a.

Certifies:
 (1) Phi1 is an automorphism (explicit inverse).
 (2) Transition matrix M: det -1, char poly x^4-x-1, M^10 strictly positive
     (primitivity => PF eigenvalue strictly dominant, >= 5**(1/10) > 1).
 (3) Train-track property: Df, gates, unique illegal turn {A,B}.
 (4) Taken turns = exact Df-orbit of {B,c}: 13 turns; {A,B} never taken.
 (5) LW connected; SW (=LW minus B) = K_{3,4}: 7 vertices, 12 edges, connected.
 (6) Illegal turn of f^k is {A,B} only, for 1<=k<=12 (hence all k by periodicity
     argument checked on orbits); taken sets contain no {A,B}.
"""
import numpy as np
from itertools import combinations

names = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']

def inv(x):
    return x + 4 if x < 4 else x - 4

# images of the 8 oriented edges
f = {0: [1, 2], 1: [2], 2: [3], 3: [0]}
for e in range(4):
    f[e + 4] = [inv(x) for x in reversed(f[e])]

# (1) explicit inverse automorphism Psi: a->d, b->ab^-1, c->b, d->c
# check Psi(Phi(x)) reduces to x for all generators (free-group reduction)
Psi = {0: [3], 1: [0, 5], 2: [1], 3: [2],
       4: [6], 5: [1, 4], 6: [5], 7: [0 + 4]}  # inverses forced below
# build inverse images properly: Psi(x^-1) = Psi(x)^-1
for e in range(4):
    w = Psi[e]
    Psi[e + 4] = [inv(x) for x in reversed(w)]

def red(w):
    st = []
    for x in w:
        if st and st[-1] == inv(x):
            st.pop()
        else:
            st.append(x)
    return st

for e in range(8):
    comp = []
    for x in f[e]:
        comp.extend(Psi[x])
    assert red(comp) == [e], (e, comp, red(comp))
print("(1) automorphism with explicit inverse: OK")

# (2) transition matrix
M = np.zeros((4, 4), dtype=int)
for e in range(4):
    for x in f[e]:
        M[e, x if x < 4 else x - 4] += 1
assert M.tolist() == [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0]]
assert round(np.linalg.det(M)) == -1
cp = np.poly(M.astype(float))  # char poly coefficients
assert [round(c) for c in cp] == [1, 0, 0, -1, -1], cp
p = lambda t: t**4 - t - 1
assert p(1.22) < 0 < p(1.221)  # PF root in (1.22, 1.221)
M10 = np.linalg.matrix_power(M, 10)
assert (M10 > 0).all(), M10
rsmin = int(M10.sum(axis=1).min())
assert rsmin == 5  # rho(M)^10 >= 5 so rho >= 5**(1/10) ~ 1.1746 > 1
print("(2) M det=-1, charpoly x^4-x-1, PF root in (1.22,1.221), M^10>0: OK")
print("M^10 =\n", M10.tolist())

# (3) direction map, gates, illegal turn
Df = {e: f[e][0] for e in range(8)}
# gates: d1~d2 iff Df^k(d1)==Df^k(d2) for some k (check k<12, orbits preperiodic)
traj = {d: [d] for d in range(8)}
for d in range(8):
    for _ in range(12):
        traj[d].append(Df[traj[d][-1]])
parent = list(range(8))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

for d1 in range(8):
    for d2 in range(8):
        if any(traj[d1][k] == traj[d2][k] for k in range(13)):
            a, b = find(d1), find(d2)
            if a != b:
                parent[a] = b
from collections import defaultdict
gates = defaultdict(list)
for d in range(8):
    gates[find(d)].append(d)
gate_list = sorted([sorted(v) for v in gates.values()])
assert gate_list == [[0], [1], [2], [3], [4, 5], [6], [7]], gate_list
illegal = [tuple(sorted((d1, d2))) for d1 in range(8) for d2 in range(d1 + 1, 8)
           if find(d1) == find(d2)]
assert illegal == [(4, 5)], illegal
# Df permutes gates -> legal turns map to legal turns; images contain no {A,B}
for e in range(4):
    w = f[e]
    for i in range(len(w) - 1):
        assert tuple(sorted((inv(w[i]), w[i + 1]))) != (4, 5)
print("(3) 7 gates, unique illegal turn {A,B}, f-images legal: OK")

# (4) taken turns = Df-orbit of seed {B,c} = {5,2} sorted -> (2,5)
def Df_turn(t):
    return tuple(sorted((Df[t[0]], Df[t[1]])))

seed = (2, 5)
orbit = []
cur = seed
while cur not in orbit:
    orbit.append(cur)
    cur = Df_turn(cur)
assert len(orbit) == 13, orbit
assert (4, 5) not in orbit  # illegal turn never taken
# every taken turn is mixed sign (one positive 0..3, one negative 4..7)
for t in orbit:
    assert (t[0] < 4) != (t[1] < 4), t
# cumulative turns in f^k(e) stabilize exactly to orbit
def itword(e, k):
    w = [e]
    for _ in range(k):
        nw = []
        for x in w:
            nw.extend(f[x])
        w = nw
    return w

cum = set()
for K in range(1, 25):
    for e in range(4):
        w = itword(e, K)
        for i in range(len(w) - 1):
            cum.add(tuple(sorted((inv(w[i]), w[i + 1]))))
assert cum == set(orbit), (len(cum), sorted(cum))
print("(4) taken turns = 13 (Df-orbit of {B,c}), {A,B} never taken: OK")

# (5) LW connected; SW = K_{3,4}
adj = defaultdict(set)
for t in orbit:
    adj[t[0]].add(t[1])
    adj[t[1]].add(t[0])
seen = {0}
stack = [0]
while stack:
    v = stack.pop()
    for u in adj[v]:
        if u not in seen:
            seen.add(u)
            stack.append(u)
assert seen == set(range(8)), seen  # LW connected
sw_edges = [t for t in orbit if 5 not in t]  # drop nonperiodic direction B=5
assert len(sw_edges) == 12
verts = sorted({v for t in sw_edges for v in t})
assert verts == [0, 1, 2, 3, 4, 6, 7]  # 7 periodic directions
# bipartition positives {a,b,c,d} x negatives {A,C,D}: all 12 pairs present
pairs = {(t[0], t[1]) for t in sw_edges}
full = {(p, n) for p in [0, 1, 2, 3] for n in [4, 6, 7]}
norm = set()
for a, b in pairs:
    norm.add((a, b) if a < 4 else (b, a))
assert norm == full, norm
# SW connected
adj2 = defaultdict(set)
for t in sw_edges:
    adj2[t[0]].add(t[1])
    adj2[t[1]].add(t[0])
seen = {0}
stack = [0]
while stack:
    v = stack.pop()
    for u in adj2[v]:
        if u not in seen:
            seen.add(u)
            stack.append(u)
assert seen == set(verts)
degs = sorted([len(adj2[v]) for v in verts])
assert degs == [3, 3, 3, 3, 4, 4, 4], degs
print("(5) LW connected; SW = K_{3,4} (7 vertices, 12 edges, connected): OK")

# (6) illegal turns of f^k are {A,B} only for 1<=k<=12
DfK = {d: d for d in range(8)}
for k in range(1, 13):
    DfK = {d: Df[DfK[d]] for d in range(8)}
    ill = [tuple(sorted((d1, d2))) for d1 in range(8) for d2 in range(d1 + 1, 8)
           if DfK[d1] == DfK[d2]]
    assert ill == [(4, 5)], (k, ill)
print("(6) unique illegal turn {A,B} persists for powers 1..12: OK")

print("index sum = 1 - 7/2 =", 1 - 7 / 2)
print("ALL CERTIFICATE CHECKS PASSED")
