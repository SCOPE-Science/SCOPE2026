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

The analytical proof is given in `RESULT.md`. In a directory containing the seven complete files, run `python verify.py` (Python 3, SciPy). The checker performs 158 deterministic assertions and exits nonzero on a mismatch.

The checker numerically integrates the stationary exponential-age mixture variance and the independent velocity-covariance variance formula; evaluates exact Laplace-plus-Gaussian tails; compares the predicted fixed-window no-reset tail constant over several positive parameter triples; tests moments strictly inside their proven finite domain; and checks exponential suppression in an interior one-reset event class.

The rigorous proof uses the exact Poisson partition, Gaussian integrals and dominated convergence; numerical tests check formulas but do not certify their infinite-threshold limits. The comparison to the directly relevant 2024 velocity-resetting manuscript was limited to accessible abstract material, and scholarly priority is not independently validated.
