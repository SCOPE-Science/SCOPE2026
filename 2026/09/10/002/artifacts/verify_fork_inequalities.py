"""Stress-test the per-block defect inequality on random embeddings (corrected).

Checks, for arbitrary Hilbert vectors at the six fork vertices
(A,T,L,R,B,U) with subcell scale L, the exact (D-free) forms actually
used in DRAFT.md:
  (H1) quadrilateral: ||t-b||^2 <= sum4 - ||l-r||^2
  (H2) per-block drop: e(C) <= ebar - ||l-r||^2/(8 L^2)
       proved by equal-weight Jensen (factor 4) + Apollonius.
  (G)  general-2UC-shaped consequence with mu=1/8 (Hilbert constant):
       e(C) <= ebar - mu*s/(2 L^2), i.e. s/(16 L^2) drop.
Any violation -> ASSERT fail. Earlier pointwise midpoint form (U1) was
dropped after it failed on random data; it is NOT used in the proof.
"""
import random

def add(a, b): return [x + y for x, y in zip(a, b)]
def sub(a, b): return [x - y for x, y in zip(a, b)]
def sc(a, c): return [c * x for x in a]
def n2(a): return sum(x * x for x in a)

def trial(rng, dim=10, L=4.0):
    rnd = lambda: [rng.uniform(-5, 5) for _ in range(dim)]
    a, t, l, r, b, u = rnd(), rnd(), rnd(), rnd(), rnd(), rnd()
    sides = [n2(sub(t, l)), n2(sub(t, r)), n2(sub(b, l)), n2(sub(b, r))]
    S = sum(sides)
    s = n2(sub(l, r))
    # H1: quadrilateral (Apollonius pair summed)
    assert n2(sub(t, b)) <= S - s + 1e-9, "H1 violated"
    # H2: per-block energy drop
    eC = n2(sub(a, u)) / (16 * L * L)
    eY = n2(sub(a, t)) / (L * L)
    eZ = n2(sub(b, u)) / (L * L)
    eS = [v / (L * L) for v in sides]
    ebar = (2 * eY + sum(eS) + 2 * eZ) / 8.0
    assert eC <= ebar - s / (8 * L * L) + 1e-9, "H2 violated"
    # G: lossy general-shaped form with mu = 1/8
    mu = 1.0 / 8.0
    assert eC <= ebar - mu * s / (2 * L * L) + 1e-9, "G violated"

rng = random.Random(7)
for i in range(3000):
    trial(rng)
print("3000 randomized trials: H1 + H2 + G all OK")
print("STRESS_OK")
