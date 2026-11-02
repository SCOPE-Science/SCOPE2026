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

# Verification record

The complete classification is embedded as `data/additive_orders.csv` and `data/abelian_orders.csv`. Run `python3 verify.py` with Python standard library only, in the directory containing both CSVs and the script.

The implemented checks verify that all \(1705\) orders are represented exactly once in each table, all positive witnesses satisfy their stated equality predicates in the level-sixteen substitution cover, every absence and presence classification agrees with a separate minimum-sufficient-level exhaustive scan, and every cumulative count agrees with the theorem. The expected output is `VERIFY_OK additive=579 abelian=462 additive_only=117 cutoff=1705`.

The finite procedure is exhaustive for the infinite word precisely because any factor of length at most \(4\cdot1705\) lies inside one of five permitted adjacent level-sixteen substitution images. This claim is proved in `RESULT.md`, independently of the CSV values. No order greater than \(1705\) is checked or asserted to be classified. An independent audit has not been performed.
