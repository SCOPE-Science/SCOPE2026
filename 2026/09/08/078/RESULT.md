# Certified metric-nodal resolution at the first generic mode of the equilateral BSS dihedral Sunada pair

## Context

Band–Shapira–Smilansky (arXiv:nlin/0608031) constructed non-isometric isospectral
Kirchhoff quantum graphs via Sunada's method and conjectured that nodal-domain
counts resolve the isospectrality. They proved asymptotically (density 1/2) that
discrete and metric counts differ for the dihedral pair with *rationally
independent* lengths (Theorems 1–2), and gave only uncertified numerics for the
7-vertex tree families (737_3, 13313_3, 13813_8). Gutkin–Smilansky
(arXiv:nlin/0105020) proved generic uniqueness for incommensurate lengths,
leaving the commensurate/Sunada case as the non-uniqueness boundary.
Alon–Band–Berkolaiko (arXiv:1709.10413) proved nodal-surplus distribution laws
without pair-specific tables. Oren–Band (arXiv:1110.0158) and Juul–Joyner
(arXiv:1801.05246) built isonodal counterexamples for *different* graphs and
mechanisms, which do not decide this canonical pair.

This record certifies the equilateral instance: the dihedral pair at unit
lengths, the symmetric boundary point where the BSS ergodic argument does not
apply as stated.

## Definitions

- Objects: the canonical dihedral Sunada pair of BSS Fig. 3 / Appendix A:
  two connected non-isometric Kirchhoff metric graphs with 2 interior vertices
  (Neumann–Kirchhoff at interior vertices; boundary conditions as in BSS Fig. 3,
  including the Dirichlet-vertex modification behind BSS (42)).
- Lengths: equilateral `a = b = c = 1` with `t = 2k`.
- Secular function (BSS (28) at equilateral):
  `F(k) = sin(t)·(9·cos²(t) − 5)`, `t = 2k`.
- Slope (BSS (33) at equilateral): `g(k) = 3·cos(t) − 2`.
- Discrete counts (BSS (34)): `μ = 1 + (1 − sign(g))/2`, i.e. `μ = 1 ⟺ g > 0`.
- Transplantation: BSS π/4-rotation matrix `T`; discrete (in)equality decided by
  certified signs of `g`, `1+g`, `1−g`.
- Metric difference (BSS (42) at equilateral):
  `δν = ½[1 − sign(g·s) + 2·sign((1+g)·s)]`, `s = sin(t)`.
- Generic mode: root of the `cos(2k) = ±√5/3` family with simple eigenvalue and
  eigenfunction nonvanishing at vertices; the singular family `k = mπ/2`
  (`sin(2k) = 0`) is excluded as non-generic.

## Result

**Theorem.** For the equilateral (`a=b=c=1`) BSS dihedral pair:

1. `F(k) = 0 ⟺ sin(2k) = 0` (singular, non-generic, `k = mπ/2`)
   or `cos(2k) = ±√5/3` (generic).
2. The first 10 generic roots lie one each in the disjoint brackets below
   (each width `8e-9 ≤ 1e-8`), with certified sign change of `F` and `F′ ≠ 0`
   (hence exactly one simple root each).
3. Genericity holds per mode: `|sin t| = 2/3 ≠ 0`,
   `g ∈ {√5−2, −√5−2}` (both nonzero), `1+g ≠ 0`, `1−g ≠ 0`.
4. Discrete counts agree through generic mode 10:
   `μ^I_n = μ^II_n`, pattern `1,2,2,1,1,2,2,1,1,2`.
5. Metric differences alternate `1,0,1,0,1,0,1,0,1,0`; the metric resolution
   index is `n⋆_gen = 1` (first generic mode distinguishes; 5 of 10 differ).
6. Completeness: each window `(jπ,(j+1)π)` in `t`, `j = 0…4`, contains exactly
   two generic roots; the four singular values `k = mπ/2`, `m = 1…4`, in range
   are certified disjoint and excluded. No generic root below bracket 10 is missed.

| generic n | k_lo | k_hi | branch cos(2k) | μ^I=μ^II | δν |
|---|---|---|---|---|---|
| 1 | 0.364863823 | 0.364863831 | +√5/3 | 1 | 1 |
| 2 | 1.205932493 | 1.205932501 | −√5/3 | 2 | 0 |
| 3 | 1.935660149 | 1.935660157 | −√5/3 | 2 | 1 |
| 4 | 2.776728820 | 2.776728828 | +√5/3 | 1 | 0 |
| 5 | 3.506456476 | 3.506456484 | +√5/3 | 1 | 1 |
| 6 | 4.347525147 | 4.347525155 | −√5/3 | 2 | 0 |
| 7 | 5.077252803 | 5.077252811 | −√5/3 | 2 | 1 |
| 8 | 5.918321474 | 5.918321482 | +√5/3 | 1 | 0 |
| 9 | 6.648049130 | 6.648049138 | +√5/3 | 1 | 1 |
| 10 | 7.489117800 | 7.489117808 | −√5/3 | 2 | 0 |

## Proof / evidence

- Hand exact algebra: BSS(28) → `sin(t)(9c²−5)`; `F′(k) = −16c` at generic
  roots so `|F′| = 16√5/3 ≈ 11.93 ≠ 0`; `g = 3c−2`; all genericity margins
  nonzero (`|sin t| = 2/3`, `|g| > 0.23`, `|1+g| > 1.23`, `|1−g| > 0.76`).
- Machine certificate (stdlib only, exact `Fraction` intervals):
  Machin-π bounds (width 1.6e-19), `√5/3` via `isqrt` (width 1e-12), rigorous
  Taylor sin/cos with Lagrange remainder (order 80, error < 1e-30), per-bracket
  `F` sign change + `F′≠0` (margin ≥ 10.9), per-mode certified signs of
  `sin`, `g`, `1+g`, `1−g`, independent window replay
  (sin-sign grid + cosine endpoint straddle + `|cos|>0.75` caps + bracket
  containment), singular-family disjointness. Script exits 0, `ALL CHECKS PASSED`.
- Auditor re-ran the script and independently recomputed all roots/patterns in
  floating point: agreement to ~1e-15 with the claimed table.

## Limitations

- Scoped to the dihedral member at equilateral lengths; the 7-vertex
  transplantation families are not treated.
- Indexing over generic modes only; singular family `k = mπ/2` excluded with
  certified disjointness (standard BSS genericity restriction).
- Certificate is rigorous stdlib interval arithmetic, not a formal
  proof-assistant derivation.
- Originality at claim level (first certified equilateral low-mode closure),
  not a new method.

## Reproducibility

Run from the workspace root:

    python3 output/artifacts/verify_equilateral_dihedral.py

Expected: `ALL CHECKS PASSED`, exit 0, regenerating
`output/artifacts/verify_log.txt` and `output/artifacts/table.json`.
Runtime: seconds to a few minutes (Taylor order-80 `Fraction` arithmetic).

## References

- R. Band, T. Shapira, U. Smilansky, Nodal domains on isospectral quantum
  graphs: the resolution of isospectrality? arXiv:nlin/0608031.
- B. Gutkin, U. Smilansky, Can one hear the shape of a graph?
  arXiv:nlin/0105020.
- L. Alon, R. Band, G. Berkolaiko, Nodal statistics on quantum graphs.
  arXiv:1709.10413.
- I. Oren, R. Band, Isospectral graphs with identical nodal counts.
  arXiv:1110.0158.
- J. S. Juul, C. H. Joyner, Isospectral discrete and quantum graphs with the
  same flip counts and nodal counts. arXiv:1801.05246.
