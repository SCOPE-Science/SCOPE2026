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

# Reproducible verification

Run `python verify.py` using Python 3.10 or newer. Exact fraction-based checks require only the standard library. Installing `mpmath` also enables independent high-precision Bessel-transform comparisons.

The executed checks passed: **387** in total, comprising 378 exact finite-dimensional inequalities or witness identities plus 9 modified-Bessel-transform comparisons. The Bessel comparison independently computes the Laplace transform of an unreset radial first-exit time and differentiates the renewal mean numerically at a small positive rate. The exact arithmetic tests dimensions 2 through 80, including both sides of the dimension-seven transition, and verifies the rational 7-dimensional witness.

All-dimensional correctness comes from the Dirichlet problems, renewal identity, and pointwise quadratic inequality in `RESULT.md`; finite computation alone would not establish it. Floating-point comparisons were performed at 65 decimal digits and tolerated an absolute derivative discrepancy below \(2\times10^{-9}\) when \(R=D=1\). This is computational corroboration, not an independent audit or an external verification certificate.
