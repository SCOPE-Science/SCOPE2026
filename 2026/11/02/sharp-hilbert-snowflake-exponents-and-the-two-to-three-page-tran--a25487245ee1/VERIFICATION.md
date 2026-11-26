---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The within-page and cross-page distances and the two endpoint-to-page rows in RESULT.md lines 23–31 follow by routing through u or v. Split coefficients into mean page triples, page contrasts with zero sum across pages in each coordinate, and endpoint coefficients; the contrasts are orthogonal to the mean sector for the quadratic form. Reflection splits the mean sector into two odd and two even coordinates after imposing zero total mass. The contrast matrix has odd eigenvalue b−2a<0 and even determinant bc−2(b−1)²>0 with negative diagonal on [0,6/5]; the bounds b≤3 for p≤1 and b<4, c/b≥4/3 above 1 verify the latter. Completing the square in the global odd block gives O_r=r(b+a−a²−1)+(2a−b)>0 for p≤1 by concavity. At r=2 this remains positive up to 6/5, by monotonicity of 2(a−1)²/b and the rational endpoint bounds. For even page coefficients (z,w,z) and endpoints both −r(2z+w)/2, the within-page term is 2az²+4zw and the cross-page term per ordered pair is (2a+2b)z²+4bzw+cw²; adding the endpoint terms gives the displayed rE_r. E_11 is strictly negative on the required ranges, and F_r(0)=3r+2, F_r(1)=8−3r; the source's fifth-power rational enclosures give F_2(6/5)<−234923/125000. The first zero therefore has precisely one null direction; Li–Weston Theorem 5.4 supplies strictness below and excludes any higher exponent, so the strict form at p=1 for r=2 puts its endpoint above 1. The squared Hilbert distance Gram rank agrees with the dimensions. For F_r=r²A+rB+C, differentiation gives A(0)=0, A'(0)=log(27/32), B(0)=3. On bounded x, F_r(x/r)/r=3−x log(32/27)+O(1/r) uniformly. This excludes earlier scaled zeros away from the limiting simple zero and bounds the displacement of the first root by O(1/r) in x, giving the claimed O(r^-2) in p. Independent BFS distances and zero-sum spectral bisection for r=2,3,4,5 corroborated the listed approximations (r=5 gave 0.775437849427, a roughly 3×10^-12 last-place discrepancy only). Those checks do not prove the theorem. Frozen VERIFICATION.md and verify.py were inspected, not executed.

## originality

PASS

The distinct supported claim is the all-page, variable-exponent edge-book threshold, its corank and its asymptotic, with the transition to failure for at least three pages. Ordinary quadratic embeddability of two pages already follows from the three-path theta theorem and is not credited as new. Same-day pentagonal catalogue work has materially similar methods but different metrics and threshold regimes; no priority claim is made from dates.

## value

PASS

Edge-sharing is a natural change from single-vertex gluing with a qualitatively different geometric effect: adding a third pentagon destroys ordinary QE, and many pages drive the snowflake exponent to zero on an exact inverse-size scale. The proof distinguishes which symmetry sector changes sign and gives precise endpoint dimension and threshold for every size, rather than just computing selected graph examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
