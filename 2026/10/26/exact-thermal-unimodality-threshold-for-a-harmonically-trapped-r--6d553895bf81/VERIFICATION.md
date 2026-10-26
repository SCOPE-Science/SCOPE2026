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

# Verification and limits

Run `python verify.py` with Python 3, NumPy and SciPy. The executed check completed successfully: 54 checks of the scalar positive root, the exact Kummer root derivative, independent Gauss–Jacobi integration of stationary curvature, sampled density-mode signs on both sides of the transition, and the limiting behaviors near switching ratios zero and one. It reports \(\tau_c(0.5)=0.316464340348\ldots\), consistent with direct numerical quadrature.

The exact distributional identity is obtained from the two-component stationary transport equation; the critical root is proved unique by its exact Kummer crossing derivative, not by numeric root scanning. The global number of modes is proved by the sign-variation property of Gaussian smoothing of a two-edge-peaked density, and the quartic degeneracy by the heat equation. Finite quadrature and a finite mode mesh are supporting checks only. The full texts of the 2014 nanoswimmer study and the 2026 convolution preprint were not accessible for exhaustive priority comparison. No independent audit is asserted.
