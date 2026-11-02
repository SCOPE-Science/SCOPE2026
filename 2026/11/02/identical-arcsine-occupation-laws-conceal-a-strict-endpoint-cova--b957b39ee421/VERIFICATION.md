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

The standalone `checker.py` enumerates every uniform permutation of lengths \(3,5,7,9\), totaling \(368{,}046\) instances, and every independent sign sequence of respective lengths \(2,4,6,8\). The computations use exact rational arithmetic for finite-size covariances, means, variances and discrete-arcsine probabilities. The same program computes Eulerian polynomials using their integer recurrence, checks the terminal-rank identity against direct enumeration through permutation length eight, and compares three large finite Eulerian sums to the proved leading constant. It also checks the finite strict comparison against the simple walk.

Invocation: `python checker.py`.
Expected terminal message: `PASS`.

The proof of all-size covariance rests on the Eulerian terminal-rank insertion identity and the local-independence argument, not on enumeration. Strict comparison rests on a Cauchy–Schwarz upper bound and an elementary binomial recurrence. The limiting covariance requires the one-dependent descent CLT and uniform integrability, which are justified by bounded one-dependent summands and their exact variances. The exact arcsine marginal is a cited existing theorem; its proof is not reproduced or claimed as new.

No independent mathematical validation has been performed.
