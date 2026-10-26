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

# Verification of the geometric-phase crossing theorem

The analytic proof is in `RESULT.md`. Run `python triad_checker.py` in an environment with NumPy and SciPy installed. The checker evaluates finite Fock-basis Toeplitz blocks for the three cyclic rotation characters, integrates each equal disk by tensor-product radial Gauss--Legendre and angular trapezoidal quadrature, and searches for a sign change of the leading-sector eigenvalue difference. Its checks are supplemental sanity tests, not an infinite-dimensional certificate.

Observed successful checks: the first three predicted limiting resonance radii were approximately \(1.099636110791\), \(1.904625613728\), and \(2.458861094243\). Finite positive-disk numerical crossings were located respectively near \(1.100379601129\), \(1.904665597932\), and \(2.458861227263\); the two crossing modes dominated the third, with computed normalized sector gaps approximately \(0.4853762894\), \(0.0129547994\), and \(0.0003454377\). At radii \(0.3\), \(0.9\), and \(1.7\), the sorted small-disk spectral levels agreed with the analytic coherent-Gram eigenvalues to better than \(3\times10^{-5}\) using disk radius \(0.004\).

The infinite-dimensional conclusion relies separately on an exact reproducing-kernel identity, operator-norm \(C^1\) Taylor estimates, the explicit circulant Gram spectrum, the nonzero crossing slope \(6R_m e^{-3R_m^2/2}\), threefold invariant subspaces and local isolated-eigenvalue continuity. Finite sections cannot certify these steps for all indices or finite widths. No claim is made of external or independent mathematical validation.
