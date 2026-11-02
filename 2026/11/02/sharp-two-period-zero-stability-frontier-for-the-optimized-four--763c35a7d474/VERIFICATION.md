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
# Verification

The complete analytic argument and precise fixed-grid assumptions are in RESULT.md. Run `python verify.py` after installing dependencies listed in requirements.txt. Its current observed output is `PASS: 278 symbolic and finite tests; R= 4.222826044904903`.

The checker reconstructs coefficients from distinct alternating-step order conditions, checks the exact monodromy polynomial and reciprocal-polynomial factor, confirms explicit threshold signs and representative eigenvalue behavior, and exercises finite parameter values. The exact interval and boundary cases are consequences of the proof's rational sign bounds, Schur criteria, and factorization, not experimental extrapolation. The verification is reproducible on the files supplied here; no independent audit has occurred.
