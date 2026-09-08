# Fixed-(29,6) 6-Regular Circulants: Ramanujan Dichotomy, Best-Expander Witness, and Spectral Reference Table

## Context

Which circulants are Ramanujan and how do spectral defects distribute inside a
fixed order-degree stratum is a recognized question in spectral graph theory,
at the Alon-Boppana boundary used for expander benchmarking (codes,
derandomization). The valency-bound literature (e.g. Hirano-Katata-Yamasaki)
gives asymptotic guarantees, not a per-type census at a fixed pair. This record
fixes the natural stratum n = 29 (prime Paley order), d = 6 (smallest
nontrivial even valency above 4-regular), quotiented to isomorphism types.
Paley-29 (14-regular) appears only as a normalized external calibration, not a
competitor.

## Definitions

- n = 29, d = 6. For 1 <= a < b < c <= 14 put
  S(a,b,c) = {+-a, +-b, +-c} subset Z_29 and C(a,b,c) = Cay(Z_29, S(a,b,c)).
- Eigenvalues: lambda_j = sum_{s in S} omega^{j s}, omega = exp(2 pi i/29),
  j = 0..28; lambda_0 = 6.
- lambda_2 = second-largest eigenvalue; lambda* = max nontrivial |lambda|
  = max(|lambda_min|, |lambda_2|).
- Ramanujan bound for d = 6: 2*sqrt(5) approx 4.47213595.
  Two-sided Ramanujan: lambda* <= 2*sqrt(5). One-sided: lambda_2 <= 2*sqrt(5).
- Defect delta = max(0, lambda* - 2*sqrt(5)).
- Normalized gap = (6 - lambda_2)/6. Energy E = sum_j |lambda_j|.
- Isomorphism: for prime order, Turner theorem — two such circulants are
  isomorphic iff connection sets differ by a multiplier u in Z_29^*.

## Result

1. Census: C(14,3) = 364 labelled triples quotient to exactly 26 isomorphism
   types, each with multiplier orbit of size exactly 14 (26 x 14 = 364).
   Canonical least-lex representatives:
   (1,2,3), (1,2,4), (1,2,5), (1,2,6), (1,2,7), (1,2,8), (1,2,9), (1,2,10),
   (1,2,11), (1,2,12), (1,2,13), (1,3,4), (1,3,5), (1,3,7), (1,3,8), (1,3,9),
   (1,3,11), (1,3,12), (1,4,5), (1,4,6), (1,4,7), (1,4,9), (1,5,11),
   (1,5,13), (1,8,9), (1,8,12).

2. Ramanujan dichotomy (two-sided, 2*sqrt(5)): exactly 12 of 26 types are
   Ramanujan and 14 are not. Ramanujan types:
   (1,2,7), (1,2,11), (1,5,13), (1,2,12), (1,2,10), (1,2,8), (1,4,5),
   (1,2,9), (1,2,6), (1,8,9), (1,5,11), (1,3,12).
   One-sided (lambda_2): 20/26 qualify. Tightest boundary: (1,3,12) at
   lambda* = 4.46967146 (margin -0.002464, Ramanujan); next non-Ramanujan
   (1,4,7) at 4.56264103 (defect +0.090505).

3. Best expander (lambda*-criterion): unique minimizer (1,2,7) with
   lambda* = 3.87666977, ahead of runner-up (1,2,11) at 3.90598165 by
   margin 0.02931188 > 1/40. Normalized gap (6-3.87666977)/6 approx 0.353888.
   The lambda_2-minimizer differs: (1,5,13) has lambda_2 = 2.33986727 but
   most-negative eigenvalue -4.02555449, so lambda* = 4.02555426 > 3.87666977.

4. Spectral reference table: all 26 types have pairwise distinct exact integer
   characteristic polynomials (26 cospectral singletons; monic, trace 0,
   [x^27]-coefficient -87 iff Tr(A^2) = 174). All 26 energies are pairwise
   distinct (26 equienergetic singletons): range 49.845813 ((1,3,5)) to
   61.498327 ((1,8,9)); minimum energy gap 0.02578660 for pair
   (1,2,4)/(1,8,12). Minimum sorted-spectrum L_infty distance 0.55397751 for
   pair (1,3,9)/(1,3,11). Full per-type (lambda_2, lambda*, defect,
   normalized gap, energy) table in artifacts/table.csv.

5. Calibration: Paley-29 eigenvalues 14, (-1+sqrt(29))/2 approx 2.19258240
   (x14), (-1-sqrt(29))/2 approx -3.19258240 (x14); normalized gap
   (14-2.19258240)/14 approx 0.843387.

## Proof / evidence

- Census and orbit sizes: exact finite exhaustion over 364 triples with
  canonical least-lex multiplier representatives; every orbit has size 14
  (kernel {+-1} forces divisibility by 14; verified equal to 14). Exact
  combinatorics, reproduced by independent stdlib re-derivation.
- Characteristic-polynomial distinctness: exact integer computation (sympy
  charpoly of 29x29 adjacency matrices); all monic, trace 0, x^27 = -87,
  pairwise distinct. Finite exact certificate.
- Spectra, dichotomy, ranking, energies: dual-method numerical linear
  algebra — closed-form DFT vs numpy eigvalsh agree to <= 2.3e-14 (max over
  types); exact Fourier-vector residuals Av - lambda v <= 5.6e-14; cross-
  validated at 80-digit precision (mpmath cos-sum). Decision margins exceed
  discrepancy by 9-12 orders: ranking margin 0.02931, energy gap 0.02579,
  tightest Ramanujan-boundary distance 0.002464. `numpy.roots` on degree-29
  polynomials was tested and rejected (ill-conditioning ~1e-3); not used.
- Isomorphism quotient uses Turner's prime-order multiplier theorem
  (standard) plus exact orbit computation; connectedness uses primality
  of 29.

## Limitations

- Spectral inequalities (Ramanujan membership, winner margin, energy
  distinctness) are certified at the level of dual-method numerical linear
  algebra plus high-precision cross-check, not interval arithmetic.
- Cospectral-singleton shape is implied by the known theorem that two
  singularly cospectral circulants on odd prime vertices are isomorphic
  (Conde et al.), since cospectrality implies singular cospectrality;
  novelty of the cospectral part lies in the explicit polynomials and table.
  Equienergetic distinctness (strictly weaker than singular cospectrality)
  and the defect ranking are not implied by that theorem.
- One-sided vs two-sided Ramanujan conventions differ (20/26 vs 12/26);
  both are tabulated; headline dichotomy is two-sided.

## Reproducibility

`output/artifacts/census.py` (stdlib + numpy + sympy) recomputes everything
in ~1 s and writes `table.csv`, `summary.json`, asserting: 364 total,
uniform orbit size 14, 26 types, DFT-vs-eigvalsh agreement < 1e-8, Fourier
residuals < 1e-9, charpoly trace identities. Run: `python3 census.py`.

## References

- M. Hirano, K. Katata, Y. Yamasaki, Ramanujan circulant graphs and the
  conjecture of Hardy-Littlewood and Bateman-Horn, arXiv:1310.2130 —
  asymptotic valency bound, not a (29,6) per-type census.
- M. Minac et al., On the Paley graph of a quadratic character,
  arXiv:2212.02005 — generalized-Paley spectra and infinite Ramanujan
  families, different family/question.
- S. Ilic, M. Basic, New results on the energy of integral circulant
  graphs, arXiv:1104.4261 — integral (gcd) class, disjoint from
  non-integral prime-order 6-regular stratum.
- L. Louis, A formula for the energy of circulant graphs with two
  generators, arXiv:1508.02348 — two-generator family, disjoint from
  three-pair (29,6) stratum.
- C. Conde et al., Singularly cospectral circulant graphs,
  arXiv:2408.07200 — even-order constructions; odd-prime singularly
  cospectral => isomorphic (implies (29,6) cospectral-singleton shape;
  does not give polynomials, energies, or defect ranking).
