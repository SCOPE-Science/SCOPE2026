---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For every d>=2, nondegenerate simplex S, s>0 and 0<beta<=min(s,1)^d, each translate of sS has unique affine facet thresholds a_i summing to 1-s, with relative overlap (1-sum_i max(a_i,0))_+^d. The overlap constraint is sum positive parts <=h=1-beta^(1/d). For each j, a_j<=h and equality is achievable by setting a_j=h and distributing the sum 1-s-h<=0 over the other facets. Thus intersection over all admissible translates is exactly {lambda_i>=h}, independent of scale beyond admissible beta. Barycentric sum=1 proves the empty/centroid/homothetic simplex trichotomy at beta_c=(d/(d+1))^d and scale threshold s=d/(d+1); volume ratio ((d+1)beta^(1/d)-d)^d. The independent sample verifies positive-part budget and overlap including admissible endpoints, whereas the analytic facet supremum proves all dimensions and continuous parameters.

## originality

PASS

Best-of-knowledge PASS: the full barycentric closed form, all-scale feasibility and sharp extinction were not mathematically provided by the primary general-depth results examined. The method is elementary but extracting exact apex-facet extrema and the global scale diagram adds a concrete sharp computation for this canonical body.

## value

PASS

An exact translation-depth/floating-core profile for ALL dimensions, dilation scales, and overlap fractions of the natural homothetic simplex test body. The sharp extinction scale distinguishes the ball-convexity-compatible regime and its extension, making a mathematically motivated boundary rather than an arbitrary example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
