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

# Reproducibility and verification

Run `python3 verify.py` in a directory containing the accompanying source file. No external libraries are required. The program directly constructs the affine groups of 14 finite chain rings, partitions elements into conjugacy classes by explicit conjugation, directly counts centralizers, computes the unit-group orbits in the additive dual, evaluates the character orbit sums using genuinely generating additive characters, and cross-checks the formulas and the group-order sum-of-squares identity.

The tested coefficient rings are truncated polynomial rings over the prime fields of sizes 2, 3, and 5; integer residue rings with the corresponding prime powers; and two truncated polynomial rings over the four-element field. All 14 configurations passed the actual standalone execution. The case of both nonisomorphic order-eight rings and their affine groups of order 32 was included.

The source tests only finite examples; it does not prove the formulas for arbitrary ring sizes. General correctness rests on the conjugacy, ideal-annihilator and representation-theoretic arguments in `RESULT.md`. All bibliographic-originality claims have residual independent-review risk. No independent audit or external mathematical certification was performed.
