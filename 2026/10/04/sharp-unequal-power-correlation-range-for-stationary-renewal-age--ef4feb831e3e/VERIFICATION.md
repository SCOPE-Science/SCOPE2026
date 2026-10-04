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

The proof is analytic. The accompanying checker uses exact rational arithmetic for unequal positive integer exponents.

It verifies the beta constants, exact stationary mixed moments from arbitrary rational finite-support interarrival laws, deterministic lower-endpoint equality, and the two-sided correlation inequalities over a large randomized family.

The checker also constructs two-point size-biased interval laws and converts them back to genuine two-point interarrival laws by inverse size biasing. Along the explicit rare-large family it confirms convergence toward the upper endpoint.

Finite integer-power checks do not establish the real-exponent theorem; the universal proof in `RESULT.md` uses only monotonicity, covariance decomposition, Cauchy--Schwarz, and continuity.

Independent audit has not been performed.

Replay result: `VERIFY_OK random_bound_checks=33471 deterministic_endpoint_checks=42 upper_path_checks=42`.
