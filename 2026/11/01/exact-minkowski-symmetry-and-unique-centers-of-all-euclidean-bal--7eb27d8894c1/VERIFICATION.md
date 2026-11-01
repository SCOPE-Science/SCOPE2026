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

# Verification

The proof of the complete parameter family is analytic. The critical identity \(\lambda_a^2-a\lambda_a=(1-a)/2\) follows directly from the positive quadratic root. The necessary pole and rim inequalities imply the upper bound, while the proposed reflected copy verifies both original constraints for all points of the body. Equality forces the unique Minkowski center. The limiting truncated paraboloid has a separate exact apex/rim proof; finite-volume approximation or numerical convergence is not substituted for that proof.

The accompanying standalone standard-library Python diagnostic `verify.py` was run successfully. It reported 92,448 cap checks and 14,405 independent paraboloid checks, **106,853 successful checks total**, across dimensions 2, 3, 5, 8, and 12 where applicable, and truncation heights close to both endpoints. The printed values include symmetry 0.707106781186548 for a=0 and its center -0.414213562373095 (coordinate orientation opposite to the previously published right half-ball). These checks cover sampled points, not all real parameters or all dimensions, and do not establish novelty.

Scientific boundaries: the base theorem requires dimension at least 2 and strictly interior cut depth; the parabolic result concerns the separately defined limit body. The half-ball subcase is prior. Publication priority could be affected by older unindexed work. The universal rounding factor is an existence bound, not claimed as an optimum for these caps.
