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

# Reproducibility and verification

The standalone file `hermite_two_windows_checker.py` evaluates the Gaussian moments of orders zero, two and four by closed antiderivatives, builds the full parity-split matrix, checks the exact symbolic second-order coefficient and both squared-center shifts, and tests a sequence of finite positive widths. Run `python hermite_two_windows_checker.py` with Python 3, NumPy, SciPy and SymPy. The file was actually run with output `PASS: 565 symbolic/numeric assertions; independent audit not performed`.

The proof requires no numerical limit or experimental extrapolation: Hermite parity yields the direct sum, perturbation of the simple rank-one limiting even eigenvalue determines the two shifts, analyticity and simple-root stability control all centers in a compact interval, and strict pointwise comparisons to the first or third Hermite mode cover the remaining noncompact ranges. A finite checker is supporting evidence only, not a substitute for these arguments. Historical-priority comparison is limited to the specifically inspected literature and scholarly-search results. Independent verification has not been performed.
