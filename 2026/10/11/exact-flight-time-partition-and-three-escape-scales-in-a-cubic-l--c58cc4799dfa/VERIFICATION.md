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

The executable `verify.py` is a standalone SymPy check of the rational first-integral identity, Jacobians at both centers, invariant-line reductions, exact parabolic equation and velocity, and final time-partition algebra. It was executed against the actual embedded source and returned `CHECK_OK`. Dependencies are declared in `requirements.txt`; run `python -m pip install -r requirements.txt` and `python verify.py` in a directory containing these files.

The exact period integrals, the rational quartic integral for parabolic flight, and the rigorous one-dimensional comparison at finite escape endpoints are shown in `RESULT.md`. These analytic arguments, not a finite computational search or execution transcript, support statements for all positive parameters and all trajectories in the specified regions.

Source-inspection limits concern the possible presence of equivalent time identities in inaccessible complete bi-center papers. The independent audit is not performed.
