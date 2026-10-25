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

# Verification of the dihedral wheel matching-complex character

Run `python3 check_wheel.py` in the same directory as this document. This standalone script uses only Python's standard library.

The program constructs every matching as a simplex, checks setwise invariance under every rotation and reflection, and includes the permutation sign on its oriented simplicial chain. It subtracts the empty-simplex contribution to obtain the reduced Lefschetz number and extracts the expected homology trace using the proved single-degree homology concentration. It independently enumerates the rim-cycle faces and compares with the explicit path-recurrence character formula.

**Actual results:** `PASS: signed wheel and rim character equalities: 672`; `PASS: independent mod-two boundary-matrix homology: 8 wheel sizes`. The group-element checks cover all \(D_n\) elements for every \(3\le n\le18\); the mod-two boundary checks cover \(3\le n\le10\).

**Verification limits:** The character checks rely on the mathematically established concentration of homology in one degree. The mod-two ranks do not exclude integral torsion for untested sizes. Universal torsion-freeness and the exact integral module sequences instead follow from the proof in RESULT.md. Neither finite checks nor a self-review constitute independent auditing.
