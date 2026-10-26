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

# Reproducibility and limitations

Run `python verify.py` with Python 3 and NumPy in the directory containing the attached files. The script uses exact rational arithmetic to evaluate every integer spectrum in a specified bounded enumeration and directly constructs independent rotated real matrices for projector checks. It compares all predicted endpoint bounds, verifies the exact weighted-projection eigenspectrum, and checks the two extremizing profiles.

The run completed 5,704 enumerated integer spectra and 153,536 exact assertions, plus 972 direct-geometry assertions; the largest Frobenius discrepancy between two differently implemented projector constructions was below \(3\times10^{-15}\). No proof claim rests on Monte Carlo testing, numerical logs, or finite enumeration.

The analytic verification rests on the determinant-generating formula, ordering of the spectral eigenvalues, and Newton's log-concavity inequality for positive elementary symmetric polynomials. It establishes universality over every full-rank real matrix of the stated dimensions and condition number, including sharp equality examples. Historical priority and independently performed mathematical audit remain open.
