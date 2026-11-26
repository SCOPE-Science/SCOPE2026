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

Each facet has area sqrt(3)/2 and normal proportional to −(e_i−1/4·1); summing the absolute projected facet areas and dividing by two gives A=||u||_1/2 in the stated edge-length units. An independent formulation uses the orthonormal columns (1,1,−1,−1)/2, (1,−1,1,−1)/2, (1,−1,−1,1)/2 as coordinates x in the tangent hyperplane. The maximizing orbit is the signed coordinate axes, so chord distance squared is 2(1−M) where M=||x||_infinity. Sorting absolute values and summing the four signed linear forms gives A=max(M,||x||_1/2). On the M branch, away from the axes, the stability quotient is exactly 1/2. On the other branch put B=||x||_1/2; M≥2B/3 and B≤sqrt(3)/2 give quotient at least (1−B)/(2(1−2B/3)), decreasing strictly in B. At its minimum B=sqrt(3)/2 both bounds are attained and force |x_i|=1/sqrt(3), giving exactly the eight vertex axes in the original coordinates. At the maximizing axes both sides are zero; the branch interface causes no additional equality. The exact witness evaluates to (3−sqrt(3))/8, so the lower bound is globally sharp.

## originality

PASS

The supported distinct claim is the best global coefficient and its full equality set, not the previously known area function, maximizing orbit, or optimal quadratic exponent. The strongest same-setting stability theorem has coefficient 1/10 in the same normalization, strictly below (3−sqrt(3))/8. Same-body shadow distribution and chamber formulas supply inputs but no pointwise optimal distance-deficit tradeoff. An indexed same-form sharp theorem on a 5D cross-polytope has neither the same body nor an identified reduction that yields this coefficient.

## value

PASS

This resolves the exact global coefficient for the first nonplanar regular simplex, a specified case of an existing quantitative projection theorem. Its sharp obstruction is qualitatively useful: the local coefficient near the maximizing square-shadow directions is 1/2, whereas the true bound is smaller and is forced by vertex-axis triangular shadows. This is a complete sharpness and equality result, not a tiny numeric improvement or a finite sampling exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
