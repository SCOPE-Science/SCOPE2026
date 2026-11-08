---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For 0<epsilon<1, the normalized 3x3 mean matrix has determinant epsilon^2(1-epsilon)/3>0. Expressing the three overlapping means through independent cell means on the left/core/right disjoint intervals yields weights w_±=(3x^2±2x-(1-epsilon)^2)/(2(2-epsilon)) and w_0=(2-epsilon+(1-epsilon)^2-3x^2)/(2-epsilon). Every cell mean in [-1,1] is attainable by a common bounded measurable f, so the norm equals max_x sum |w_i(x)|. The proof uses |z-y|+|z+y|=2max(|z|,|y|) and a convex/concave branch analysis showing the maximum occurs at x=0 or ±1. The resulting norm is max{1+2(1-epsilon)^2/(2-epsilon),1+2epsilon(3-epsilon)/(2-epsilon)}. The branches cross once at epsilon=(5-sqrt17)/4, with minimum 3(sqrt17-3)/2. Independent mean perturbations instead have coefficient sum Lambda=1+4/(epsilon(1-epsilon)). Independent rational signs/cell averages checked 220 representative exact cases; proof covers the continuum.

## originality

PASS

Best-of-knowledge originality after direct statement/implication comparisons against indexed findings and relevant primary sources. Known antecedents and any covered symmetric/special cases are acknowledged; no comprehensive priority certificate is claimed.

## value

PASS

The distinction between a shared unknown bounded function and independently perturbed overlapping measurements is important in stability analysis: the generalized Lebesgue constant explodes while the true operator norm stays bounded. The unique minimax overlap is a natural three-measurement design invariant, not a random slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
