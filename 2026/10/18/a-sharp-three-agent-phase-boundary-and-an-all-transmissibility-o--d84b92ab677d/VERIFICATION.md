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
# Reproduction

With Python and SymPy available, run `python verify_influence_risk.py` from this directory. The standalone program checks the complete list of variance-submodularity gaps for all connected graphs on at most three vertices, and it cross-checks the bond-exploration formulas against independent directed-edge outcomes on the triangle, path, and five-vertex star at two rational probabilities. It verifies the star conditional-moment expression for stars with two through six leaves and tests the factorized obstruction algebraically through seven leaves.

The successful program result is `PASS` followed by the numerically isolated cubic threshold. The formal proofs of the arbitrary-size star identity, the exact floor formula, the limit, and root uniqueness appear in `RESULT.md`; exhaustive small-instance testing is not an infinite proof. No independent audit or independent model validation is asserted.
