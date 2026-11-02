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

# Reproducibility

Execute `python3 verify.py` with a standard Python 3 installation. Expected output: `VERIFY_OK checks=506`. The verifier evaluates the three original Debye loss components and their derivative separately from the rational hyperbolic-cosine representation; it checks 14 parameter settings across the discriminant threshold, root counts by sign-change bracketing and bisection, critical-point locations and sign patterns, the near-threshold square-root splitting, and the high-contrast minimum intensity law.

The exhaustive classification for all real parameter values is proved in `RESULT.md` from the derivative's quadratic discriminant and sign analysis. Grid calculations do not certify absence of additional roots outside the checked finite samples; the algebraic degree bound is essential. Derivative comparisons use floating-point tolerances and are implementation cross-checks, not a formal certificate. No experiment or independent external audit has been performed.
