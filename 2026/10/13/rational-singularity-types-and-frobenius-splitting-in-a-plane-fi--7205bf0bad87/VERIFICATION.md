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

# Reproducibility and limits

Run `python3 verify.py` using Python 3.8 or newer. No packages beyond the standard library are required. The program enumerates rational parameter-point pairs and confirms the local affine second and third jets for fourteen prime fields (characteristics \(3,5,7,11,13,17,19,23,29,31,37,43,71,113\)). It compares node splitting with quadratic characters, verifies the total cusp/split/nonsplit counts and the characteristic-independent parameter condition, and for the five prime fields up to \(19\) exhaustively checks all projective rational points for omitted singularities, including infinity.

Expected terminal status: `VERIFY_OK: rational node/cusp, branch splitting, and finite-field census tests`.

All-field statements, including nonprime finite fields, follow from the exact algebraic proof in `RESULT.md`: the rational gradient equations, the local jets and formal normal form, and the finite-field character identity. The executed examples do not constitute an exhaustive computation over all finite fields, nor do they decide global smoothness or singularities over extension fields. Independently collected mathematical validation has not been performed.
