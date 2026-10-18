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
## Reproducibility
Run `python verify.py` with Python 3 and SymPy (tested with SymPy 1.13 or later). This checks the exact Hamming-shell rational expressions, their row sums, selected rational timesteps, and the binomial recurrence for a finite range. Numerical root isolation is reproducible by bisection on the stated quartic, whose positive root is unique by Descartes' rule.

## Analytical checks and limits
The proof is self-contained: Walsh eigenvalues are exactly \(-2k\), the nearest-neighbor large-step coefficient is explicit, and the positive recurrence proves the sign for every dimension \(d\ge3\). A finite checker cannot certify the infinite-family argument. The update is positive definite because its scalar multipliers are positive, but positive definiteness does not imply coordinatewise nonnegativity. No independent audit has been performed.
