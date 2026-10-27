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

# Reproducibility and verification limits

Run `python3 verify_quadratic.py` with Python 3 standard library, from the directory containing this file and the script. Successful execution prints five PASS lines and `PASS ALL CHECKS 1548`.

The script implements the normalized harmonic Fourier projection weights, checks 1,452 exact eigenvector mode relations over rational coefficients and indices, and checks 12 exact projection identities and 59 exact spectral-gap identities. It also checks 18 complex-phase distance samples and seven endpoint norm-asymptotic samples. All finite experiments only corroborate formulas. The proof of no further off-curve eigenvalues is the root-count argument in `RESULT.md`; the exact extremal gap and both boundary laws are established by calculus and convergent Bergman power series there. No external verifier or independent scientific audit has been performed.
