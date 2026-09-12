# Disproof of the line-capped point–plane incidence bound N^{3/2−δ} in F_q^3

## Context

Let q be an odd prime power and P, Π be sets of m points and n planes in
affine 3-space F_q^3 with m = n = N ≤ q^{3/2}. The admitted target asked
whether a non-degeneracy cap — every F_q-line contains at most N^{1/4}
points of P and lies in at most N^{1/4} planes of Π — forces a power
saving over the trivial N^{3/2} scale. Precisely, do absolute constants
C > 0 and δ = 1/20 exist such that every capped configuration satisfies
I(P,Π) ≤ C N^{3/2−δ}, where I(P,Π) counts incident point–plane pairs?
The envisioned proof route was polynomial partitioning with
ruled-component classification, using the line cap to control
line-concentrated mass on the partitioning zero set.

## Definitions

- q = r^2 with r = 3^k an odd prime power; F = F_r ⊂ F_q.
- Starter: P_0 = F^3 (|P_0| = r^3); Π_0 = planes of F_q^3 spanned by
  their F-points (|Π_0| = r^3 + r^2 + r), i.e. non-vertical planes with
  coefficients in F plus vertical planes over F-lines.
- An F-line is an F_q-line spanned by its F-points (equivalently through
  two F-points). There are r^2(r^2 + r + 1) ≤ 3r^4 F-lines meeting P_0 or
  carrying Π_0-planes.
- Thinning: keep each point of P_0 and each plane of Π_0 independently
  with probability α = 1/r, producing random (P, Π).
- N_det = floor(3r^2/4); cap thresholds A = N_det^{1/4} for points and
  the matching plane threshold.
- Failure majorant M(r) = 4e^{−r^2/48} + 16/r + 6r^4 2^{−c√r} with
  c = 2^{−1/4}.

## Result

The bound is FALSE, and in a strong sense. For every r = 3^k ≥ 6561
(hence arbitrarily large), q = r^2, there exist configurations P, Π in
F_q^3 with |P| = |Π| = N_det = floor(3r^2/4) ≤ q^{3/2}, every line
carrying at most N_det^{1/4} points of P and lying in at most
N_det^{1/4} planes of Π, yet I(P,Π) ≥ r^3/8 ≥ N_det^{3/2}/8. Hence
I/N^{3/2−1/20} ≥ r^{1/10}(r^2/N_det)^{1.45}/(8C) → ∞ as r → ∞,
violating I ≤ C N^{3/2−1/20} for every absolute constant C. In fact the
construction defeats every δ > 0, not only δ = 1/20.

## Proof / Evidence

Starter counts. Each plane of Π_0 contains exactly r^2 points of F^3,
so K_0 := I(P_0,Π_0) = |Π_0|r^2 = r^5 + r^4 + r^3; dually each point of
P_0 lies on r^2 + r + 1 planes of Π_0. Each F-line carries exactly r
points of P_0 and lies in exactly r + 1 planes of Π_0, violating the
N^{1/4} cap (r vs r^{3/4}), so thinning is required.

Only F-lines matter. If x,y ∈ P_0 are distinct, resp. H_1,H_2 ∈ Π_0 are
distinct, the unique F_q-line through x,y resp. the intersection line of
H_1,H_2 is an F-line, since the cross product of F-vectors is an
F-vector up to F_q-scaling. Hence any non-F-line carries at most one
point of P_0 and lies in at most one plane of Π_0, trivially within any
cap A ≥ 1.

Thinned means. With α = 1/r: μ_P = r^2, μ_Π = r^2 + r + 1,
E[I] = K_0/r^2 = r^3 + r^2 + r ≥ r^3. Per-F-line means are 1 (points)
and (r+1)/r = 1 + 1/r (planes).

Failure events. Sizes via multiplicative Chernoff with deviation 1/4
give 4exp(−r^2/48) total. Incidences: writing
I = Σ B_x C_H over incident starter pairs with independent Bern(1/r)
factors, disjoint index sets give independent (hence zero-covariance)
pairs; all other covariances are bounded by 1/r^3 (diagonal 1/r^2) and
class-d four-factor products by 1/r^4 as a valid majorant, yielding
Var(I) ≤ 4r^5 for r ≥ 9, so Chebyshev gives P(I < E[I]/2) ≤ 16/r.
Line caps: per-F-line multiplicative Chernoff gives
P(X_ℓ ≥ A) ≤ (e/A)^A and P(Y_ℓ ≥ A) ≤ (e(1+1/r)/A)^A; union over
≤ 3r^4 F-lines (non-F-lines contribute ≤ 1) gives at most
6r^4 2^{−c√r} once A ≥ c√r with e/A ≤ 1/2.

Existence. With N_det = floor(3r^2/4) ≥ r^2/2, A ≥ 2^{−1/4}√r. At
r = 6561, A_lower = 68.11 > 5.44 = 2e(1+1/r) and
M(6561) = 2.47×10^{−3} < 1 (Chebyshev 2.44×10^{−3}, cap 3.48×10^{−5},
size negligible), certified by output/artifacts/check_bounds.py in
log-space; the cap majorant decreases for √r > 8/(c ln 2) = 13.73, so a
good sample with sizes in the [3/4, 5/4] window, I ≥ E/2 ≥ r^3/2, and
all line loads ≤ A exists for every r = 3^k ≥ 6561.

Equalization. Delete lowest-degree vertices from the larger side until
both sides have size exactly N_det. Each deletion removes at most the
current average degree, so at least half the incidences survive each of
the two phases: I′ ≥ I/4 ≥ r^3/8. Degrees only drop, so caps persist
with threshold exactly N_det^{1/4}, and N_det ≤ r^3 = q^{3/2}.
The violation ratio diverges, with sufficient thresholds k ≥ 19/40/82
for C = 1/10/1000 (checked exactly; the r^{1/10} phrasing is a valid
sufficient lower bound for the true ratio r^3/(8CN^{1.45})).

Interpretation. The thinned configuration inherits the extremal
subfield incidence graph while line loads are O(1) on average and
O(N^{1/4}) worst-case, so no line-concentrated mass remains to charge;
the N^{1/4} cap alone is too weak to force the claimed saving.

## Limitations

The disproof is probabilistic-existential per parameter r: existence is
certified by M(r) < 1, and no derandomized explicit construction is
given, so “explicit infinite family” means an infinite sequence of
parameters with certified existence. It defeats the N^{1/4} cap but does
not characterize the optimal exponent under stronger caps. The variance
majorant Var ≤ 4r^5 is deliberately loose and the violation thresholds
are sufficient but not optimized.

## Reproducibility

Run `python3 output/artifacts/check_bounds.py`: it certifies
M(6561) = 2.47×10^{−3}, monotone decrease beyond, violation thresholds
for C = 1, 10, 1000, and N_det ≤ q^{3/2}. All constants are explicit
with no hidden dependence on q. Oddness: r = 3^k is odd and q = r^2 is
an odd prime power as required.

## References

- M. Rudnev, Point-plane incidences and some applications in positive
  characteristic, arXiv:1806.03534 (2018): upper bound
  O(m√n + mk) with n < p^2; compatible with, not implying, this disproof.
- F. de Zeeuw, A short proof of Rudnev's point-plane incidence bound,
  arXiv:1612.02719 (2016).
- L. A. Vinh, On point-line incidences in vector spaces over finite
  fields, Discrete Appl. Math. (2014).
- S. Stevens and F. de Zeeuw, An improved point-line incidence bound
  over arbitrary fields, Bull. London Math. Soc. (2017).
- X. Kong and I. Tamo, A point-variety incidence theorem over finite
  fields, arXiv:2408.10977 (2025).
