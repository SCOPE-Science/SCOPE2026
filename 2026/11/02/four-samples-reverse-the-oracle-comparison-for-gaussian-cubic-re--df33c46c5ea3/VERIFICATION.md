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

Run `python3 verify.py` using only the Python 3 standard library. The verifier independently constructs the risk from the Wick/chi-square moment identities, compares it to the closed rational law at every integer sample size from 2 through 200, checks the exact oracle crossover, evaluates the OLS intercept reduction on deterministic rational samples, and independently simulates Gaussian samples for several dimensions.

Observed run: 1,790 independent exact-rational assertions passed. Fixed-seed Gaussian diagnostics passed at sample sizes 2, 3, 4, 6, and 10. The exact small-sample values 6, 37/18, and 8/7 were checked. The script is a reproducibility aid; finite checks do not certify an infinite theorem, and simulations are not used to establish the sign classification.

The proof uses elementary Gaussian projection independence, Wick pairings, chi-square radial moments, and direct polynomial positivity. It does not claim numerical floating-point accuracy or validity for other sampling distributions.
