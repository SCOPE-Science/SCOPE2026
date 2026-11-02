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

Run `python3 verify_three_core.py` with Python 3 standard library only. The script independently calculates a Pareto completion by exact-integer satisfaction-vector dynamic programming and checks every coalition and every quota-sized partial alternative assignment against the complete outcome.

Results: all 31,464 profiles represented by unordered multisets of the 27 possible full round-ballot triples through four rounds passed; all 1,715 profiles represented by seven specified structural round types through six rounds passed; and 900 further seeded full-ballot profiles with 3–7 rounds passed. The first exhaustive statement is exhaustive only up to permutation of rounds, which does not affect any utility or core condition. The second set does not enumerate all longer full-ballot types. These finite computations check consistency only; the all-horizon theorem follows from the analytic proof in RESULT.md.

No independent audit, externally verified certificate, or claim for larger electorates or more candidates is provided.
