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

# Reproducibility and proof limits

The mathematical argument is self-contained in `RESULT.md`. The exact conjugacy, uniform return-displacement estimate, distributional convolution calculation and Wronskian identity can be verified symbolically by differentiating the displayed functions. These algebraic steps are the basis for the global analytic count; no computer calculation replaces them.

Run `python3 verify.py` with a Python 3 standard-library interpreter from a directory containing this file and `verify.py`. The checker performs numerical midpoint quadrature, bracketing of four roots of the limiting response level, and fourth-order Runge–Kutta integration of the exact transformed flow at a small positive perturbation. The executable was run from the distributed source file and printed `CHECK_OK`.

The example parameters are \(p=7\), \(r=20\), and \(\varepsilon=10^{-3}\); all sample calculations are finite-precision evidence only. This script does not certify global uniqueness of the roots, the inequalities at all parameters, or publication priority. The analytic theorem covers the open response-level ranges specified in `RESULT.md`, excludes the two critical levels, and is valid only for sufficiently small positive perturbation.
