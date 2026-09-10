# Finite-residue Hensel obstruction above a non-vertex-avoiding circle in W^1_5 of a genus-6 chain of loops

## Context

Let g=6, r=1, d=5, so rho = g-(r+1)(g-d+r) = 6-2*2 = 2.
Let Gamma6 be the chain of 6 loops with every top edge of length 12 and every
bottom edge of length 1 (total N=13 per loop). Cools-Draisma-Payne-Robeva
(CDPR) Definition 4.1 requires no l_i/m_i equal a/b with a,b>=1, a+b<=2g-2=10.
Since 12/1 hits none of the 45 such pairs (max value 9), Gamma6 is generic and
the lingering-path / component classification applies.

Cartwright-Jensen-Payne (CJP) Theorem 1.1 proves that every divisor class on a
generic chain of loops rational over the value group lifts to the same rank on
a totally degenerate curve, but only over a complete field with INFINITE
residue field: the final Hensel step needs a smooth rational point found via
infinite residue. Its sole finite-residue failure (Example 1.3) is a
vertex-supported class [v2] over F3((t)) failing because all F3-points of a P1
component are nodes — a different cell, object geometry, and obstruction
mechanism. Questions 1.4-1.5 leave general lifting open.

## Definitions

- Let C2/Q2 be the totally-split Mumford curve with skeleton Gamma6 (residue
  field F2). Work in the cell (g,r,d)=(6,1,5).
- Lingering paths in Z^1 starting at p0=(d0,) with steps in {-1,0,+1} have
  rank >=1 iff every p_i>=1 (CDPR Theorem 4.6; cited, not newly proved). With
  p0 in the open chamber (d0>=1), there are 122 valid paths, 30 with exactly 2
  lingers (=rho), 2 per linger-position pair, 15 pairs. Each such component is
  a 2-dimensional torus.
- Two such components meet above loop 3. With N=13 chip coordinates:
  - Branch A: d0=1, steps (1,0,0,-1,1,-1), lingers {2,3},
    Abel-Jacobi fixed pattern (5,.,.,1,2,0).
  - Branch B: d0=1, steps (1,-1,0,0,1,-1), lingers {3,4},
    fixed pattern (5,3,.,.,2,0).
  Both agree on the fixed loops with
    T = { AJ = (5,3,s,1,2,0) : s in R/13Z },
  the 1-dimensional circle above loop 3 where the free coordinate s runs while
  loops {1,2,4,5,6} stay fixed. T is non-vertex-avoiding in the CJP sense: it
  lies at the intersection of two maximal tori, exactly where the
  vertex-avoiding transversality argument breaks. Every class of T has tropical
  rank >=1 by CDPR Theorem 4.6 applied to the two cited lingering paths.

## Result

For the genus-6 chain Gamma6 with top lengths 12 and bottom lengths 1 and the
totally-split Mumford curve C2/Q2 with skeleton Gamma6, let T be the named
1-dimensional non-vertex-avoiding intersection circle in W^1_5(Gamma6) where
two maximal 2-dimensional torus components meet above loop 3. The initial
degeneration W0 over F2 above T, defined by the recorded local
theta-translate equations, has zero smooth F2-rational points, so no class of
T lifts to algebraic rank 1 over Q2 (Hensel-step consequence: no smooth F2
starting point to Hensel-lift).

## Proof / evidence

Following CJP Proposition 3.2, W^1_5(C2) is locally an intersection of
translates of the theta divisor. At the anchor w*=(5,3,6,1,2,0) above T (circle
parameter s=6), the two branches impose torus-plane equations in G_m^6/F2 with
multiplicative coordinates (u1..u6) (1 is the identity / anchor point):

- Branch A (free loops 2,3): u1=1, u4=1, u5=1, u6=1; u2,u3 free.
- Branch B (free loops 3,4): u1=1, u2=1, u5=1, u6=1; u3,u4 free.

Hence the recorded initial degeneration is the union
  W0 = W0,A union W0,B subset G_m^6 / F2,
  I(W0) = (u1+1, u5+1, u6+1, (u2+1)(u4+1)).
In words: u1=u5=u6=1 and (u2=1 or u4=1); u3 is free throughout. The factor
(u2+1)(u4+1) is the transverse node of the two planes along T.

G_m(F2) = {1}, so G_m^6(F2) is the single point (1,1,1,1,1,1), which satisfies
all four generators: W0(F2) = {(1,1,1,1,1,1)} (one F2-rational point).

Jacobian of (u1+1, u5+1, u6+1, (u2+1)(u4+1)) at that point in characteristic 2:
d(u1+1)=e1, d(u5+1)=e5, d(u6+1)=e6,
d((u2+1)(u4+1)) = (u4+1)e2 + (u2+1)e4 = 0 at (1)^6.
Rank = 3 < 4 = number of generators (expected codimension), so the unique
F2-point is singular. Count of smooth F2-rational points of W0: 0.

Affine-closure control (all 64 points of A^6(F2)): 6 zeros of the same
polynomials; only (1)^6 lies in the torus (singular). The other 5 zeros have a
zero coordinate, hence lie off G_m^6 and cannot be reductions of torus points;
4 are smooth points of the affine closure but outside the torus scheme W0.
Torus smooth count remains exactly 0.

Residue-specificity control (same equations over F4=F2[t]/(t^2+t+1)): W0 has
15 torus F4-points, 12 of them smooth. So the singularity obstruction is
specific to F2 — the Hensel step that CJP's infinite-residue-field proof uses
has no smooth starting point over F2 here while smooth points appear after
finite extension.

## Limitations

- Rank >=1 along T is cited to CDPR Theorem 4.6, not newly proved.
- The theta-translate form follows CJP Proposition 3.2; the new recorded
  finite-field facts are the instantiated equations at this T over Q2/F2 and
  the 2^6-scale Jacobian count.
- The final "no lift" clause is the admitted fallback's Hensel consequence of
  the verified zero-smooth-point count (no smooth F2-point to Hensel-lift),
  not a separately proved full analytic non-lifting theorem over Q2 for all of
  T. The full target (complete Mumford theta-series analysis) is not claimed.

## Reproducibility

Stdlib-only scripts, rerun to archived logs:

    python3 output/artifacts/verify_W0.py
    python3 output/artifacts/verify_W0_affine64.py
    python3 output/artifacts/step12_enumerate.py
    python3 output/artifacts/paths_tableaux.py
    python3 output/artifacts/name_T_fixed.py

Expected: VERIFY_FALLBACK_OK (torus singleton, singular, F4 15/12 control),
VERIFY_AFFINE64_OK (6 affine zeros, torus smooth count 0), GENERIC=True,
122 valid paths / 30 components / 2 per pair, T-agreement True.

## References

- Cools-Draisma-Payne-Robeva, A tropical proof of the Brill-Noether theorem,
  arXiv:1001.2774 (genericity Def 4.1, lingering paths Def 4.4 / Thm 4.6, rho).
- Cartwright-Jensen-Payne, Lifting divisors on a generic chain of loops,
  arXiv:1404.4001 (Thm 1.1 infinite-residue hypothesis, Prop 3.2 local theta
  equations, Ex 1.3 vertex-supported F3((t)) failure, Qns 1.4-1.5).
- Xiang He, Lifting divisors with imposed ramifications on a generic chain of
  loops, arXiv:1710.02288 (algebraically-closed extension; no F2 degeneration).
- Jensen-Payne, arXiv:1401.2584; Baker-Rabinoff, arXiv:1308.3864 (method context).
