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

# Reproducibility and proof checks

The standalone script `verify_modal_bifurcation.py` requires Python with `sympy` and `mpmath`. Run `python verify_modal_bifurcation.py` after extracting the accompanying files into one directory. It symbolically differentiates the exact Haq CDF, checks the rational expression for the derivative of the log density, and confirms both the algebraic critical scale and the second derivative at its double root.

It then uses 65-digit arithmetic and interval bisection across a finite, explicit logarithmic grid to locate illustrative stationary points for \(\tau=0.2\), \(\tau=\sqrt{3/2}-1\), and \(\tau=0.25\), each at \(\delta-1=0.01,0.001,0.0001\). These tests reproduce three stationary points on the subcritical and critical examples and one on the supercritical example. At criticality the signed split distances divided by \(\sqrt{\delta-1}\) approach \(2/\sqrt{3(e-2)}\).

No numerical root-finding output is used as a proof that no additional roots exist. That assertion follows analytically from the simple-root persistence, strict-concavity, compactness, and negative-tail arguments in RESULT.md. The asymptotic conclusions are for every fixed admissible \(\tau\) and sufficiently small positive \(\delta-1\), not for arbitrary positive exponents. No independent external audit was performed.
