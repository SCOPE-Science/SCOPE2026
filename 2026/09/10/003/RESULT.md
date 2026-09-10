# Uniform real zero-free half-line for a signed-K4 subdivision family

## Context

Sharp real zero-free intervals for signed-graph chromatic polynomials and
extremal signed chromatic roots lie on the recognized Zaslavsky
signed-coloring / Sokal-Jackson zero-freeness / matroid
characteristic-polynomial frontier. Generic complex large-|q| discs apply to
any fixed graph but give no sharp uniform real half-line for a specific
infinite signed family. This record decides such an interval for the
canonical one-parameter positive-path deformation of the unbalanced
signed K4.

## Definitions

Let Sigma_0 be the unbalanced signed K4 with exactly one negative edge
e* = 12 and all other edges positive. For n >= 1 let F_n be the signed
graph obtained by replacing the positive edge 34 (the unique edge disjoint
from e*) by a positive path of length n; |V(F_n)| = n+3.
Work in Zaslavsky's signed coloring: for odd q = 2k+1, colors
{-k,...,k}; a coloring is proper if c(v) != c(w) on positive edges and
c(v) != -c(w) on negative edges. Let P_n(q) = P_{F_n}(q) count proper
colorings on all odd q; this determines the signed chromatic polynomial.
All root claims are in this q-normalization (unsigned-K4 comparison frame:
unsigned K4 has chromatic roots 0,1,2,3).

## Result

With explicit a = 3 (<= 4), for every n >= 1, P_n has no real zero in
[a, infinity).

Stronger sharp form: no P_n vanishes on (2, infinity), and P_n(2) = 0
for every odd n. Hence 2 is the optimal uniform barrier.

Exact closed form (valid as polynomials):

  q * P_n(q) = (q-1)^2 * S_n(q),
  S_n(q) = (q-1)^n * f(q) + (-1)^n * g(q),
  f(q) = q^2 - 3q + 3, g(q) = 2q - 3.

Consequences: S_n(0) = 0 so P_n is a polynomial, monic of degree n+3;
(q-1)^2 divides P_n. Head values:
P_1 = (q-1)^2 (q-2)^2,
P_2 = q^5 - 7q^4 + 21q^3 - 32q^2 + 24q - 7,
P_3 = q^6 - 8q^5 + 28q^4 - 55q^3 + 63q^2 - 39q + 10.

Head real-root data (Sturm-certified, disjoint rational boxes):
P_1: 2 distinct real roots, [63/64,65/64] ni 1, [127/64,129/64] ni 2;
P_2: 2 distinct real roots, [63/64,65/64] ni 1, [91/64,185/128] ni ~1.43016;
P_3: 3 distinct real roots, [63/64,129/128] ni 1, [199/128,101/64] ni ~1.56984,
  [127/64,257/128] ni 2.

## Proof / Evidence

Lemma 1 (closed form via transfer matrix / deletion-contraction induction):
Delete negative edge e*; H_n = F_n - e* is all-positive. Fix colors of e*
endpoints (c_1,c_2) = (a,b) with a != -b. With M = J - I (q x q) the
positive-path transfer matrix, M^k = ((q-1)^k - (-1)^k)/q * J + (-1)^k I.
Path-endpoint counts A_k = s^T M^k s = (q-1)/q ((q-1)^{k+1} + (-1)^k) for
a = b != 0 and B_k = s'^T M^k s' = (q-2)/q ((q-2)(q-1)^k + 2(-1)^k) for
a != b both satisfy X_{k+1} = (q-2) X_k + (q-1) X_{k-1}. Admissible (a,b)
pairs with a != -b: q-1 diagonal plus (q-1)^2 off-diagonal, giving
P_n = (q-1) A_n + (q-1)^2 B_n, which simplifies to the boxed identity.
Agreement on all odd q lifts to polynomial identity.

Lemma 2 (eigenvalue-dominance uniform sign on (2,infinity)):
f = (q-1)(q-2)+1 > 0 and g = 2(q-2)+1 > 0 on q > 2. Even n: both summands
of S_n positive. Odd n: exact identity (q-1)f - g = q(q-2)^2 and
(q-1)^n >= (q-1) give S_n >= (q-1)f - g = q(q-2)^2 > 0 on q > 2.
Hence P_n > 0 on (2,infinity) for all n; a fortiori none on [3,infinity).
Sharpness: S_n(2) = 1 + (-1)^n, so P_n(2) = 0 for all odd n.

General even-n monotonicity: S_n' = (q-1)^{n-1}(n f + (q-1)(2q-3)) + 2(-1)^n;
SoS identities f - 3/4 = (q-3/2)^2 and (q-1)(2q-3) + 1/8 = 2(q-5/4)^2 give
S_n' > 0 on [1,infinity) for even n >= 2 (at least 2; at least 27/8 on
[2,infinity)), and S_n(1) = -1 < 0 < 2 = S_n(2), so every even P_n has
exactly one real root > 1, pinned in (1,2), for all n.

Lemma 3 (Heilmann-Lieb backbone instance): path matching polynomials
m_k(x) = x m_{k-1} - m_{k-2} (m_0 = 1, m_1 = x), k <= 8, are fully
real-rooted in boxes of width <= 1/64 with rightmost box < 2 (largest
roots < 1.9) and consecutive interlacing by exact Sturm-count midpoint
alternation. Auxiliary to the main implication; not asserted for P_n
themselves (non-real-rooted for n >= 2).

Machine evidence (stdlib only, exact Fractions/Sturm/backtracking):
`python3 output/artifacts/verify.py` -> CHECKS=237 VERIFY_OK, covering
brute-force Zaslavsky counts n <= 4, q <= 7 vs formula; all exact
identities, recurrences and recomposition; Sturm V(3)-V(inf) = 0 for
n <= 6; certified census n <= 12 (zero roots in (2,inf), exactly one in
(1,2) for n >= 2); even-n derivative/SoS/pinning; k <= 8 matching
real-rootedness and interlacing; F_1-F_3 disjoint Sturm-1 boxes with
total-count match and leaf recomposition.

## Limitations

- Certificate is in Zaslavsky's signed-chromatic q-counting normalization
  (odd-q evaluations); no claim about other normalizations.
- Interlacing is certified for path-backbone matching polynomials (k <= 8),
  not for P_n themselves (complex pairs exist for n >= 2).
- Even-n root trend values toward 2 (1.430, 1.480, 1.495, 1.499 for
  n = 2,4,6,8) are numpy numerics (~1e-6), not Sturm-certified; only the
  uniform (2,infinity) freeness and exact odd-n root 2 are certified.
- Remark lower bound: S_n' >= 2 on [1,infinity) (>= 27/8 on [2,infinity))
  for even n >= 2; the uniform 27/8 phrasing on [1,infinity) is corrected here.

## Reproducibility

Run `python3 output/artifacts/verify.py` (stdlib only: fractions, json, os,
math for dyadic snapping) to replay all 237 exact checks and regenerate plus
re-verify `output/artifacts/fallback_table.json` (F_1-F_3 polynomials,
distinct-real counts, isolating intervals, transfer-tree leaf logs).

## References

- M. Beck et al., The Chromatic Polynomials of Signed Petersen Graphs,
  arXiv:1311.1760. Fixed signed Petersen and signed K_n (n <= 5) polynomials;
  no subdivision family or interval.
- B. Jackson, A. Procacci, A. D. Sokal, Complex zero-free regions at large
  |q| for multivariate Tutte polynomials, arXiv:0810.4703. Generic complex
  discs; no sharp real half-line for F_n.
- D. Sehrawat, B. Bhattacharjya, Chromatic Polynomials of Signed Book
  Graphs, arXiv:2206.08580. Unrelated book-graph family B(m,n).
- G. R. W. Greaves, J. Syatriadi, C. I. Utomo, Chromatic polynomials of
  signed graphs and dominating-vertex deletion formulae, arXiv:2407.00883.
  Joins/threshold families; no subdivision family or uniform real interval.
- N. Goregaokar, Interpreting the (signed) chromatic polynomial coefficients
  via hyperplane arrangements, arXiv:2506.00941. Coefficient interpretation;
  no family root locus.
