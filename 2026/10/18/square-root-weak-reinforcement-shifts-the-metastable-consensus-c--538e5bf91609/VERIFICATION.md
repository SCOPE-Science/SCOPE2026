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

# Reproducibility and boundaries

Run `python verify.py` with NumPy and SciPy available. The deterministic checks verify the finite identity for the two-candidate killing probability, the exact neutral-case geometric parameter, normalization of all computed substochastic transition rows, and finite-size convergence of the normalized quasi-stationary killing rates. The checker executed successfully with 408 assertions for the reported package.

The asymptotic result is not established by finite tests. Its analytical dependencies are the precise deletion and direct-skip bounds, two-step resurrected-chain contraction, stationary killing identity, binomial Gaussian limit with uniform integrability, and rare-killing perturbation argument stated in RESULT.md. In particular, the exact invariant-measure equation includes a resurrection term that cannot be discarded until its smallness is proved.

Assumptions: a fixed nonnegative \(c\), independent ballots each round, initially one positive vote per label, and absorption only at full unanimity. The theorem does not cover varying \(c\), partial-consensus thresholds, or dependent choices.
