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

# Verification instructions

Run `python3 check_cylindrical_king.py`. The checker is fully self-contained, uses only the Python standard library, constructs the exact graphs by their adjacency rule, and fails with an assertion if any check differs.

It first tests all fifteen local graph-reduction templates over seven or six sample full-tail lengths, for a total of 104 exact inclusion-and-child-mask tests. Their universal force comes from the separate locality proof in RESULT.md: every involved vertex lies in the first three rows, and graph edges join only adjacent rows, so arbitrary later tail rows cannot affect the checks. The same executable then derives initial homotopy types by complete finite graph reductions, compares direct mod-two simplicial boundary ranks for both the full and fixed complexes through nine rows, independently executes homotopy reductions through eleven rows, and checks total Betti equality through thirteen rows. The finite tests are corroboration, never a replacement for the unrestricted symbolic proof.

Computational checks cannot establish independent mathematical validation or prove absence of a result in unindexed literature. The theorem is nonequivariant except for the expressly stated fixed-point homeomorphism and equality of total Betti numbers.
