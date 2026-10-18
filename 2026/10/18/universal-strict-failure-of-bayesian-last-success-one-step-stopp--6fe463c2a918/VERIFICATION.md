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

The exact finite-horizon posterior and policy identities were checked in `verify.py` with Python's arbitrary-precision `fractions.Fraction`. The checker independently accumulates rewards over every possible next success time and (after a second rejection) the following success, and confirms equality with the closed positive-part sum. It also checks the constant joint terminal-event probability and the one-step recommendation for seven rational-parameter examples. The program exits with success only if all assertions hold.

The proof, not finite testing, establishes the result for arbitrary positive real shape parameters and all sufficiently large integers. The asymptotic constants follow from bounded ceiling residuals, a Riemann sum and Gamma-function ratio limits. No computer-assisted infinite certificate or independent audit was performed.
