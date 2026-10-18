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

# Verification of the dihedral wheel character

The proof is universal and combinatorial: the unsubdivided two-particle cubical model is valid for every wheel in scope, its second boundary has no kernel by the spoke-and-rim fiber argument, and the signed fixed-cell table exhausts rotations and reflections. Equality of rational characters gives the representation theorem.

The included Python verifier constructs the ordinary unordered cubical cells using disjoint closures, checks the signed cellular identity \(\partial_1\partial_2=0\) over integers, obtains full column rank of \(\partial_2\) over \(\mathbb F_2\), checks the rank of \(\partial_1\), and computes the actual signed Lefschetz trace for every rotation and reflection, for each \(4\le n\le14\). It reports `VERIFY_OK_WHEEL_TWO_POINT_DIHEDRAL` on success.

Run `python verification/check_wheel.py` using Python 3.10+ without other dependencies. The finite range does not independently establish the all-parameter theorem. No independent scientific audit has been performed, and no integral equivariant decomposition is certified or claimed.
