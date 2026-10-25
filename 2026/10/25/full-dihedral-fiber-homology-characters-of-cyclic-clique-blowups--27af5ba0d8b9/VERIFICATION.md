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

# Reproducibility and checks

Execute `python3 VERIFY.py` using Python 3 standard library. The script explicitly constructs the simplices of clique-blown-up cycles; it does not load or trust an external topology table. It compares exact mod-two Betti numbers against the proposed formula for fourteen base/width pairs, verifies 1332 fiber-element signed Euler identities, and checks 864 full semidirect-product chain-character identities with reflections and rotations. Successful output contains `EXACT_MOD2_HOMOLOGY_MATCHES_WEDGE_FORMULA 14`, `FIBER_PERMUTATION_LEFSCHETZ_IDENTITIES_VERIFIED 1332`, `CYCLE_CLIQUE_BLOWUP_VERIFICATION_OK`, and `FULL_WREATH_EQUIVARIANT_CHAIN_SPLITTING_VERIFIED 864`.

The general correctness claim rests on the augmented rational chain-level decomposition and path/cycle link calculations in RESULT.md; finite computations are not asserted to prove the infinite family by enumeration. Mod-two checks test torsion-free dimensions only for the indicated instances, not all integral Smith forms. Independent mathematical review has not occurred.
