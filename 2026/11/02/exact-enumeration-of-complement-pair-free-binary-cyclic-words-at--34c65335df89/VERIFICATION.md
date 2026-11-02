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

**Actual command:** `python3 verify.py`.

The self-contained script reconstructs the 256 orientations of all eight complement-pairs of length-four factors in the eight-state de Bruijn graph. It directly computes all 324 cycle-bearing SCC edge sets and checks coverage by the six displayed families. It also checks the recurrent cycles of all 15 pairwise family intersections, and computes each of the six eight-by-eight adjacency determinants with exact integer power traces and Newton's identities. These checks establish the finite graph premises used for an all-length theorem.

A separate direct source-word enumeration checks every one of the 131,056 marked binary circular words of lengths 4 through 16, and both the general counts and the mixed-doublet counts agree. Exact transfer traces agree at all lengths 1 through 30. The script prints `VERIFY_OK; orientations=256; recurrent_SCCs=324; families=6; pair_intersections=15; bruteforce_instances=131056; lengths=4..16; transfer_lengths=1..30` when successful.

**Scope of verification:** finite component coverage and characteristic polynomials are exhaustive for their stated fixed graph classes; direct word enumeration is only finite validation, not an infinite proof. The all-length deduction, inclusion-exclusion correction and spectral consequences are reconstructed in `RESULT.md`. The priority comparison is qualified by potential unindexed literature. This verification is not an independent scientific audit.
