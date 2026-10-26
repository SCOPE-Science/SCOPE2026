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

`verify.py` evaluates the generator-derived triangular stationary moment recursion symbolically through total degree four. It checks the second moment, fourth moment, and rational excess-kurtosis formula as exact symbolic identities, plus rational examples on both sides of the polynomial sign transitions. Invoke `python verify.py` from this directory with SymPy installed; the program reads no external files.

An independent event-driven numerical computation propagated the continuous-time process between exponentially distributed chirality-flip events without time-step discretization for the zero-angular-diffusion sample \((d,g,w)=(0,1,10)\). With 150,000 independent trajectories initialized at zero position and independently uniform angles, 20 trap-relaxation times yielded excess kurtosis about \(0.213\), compared with exact stationary kurtosis about \(0.205\). Its statistical and relaxation errors are not certified; this check is supporting evidence only.

The proof's infinite-time assertion follows from the stationary convolution and exact generator algebra, not numerical sampling. The exact sign classification follows from elementary quadratic-root criteria, while the two separated root scales follow from leading polynomial coefficients. No result here establishes moments of models with translational diffusion, finite-duration switching, or nonharmonic traps.
