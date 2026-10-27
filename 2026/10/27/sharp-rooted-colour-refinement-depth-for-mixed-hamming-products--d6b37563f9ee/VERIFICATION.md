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

Run `python verify_mixed_hamming.py` with Python 3 standard library. The verification program is complete and self-contained, and its recorded successful terminal output is in `verification_output.txt`.

The independent full-graph construction checks 242 combinations of dimensions one to five and factor sizes in \(\{2,3,4,5,6\}\) (retaining products with at most 3500 vertices). It refines each actual graph from one marked root, tests the exact first stable round against the theorem, and verifies the full partition by pairwise equivalence with the coordinate profiles.

A separate weighted quotient uses exact neighbor multiplicities and tests seven selected higher-dimensional cases, including ten and twelve factors. The two approaches use different adjacency constructions. The exact pass record contains `FULL_GRAPH_CONFIGURATIONS=242`, `WEIGHTED_QUOTIENT_CONFIGURATIONS=7`, `SHARP_ROUNDS_AND_ORBITS=PASS`, and `ALL_TESTS_PASS`.

The general theorem is proved by the frontier induction, the profile-recovery induction, and explicit orbit symmetries in `RESULT.md`. Finite computations are corroboration only. No exhaustive enumeration of all dimensions or factor sizes is asserted, and no independent validation is represented by these records.
