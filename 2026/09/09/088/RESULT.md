# Certified secant-sharpness reality boundary on Gr(2,6): 14 real vs 12 real + 1 pair

## Context

The secant conjecture in real Schubert calculus asserts that an intersection
of Schubert varieties on a Grassmannian is transverse with all points real
when the defining flags are secant to a rational normal curve along pairwise
disjoint intervals. Prior evidence is large-scale floating computation
(terahertz-years) plus theorems for osculating flags (Mukhin–Tarasov–Varchenko),
a square primal-dual formulation enabling certification, and a recent
divisor/positivity form via Wronski operators. No prior source logs an
alpha-certified disjoint-vs-overlapping sharpness pair for an explicit
Gr(2,6) cell.

## Definitions

- `Gr(2,6)`: Grassmannian of 2-planes in `C^6`.
- `P = (sigma_1)^8`: eight hypersurface Schubert conditions; complex degree 14
  (Catalan number C_4).
- `gamma(t) = (1,t,t^2,t^3,t^4,t^5)` in `C^6`: fixed rational normal curve.
- Chart `H = [I_2 | M]`, `M in C^{2x4}` (8 unknowns). For each secant 4-plane
  `K_i` spanned by `gamma` at four rational parameters, one quadratic equation
  `f_i(M) = det([H; K_i]) = 0`. Total: 8 quadratics in 8 unknowns.
- Instance A (disjoint): eight groups `c + {0, 0.08, 0.16, 0.24}` with centers
  `c = -1.4 + 0.4k`, `k = 0..7`. All eight open intervals pairwise disjoint.
- Instance B (single nested overlap): same as the base except group 4 is
  `{0.04, 0.16, 0.44, 0.60}` (i.e. `6/25, 13/50, 7/25, 3/10`), group 3 is
  `{0.24, 0.26, 0.28, 0.30}`, and group 6 starts at `0.61` (not `0.60`).
  Open intervals are pairwise disjoint except one nested overlap
  `I_3 = (0.24, 0.30)` inside `I_4 = (0.04, 0.60)` (length `0.06`).
  All eight closed 4-point secant sets are pairwise disjoint.
- Smale threshold: `(13 - 3*sqrt(17))/4 = 0.15767...`; certificates use the safe
  lower bound `0.157671` (reported as `0.1577`).

## Result

For `P = (sigma_1)^8` on `Gr(2,6)` in the chart above with the logged rational
secant parameters:

(a) The disjoint-interval instance has 14 certified pairwise-disjoint
transverse chart solutions, all real: each Smale alpha-certified with
`alpha <= 4.3e-9`, each in an exact-rational Krawczyk real box (`r = 1e-6`),
pairwise separation `dmin = 0.298`, exact nonzero Jacobian determinants.
Count matches the known degree 14; no additional chart solutions were found in
an 800-start search plus reseeds (global exactly-total conditional, see below).

(b) The single-nested-overlap instance (one open-interval overlap of length
`0.06`, all closed point sets disjoint) has 14 certified pairwise-disjoint
transverse chart solutions: exactly 12 real plus one complex-conjugate pair.
All 14 are Smale alpha-certified with `alpha <= 1.2e-2`; the 12 real ones each
lie in an exact-rational Krawczyk real box (`r = 1e-6`); pairwise separation
`dmin = 0.332`; exact nonzero `Q(i)` Jacobian determinants at all 14 centers.
Count matches the known degree 14; no additional chart solutions were found in
1500-2000-start searches plus an independent seed-777 reseed replay
(`VERIFY_OK n=14 nreal=12 npair=1 dmin=0.3319`).

Jointly: the disjointness hypothesis is sharp for this cell — the one-nested-
overlap deformation turns certified all-reality into a certified reality drop
(14 real vs 12 real + 1 pair).

## Proof / evidence

- System construction: exact-rational quadratic tensors built from the
  determinant expansion `det([H; K_i])` (`build_solve.py`); verified by rebuild.
- Alpha certification: exact `Q(i)` (resp. exact-Fraction complex) arithmetic
  for `beta = ||J^{-1} F||`, `gamma <= ||J^{-1}|| * S` with the standard
  quadratic majorant `S`; `alpha = beta*gamma` below threshold for all 14+14
  solutions (`alpha_base.json` max `4.28e-9`; `alpha_narrow.json` max `0.0118`).
- Reality: exact-`Fraction` interval Krawczyk `K(B) subset interior(B)` at
  `r = 1e-6` gives existence plus uniqueness of a true zero in each real box,
  hence real (`kraw_real.py` 14/14; `kraw_narrow.py` 12/12). The two remaining
  instance-B balls have `|imag| >= 0.23` versus ball radii `~1e-12` and
  conjugate centers to `1e-6`; the system has real rational coefficients, so
  they form one complex-conjugate pair.
- Transversality: `alpha < 0.1577` plus exactly invertible Jacobian (exact
  nonzero determinants in `Q` / `Q(i)` at all centers) implies convergence to a
  simple zero (Blum–Cucker–Shub–Smale alpha theory). Float determinants are a
  cross-check only.
- Separation: pairwise `dmin = 0.298` (A) / `0.332` (B) versus Newton
  corrections `beta <= 5e-13` (A) / `<= 3.7e-12` (B); 14 disjoint balls each.
- Independent replay: `verify_narrow.py` (fresh seed 777) gives
  `VERIFY_OK n=14 nreal=12 npair=1 dmin=0.3319`; disjoint instance re-found with
  14 real solutions from a fresh seed.

## Limitations

- What is rigorously certified: 14 pairwise-disjoint alpha/Krawczyk balls per
  instance with the stated reality pattern and transversality *within the
  chart* `H = [I|M]`.
- What is not independently certified: no proof that further solutions do not
  exist outside these 14 balls or outside the chart (no certified homotopy from
  a generic 14-solution instance, no rigorous complement exclusion). The total
  "14" is therefore: 14 certified disjoint solutions whose count matches the
  known complex degree 14 of `(sigma_1)^8`, with no additional solutions found
  in 800-2000-start searches plus reseeds — global exactly-total is conditional
  on chart-containment/properness. The certified 14-ball reality patterns stand
  regardless.
- "Overlapping" means exactly one nested open-interval overlap of length
  `0.06`; all other open pairs disjoint, all closed 4-point sets disjoint. It
  is the minimal one-pair hypothesis violation tested, not a proven global
  minimizer of overlap length.
- The reality drop is shape-dependent: ~90 positional single-pair
  slides/incursions near the tested bases retained all-reality; the drop
  required the nested narrow-inside-wide shape.
- Gamma bounds use the standard quadratic-only majorant; arithmetic is exact
  rational / exact `Q(i)` apart from float absolute-value norms with large
  margins.

## Reproducibility

- `python3 verify_narrow.py` — independent instance-B resolve (seed 777):
  expect `VERIFY_OK n=14 nreal=12 npair=1 dmin=0.3319`.
- `python3 run_cert_base.py` — exact-Fraction alpha certificates, instance A
  (all `alpha <= 4.3e-9`); `python3 kraw_real.py` — real Krawczyk boxes, A.
- `python3 recert_v2.py` — exact-`Q(i)` alpha + exact nonzero dets, instance B
  (all `alpha <= 1.2e-2`, `dmin = 0.332`); `python3 kraw_narrow.py` — real
  Krawczyk boxes for the 12 real solutions.
- `python3 sep_trans.py` — separation matrix + transversality, instance A.
- Parameters in `system_B_groups.json` (= `narrow_groups.json`); approximations
  in `narrow_sols.npy` / `base_sols.pkl`; system builder in `build_solve.py`.

## References

- L. Garcia-Puente et al., The Secant Conjecture in the real Schubert
  calculus, https://arxiv.org/abs/1010.0665
- N. Hein et al., The monotone secant conjecture in the real Schubert calculus,
  https://arxiv.org/abs/1109.3436
- J. D. Hauenstein, N. Hein, F. Sottile, A primal-dual formulation for
  certifiable computations in Schubert calculus,
  https://arxiv.org/abs/1406.0864
- N. Hein, Reality and Computation in Schubert Calculus,
  https://arxiv.org/abs/1307.1833
- S. N. Karp, K. Purbhoo, Universal Plucker coordinates for the Wronski map
  and positivity in real Schubert calculus,
  https://arxiv.org/abs/2309.04645
