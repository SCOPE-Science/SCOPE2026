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

# Reproducible scientific verification

Run `python3 verify_clique_cycles.py` in a directory containing the two files `verify_clique_cycles.py` and `verification_output.txt`. Python 3.9+ (standard library only) is sufficient. The final stdout line must be `VERIFY_OK`, and the full stdout must match `verification_output.txt`.

The checker implements exact full-subset vertexwise validation with no clique-fiber assumptions for eight graphs of up to 18 vertices, an independently coded min-plus cyclic local-state transfer for 240 parameter instances, and verification of the explicit minimum sets for 4424 parameter instances. The finite computations are consistency checks, not an infinite proof.

The unrestricted proof is in `RESULT.md`. It relies on the independently published exact total-domination number of cycles and on the fully stated fiber/run lower-bound argument. No external proof assistant or independent research auditor was used.
