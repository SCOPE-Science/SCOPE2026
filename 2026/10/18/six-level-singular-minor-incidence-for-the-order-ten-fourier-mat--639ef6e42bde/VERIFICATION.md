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

Run `python3 verify_fourier10.py` for the complete exact characteristic-zero 44,100-minor census. Run `python3 fourier10_modcheck.py` for three independent modular Gaussian-elimination cross-checks. Both use Python 3 standard library only, without network calls. Outputs from the actual packaged program paths are included in `verification_output.txt`. An exact determinant remainder in the minimal-polynomial basis is zero exactly for a vanishing complex determinant; modular checks are additional comparisons and do not certify complex vanishing on their own. No infinite-domain claim is made.
