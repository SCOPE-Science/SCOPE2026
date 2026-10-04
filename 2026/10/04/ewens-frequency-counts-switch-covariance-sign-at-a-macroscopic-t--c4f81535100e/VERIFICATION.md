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

The proof is analytic. The accompanying checker uses exact rational arithmetic for all finite identities.

For each \(2\le n\le8\) and several rational values of \(\theta\), it exhaustively enumerates every permutation, weights it by \(\theta^{K_n}\), and verifies the exact mean of \(A_{n,r}\), the Palm identity for multiple test functions of \(K_n\), and the covariance formula for every \(r\).

A separate exact-rational computation checks strict monotonicity and the unique finite sign threshold. Large-\(n\) floating-point checks for several \(\theta\) values verify convergence of \(t_n/n\) to \(1-e^{-1/\theta}\) and of the scaled covariance to the profile in `RESULT.md`.

Finite replay is supplementary. The universal theorem is proved by the marked-cycle bijection, harmonic-tail monotonicity, a Riemann-sum limit, and a gamma-ratio asymptotic.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK permutation_parameter_evals=17736 mean_checks=81 palm_checks=660 covariance_checks=81 threshold_checks=18 asymptotic_checks=20`.
