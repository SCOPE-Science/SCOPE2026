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

# Reproducible checks

Run `python3 verify.py` in this directory with Python 3 and no third-party packages. The program recomputes reflection orbits, all admissible stable faces of the Alexander-dual complex, the component graph and its contractible local cones for 126 parameter/axis cases. It also independently constructs the original ordinary three-cut simplicial complex for 21 cases and computes its signed reflection Lefschetz trace. The observed output is `VERIFY_OK orbit_cases=126 orbit_faces=6447 direct_cut_cases=21`.

Finite enumeration does not imply the infinite theorem. The proof is the distance-based orbit confinement lemma, conical-block decomposition and equivariant Alexander duality in RESULT.md. The earlier cyclic character is independently sourced, not recreated or claimed as new. Complete source-text exclusion of equivalent published claims remains limited; no independent validation has occurred.
