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

# Verification scope

The proof of the joint weak limit appears in `RESULT.md` and uses a Poisson embedding, an exact conditional binomial distribution, locally uniform characteristic-function convergence, moment-controlled de-Poissonization, and an explicit characteristic-function integral. The limiting distribution is not inferred from finite simulation.

Run `python3 checks/verify.py` to reproduce 724 finite assertions. The script checks exact occupancy-state dynamic programming, the associated-Stirling enumeration for the stopped singleton count, the conditional maximum-time representation, the truncated Poisson moments, and the numerical approach to the Laplace characteristic function. Numerical tolerances in the last check are illustrative, not rigorous approximation certificates.

This verifies the consistency of the derivations on the checked finite domain, not historical priority, formal proof correctness, or independent validation.
