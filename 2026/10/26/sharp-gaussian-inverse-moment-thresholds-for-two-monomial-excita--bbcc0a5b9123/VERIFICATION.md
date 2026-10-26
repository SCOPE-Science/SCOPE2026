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

# Reproducible mathematical checks

Run `python3 verify.py` using Python 3.9 or newer; no dependencies are required. The verifier checks 1,302 exact Cauchy–Binet determinants for finite rational feature samples and six analytical roots at three perturbation scales (18 tests); it additionally checks the exceptional angular coefficient. Success emits `VERIFY_OK`. The infinite probability claims are proved analytically in RESULT.md, not by finite enumeration.

The proof uses exact Gaussian radial density, finite transverse angular singularity charts, and the independent radial–angular factorization; these are not formally certified by the computation. Independent audit and independent validation have not been performed.
