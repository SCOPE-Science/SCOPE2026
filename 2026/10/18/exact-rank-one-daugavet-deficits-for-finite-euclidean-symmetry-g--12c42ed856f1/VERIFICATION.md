---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

The entire theorem is proved analytically in `RESULT.md`. Reproduction requires only elementary linear algebra, the rearrangement inequality (which can be verified by adjacent swaps), the triangle inequality, and the classification of finite subgroups of the planar orthogonal group. For numerical spot checks, evaluate the displayed closed form with unit operator norm: `H_2` gives approximately 1.8989663259659066, `H_4` approximately 1.8228756555322954, and `C_2` approximately 1.618033988749895. These are diagnostic values, not infinite-dimensional or all-dimension certificates.

Critical symbolic verification: the two relevant eigenvalues of the Gram matrix of the rank-one perturbation have sum \(2+t^2+2tc\), product \((1+tc)^2\), and discriminant \(t^2(t^2+4+4tc)\). The orbit-support inequality has an explicit equality case; strictness and full rigidity follow from non-collinearity of distinct prefix vectors. The derivative at \(c=1\) is \(t/(t+2)\), giving the quadratic finite-rotation deficit. No unproved numerical extrapolation or hidden external certificate is used.

The primary publication date and primary MSC category were verified from arXiv's first submission and displayed classification. Priority checking compared the relevant primary preprint and related research records, but is not a substitute for exhaustive independent literature review.
