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

The accompanying `verify.py` is standalone and uses only Python's standard library. Execute `python verify.py` from this directory. Its successful terminal line begins `VERIFY_OK` and lists the separately counted checks.

The implementation contains two independent depth-type constructions: ordinary one-relation modal signature refinement and reversal classes of explicit cyclic substrings. A separate dihedral-group enumeration supplies orbit partitions, while a small Boolean-algebra closure implementation checks the cardinalities of generated algebras without relying on either partition method. For disconnected cases a joint refinement is calculated from actual adjacency tables.

The replayed checks covered 8,184 exhaustive binary cycle words of sizes 3 through 12, 43,688 comparisons of bounded-depth partitions, 5,400 generating cycle colorings, 56 direct Boolean closures, all 28,672 colorings of the two-component cases \(C_6\sqcup C_7\), \(C_7\sqcup C_7\) and \(C_6\sqcup C_6\), and 320 seeded random examples on four larger cycle lengths. The two-component counts are respectively 336, 392 and 0. The three-mark pattern is tested at all sizes 6 through 120. The Möbius count is compared with exhaustive labeled-coloring counts, not merely with a copied numerical table.

These finite tests check implementation consistency and small cases only. The all-length statements rely on the string reconstruction lemma, the parity-aware dihedral orbit proof, and the periodic-word argument documented in RESULT.md. No claim of independent expert verification or a formal proof assistant certificate is made.
