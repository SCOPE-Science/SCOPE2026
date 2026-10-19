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
# Verification record

`verify.py` is self-contained Python (standard library only). Running `python verify.py` checks reduced-row-echelon subspace enumeration, alternating-form isotropy, complement adjacency, common-neighbor triangle counts, closed isotropic counts, independent nonsingular-symmetric matrix counts, and direct Lie-bracket generation for \((q,n)=(2,1),(3,1),(2,2),(3,2)\). It additionally checks the higher-rank \((q,n)=(2,3)\) case by exact subspace and common-complement enumeration. All five tests succeeded and printed `VERIFY_OK 5 cases; direct Lie-bracket closure and triple counting`.

The cases \(n=1,2\) are boundary consistency tests, not accepted novel claims. An exhaustive finite sample is not proof for all prime powers; the general result rests on the written algebraic argument. No full-graph invariants are certified and no independent audit has been performed.
