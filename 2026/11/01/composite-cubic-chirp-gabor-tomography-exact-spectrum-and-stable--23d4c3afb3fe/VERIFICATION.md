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

# Verification record
The derivation uses a complete exact prime-power Gauss-sum magnitude argument, local valuation counting, CRT tensor products, and an exact Weyl-operator diagonalization. The nonlinear phase retrieval assertion follows from equal shift-one correlations on an odd cycle. The quantitative flat-state inequality is derived from the unit-shift eigenvalue one and the cycle Poincaré spectral gap.

Run `python cubic_chirp_check.py` using Python 3 and NumPy. It verifies all ambiguity coefficients and the circulant Gram spectrum for \(N=5,7,25,35,49,55,125\), and tests the lower stability inequality against independently computed nonlinear intensities for eight seeded pairs at each of \(N=5,25,35\). The actual run completed with markers `FLAT_SIGNAL_STABILITY_DIRECT_INTENSITY_OK` and `CUBIC_CHIRP_GABOR_SPECTRUM_CHECK_OK`.

Finite checks establish only the displayed sample cases. The universal statements rely on the explicit analytic proof, not on extrapolation. No independent audit or verification is represented here.
