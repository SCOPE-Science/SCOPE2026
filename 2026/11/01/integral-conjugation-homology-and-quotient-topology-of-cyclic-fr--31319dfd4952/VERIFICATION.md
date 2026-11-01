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

Run `python verify.py` from the extracted files using Python 3. No third-party packages are needed. The checker enumerates all prime-power commuting edges and components for four finite Frobenius groups, compares the predicted first Betti numbers, and checks the three-prime local join face count. The expected Betti-one values are 0, 26, 93 and 215, followed by a local rank-15 computation from the join formula.

The unrestricted claim is proved through unique complement containment, the commuting criterion, join Künneth homology, affine conjugation and stabilizer analysis in RESULT.md. Finite tests do not certify the theorem for infinite parameter ranges. The homotopy statement holds only for the stated fixed-point-free cyclic semidirect products. Independent mathematical audit has not been performed.
