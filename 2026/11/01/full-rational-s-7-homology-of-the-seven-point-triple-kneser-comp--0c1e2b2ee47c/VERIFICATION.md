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

# Exact verification

Execute `python CHECKS/verify_character.py` and `python CHECKS/verify_faces.py` from the extracted directory; both use only Python 3's standard library. The first computes the exact signed independence-polynomial recurrence on all fifteen orbit graphs and the complete irreducible-character inner products by Murnaghan–Nakayama. The second enumerates every compatible orbit subset and independently accumulates signed chain traces. Both passed the stated checks, including the identity's \(1{,}278{,}686\) invariant faces and the \(29\) and \(7\) rational rank constraints taken from arXiv:2610.17394v1.

The finite computation is exhaustive because all three-element subsets of seven points, every permutation orbit, every admissible orbit collection, and every partition of seven are considered. The fixed-face formula, chain orientation sign, character decomposition, and semisimple-dimensional argument are spelled out in `RESULT.md`; scripts alone are not treated as proofs of the homology-rank input. No assertion about integral torsion, wider parameters, or independent verification is made.
