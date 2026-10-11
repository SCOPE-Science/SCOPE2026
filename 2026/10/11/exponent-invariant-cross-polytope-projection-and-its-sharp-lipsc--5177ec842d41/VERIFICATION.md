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

The analytic proof in `RESULT.md` supplies all quantifiers and critical steps: unique \(\ell_p\) nearest points, their active-coordinate linearization, exact global Lipschitz upper and matching lower bounds, sharp failure outside Hilbert geometry from three coordinates, and an exact fourth-power extremal calculation.

The standalone program `verification/check.py` was run from its actual package path with `python verification/check.py`. Its observed success marker was `CROSSPOLYTOPE_LP_METRIC_PROJECTION_CHECK_OK`. It performs rational identities and finite numerical tests; these calculations do not certify every dimension, exponent, or input pair, and they are not used as a substitute for the proof. No independent audit has been performed.
