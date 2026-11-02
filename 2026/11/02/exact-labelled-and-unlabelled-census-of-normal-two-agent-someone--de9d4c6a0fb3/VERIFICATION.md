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

The included `checker.py` uses only the Python standard library. Run `python3 checker.py` from the folder containing this file. It enumerates all ordered pairs of partitions for world sizes one through six, compares direct local-cell nesting with the independent incidence-star test, verifies all meet equations over every pair of propositions through four worlds, and checks the global-comparability count. It separately enumerates simultaneous relabelling orbits through five worlds and checks both generating-function coefficient sequences. A completed run printed `ALL_CHECKS_OK`.

The finite checks establish finite instances only; the symbolic all-size proof in `RESULT.md` supports the infinite family of enumerative identities. No independent audit or external mathematical certification has been performed.
