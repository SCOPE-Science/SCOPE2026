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

The proof is analytic. The accompanying checker uses exact integer and rational arithmetic.

For every \(1\le n\le9\), it enumerates all set partitions by restricted-growth strings. For every admissible \(r\), it checks the exact mean of \(X_{n,r}\), the Palm identity for several functions of \(K_n\), and the covariance formula.

It also computes Bell numbers exactly through \(n=300\), verifies strict monotonicity of the covariance bracket in block size, reconstructs the exact threshold \(t_n\), and checks the finite sign pattern.

Numerical Lambert-\(W\) values are used only to sanity-check that \(t_n/(\alpha_n+1)\) lies near one at moderate sizes. The asymptotic theorem itself is proved analytically in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK partitions_enumerated=26442 mean_checks=45 palm_checks=420 covariance_checks=45 monotone_checks=299 threshold_checks=299 asymptotic_sanity_checks=7`.
