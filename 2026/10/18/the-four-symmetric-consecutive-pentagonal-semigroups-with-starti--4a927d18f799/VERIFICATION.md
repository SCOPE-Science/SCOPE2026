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

Run `python verify.py` from the directory containing the seven included files. The script uses only Python's standard library. It asserts exact gcd-and-representation certificates for all minimal three-generator cases with indices 3 through 70 (excluding index 5, where one generator is redundant). Independently it computes Apéry representatives by a shortest-path algorithm for every index 2 through 70, checks the genus/Frobenius symmetry criterion, and returns the same four exceptions.

The infinite tail is handled by the explicit inequalities in RESULT.md. The executable confirms the boundary polynomial signs at indices 6, 10, and 71, but these tests are not substituted for the proof that the quadratics are increasing beyond those indices. Computations beyond the fixed finite interval are not used to establish the theorem.

The gluing classification is a cited published theorem; this package does not attempt to prove that general structural theorem. No independent mathematical audit or third-party validation has been performed.
