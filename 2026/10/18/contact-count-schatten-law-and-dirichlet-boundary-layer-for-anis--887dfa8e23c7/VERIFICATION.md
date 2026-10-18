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
# Verification record

The analytical verification uses orthogonal source degrees and normalized Bergman output basis to reconstruct the Gram eigenvalues. Dirichlet–multinomial uniform compositions verify decreasing order; pole extraction verifies the algebraic/exponential large-degree constants. Conditional Jensen and Dirichlet second moments verify the finite critical-window inequality. A uniform Taylor expansion of the conditional log-moment generating function proves the stated first-order correction and remainder. No mathematical inference is drawn solely from a finite test.

Run `python3 checker.py` with Python 3.10 or newer to reproduce the finite checks. The packaged script passed 7,936 assertions using exact rational arithmetic where feasible, finite Gram comparisons, and dimension-two numerical crossover diagnostics. It does not certify every dimension, exponent, or parameter value, and does not constitute independent audit.
