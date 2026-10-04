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

The universal theorem is proved analytically in `RESULT.md`. The bundled deterministic script `verify_routh_profile.py` is supplementary. It checks the classical Routh formula against the proposed envelope on 30,000 seeded positive triples over wide logarithmic ranges, verifies the exact equal-parameter branch, checks the inverse inequality, and follows explicit fixed-product paths toward zero area.

Replay command:

`python3 verify_routh_profile.py`

Observed replay output during packaging:

`VERIFY_OK`

`cases=30265`

`worst_profile_violation=0.000e+00`

`worst_equality_error=6.661e-16`

`worst_inverse_violation=0.000e+00`

Finite numerical checks do not certify the universal quantifiers; those are established by the strict-convexity proof.
