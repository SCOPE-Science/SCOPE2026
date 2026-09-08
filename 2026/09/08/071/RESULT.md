# Serre-Maximal Genus-2 Curves over F_19 and F_29 with Exact Weil Data and Full Point Lists, plus Hasse–Weil Census over a Fixed Small-Height Slice (p ≤ 37)

## Context

The Hasse–Weil–Serre bound for a genus-g curve C over F_q is
# C(F_q) ≤ q + 1 + g·⌊2√q⌋. Curves attaining it are called Serre-maximal.
Explicit Serre-maximal models with full rational-point lists, Weil
polynomials, zeta functions, and Jacobian orders calibrate the
Serre / Howe–Lauter N_q(g) bound tables and supply concrete curves for
Weil-conjecture examples and Goppa-code curve selection. General bound
theorems and isogeny-class databases do not provide uniform
Frobenius-orbit enumeration logs from fixed small-height models with an
in-run maximality certificate.

## Definitions

- Slice S: odd primes p ≤ 37 (11 primes: 3,5,7,11,13,17,19,23,29,31,37;
  p = 2 excluded because y² = f(x) is singular/inseparable in
  characteristic 2) × 12 fixed monic models with integer coefficients in
  {−2,…,2} (6 quintics M01–M06, 6 sextics M07–M12; coefficient vectors
  low→high in artifacts/census_table.json). 132 cells total.
- For smooth C of degree 5: one point at infinity; of degree 6 with
  square leading coefficient: two points at infinity. Smooth ⇒ genus 2
  (standard hyperelliptic genus theorem).
- Serre bound (g = 2): S(q) = q + 1 + 2·⌊2√q⌋.
- Weil polynomial: P_C(T) = 1 + a1·T + a2·T² + q·a1·T³ + q²·T⁴, where
  a1 = N1 − q − 1, S1 = q+1−N1, S2 = q²+1−N2, a2 = (S1² − S2)/2,
  N1 = #C(F_q), N2 = #C(F_q²).
- Zeta function: Z_C(T) = P_C(T)/((1−T)(1−qT)).
- Jacobian order: #J_C(F_q) = P_C(1) = 1 + a1 + a2 + q·a1 + q².
- Frobenius-orbit tally: (n0, n1, n2) = number of x ∈ F_p with
  0 / 1 / 2 lifts y, satisfying n0+n1+n2 = p and n1 + 2·n2 + #∞ = N1.

## Result

For every smooth cell in S the exact values of #C(F_p), #C(F_p²),
orbit tally, Weil polynomial, zeta function, and Jacobian order recorded
in artifacts/census_table.json are correct: 118 smooth genus-2 cells
verified, 14 singular cells excluded with logged reason (repeated root
mod p). In particular:

- **Primary witness.** C* : y² = x⁶ − x⁵ − 2x⁴ + 2x³ − 2x² − x + 1
  (model M11, coeffs [1,−1,−2,2,−2,−1,1]) over F_19 has
  #C*(F_19) = 36 = 19 + 1 + 2·⌊2√19⌋ (Serre-maximal),
  (a1, a2) = (16, 102), #C*(F_19²) = 310,
  P(T) = 1 + 16T + 102T² + 304T³ + 361T⁴,
  #J(F_19) = P(1) = 784 = 28².
  Full list: 34 affine points + 2 points at infinity
  (artifacts/points_M11_p19.json, 36 points), each affine point
  satisfying the curve equation.
- **Secondary witness.** C2 : y² = x⁶ − 2x⁵ + x⁴ + x³ + x² − 2x + 1
  (model M12, coeffs [1,−2,1,1,1,−2,1]) over F_29 has
  #C2(F_29) = 50 = 29 + 1 + 2·⌊2√29⌋ (Serre-maximal),
  (a1, a2) = (20, 158), #C2(F_29²) = 758,
  P(T) = 1 + 20T + 158T² + 580T³ + 841T⁴,
  #J(F_29) = P(1) = 1600 = 40².
  Full list: 48 affine points + 2 points at infinity
  (artifacts/points_M12_p29.json, 50 points), each affine point
  satisfying the curve equation.

All 118 Weil polynomials satisfy |a1| ≤ 4√q, |a2| ≤ 6q, and the
reciprocal-root Riemann-hypothesis check.

## Proof / Evidence (replayable computation)

1. Smoothness/genus: gcd(f, f′) over F_p by Euclid's algorithm; smooth
   ⟺ gcd constant. Leading coefficient 1 (square) ⇒ infinity counts
   above.
2. #C(F_p) by two independent in-run methods asserted equal: (A)
   Euler-criterion sum p + Σ(1+χ(f(x))) + #∞; (B) brute-force (x,y)
   double loop; orbit tally cross-checked. Audit script re-derives N1
   by a separately typed direct double loop.
3. #C(F_p²) by enumeration over F_p[t]/(irreducible quadratic) with
   quadratic-character test v^((q²−1)/2) ∈ {0,1,−1}. The auditor
   re-enumerated N2 = 310 and 758 with independently written code and a
   different irreducible-polynomial choice.
4. Weil coefficients from (N1, N2) with integrality assertion
   (S1²−S2 even); P(1) = Jacobian order; Serre bound comparison.
   Auditor recomputed (16,102)/784 and (20,158)/1600 exactly.
5. `verify_audit.py` (five registered audit-plan steps) prints
   `AUDIT_OK rows=118 witnesses=2`. Auditor ran it and re-ran
   `census.py`, reproducing the same maximals list. Full-table sweep:
   orbit identities, Weil consistency, and coefficient bounds hold for
   all 118 smooth rows with 0 inconsistencies.

This is proof by exhaustive enumeration with independent replay, not a
theoretical proof; the computation is the evidence.

## Limitations

- Maximality means attainment of the Serre bound at q = 19 and q = 29;
  it does not decide N_q(2) for any q.
- Genus attribution rests on smoothness + degree via the standard smooth
  quintic/sextic hyperelliptic genus-2 theorem, plus the gcd test and
  leading-coefficient check; no separately certified genus routine.
- 14/132 singular cells carry no zeta data; p = 2 is out of scope.
- The "Schoof-type cross-check" is the RH root-magnitude plus
  coefficient-bound check, not a full Schoof–Pila implementation.
- Completeness is claimed only over the fixed slice S, not as a
  genus-2 classification.

## Reproducibility

Stdlib Python only:

```
cd output/artifacts
python3 census.py        # regenerates census_table.json, census_log.txt, point files
python3 verify_audit.py  # expect: AUDIT_OK rows=118 witnesses=2
```

## References

- E. W. Howe, K. E. Lauter, Improved upper bounds for the number of
  points on curves over finite fields, https://arxiv.org/abs/math/0207101
- E. W. Howe, E. Nart et al., Principally polarizable isogeny classes of
  abelian surfaces over finite fields,
  https://doi.org/10.4310/MRL.2008.v15.n1.a11
- M. Kudo, S. Harashita, Algorithmic study of superspecial hyperelliptic
  curves over finite fields, https://arxiv.org/abs/1907.00894
- LMFDB, Isogeny classes of abelian varieties over finite fields (+
  Completeness page), https://www.lmfdb.org/Variety/Abelian/Fq/
- LMFDB, Genus 2 curves over Q, https://www.lmfdb.org/Genus2Curve/Q/
