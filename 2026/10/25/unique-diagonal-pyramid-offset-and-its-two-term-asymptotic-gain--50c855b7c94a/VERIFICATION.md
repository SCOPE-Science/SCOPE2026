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

Execute `python3 checker.py` with Python 3 (standard library only). It separately computes cardinal uniform-convolution splines recursively and by alternating inclusion–exclusion, checking 440 exact rational evaluations. It evaluates the four-dimensional stationary cubic and five large-dimensional offset/volume estimates. Expected final line: `DIAGONAL_PYRAMID_CHECK_OK exact_rational_cases=440 asymptotic_cases=5`.

The program is an **independent implementation of the finite formulas**, not an external independent scientific audit. Finite tests do not prove uniqueness in all dimensions or the \(O(n^{-2})\)/\(O(n^{-3})\) remainder bounds. Those depend on the strict log-concavity and the differentiated Fourier–Gaussian expansion in RESULT.md.

The only earlier statement taken from Nikolov is the diagonal pyramid volume formula and the fact that its central derivative is positive. The newly asserted quantities are the all-dimensional unique full-offset optimizer and its two-term asymptotics.
