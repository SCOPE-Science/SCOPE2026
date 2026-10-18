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

# Mathematical verification and scope

The proof is a direct proof for all strictly positive parameter values and all strictly interior states. Exact coordinate reduction, Lyapunov derivative factorizations, and the critical auxiliary ratio equation are independently amenable to algebraic inspection.

Run `python verification/check_consensus.py` with `sympy` and `scipy` installed. The script checks seven exact symbolic identities, two rational parameter cases, and nine numerical initial-value tests. It returned `PASS` in the documented environment. The numerical tests are sanity checks only: they neither enumerate the continuum of initial conditions nor prove an infinite-time asymptotic.

The entropy Lyapunov function is used only for initially nonzero opinion imbalance and below the threshold. The quadratic Lyapunov function covers the threshold and the no-consensus regime. The critical law is restricted to initially nonzero imbalance; symmetric starts stay symmetric and have a zero amplitude. No stochastic-model or experimental-data claim is verified here.

The accessible primary paper has been compared at the level of its exact deterministic drift and main-text claims. Its supplementary equilibrium classification was not materially read because access returned a verification gate; that source remains an originality limitation. Independent validation has not been conducted.
