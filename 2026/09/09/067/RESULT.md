# Exact Baker–Norine rank 2 of a degree-6 divisor on a genus-8 augmented hinge complex

## Context
Tropical Brill–Noether theory asks which tropical linear series lift to
algebraic curves (Baker specialization; Amini–Baker metrized complexes;
Jensen–Ranganathan fixed gonality; realizability programs). Pure chains of
loops are Brill–Noether general (CDPR). The hinge program studies the minimal
augmentation where vertex-genus gonality interacts with graph gonality. This
record certifies the exact extremal test input: a tropically BN-special
divisor (rho < 0 yet rank 2) on the named hinge complex.

## Definitions
- **M8 (exact finite metric model G):** chain of six loops L1..L6. Each loop
  is two parallel unit edges a_i–b_i (length 1 each). Consecutive loops joined
  by bridges of total length 2 via midpoint vertices:
  b1–c1–a2, b2–c2–a3, b3–dL–vs, vs–dR–a4, b4–c4–a5, b5–c5–a6, each subedge unit.
  Vertex vs = v* (between L3 and L4) carries a smooth genus-2 curve C0.
  V = 19 (a1..a6, b1..b6, c1, c2, c4, c5, dL, dR, vs), E = 24,
  graph genus E−V+1 = 6, augmented genus 6+2 = 8.
  Bridge : loop-edge ratio 2:1 as admitted.
- **Divisor:** D* = 2·(vs) + (a1) + (a2) + (b4) + (a5), deg D* = 6,
  with a1, a2, b4, a5 the designated outer vertices of L1, L2, L4, L5.
- **Rank:** Baker–Norine (graph) chip-firing rank on G: r(D) ≥ s iff D − E is
  winnable (linearly equivalent to an effective divisor) for every effective E
  of degree s; r(D) ≤ s−1 is witnessed by one unwinnable D − E of degree s.
  Vertex support tested per admitted finite criterion; cross-checked on
  midpoint-refinement models.
- **BN number:** g = 8, d = 6, r = 2 gives rho = 8 − 3·4 = −4 < 0.

## Result
On the above M8, the Baker–Norine tropical (graph) rank of D* is exactly 2.
The divisor is tropically BN-special (rank 2 with rho = −4).

## Proof / evidence
- **(i) r(D*) ≥ 2:** all 190 = C(19+2−1,2) vertex multisets {x,y} tested;
  D* − (x) − (y) is winnable in every case, 0 failures.
- **(ii) r(D*) ≤ 2:** for E = (b2)+(b3)+(b4),
  T = D* − E is unwinnable: its q-reduced divisors are ineffective for each
  probed q (archived q ∈ {a1, b2, vs, a6}), e.g. q = a1 gives
  (−1 at a1, +1 at b1, b2, b3, b4); q = vs gives (+1 at a1,a2,a3,b4,−1 at vs).
- Hence r(D*) = 2 exactly. Engine validated by Riemann–Roch spot-checks
  r(D) − r(K−D) = deg D − g + 1 (PASS, genus 6, deg K = 10).
- Independent audit: replayed both verifiers; independently verified each
  archived q-log is linearly equivalent to T (integral Laplacian firing),
  burns all vertices (q-reduced), and is ineffective; re-ran full-midpoint
  subdivision (V = 43) with 946/946 pairs winnable and triple still
  unwinnable.
- Load-bearing coordinates: the symmetric pattern 2(vs)+b1+b2+b4+b5 has
  combinatorial rank 1 (obstruction a1+b3), so the stated a1/a2/b4/a5
  placement is not interchangeable.

## Limitations
Proves graph Baker–Norine rank 2 only. Metrized-complex rank with genus-2
vertex-curve interaction (Amini–Baker) and characteristic-zero non-liftability
(no smooth genus-8 lift with skeleton M8) are NOT proved. No new general
lifting theorem. Verification set is vertex multisets per admitted criterion;
continuum interior points covered by subdivision cross-evidence as documented.

## Reproducibility
- `python3 output/artifacts/verify19.py` → `VERIFY19_OK`
  (exact 19-vertex model, 190 pairs + triple; stdlib only, seconds).
- `python3 output/artifacts/verify.py` → `VERIFY_OK`
  (31-vertex midpoint refinement, 496 pairs).
- `output/artifacts/cert19_log.json` archives pair counts and q-reduced
  obstruction logs.

## References
- Baker, Specialization of linear systems from curves to graphs
  (math/0701075) — specialization inequality, general only.
- Amini–Baker, Linear series on metrized complexes (1204.3508) — general
  metrized-complex RR/specialization; no hinge value.
- Cools–Draisma–Payne–Robeva, Tropical proof of Brill–Noether (1001.2774) —
  pure chains BN-general (opposite phenomenon).
- Lim–Payne–Potashnik, BN theory and rank determining sets (1106.5519) —
  unweighted metric graphs, no augmentation.
- Hladky–Kral–Norine, Rank of divisors on tropical curves (0709.4485) —
  finite computability.
