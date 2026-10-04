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

The bundled `verify.py` interprets every displayed potential outcome as an exact rational number with denominator \(1000\). It first verifies that the six treatment effects sum to \(0\). It then enumerates all \(\binom{6}{3}=20\) actual treatment allocations. For each actual allocation, it fixes the observed response vector as required by the sharp-null Fisher reference distribution and enumerates all \(20\) reference allocations.

The checker compares the exact rational values of \(T^2\), which preserves the ordering of the nonnegative studentized statistic \(T\). It verifies that all \(400\) variance denominators are positive, that the p-value multiplicities are \(7\) at \(1/10\), \(3\) at \(1/5\), \(3\) at \(9/10\), and \(7\) at \(1\), and that the rejection probability at \(\alpha=0.1\) is exactly \(7/20\).

This verification is exhaustive for the stated six-unit finite population. It does not establish minimality, a worst-case envelope, or any asymptotic claim.
