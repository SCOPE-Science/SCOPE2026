---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

The same polygonal norm and Example 6 facet parameterization were checked in Fang et al. For every pair improving m>331/206 the focal reduction puts u>=v and u+v>c, S(u)+S(v)>7c/5; S3/S3 is infeasible. On S2/S2 and S3/S2, the displayed rational D(u,v) increases with u; the active boundaries and derivative quadratic signs yield cell suprema 29270497/30250300 and 18910336411/19465125400 respectively. The latter is larger. Exact rational reconstruction of the boundary pair (u0,v0) verifies both unit norms, m=c, and its independently optimized directed distance D*=18910336411/19465125400. The strict-feasible perturbation approaches D*, proving equality as a supremum, so the endpoint plateau is closed and sharp.

## originality

PASS

Fang et al. 2026 Example 6 computes the same norm and demonstrates only the interior value J_B^(1/40)=331/206 and saturation 100999/3009900. It bounds every improving pair by 39/40, not the exact maximum directed distance D*; the exact first-departure fraction is not implied by those two values. Earlier other-space James constants cannot imply the initial plateau for this norm.

## value

PASS

The focal comparison was designed to show that endpoint and saturation data do not determine the approximate-orthogonality profile. Its sharp onset at 554788989/19465125400 is a natural missing boundary: a complete interval of equality followed by strict gain, rather than an arbitrary parameter slice or a tiny unmotivated decimal adjustment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
