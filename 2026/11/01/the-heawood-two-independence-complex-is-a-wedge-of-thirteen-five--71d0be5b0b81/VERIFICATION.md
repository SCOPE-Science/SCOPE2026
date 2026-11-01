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

# Reproduction

Run `python3 VERIFY.py` using only Python standard-library modules. `VERIFY_OUTPUT.txt` contains a captured execution, including the marker `ALL_CHECKS_PASS`. The verifier performs exhaustive face enumeration from the incidence definition; checks the exact seven-entry face vector and closure; constructs a 1,121-pair simplicial matching; topologically sorts the 2,256-vertex oriented Hasse diagram, proving acyclicity; and independently computes the six mod-two boundary ranks and all reduced Betti numbers. The proof of the integral wedge rests on the acyclic matching, not on ranks alone.

The computation is finite, deterministic and bounded at 16,384 candidate subsets. It proves no statement about other graphs, higher parameters, or equivariant structures. Independent external auditing has not been performed.
