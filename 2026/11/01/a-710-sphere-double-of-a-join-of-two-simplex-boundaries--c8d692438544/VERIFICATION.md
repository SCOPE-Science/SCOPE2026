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

# Reproducibility

Execute `python3 verify.py` in this directory using any ordinary recent Python 3 interpreter. No third-party package is required. The executable reconstructs the two-block boundary join, lists every admissible matching, compares a separate exhaustive family tester, computes mod-two chain boundary ranks, constructs the deterministic acyclic matching and checks the complete 3,900-incidence directed Hasse diagram for cycles.

It separately evaluates the signed fixed-simplex Lefschetz formula over all 2,880 permutations in \(S_4\times S_5\), checks constancy on 35 conjugacy classes and zero invariant multiplicity, then uses exact rational class sums and Murnaghan–Nakayama characters to verify and regenerate `character_table.csv` and `irreducible_multiplicities.csv`.

Expected terminal success signal: `ALL_VERIFY_OK`. The relevant exact quantities are 36 vertices, 375 edges, 1,050 triangles, 375 matched pairs, one critical zero-cell, 710 critical two-cells, 35 conjugacy classes, and 22 nonzero irreducible constituents (counting types, not multiplicity).

The mod-two Betti check alone would not establish integral homotopy. The integral conclusion uses the complete acyclicity and critical-cell certificate. No generalization to larger joins, independent external audit, or equivariant homotopy equivalence is asserted.
