# Certified Gauss–Kuzmin discrepancy table and badly-approximable extremal for nine committed quadratic surds and cubic irrationals (N = 2000)

## Context

Whether explicit algebraic numbers of degree ≥ 3 follow the Gauss–Kuzmin (GK) law and
Khinchin statistics is an open, actively debated metric-number-theory question:
Sibbertsen et al. (arXiv:2208.14359) apply Kullback–Leibler divergence and argue the GK
fit is poor for degree > 2 algebraics, with per-number bounds. Exact partial-quotient
data, convergent-based approximation constants, and discrepancy tallies for named
small-height quadratic surds and cubic Pisot numbers are the raw material for
Hurwitz / Roth / Jarník–Besicovitch tests of badly-approximable versus
very-well-approximable behaviour. Badly approximable ⟺ bounded partial quotients is
standard; quadratic surds have periodic continued fractions hence are badly
approximable; max c(x) = 1/√5 (MathWorld, Badly Approximable).

## Definitions

- The nine committed (polynomial, root selector, rational isolation interval) triples:
  1. √2: x²−2, positive, [1.4142, 1.4143];
  2. √3: x²−3, positive, [1.7320, 1.7321];
  3. φ: x²−x−1, positive (golden ratio), [1.6180, 1.6181];
  4. √7: x²−7, positive, [2.6457, 2.6458];
  5. plastic: x³−x−1, unique real (smallest Pisot), [1.3246, 1.3248];
  6. tribonacci: x³−x²−x−1, unique real, [1.8392, 1.8393];
  7. r7: x³−x²−1, unique real, [1.4655, 1.4657];
  8. ∛2: x³−2, unique real, [1.2599, 1.2600];
  9. rho9: x³−3x−1, largest of three real roots, [1.8793, 1.8794].
- For each α: a₀..a₁₉₉₉ are the first 2000 regular-continued-fraction partial quotients,
  pₖ/qₖ the convergents (p₋₂=0, p₋₁=1, q₋₂=1, q₋₁=0),
  M = 1999 the tally length over a₁..a₁₉₉₉ (a₀ excluded, standard GK convention),
  B = max_{k<2000} aₖ, θₖ = qₖ²|α − pₖ/qₖ|.
- GK expectations: p_k = −log2(1 − 1/(k+1)²) for k = 1..10, p_tail = 1 − Σ p_k;
  L1 = Σ|f − p|, χ² = Σ(O−E)²/E over all 11 bins (10 + tail, df = 10;
  5% critical value 18.31). Extremal rule: smallest B, tie-break lowest index.

## Result

The following finite statements are proved by the certificates in
`output/artifacts/table.json` (quotient vectors, counts, intervals) together with
the replay script `poly_cf.py` and the independent checker `verify_poly.py`
(114/114 PASS, `VERIFY_OK`):

(a) **Root isolation.** Each committed interval exhibits a strict sign change of its
polynomial at the rational endpoints (exact rational arithmetic) and contains exactly
one root (exact integer-subresultant Sturm count 1). Each polynomial is certified
rational-root-free (monic integer-divisor test).

(b) **Exact partial quotients.** For each of the 9 numbers, the logged vector
a₀..a₁₉₉₉ (plus LT+2 = 17 lookahead quotients used only for theta brackets) equals the
true regular continued fraction. Method — exact integer polynomial-shift chain: with Q₀
the minimal polynomial and Q_{k+1}(y) = y^d Q_k(m_k + 1/y) in exact integer arithmetic,
each step k is certified by E1, Q_k(m_k)·Q_k(m_k+1) < 0; E2, integer-Sturm count of Q_k
on (m_k, m_k+1) equals 1; E3, the same for Q_{k+1}; E4, exact Fraction link evaluations
forcing x_{k+1} ∈ (m, m+1). Multiple roots excluded a priori (gcd(Q,Q′) = 1 via Sturm
chain completing). Float arithmetic (mpmath secant at 4000 dps) supplies only hints;
every accepted digit is proved by E1–E4.

(c) **Convergent error bounds.** For every k ≤ 1998 and every number,
|α − p_k/q_k| < 1/(q_k q_{k+1}), verified as θ_hi(k) < q_k/q_{k+1}.

(d) **Approximation-constant intervals.** For every k < 2000,
θ_k ∈ [theta_lo[k], theta_hi[k]] with theta_lo[k] > 0, from
θ_k = 1/(x_{k+1} + q_{k−1}/q_k) and a rigorous bracket of x_{k+1} between consecutive
exact Fraction convergents LT = 15 steps down the tail. Float rounding enclosed by
relative (1e−12) plus nextafter widening; containment checked with deeper lookahead
LT2 = 20.

(e) **Tally statistics.** Per-number counts, L1, χ² recompute exactly from the logged
a-vectors (counts sum to M = 1999; verifier re-tallies independently).

(f) **Extremal.** Minimum of B uniquely at index 3 (φ) with B = 1 — the global minimum
possible for any irrational — carrying c = min-theta lower endpoint = 0.38196594…
at k* = 1, i.e. θ₁(φ) ∈ [0.38196594, 0.38196619].

Certified values (tally over a₁..a₁₉₉₉, M = 1999; χ² on 11 bins, df = 10):

| # | name | B | counts k=1..10 | tail ≥ 11 | L1 | χ² | min-θ k | θ interval |
|---|------|---|----------------|-----------|------|------|---------|------------|
| 1 | sqrt(2) | 2 | [0,1999,0,0,0,0,0,0,0,0] | 0 | 1.66015 | 9765.0 | 1 | [0.34314575, 0.34314575] |
| 2 | sqrt(3) | 2 | [1000,999,0,0,0,0,0,0,0,0] | 0 | 0.83007 | 2144.4 | 1 | [0.26794919, 0.26794919] |
| 3 | phi | 1 | [1999,0,0,0,0,0,0,0,0,0] | 0 | 1.16993 | 2817.4 | 1 | [0.38196594, 0.38196619] |
| 4 | sqrt(7) | 4 | [1500,0,0,499,0,0,0,0,0,0] | 0 | 1.05214 | 2828.0 | 3 | [0.18823820, 0.18823820] |
| 5 | plastic | 22054 | [816,341,193,108,78,57,50,40,25,27] | 264 | 0.03310 | 4.1 | 319 | [0.00004534, 0.00004534] |
| 6 | tribonacci | 10608 | [814,339,190,110,73,62,50,36,29,25] | 271 | 0.03233 | 3.9 | 1546 | [0.00009426, 0.00009426] |
| 7 | r7 | 20467 | [800,342,195,130,104,58,39,42,30,25] | 234 | 0.05451 | 12.4 | 745 | [0.00004886, 0.00004886] |
| 8 | cbrt(2) | 12737 | [854,331,175,123,87,65,42,34,28,29] | 231 | 0.04599 | 5.8 | 1989 | [0.00007851, 0.00007851] |
| 9 | rho9 | 4130 | [822,349,213,113,75,61,39,30,24,13] | 260 | 0.04682 | 12.9 | 156 | [0.00024208, 0.00024208] |

Quadratic cross-check (independent exact (P,Q)-state engine with period proved by first
state repetition): periods [2], [1,2], [1], [1,1,1,4] with preperiods 1,1,0,1;
B, L1, χ² agree exactly.

Interpretation (not part of the certified claim): the five cubics show
χ² ∈ [3.9, 12.9], all below 18.31 — no rejection of the GK fit at N = 2000 on these
examples — while the four periodic quadratics reject strongly, as expected. Large cubic
B values (4130–22054) are single large quotients, consistent with unbounded-quotient
behaviour, whereas φ's B = 1 is the classical badly-approximable extreme.

## Proof / evidence

- `poly_cf.py` (≈ 35 s; stdlib + mpmath for hints only) writes
  `output/artifacts/table.json` and prints per-number lines plus `EXTREMAL`.
- `verify_poly.py` (independent: re-derives the Q-chain from coefficients, re-checks
  E1–E4, re-tallies, re-brackets thetas with deeper lookahead, re-applies extremal rule)
  prints 114 PASS lines ending in `VERIFY_OK`.
- `qquad.py` (stdlib only, exact integer (P,Q) algorithm) writes
  `output/artifacts/quads.json`, the independent quadratic cross-check.
- Audit re-verification (independent, from polynomials only): exact Fraction sign
  changes on all 9 intervals; integer-Sturm V(lo)−V(hi) = 1 all 9; exact Fraction
  Q-chain E1 exhaustive 2000/2000 all 9 and E2+E4 exhaustive 2000/2000 all 5 cubics;
  3000-dps mpmath full-2000 agreement 0 mismatches all 5 cubics; plastic 97-term OEIS
  prefix matches; tallies/L1/χ²/B/extremal recompute exactly; theta stable-identity
  containment at all 9 minima; error-bound Fraction(hi)·q_{k+1} < q_k exhaustive
  0 violations for k ≤ 1998.

## Limitations

- Finite window k < 2000 only (plus certified lookahead to index 2016 for theta
  brackets). Proves nothing about lim inf θ_k, the true Lagrange constant, boundedness
  of quotients beyond 2000, or Khinchin/GK convergence in the limit; min-theta is the
  minimum over the computed range.
- Theta brackets depend on exact tail-quotient certification plus the elementary
  θ = 1/(x + s) identity; float-to-interval conversion is guarded by explicit widening
  and verifier containment, not by a fully formal interval-arithmetic library.
- Quadratic rows are classical (periodicity); the new, non-implied content is the five
  certified cubic N = 2000 vectors with re-tallied GK discrepancies and theta
  intervals, plus the combined 9-number extremal selection. The cbrt(2) quotient prefix
  was already listed (OEIS A002945, uncertified fixed-precision b-file); novelty rests
  on certification plus GK/theta statistics and the extremal, not on that prefix alone.

## Reproducibility

1. `python3 poly_cf.py` writes `output/artifacts/table.json`, prints per-number lines
   plus `EXTREMAL`.
2. `python3 verify_poly.py` prints 114 PASS lines ending in `VERIFY_OK`.
3. `python3 qquad.py` writes `output/artifacts/quads.json`.
Artifact inventory: `output/artifacts/table.json` (9×2000 quotient vectors, counts,
L1/χ², B, 9×2000 theta intervals, extremal), `output/artifacts/quads.json`
(independent quadratic periods), `output/artifacts/verify.log` (114 PASS),
`output/artifacts/poly_cf.log` (per-number summary + EXTREMAL).

## References

- P. Sibbertsen, T. Lampert, K. Müller, M. Taktikos, "Do algebraic numbers follow
  Khinchin's Law?", arXiv:2208.14359 (2022). https://arxiv.org/abs/2208.14359
- V. Zhuravleva, "Diophantine approximations with Pisot numbers", arXiv:1406.0518
  (2014). https://arxiv.org/abs/1406.0518
- M. Wolf, "Continued fractions constructed from prime numbers", arXiv:1003.4015
  (2010). https://arxiv.org/abs/1003.4015
- OEIS A072117, Continued fraction of smallest Pisot number (~97 terms).
  https://oeis.org/A072117
- OEIS A002945, Continued fraction for cube root of 2 (uncertified prefix + b-file).
  https://oeis.org/A002945
- MathWorld, Badly Approximable; Periodic Continued Fraction.
  https://mathworld.wolfram.com/BadlyApproximable.html
