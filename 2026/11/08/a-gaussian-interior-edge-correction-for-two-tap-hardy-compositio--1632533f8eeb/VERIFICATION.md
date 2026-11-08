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

# Reproducibility and scientific limits

The standalone `edge_check.py` verifies the exact two-tap shift norm identity using rational vectors and compares numerical largest singular values of finite residue blocks against the analytic correction. It uses Python 3, NumPy and SciPy and is invoked with `python edge_check.py` from the extracted directory. A successful check reports 918 exact finite rational identities and 35 numerical finite-section diagnostics (953 total). These are supplementary diagnostics; the infinite-dimensional claim relies on the localization, compactness and harmonic-oscillator proof in RESULT.md.

For the central lower bound the lattice rounding and shift of the coefficient maximum require an explicit \(O(\varepsilon^2)\) subtraction; dropping it makes the pointwise potential bound invalid at the maximizing lattice index. The displayed corrected bound in RESULT.md is used throughout. Spectral prior-art limitations appear in REVIEW.md. This is not independent mathematical validation.
