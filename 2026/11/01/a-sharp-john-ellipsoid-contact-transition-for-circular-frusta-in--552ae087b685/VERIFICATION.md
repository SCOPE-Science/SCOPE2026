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

PASS: The source RESULT.md explicitly defines the affine-normalized d-dimensional circular frustum, positive radii, center/axis normalization and both endpoint regimes. For an axis-aligned ellipsoid, conical-side containment is the support-function inequality As*m+sqrt(q+A^2 s^2 p)<=A, plus the two end-plane bounds. Direct substitution gives equality at the lateral side in both regimes; the end constraints and positive transverse radius hold, including s=0 and s=1/d. In the first regime the normalized latitude at s plus the upper/lower poles have weights w=(d-1)/(d(1-s^2)) and w_±=(1-w∓ws)/2; these are nonnegative precisely for s<=1/d and have mean zero and covariance I_d/d. In the second regime the touching latitude is 1/d and weights are d/(d+1) for the latitude and 1/(d+1) for the lower pole; their first and second moments again satisfy John's criterion. Rotational averaging (not an assumption of optimality) supplies valid contact measures, so the global John theorem gives maximal volume and uniqueness among all ellipsoids. Independent symbolic equations and 95 numerical regimes were checked with the saved independent_checks.py; those samples do not prove the all-d statement.

## originality

PASS

Qualified best-of-knowledge PASS: Güler and Gürtuna (arXiv:0709.0707) work with exactly the affine-equivalent truncated second-order cones, but Theorem 8.1 solves the minimum-volume enclosing ellipsoid, and their introduction expressly leaves the inscribed ellipsoid of this class untreated. John contact conditions are a general criterion, not a radius-ratio classification. The two-regime contact transition and saturation are not implied by those checked results or the different fixed half-cone family. Subsequent implicit prior derivations remain a priority risk.

## value

PASS

PASS: Right circular frusta are a natural continuous family of truncated second-order cones; the closest primary paper explicitly identifies the missing inscribed problem. A dimension-sharp cap-contact threshold and saturation of the transverse semiaxis constitute a useful structural classification, not a one-off numerical constant or a restatement of the general contact theorem. The exact boundary s=1/d and every d>=2 are included.

The dated certificate retains the supplied scientific assessment, sources and limitations.
