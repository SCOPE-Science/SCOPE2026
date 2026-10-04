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

`verify.py` is a standard-library exact-arithmetic cross-check. It enumerates every orientation of every cycle of length \(3\) through \(8\). For each orientation it checks the primitive signed cycle relation; every spanning-tree determinant; the normalized determinant \(|p-q|\) of every un-semibalanced root simplex; the predicted half-open fundamental-parallelepiped heights; and the \(h\)-polynomial of the relevant circuit triangulation reconstructed from its full face set.

The analytic proof in `RESULT.md`, not the finite enumeration, establishes the theorem for all \(m\ge3\). The computation does not check arbitrary unicyclic graphs or any family beyond cycles.
