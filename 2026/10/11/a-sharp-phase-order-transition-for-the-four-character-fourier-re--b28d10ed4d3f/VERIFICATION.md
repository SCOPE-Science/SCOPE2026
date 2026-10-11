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

# Verification and scope

The analytic proof establishes the result for all finite \(p>0\), all positive amplitudes, and all continuous torus phases. A binomial-coefficient recurrence proves the mixed-derivative identity; strict covariance and elementary circular-arc overlap settle phase ordering. Singularities on the diagonal of the intermediate bivariate function are handled by continuity and finite four-corner inequalities rather than assuming a globally bounded second derivative.

Run `python3 checker.py` from this directory with the Python standard library. The recorded result was `FINITE_CHECK_PASS 944 supplementary assertions`, including four exact-integer even-moment checks, grid phase monotonicity for multiple exponents and amplitude quadruples, and zero-amplitude phase-independence checks. The sampling grid is \(64\times64\); it is not an exhaustive test of all phases, exponents, or amplitudes. The proof, not the numerical checks, supports the general theorem. No independent audit was performed.
