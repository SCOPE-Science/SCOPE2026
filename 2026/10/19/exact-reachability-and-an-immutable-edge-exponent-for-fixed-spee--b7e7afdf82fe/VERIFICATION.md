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

The analytical claim follows from the pathwise right-frontier representation, a sharp no-switch asymptotic with bounded-switching-error control, a strict positive-stiffness speed bound, and a stationary Markov time change. Those steps, including all exponents and the coefficient, are written in `RESULT.md`.

Run `python verify.py` with NumPy and SciPy. Five parameter families with different increasing or decreasing support radii and positive stiffness were integrated in the four-moment system. The largest absolute residual across the tests was approximately \(2.6\times10^{-10}\). Four stationary edge-layer integrals with \(\beta=-0.5,0,0.75,2\) reproduce the analytic leading edge coefficient to relative errors below \(1.5\times10^{-4}\) at layer thickness \(10^{-4}\).

The numerical checks test consequences of the exact equations only. They are not substitutes for the infinite-state law equality, full necessity proof, or originality assessment. No independent audit or independent certification has been performed.
