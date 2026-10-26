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

The exact-arithmetic checker `verify.py` constructs the 84-state transition graph from the stated definitions, computes all 84 required power traces, reconstructs the characteristic determinant via Newton identities, and compares every coefficient with the independent seven-factor product. It separately performs small direct graph-coloring backtracking, verifies strong connectivity, and checks three constructive closed walks.

Command: `python3 verify.py`.
Expected terminal marker: `VERIFY_OK: transfer, exact determinant, direct counts, constructions`.

The infinite sequence count follows mathematically from the transfer bijection and formally proved determinant identity, not from observing finite circumferences. Independent scientific audit is not performed.
