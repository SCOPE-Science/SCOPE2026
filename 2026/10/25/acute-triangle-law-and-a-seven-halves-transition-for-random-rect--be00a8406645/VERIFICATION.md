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

# Verification instructions and actual scope

`verify.py` is a standalone Python 3 program requiring NumPy, SciPy and mpmath. Run it from the directory containing the file with `python verify.py`. It computes the side-conditional probability by numerical quadrature of the *raw geometry-based integrands*, independently samples uniform points directly on all four sides and tests all three angle-dot-products, checks the already-known square value \(23/96\), and numerically tests the precise \(7/2\) and thin-rectangle asymptotics using high-precision calculations. It prints `ALL_RECTANGLE_BOUNDARY_ACUTENESS_CHECKS_OK` only if all checks pass.

One actual execution on the submitted program passed: independent quadrature agreed with the elementary formula to better than \(3\times10^{-10}\) for aspect ratios \(1,1.4,2,2.1,3,6\). Cartesian sampling used 180000 independently sampled triples at each ratio, and measured each probability within \(0.006\) of its formula. High-precision crossover tests at \(arepsilon=0.03,0.005,0.0002,0.000001\) converged to unnormalized coefficient \(-16/105\); ratios \(100,500,1000\) confirmed the stated leading thin asymptotic.

Finite sampling and numerical quadrature do not constitute infinite proof or historical-priority certification. The RESULT.md analytic proof handles all \(r\ge1\) and the stated limits. No external or independent review was performed.
