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

# Reproducibility and verification

The proof uses the classical sharp maximum and maximizing-direction locations; the novel analytic steps are the local support formula and uniform spherical-cap calculation. The executable `verify.py` (Python 3.9+, standard library) enumerates exposed face, arc and vertex candidates for support functions and numerically confirms the local formula. A deterministic 1,400-direction grid tests for possible competing maxima but is **not** an exhaustive proof.

The program then uses 8,192 polar midpoints and 65 bisections per angle to estimate six axial spherical-cap measures at four deficits. It checks the two exact coefficients numerically and prints the scaled third-order residuals. This diagnostic is not independent verification or a certificate of global uniqueness.

Command: `python verify.py`. All required code is supplied within this package.
