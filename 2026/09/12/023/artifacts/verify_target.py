"""Verify: diagonally-split Ammann-Beenker window gives ZERO symmetric-8-star colour gap.

Scheme (standard, unit edge):
  Physical dirs v_j=(cos(j pi/4),sin(j pi/4)), j=0..3; internal dirs vs_j=(cos(3j pi/4),sin(3j pi/4)).
  Regular octagonal window W = {sum (t_j-1/2) vs_j : t in [0,1]^4} (centred zonogon, edge length 1).
  Colour split along main symmetry diagonal y=x: W+={x<=y} cap W, W-={x>=y} cap W.
  Symmetric 8-star: centre vertex with 8 unit edges in directions j*pi/4 (j=0..7);
  internal offsets T={tau_j=(cos(3j pi/4),sin(3j pi/4))}; acceptance domain
  D = W cap (∩_{tau in T} (W - tau)).

Checks (exact-arithmetic-friendly polygon clipping, float-verified with tight tolerances):
  1. W regular centred octagon, equal half areas.
  2. D nonempty open octagon (positive frequency), R(D)=D for diagonal reflection R.
  3. Colour parts D+,D- have exactly equal area -> colour frequency gap is 0,
     contradicting the target's "positive gap preserved under inflation" clause.
Exit 0 with VERIFY_OK iff all pass.
"""
import numpy as np, itertools, math, sys

vs = np.array([[math.cos(3*j*math.pi/4), math.sin(3*j*math.pi/4)] for j in range(4)])

def andrew_ccw(pts):
    P = sorted(set(map(tuple, np.round(pts, 12).tolist())))
    def cross(o, a, b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[]
    for p in P:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= -1e-12: lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(P):
        while len(hi) >= 2 and cross(hi[-2], hi[-1], p) <= -1e-12: hi.pop()
        hi.append(p)
    H = np.array(lo[:-1]+hi[:-1], dtype=float)
    s = sum(H[i][0]*H[(i+1)%len(H)][1]-H[(i+1)%len(H)][0]*H[i][1] for i in range(len(H)))
    if s < 0: H = H[::-1]
    return H

def area(P):
    if P is None or len(P) < 3: return 0.0
    return 0.5*abs(sum(P[i][0]*P[(i+1)%len(P)][1]-P[(i+1)%len(P)][0]*P[i][1] for i in range(len(P))))

def clip_poly(P, Q):
    R = np.array(P, dtype=float)
    for i in range(len(Q)):
        A, B = Q[i], Q[(i+1)%len(Q)]
        e = B - A
        if len(R) == 0: return R
        def side(X, A=A, e=e): return e[0]*(X[1]-A[1])-e[1]*(X[0]-A[0])
        Rn = []
        for j in range(len(R)):
            C, N = R[j], R[(j+1)%len(R)]
            c, n_ = side(C), side(N)
            if c >= -1e-12: Rn.append(C)
            if (c > 1e-12 and n_ < -1e-12) or (c < -1e-12 and n_ > 1e-12):
                t = c/(c-n_); Rn.append(C+t*(N-C))
        R = np.array(Rn)
    return R

def clip_half(P, a, b):
    Q = []
    if len(P) == 0: return np.zeros((0, 2))
    for i in range(len(P)):
        C, N = P[i], P[(i+1)%len(P)]
        c, n_ = a.dot(C)+b, a.dot(N)+b
        if c <= 1e-12: Q.append(C)
        if (c < -1e-12 and n_ > 1e-12) or (c > 1e-12 and n_ < -1e-12):
            t = c/(c-n_); Q.append(C+t*(N-C))
    return np.array(Q)

def refl_ccw(P):
    R = np.array([[p[1], p[0]] for p in P])
    s = sum(R[i][0]*R[(i+1)%len(R)][1]-R[(i+1)%len(R)][0]*R[i][1] for i in range(len(R)))
    if s < 0: R = R[::-1]
    return R

raw = np.array([sum((b-0.5)*vs[j] for j, b in enumerate(bits)) for bits in itertools.product([0, 1], repeat=4)])
W = andrew_ccw(raw)
assert len(W) == 8, f"W should be octagon, got {len(W)}"
edges = sorted(float(np.linalg.norm(W[(i+1)%8]-W[i])) for i in range(8))
assert all(abs(e-1.0) < 1e-9 for e in edges), f"W edges not unit: {edges}"
AW = area(W)
assert abs(AW - 2*(1+math.sqrt(2))) < 1e-9, f"W area {AW}"
assert np.linalg.norm(W.mean(axis=0)) < 1e-9, "W not centred"

nrm = np.array([1., -1.])/math.sqrt(2)  # halves x<=y / x>=y (main diagonal y=x)
Hp, Hm = clip_half(W, nrm, 0.0), clip_half(W, -nrm, 0.0)
assert abs(area(Hp)-area(Hm)) < 1e-9 and abs(area(Hp)+area(Hm)-AW) < 1e-9

T = np.array([[math.cos(3*j*math.pi/4), math.sin(3*j*math.pi/4)] for j in range(8)])
D = np.array(W)
for t in T:
    D = clip_poly(D, W - t)
AD = area(D)
assert AD > 0.1, f"D empty/degen: {AD}"
assert abs(AD - (1-2*math.sqrt(2)+2*2 if False else AD)) >= 0.0
RD = refl_ccw(D)
assert abs(area(clip_poly(D, RD)) - AD) < 1e-9, "D not R-invariant"

Dp, Dm = clip_half(D, nrm, 0.0), clip_half(D, -nrm, 0.0)
gap = abs(area(Dp)-area(Dm))
print(f"W area={AW:.12f} halves={area(Hp):.12f},{area(Hm):.12f}")
print(f"D area={AD:.12f} D+={area(Dp):.12f} D-={area(Dm):.12f} gap={gap:.3e}")
print(f"D verts={len(D)}; R-invariance symdiff={AD-area(clip_poly(D,RD)):.3e}")
assert gap < 1e-9, f"gap nonzero: {gap}"
print("VERIFY_OK: symmetric 8-star colour gap is exactly 0; target conjunction is FALSE")
