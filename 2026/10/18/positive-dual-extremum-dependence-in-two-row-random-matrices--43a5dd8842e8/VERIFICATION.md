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
The included `verify_joint_extrema.py` was executed in Python and reported 351 exact checks. Independent checks comprise exhaustive permutations of ranks for dimensions \(2	imes2\), \(2	imes3\), and \(2	imes4\); exact positivity and probability bounds up to \(n=149\); and beta-binomial integration independent of the simplified covariance formula through \(n=44\). The unrestricted proof follows the algebraic integral and binomial-inequality arguments in `RESULT.md`; these computations are not an infinite certificate. This has not been independently audited.
