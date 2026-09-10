# Rank of the matching-midpoint divisor on unit K3,3 is 0: refutation of the rank-1 gonality-gap premise

## Context

Tropical Brill–Noether theory asks which combinatorial linear series lift to
algebraic curves over a valued field. Baker's specialization inequality bounds
algebraic rank by tropical rank; the converse fails in general (Amini–Baker–
Brugallé–Rabinoff Hurwitz obstructions; Jensen–Ranganathan obstructed
realization). Low-genus trigonal geometry (Markwig–Zheng) left the explicit
rank-versus-lift gap on the named genus-4 trivalent skeleton undecided. The
admitted target claimed a first explicit gap witness on that cell.

## Definitions

- Let `Gamma0` be the metric graph `K_{3,3}` with bipartition
  `A = {a0,a1,a2}`, `B = {b0,b1,b2}` and all 9 edges of length 1.
  It is trivalent of first Betti number `9 - 6 + 1 = 4` (genus 4).
- Let `m_ij` be the midpoint of edge `a_i b_j`.
- Let `D0 = m00 + m11 + m22`, the sum of midpoints of the three
  pairwise-disjoint matching edges `a_i b_i` (effective, degree 3).
- Baker–Norine (metric) rank: `r(D) >= 1` iff `D - q` is linearly equivalent
  to an effective divisor for every point `q` of `Gamma0`; `r(D) = 0` iff `D`
  is effective up to linear equivalence but some `D - q` is not.
- `q`-reduced divisors and Dhar's burning algorithm (Baker–Norine / Luo):
  `D - q` is equivalent to an effective divisor iff its `q`-reduced
  representative has no negative entries. If Dhar burning from `q` burns the
  whole graph, `D - q` is already `q`-reduced.

## Result

On `Gamma0` (unit-length `K_{3,3}`, genus 4), the divisor
`D0 = m00 + m11 + m22` has (metric) Baker–Norine rank exactly 0, not 1.
In particular the admitted target claim — which requires `D0` to have rank
exactly 1 as the basis of a rank-vs-lift gap — is false as stated for the
named divisor. The non-liftability superstructure built on the rank-1 premise
is moot. No lift / non-lift verdict for other divisors is claimed.

## Proof / Evidence

Work on model `G2` obtained by subdividing each edge of `K_{3,3}` once:
6 original vertices plus 9 edge-midpoints (15 vertices, 18 edges,
`b1 = 18 - 15 + 1 = 4`). Since `D0` and test point `q = a0` are supported on
vertices of `G2`, vertex-set chip-firing captures metric chip-firing for this
pair (Luo), and the following Dhar burning trace is valid metrically.

Consider `D0 - a0` (`+1` at each of `m00,m11,m22`; `-1` at `a0`; `0`
elsewhere). Burn from `q = a0`: start burned (`D(a0) = -1 < 0`), then
repeatedly burn any vertex `v` with `D(v)` strictly less than its number of
edges to the burned set:

1. `a0` (origin).
2. `m01, m02` (`0 < 1` edge to `a0`).
3. `b1, b2` (`0 < 1`).
4. `m12` (via `b2`), `m21` (via `b1`).
5. `a1` (via `m12`), `a2` (via `m21`).
6. `m10` (via `a1`); then `m11` with `D = 1 < 2` burned neighbors
   (`a1, b1`), so it burns.
7. `m20` (via `a2`); then `m22` (`1 < 2` neighbors `a2, b2`).
8. `b0` (`0 < 2` neighbors `m10, m20`).
9. `m00` (`1 < 2` neighbors `a0, b0`).

Whole graph (15/15) burns — independently replayed by the auditor.
Hence `D0 - a0` is `a0`-reduced with value `-1` at `a0`, so it is not linearly
equivalent to any effective divisor (metric reduced-divisor criterion).
Therefore `r(D0) <= 0`; `D0` effective gives `r(D0) = 0`.

Corroboration:

- Exact Laplacian-lattice check: on `G2`, for `q = a0`, all
  `C(15+2-1,2) = 120` effective degree-2 divisors `E` were tested;
  `D0 - a0 - E` lies in the Laplacian lattice for none (auditor replay: 0/120
  winnable).
- Resolution robustness: Dhar sweeps at subdivisions `n = 2,4,6,8` (up to
  eighth-points) all show `D0 - a0` unwinnable, as are `D0 - b0` and
  `D0 - q` for quarter-points of non-support edges.
- Sanity controls: `3*a0` passes the same sweep (rank >= 1); canonical
  divisor has degree 6 = 2g - 2, confirming the graph model.

## Limitations

- Disproof targets the named disjoint-matching midpoint divisor only.
- Other midpoint triples (e.g. the star `m00+m01+m02`, which passes vertex
  sweeps) are not certified here.
- No lift / non-lift verdict is made since the rank premise already fails.
- Metric certification rests on vertex-supported Dhar theory (Luo) plus dyadic
  refinements, not a closed-form all-interior-point argument; the single-`q`
  reduced criterion is sufficient for the upper bound.

## Reproducibility

Pure Python 3 stdlib only:

- `output/artifacts/verify_disproof.py` prints `VERIFY_OK`; full burn log in
  `output/artifacts/verify_disproof.json`.
- `output/artifacts/dhar_rank.py`, `output/artifacts/dhar_n2_log.json`,
  `output/artifacts/bruteforce_check.py`,
  `output/artifacts/bruteforce_summary.json`,
  `output/artifacts/rank_upper_bound.py`,
  `output/artifacts/rank_upper_bound.json`.

## References

- Baker–Norine, Riemann–Roch and Abel–Jacobi theory on a finite graph.
- Amini–Baker–Brugallé–Rabinoff, Lifting harmonic morphisms II:
  Tropical curves and metrized complexes, arXiv:1404.3390.
- Jensen–Ranganathan, Brill–Noether theory for curves of a fixed gonality,
  arXiv:1701.06579.
- Markwig–Zheng, Trigonal and embedded tropical curves of low genus,
  arXiv:2602.02257.
- Aidun–Dean–Morrison–Yu–Yuan, Graphs of gonality three, arXiv:1810.08665.
- Aidun et al., Gonality sequences of graphs, arXiv:2002.07753.
