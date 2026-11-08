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

# Reproduction and verification

Run the standard-library Python file `verify.py`. It checks the factored covariance against a separately evaluated second-moment/cross-bin formula for a finite grid of parameter triples; checks the zero crossing and positive/negative sides; derives exact rational moment polynomials for depth-truncated trees and compares their increasing-depth covariance with the infinite formula; checks the microscopic and logarithmic-window limits numerically; and samples the entire descending-edge tree directly under four small parameter choices.

At packaging review the script completed **301 assertions**. For \(n=2\), \(p=2/5\), \(q=9/10\), the absolute discrepancy of the finite-depth rational covariance from the infinite-tree formula at depths \(5,8,11,14,17\) was respectively approximately \(0.03368114\), \(0.0003990871\), \(1.71060\cdot10^{-6}\), \(3.55795\cdot10^{-9}\), \(4.15823\cdot10^{-12}\). The direct simulations use deterministic pseudo-random seed 20261102 and 14,000 whole-tree realizations per case. The verifier has no third-party package dependencies.

All finite comparisons and simulations are diagnostics and do not establish an infinite theorem. The exact second-moment recurrence, cross-bin factorization and Laplace-product argument in `RESULT.md` are the proof. The sole imported infinite one-point limit is Atamanchuk–Devroye–Lugosi, Theorem 2.1, https://arxiv.org/html/2501.13044. The logarithmic sign-window proof does not require this imported limit.

No independent audit or external validation has been performed.
