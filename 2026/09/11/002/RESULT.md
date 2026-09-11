# Certified refined-LGV non-product obstruction for CSTCPP: exact 3x3 minor value and anti-product certificate (with 4x4 extension)

## Context

Cyclically symmetric transpose-complementary plane partitions (CSTCPP) in the
even box B(2r,2r,2r) have a known unrefined product count (Mills–Robbins–Rumsey;
Andrews 1987; DLMF 26.12.15). No refined q-generating function for CSTCPP is
tabulated (DLMF §26.12(ii) lists only unrestricted, symmetric, cyclically
symmetric, and descending-plane-partition products). The admitted target was a
refined LGV product identity det M_4(q;t) = R_4(q;t) at the 8-box; the preset
fallback was a weight-preservation certificate plus a closed Andrews-type
product for the principal 3x3 minor. Both product identities were blocked by
exact computation. This record banks the obstruction that blocked them.

## Definitions

Let q be an indeterminate and
E(i,j) = q^{C(K,2)} · qBinom(i+j, K), K = 2j−i,
with E(i,j) = 0 when K is out of range (0 ≤ K ≤ i+j).
Here qBinom denotes the Gaussian binomial and C(K,2) = K(K−1)/2 is the
standard area-weight exponent; this is the fallback's own stipulated
area-weighted CSTCPP Lindström–Gessel–Viennot data (q = 1 specializes to the
integer matrix binom(i+j, 2j−i)).
The leading principal 3x3 minor M3 uses rows/cols 0,1,2.
Write [n]_q = 1+q+...+q^{n−1} for a q-integer.
An Andrews-type closed q-integer product means a product of q-integers
(up to a q-power and constant); the naive n = 3 quotient candidate R3 is the
termwise q-analog of the DLMF 26.12.15 product.

## Result

1. M3 = [[1,0,0],[0,q+1,q^3],[0,1,q^5+q^4+2q^3+q^2+q]] and
   det(M3) = q^6+2q^5+3q^4+2q^3+2q^2+q = q·S3,
   S3(q) = q^5+2q^4+3q^3+2q^2+2q+1, S3(1) = 11
   (the unrefined CSTCPP n = 3 count).
2. S3 is not an Andrews-type closed q-integer product:
   ZZ-irreducible (sympy factor_list singleton, degree 5);
   S3(−1) = −1 while every q-integer product is ≥ 0 at q = −1
   (since [n]_{−1} is 1 for n odd, 0 for n even);
   ascending coefficients [1,2,2,3,2,1] are non-reciprocal (c2 = 2 vs c3 = 3);
   S3(2) = 101 is prime.
3. At n = 4: det(E,0..3) = q^18+3q^17+...+3q^5+q^4
   = q^4(q+1)[5]_q Q9,
   Q9 = q^9+q^8+3q^7+q^6+4q^5+q^4+3q^3+q^2+q+1,
   Q9(1) = 17, Q9(−1) = −7, Q9(0) = 1 (hence a real zero in (−1,0)),
   ZZ-irreducible, total S(1) = 170 (unrefined n = 4 count).
   Consequently no product-form identity det = R (resp. det(minor) = Q_3) of
   the target (resp. preset-fallback) shape holds for this weighted matrix.

## Proof / evidence

- Two independent q-binomial constructions (q-factorial division and Gaussian
  recurrence C(n,k) = C(n−1,k−1)+q^k·C(n−1,k)) agree entry-by-entry and on both
  determinants.
- q = 1 specializations recomputed from the integer matrix
  binom(i+j, 2j−i): dets n = 1..4 are 1, 2, 11, 170, matching DLMF 26.12.15.
- ZZ-irreducibility via exact sympy factor_list over ZZ (singletons for S3, Q9);
  full S factorization is (q+1)[5]_q Q9 with zero remainder.
- Sign-lemma values, non-reciprocity, S3(2) = 101 primality, naive-product
  mismatches (R3(2) = 2634489/17 vs 202; R(2) = 114783149724712029/85 vs
  2069808), q = 2 integer-matrix cross-checks (D4(2) = 2069808,
  S(2) = 129363 = 3·31·1391), and 8/8 monomial-shift
  (q^{a·C(K,2)+b·i+c·j}, a,b,c ∈ {0,1}) irreducibility robustness are all
  asserted in-script.
- Replay: `python3 output/artifacts/verify_minor.py` → VERIFY_MINOR_OK;
  `python3 output/artifacts/recovery_test.py` → RECOVERY_OK (seconds, stdlib + sympy).

## Limitations

- Weighting scope: standard area weighting plus its 8 monomial shifts; exotic
  non-monomial weightings are not covered (none recorded in admitted sources).
- Minor scope: leading principal minor (indices 0,1,2); the trailing (1,2,3)
  minor equals the full D4 regime (170 at q = 1).
- No general-n non-existence theorem is claimed; the Phi bijection was not
  pursued because it cannot repair a false product conjunct.
- The label “standard CSTCPP LGV matrix” is the report's stipulated LGV data
  (validated at q = 1), not an independently proved weight-preservation theorem.

## Reproducibility

Self-contained stdlib + sympy scripts in output/artifacts/; dual-path
q-binomial agreement and exact polynomial/factorization assertions rerun in
seconds with no external data.

## References

- DLMF §26.12 Plane Partitions. https://dlmf.nist.gov/26.12
- G. E. Andrews, Plane partitions IV: A conjecture of Mills–Robbins–Rumsey.
  Adv. Math. 1987. https://doi.org/10.1007/bf01836165
- T. Eisenkölbl, (−1)-enumeration of plane partitions with complementation
  symmetry. arXiv:math/0011175.
- I. Gessel, G. Viennot, Binomial determinants, paths, and hook length
  formulae. Adv. Math. 1985.
- Sage Combinatorics: Plane partitions.
  https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/plane_partition.html
