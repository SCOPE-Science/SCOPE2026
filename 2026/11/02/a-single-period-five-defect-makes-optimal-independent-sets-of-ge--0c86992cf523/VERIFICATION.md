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

# Verification

Run `python3 verify_gp_maximum.py` and `python3 verify_gp_templates.py` in the extracted directory. Only the Python standard library is used.

The first implementation enumerates optimal words from cyclic local constraints, without using the proposed symbolic template as its search space, at graph lengths 5, 9, 10, 14, 15, 19, 20, and 24. It independently derives all one-for-one exchanges and checks the exact predicted adjacency and component structure.

The second constructs actual vertex and edge bitsets of each generalized Petersen graph. It exhaustively compares the full combinations of candidate optimum vertices for lengths 5, 9, and 10, independently verifies every possible token replacement from all templates, and checks the exact neighbor list for all indicated lengths at most 99. It verifies that every predicted exchange is an edge of the *actual* token-jumping graph. The explicit proof in RESULT.md establishes that each of the three edge types is also a token slide.

No finite run is claimed to prove the infinite result. The proof depends on a complete cyclic-run classification and an exchange-position argument valid for every positive integer parameter. No independent external audit has been performed.
