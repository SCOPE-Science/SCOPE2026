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
# Reproducibility and boundaries
Run \(\texttt{python checker.py}\) using only the Python standard library. The implementation independently checks conflict-freeness and structure-sensitive defense by quantifying over the reflexive-transitive subargument closures, without using the cutoff formula for their evaluation. All labelled direct-attack matrices of sizes 1 through 4 (66,066 total), a deterministic sample of 600 sizes 5 through 8, and 17,576 effective cutoff profiles through size 8 were tested. The recorded result was \(\texttt{ALL_CHECKS_OK 1019526 direct_attack_structures 66666 profile_n_le_8 17576}\).

This enumeration is exhaustive only on its stated finite domains. The unrestricted claims depend on the four symbolic proof steps in RESULT.md; no formal proof assistant or independent external certification was used. Edge conditions \(n=1\), self-attacks, attackless rows, and absence of a stable extension are allowed. The program and textual proof require no external data files.
