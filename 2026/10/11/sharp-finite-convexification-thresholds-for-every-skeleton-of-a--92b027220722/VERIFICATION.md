---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

In affine barycentric coordinates, skeleton membership is support size <=r+1. The sparse-splitting lemma for masses w_i>=0 summing to k with at most kr+1 positions is proved inductively. In sorted order choose the first consecutive length-r block of mass <=1. A predecessor entry (or position r+1 if the first block works) has enough mass to complete a probability row of support <=r+1; delete the r exhausted coordinates and repeat. This gives sufficiency. If kr<d, barycentric target (1-eps,eps/d,...,eps/d), 0<eps<1/k, requires every row to use the dominant vertex, leaving at most kr other positive coordinates; all d are positive, a contradiction. Independently tested 2800 exact rational decompositions across r=1..4 and k=1..7, support/sum/reconstruction, without treating them as all-dimensional proof.

## originality

PASS

The exact all-point finite saturation threshold and sparse barycentric splitting differ from asymptotic Hausdorff convexification. Independent full-text reading of the earlier 6-page note and relevant parts of the 60-page extended survey found only general convergence and nonconvexity indices, not an r-skeleton threshold. The van Hintum 2026 paper is a plausible unread overlap risk, not presumed negative.

## value

PASS

Exact finite convexification is a natural invariant of the nonconvex r-skeleton, and the sharp threshold ceils dimension by skeleton dimension for every simplex and all real barycentric weights. It gives a constructive finite cutoff and near-vertex obstruction, not a parameter substitution or an asymptotic rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
