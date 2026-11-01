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

# Reproducibility and verification

The complete analytic proof is in `RESULT.md`. Running `python3 verification/check_subdivided_star.py` from this package's root requires only Python 3 standard-library modules. A successful replay prints `PASS: 443 deterministic assertions` and sample critical exponents.

The checker constructs tree distances directly from branch/depth labels and constructs the Schoenberg Gram matrix from these distances. A separate direct formula independently constructs the two-by-two arm blocks. For each arm count from two through seventeen, several exponents are tested; for each of three through seventeen, bisection finds the proposed threshold and checks rank, null direction, positivity below it, negativity above it, and the strict ordinary-star upper bound. Further checks through ten thousand arms test convergence to the analytic coefficient. These are finite-precision corroborations, not exhaustive checks for all arm counts or a substitute for the proof.

Proof steps that cannot be inferred from numerical tests are the positive integral representation on the interval \(1<p<2\), the global scalar derivative inequalities, the strict-concavity comparison with the star threshold, and the uniform asymptotic remainder. They are established symbolically in the result. The scope is the unit-edge, two-step-per-arm family; arbitrary arm depths and fixed-scale Gaussian positivity are outside the claim.

Self-review: passed. Independent audit: not yet performed.
