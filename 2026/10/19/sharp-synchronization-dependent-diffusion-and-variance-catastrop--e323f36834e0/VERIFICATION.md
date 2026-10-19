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

# Verification notes

The exact-reduction proof in `RESULT.md` derives the stationary moment matrix, its Schur-complement sign, the killed-generator eigenfunction and the Green--Kubo integral. Run `python3 CHECK.py` to reproduce 828 independently solved exact four-state moment/propulsion configurations and 27 exact compensation-surface identities. The checker uses only Python's standard library and exact rational arithmetic.

Computational results support the derivation but are not an exhaustive check of the continuum of model parameters. The proved domain and all limiting cases are stated in `RESULT.md`. The original motivating paper treats perfect synchronization; verification of scientific priority and a fully independent mathematical audit remain unperformed.
