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

The critical polynomial/exponential-logarithmic substitution and exact stationary budget are derived in `RESULT.md`. The executable `checks/chialvo_identity.py` uses SymPy for literal symbolic cancellation and deterministic numerical sanity checks; it has no external data inputs.

Run from the root containing the included files: `python checks/chialvo_identity.py` (Python 3, SymPy >= 1.12). Expected output: `Chialvo symbolic identity and scalar checks: PASS`.

The executable does **not** prove the measure-theoretic steps, which instead require the compact-full-orbit upper bound and Poincaré recurrence arguments in the proof. It does not explore all trajectories or demonstrate existence of non-equilibrium recurrence. The known fixed-point fold and new global/measure implications have distinct provenance; no external validation is asserted.
