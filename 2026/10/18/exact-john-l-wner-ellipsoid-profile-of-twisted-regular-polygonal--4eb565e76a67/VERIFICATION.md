---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Unique extremal ellipsoids inherit n-fold rotation and base-exchanging height reflection, forcing axial form. The lateral supporting planes are determined by bottom edges versus upper vertices, support R(A+B)/2 and signed slope R(B−A)/h. Exact John containment a²+R²(B−A)²b²/h² ≤ R²(A+B)²/4 and b≤h/2 maximizes a²b at b=h/2, yielding a²=R²AB, including prism/half-step endpoints. Löwner inclusion at all 2n vertices minimizes a²b at R²/a²=2/3, h²/(4b²)=1/3. Mixed-area integration gives Vol(K)=nhR²sin(π/n)(2A+B)/3, and d[AB/(2A+B)]/dB>0. Independent direct SciPy convex-hull calculations for n=3,4,5,7,11 and five twists tested support containment, hull volume and every outer vertex contact (25 cases). Finite checks corroborate, do not prove continuum/all n.

## originality

PASS

No same-object angular all-n John-internal/Löwner-outer profile found in genuine Resultary and primary-source comparisons. Kovič classification, John's general theorem and regular antiprism descriptions explain objects/uniqueness but not arbitrary twist support/optimal semiaxes. Best-of-knowledge PASS, original PDF transcript mismatch and unindexed exact convex-geometry formulas residual risks.

## value

PASS

A complete intrinsic all-n continuum classification of extremal ellipsoids for natural two-layer regular-polygon bodies; twist-independence of Löwner ellipsoid versus strictly improved John fraction is a geometrically motivated sharp structural contrast, not a routine isolated instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
