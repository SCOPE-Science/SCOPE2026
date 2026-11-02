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

The proof of finite-ring variation is an exact derivative of the finite normalization; it does not rely on sampled parameter points. The thermodynamic result uses strict concavity of an explicit entropy functional. The finite-size Bessel limit uses a coefficientwise bound by a summable factorial series, which establishes both total-variation convergence and first-moment convergence.

`python CHECKER.py` reports 414 passed checks. It independently constructs finite-state generators for capacity-two rings at several values of the asymmetry parameter, verifies stationary balance and endpoint identities, and compares the Bessel and density-window asymptotics. This computation is auxiliary verification, not a substitute for the analytic convergence proofs. The initial stationary-factor formula is cited from Ayyer and Misra rather than reproved as a new discovery. No independent audit or independent validation has been performed.
