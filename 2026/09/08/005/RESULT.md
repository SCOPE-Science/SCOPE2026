# Certified annulus 0.30n ≤ |z| ≤ 0.75n for zeros of exponential partial sums s_n, 10 ≤ n ≤ 14

## Context

Zeros of the Taylor sections s_n(z) = sum_{k=0}^{n} z^k/k! govern stability
regions of Taylor time-stepping methods and Padé approximation. The classical
limit theory (Szegő curve |ze^{1-z}| = 1, Carpenter–Varga–Waldvogel asymptotics,
Saff–Varga parabolic regions) describes scaled zeros as n → ∞ but yields no
explicit finite-n enclosure. The textbook universal bound (Eneström–Kakeya)
gives 1 ≤ |z| ≤ n. Numerics show zeros clustered in a much thinner annulus.
This record certifies a concrete thin annulus over degrees 10–14.

## Definitions

- s_n(z) = sum_{k=0}^{n} z^k / k!, n ≥ 0.
- r_n = 0.30n = 3n/10; R_n = 0.75n = 3n/4 (exact rationals in certificates).
- T(r,n) = sum_{k>n} r^k/k! (exponential tail on |z| = r).
- f_n(t) = s_n(R_n e^{it}).

## Result

**Theorem.** For every integer 10 ≤ n ≤ 14, s_n has exactly n zeros in ℂ
(counted with multiplicity) and every zero z satisfies

  0.30n ≤ |z| ≤ 0.75n.

Equivalently: (A) s_n(z) ≠ 0 for |z| < 0.30n; (B) the winding number of s_n
about |z| = 0.75n equals n, so all n zeros lie in |z| < 0.75n.

Numerically: true moduli (companion matrix) are n=10: 3.64–6.56;
n=11: 3.91–7.29; n=12: 4.21–8.03; n=13: 4.48–8.78; n=14: 4.77–9.53,
strictly inside the certified annuli with margins ≥ 0.6 inner, ≥ 0.9 outer.
Improvement over Eneström–Kakeya [1,n]: outer radius cut by exactly 25%
uniformly; inner radius 3.0–4.2 instead of constant 1 (linear in n).

## Proof / Evidence

**Theorem A — inner disc (fully rigorous, exact rational arithmetic).**
On |z| = r, |e^z − s_n(z)| ≤ T(r,n) and |e^z| = e^{Re z} ≥ e^{−r}.
Write T(r,n) = a_n(1 + r/(n+2) + r²/((n+2)(n+3)) + …) with a_n = r^{n+1}/(n+1)!.
Since (n+2)…(n+j) ≥ (n+2)^{j−1}, T(r,n) ≤ a_n/(1−q_n) =: T^up with
q_n = r/(n+2) ≤ 4.2/16 < 0.27. Upper-bound e^r by the degree-30 Taylor sum
plus geometric remainder (all terms positive, q = r/32 < 1): e^r ≤ U^up.
Both T^up and U^up are computed in exact `fractions.Fraction` arithmetic and
the product compared with 1 exactly. Results (decimals are renderings; the
check is exact):

  n=10: T^up·U^up = 0.11885; n=11: 0.12652; n=12: 0.13496;
  n=13: 0.14422; n=14: 0.15435 — all < 1 (margin > 6×).

Hence |e^z − s_n| < |e^z| on |z| = r_n; by Rouché, s_n and e^z have the same
number of zeros (0) in |z| < r_n, and s_n ≠ 0 on |z| = r_n.

**Theorem B — outer circle (machine-checked disc-arithmetic certificate).**
N = 16384 nodes t_j = 2πj/N. Disc arithmetic (double centers, float radii)
encloses f_n(t_j) in D(c_j, ρ^node_j) via Horner evaluation with inflated
radii. Exact rational Lipschitz constant L_n = R_n·sum_{k<n} R_n^k/k! ≥
max|s_n'| on |z| = R_n, and exact-rational Machin π upper bound
(π = 16·atan(1/5) − 4·atan(1/239) with alternating-series remainders) give
inter-node tube τ_n = L_n·Δt^up containing each true arc. If
|c_j|_low > ρ_j + σ_j with ρ_j = ρ^node_j + τ_n and
σ_j = |c_{j+1} − c_j| (condition (*)), the true-arc-to-polygon homotopy
avoids 0. All 81920 segments pass with worst (ρ+σ)/|c|_low =
0.067, 0.081, 0.096, 0.113, 0.133 for n = 10,…,14 (margin ≥ 7.5×;
min|c| = 64.3–950.4, node radii ≤ 3.3e−08, tubes 4.04–120.7). The closed
polygon winding, computed exactly (vertices as exact Fractions, real-axis
crossing sum with exact crossing abscissa), equals 10, 11, 12, 13, 14.
By the argument principle, exactly n zeros lie in |z| < R_n, i.e. all of them.

**Evidence vs proof.** Dense 20001-gon winding sums (0 inner / n outer) and
numpy companion-matrix moduli are inexact cross-validation only, not proof.

## Limitations

- Theorem B is conditional on documented arithmetic assumptions (IEEE-754
  correct rounding of +,−,×,/; |cos−cos|,|sin−sin|,|hypot−|·|| ≤ 8 ulp);
  a machine-checked certificate, not a first-principles formal proof.
- Window restricted to 10 ≤ n ≤ 14 (inner estimate verified to n = 20 but
  not claimed with outer match).
- Annulus not claimed optimal; ~15% slack on both sides.
- Method uses textbook Rouché plus standard validated-numerics homotopy;
  contribution is the explicit finite-degree certificate and margins.

## Reproducibility

Python 3 stdlib only (`fractions`, `math`, `json`):

  python3 output/artifacts/inner_cert.py  # ends "INNER CERTIFICATE: PASS"
  python3 output/artifacts/outer_cert.py  # ends "OUTER CERTIFICATE: PASS"

Artifacts: `output/artifacts/inner_cert.py`, `output/artifacts/outer_cert.py`.

## References

- Saff & Varga (1976), Zero-Free Parabolic Regions for Sequences of
  Polynomials. https://doi.org/10.1137/0507028
- Carpenter, Varga & Waldvogel (1991), Asymptotics for the zeros of the
  partial sums of e^z. I. https://doi.org/10.1216/RMJM/1181072998
- Newman & Rivlin (1972), The zeros of the partial sums of the exponential
  function. https://doi.org/10.1016/0021-9045(72)90007-X
- Eneström–Kakeya theorem (textbook annulus bound).
  https://doi.org/10.15415/mjis.2015.32012
