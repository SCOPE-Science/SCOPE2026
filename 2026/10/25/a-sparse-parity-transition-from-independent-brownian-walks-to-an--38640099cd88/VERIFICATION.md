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

# Reproducibility and scope

Run `python verification.py` using standard Python 3. The program independently expands binomial parity expectations and enumerates all coefficient configurations for small input histories. Its recorded result is `PASS 122 exact-rational parity and model assertions`, reproduced in `verification_output.txt`.

The computational test verifies discrete parity identities; it is not a proof of functional convergence. The analytical argument uses conditional coefficient independence, the exact formula for the conditional parity mean, a binomial local estimate, the martingale functional central limit theorem, Donsker's theorem, and Lévy's arcsine law. In particular, the quadratic covariation of the critical limiting pair is the *random* occupation time, not merely its mean.

The result is an annealed weak-limit theorem for the specified independent Bernoulli coefficient ensemble. No quenched result, finite-sample error rate, or independent mathematical audit is asserted.
