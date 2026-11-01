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

# Verification

The complete proof is in `RESULT.md`, including the exact support-Jacobian volume identity, normalized curvature wave, limiting triangular derivative and periodic averaging. Neither computer arithmetic nor an external certificate is needed for the infinite proof.

Execute `python3 verification/reuleaux_volume_check.py` with NumPy and SciPy installed. The program computes the solid volume in two independent ways: cross-sectional disk intersection integration and the axial support/Fourier volume identity. For the odd orders \(3,5,7,9,11\), the respective observed discrepancies were \(9.79\times10^{-10}\), \(3.24\times10^{-10}\), \(5.36\times10^{-11}\), \(1.38\times10^{-10}\), and \(7.77\times10^{-11}\). The target limit coefficient is \(\pi^3/48\approx0.6459640975\), while the measured scaled gaps decrease through \(0.667239661\), \(0.653480272\), \(0.649779233\), \(0.648267171\), \(0.647504153\). These finite calculations are consistency checks only.

The argument requires that the support function be globally \(C^1\) and piecewise \(C^2\); this holds for the regular Reuleaux odd-n polygon and justifies intervalwise support integration. Its status under independent mathematical validation is unperformed.
