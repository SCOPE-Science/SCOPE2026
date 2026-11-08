---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The nonsingular affine normalization maps three consecutive vertices to (0,0),(1,0),(0,1); fourth (p,q) has p,q>0,p+q>1. For fixed X, admissible four-vertex barycentric vectors form a segment; maxima of coordinate weights occur at a triangle-representation endpoint. The two diagonals divide Q into four sectors, each with exactly two available triangle triples. Verified the supplied six linear barycentric coefficients for the A/B sectors algebraically and the symmetry under p<->q. Comparing sharp active-coordinate lower bounds with explicit attaining points produces m_A/m_B and their swaps; minimization gives the four phase formulas, continuous at p=1, q=1, p+q=2. Independently set up all four sector LPs with six barycentric inequalities plus triangle-domain inequalities, used SciPy HiGHS on 200 random positive shape pairs satisfying p+q>1, and found agreement with the formula to <2e-8. The formula yields 1/3<lambda<=1/2 with equality p=q=1; scaling the Minkowski identity yields c=1/lambda-1. LP samples are corroboration, not the all-quadrilateral proof.

## originality

PASS

No checked prior statement entails the full assigned claim. The parallelogram boundary is prior coverage; the numerical non-parallelogram profile does not follow solely from the documented qualitative statements. Full-text access risk is explicit. General existence/criterion and zonotope equality are compatible with the new four-regime values but do not *as stated* supply them; full Meyer planar-case paper remains a potentially significant comparator.

## value

PASS

The sharp affine-invariant convexification threshold for every quadrilateral is a natural geometric index; the four chamber regimes and exact attaining witnesses are potentially useful for covering and finite Minkowski convexification. This is more than a textbook restatement of the existence of the index or a known bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
