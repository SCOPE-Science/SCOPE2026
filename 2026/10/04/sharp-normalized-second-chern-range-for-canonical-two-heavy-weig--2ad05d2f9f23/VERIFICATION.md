---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The weighted Euler sequence gives c1=(r+a+b)H and c2=[binom(r,2)+r(a+b)+ab]H^2, so the ratio follows after cancellation. The canonical region is 0<=d=b-a<=r and 1<=a<=r+d; this was independently rechecked from Reid–Tai ages on finite boxes and agrees with the separate published classification. Cauchy–Schwarz gives the upper bound with equality only at all weights one. For the lower bound, the audited derivative in a is nonnegative over the triangle and the boundary derivative in d is strictly positive, forcing the unique corner (2r,3r). The inspected exact verifier independently checks the region and extrema on finite regression ranges; the theorem itself is symbolic.

## originality

PASS

General weighted-projective sources supply Chern-class machinery and the tangent Euler sequence. A separate published Resultary theorem gives the same triangular canonical/terminal parameter classification for the two-heavy family, so that ingredient is treated as prior input. Neither it nor the broader Chern sources states the normalized second-Chern extrema. The audited contribution survives as the exact optimization over that canonical triangle.

## value

PASS

The ratio is a natural dimensionless invariant built from the first two tangent Chern classes. Its complete sharp range and equality geometries on the full canonical two-heavy family form a structural extremal classification, even though the canonical parameter triangle itself is prior input.

The dated certificate retains the supplied scientific assessment, sources and limitations.
