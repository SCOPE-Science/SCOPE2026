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

# Reproduction and mathematical boundaries

The standalone file `verify.py` uses only Python's standard library. Execute it from the directory containing the extracted file with `python verify.py`.

Observed output:

`VERIFY_OK bfs_cases=105 bfs_states=1622619 interval_cases=53130 large_witnesses=1606`

The BFS independently determines the shortest reset word length for every specified pair through \(n=16\), rather than merely replaying a proposed word. A separate exhaustive check verifies inverse-interval preservation and dominance for all nonfull intervals through \(n=22\). Further direct witness checks run through \(n=60\). The theorem over all integers is proved by the inverse-preimage dominance argument and phase count in `RESULT.md`; finite tests do not prove the universal quantifier, and passing a test is not a claim of independent validation. The source-inspection comparisons and unresolved priority limits appear in `REVIEW.md` and `AUDIT.json`.
