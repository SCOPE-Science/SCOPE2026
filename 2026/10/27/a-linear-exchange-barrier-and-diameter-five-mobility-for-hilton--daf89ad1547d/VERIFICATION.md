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

Run `python3 verify_bitset.py` and `python3 verify_pairwise.py` in the same directory as the scripts. Both use only the Python standard library and construct families from triples before examining all unordered pairs of candidate extremizers. Expected standard outputs are retained in `verify_bitset.out` and `verify_pairwise.out`.

The first script checks all pairwise batch-exchange distances and exact adjacency rules for \(n=7,8,9,10\), the labeled-count and regularity formulas, edge counts, and shortest-path layers from one representative of each symmetry orbit. The second uses frozensets, independently tests pairwise intersection and nontriviality of every constructed family, and verifies the graph and diameter for \(n=7,8,9\); for \(n=7\), it tests the eccentricity of every one of the 175 configurations.

These finite validations neither enumerate all possible set systems on arbitrary \(n\) nor prove the Hilton–Milner equality classification. The latter is an explicitly cited published theorem. The all-\(n\) overlap and path proofs are in `RESULT.md`. No formal mechanized or independent external audit was performed.
