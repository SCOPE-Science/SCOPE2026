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
# Computational verification and limits

The exact analytic proof is given in `RESULT.md`. The standalone executable `check.py` uses the declared dependency `mpmath>=1.3.0` from `requirements.txt` and requires no external files other than those embedded alongside it. Execute with `python check.py` from the extracted package directory.

Finite checks: gamma-integral Fourier quadrature against the closed power formula; the sharp relative margin for seven combinations of real shape and rates; enumeration of all positive-frequency exceptional mixing weights at those parameter choices; the exact square-radical threshold for common shape three; and the first-order subcritical margin slope.

The program completed with `ALL CHECKS PASSED`, and its reference console output is embedded as `checker_output.txt`. These tests do not certify the infinity of real shapes, rates, or frequencies. Those quantifiers are settled by the explicit monotonicity, phase geometry, and quadratic derivations in `RESULT.md`.

No independent mathematical audit has been performed. Earlier-source comparisons establish only best-knowledge priority, not an exhaustive novelty guarantee.
