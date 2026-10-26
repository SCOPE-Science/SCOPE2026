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

# Reproducibility checks

The companion `check.py` uses SymPy exact algebra and rational parameters. Run it with `python check.py` in a directory containing the supplied file. It tests: the exact \(2\times2\) second-moment map against independent matrix propagation, the determinant identity, the rational cutoff factorization, the exact sign-factorization of the second derivative, the small-step derivative and large-step limit, and both fully exact step-size examples. The completed execution reported 1,526 assertions passed.

The independent reasoning needed for the infinite-parameter theorem is given in `RESULT.md`, particularly the positivity of the moment matrix, the Perron eigenvalue crossing, strict concavity of the auxiliary logarithm and Borel–Cantelli. Finite calculations alone cannot establish these universal steps. Mathematical priority and independent validation have not been certified.
