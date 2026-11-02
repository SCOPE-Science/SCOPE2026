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

The standalone `verify.py` uses only Python 3 standard-library modules. In the completed run it passed 780 exact rational checks of the closed support and moment formulas, 750 independently evaluated finite-difference identities using randomly constructed orthonormal bases, and five illustrative stationary sampling tests. It checks finite polygon support bounds and their geometric truncation errors, but does not and cannot certify infinitely many parameter values by enumeration. Analytic proof is supplied in `RESULT.md`.

Limitations: numerical sampling is diagnostic, not an argument for the full stationary support, absolute continuity or uniqueness. All of these are deduced analytically. External independent review has not been performed.
