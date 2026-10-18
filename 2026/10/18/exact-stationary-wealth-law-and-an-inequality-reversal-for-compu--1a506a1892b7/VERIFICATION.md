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

The mean-field stationary law follows from the fixed-rate one-server Poisson-arrival Markov chain. The proof establishes positive recurrence for every admissible arrival rate, derives the stationary generating function, and solves its conserved-mean closure. The Gini ordering is exact and uses only the first nonzero survival probability. The decimal Gini enclosure is obtained from the first 35 survival probabilities, whose omitted squared tail is bounded above by \(\mathbb E[2^X]^2/(3\cdot4^{35})\).

Run `python3 check.py` from the extracted package. It uses Python standard-library `decimal` arithmetic, verifies transition recurrences, generating-function values, and the numerical Gini bounds. The stationary distribution is not simulated or artificially truncated to obtain its coefficients. The analytic proof, rather than the finite checker, supports uniqueness and the infinite-series statements.

The finite-population transfer chain and all-mean Gini comparisons are outside the proved scope. No independent scientific audit is represented here.
