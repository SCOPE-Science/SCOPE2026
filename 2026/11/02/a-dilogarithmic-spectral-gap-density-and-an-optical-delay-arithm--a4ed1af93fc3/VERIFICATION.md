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

# Verification and reproducibility

The reproducibility artifact is the standalone `verify.py` file. It requires Python 3 and `mpmath` and can be executed with `python verify.py` in the extracted directory. The completed checker passed 88 finite diagnostic assertions, including calculations based on physical-layer transfer matrices independent of the simplified Bloch formula, multiple evaluations of the exact two-torus measure, and direct finite-frequency comparisons.

The mathematical proof is analytical: the SL(2) transfer-matrix trace gives the band test; Fourier equidistribution and a zero-area analytic boundary justify the incommensurate frequency limit; the phase-angle integral differentiates to an inverse-hyperbolic-tangent integral; strict concavity proves the density separation; and character convergence establishes rational-approximant behavior. These infinite assertions are not certified merely by finite numerical tests.

The numerical direct-frequency tests employ a finite cutoff and sampling step; they do not bound convergence rates for all irrational ratios. No independent external audit or experimental validation has been performed. Prior physics literature supplies the two-layer dispersion relation, not the entire stated frequency-occupancy theorem.
