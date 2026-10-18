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

# Verification notes
The analytic proof is given in `RESULT.md`. It uses the exact eigenvalues of an explicit \(2\times2\) Hermitian matrix, the sharp monotone rearrangement of mass missing from and added to a circular arc, and a trigonometric identity for the boundary-cap equality family. At fixed \(a\) and \(m\) the cap equality masks have \(Z=2\sin a(2\cos(m/2)-1)>0\), verifying the phase choice used in the proof. The condition \(m<2\pi/3\) comes from this positivity, not from an experiment.

`check_concentration.py` (Python 3 standard library, no network) evaluates the closed-form equality examples over several parameters and performs 400 finite-grid randomized mask checks (grid size 8192); the finite-grid checks use an explicit sampling tolerance and are not rigorous bounds for general measurable masks. Symbolic simplification of the equality-family Fourier integral independently gives exact zero residuals for the claimed closed-form identity and concentration deficit. No external independent audit or certification has been performed. The identity and inequality are asserted only for the two-dimensional space \(\operatorname{span}_{\mathbb C}\{1,e^{it}\}\), fixed mask mass and nonzero first moment.
