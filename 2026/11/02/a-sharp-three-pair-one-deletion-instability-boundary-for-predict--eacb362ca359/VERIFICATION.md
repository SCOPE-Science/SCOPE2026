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

# Reproducible verification

Run `python3 verify.py` using the included script and Python's standard library. A successful run prints the exact counts and `PASS`.

- The script enumerates 290 labeled markets/reference/pruning combinations with one or two pairs and checks original stability after DA.
- For the displayed three-pair witness, it checks the full list of original stable matchings, the predicted-center ranks, common radius one, one removed hospital–resident edge, the DA result, and the omitted blocking pair.
- It enumerates 1,531,392 three-pair instances of deletions lying strictly below a surviving stable reference, checking equality of pruned and full hospital-proposing DA outcomes and stability in the full market.

Exact ranks and integer comparisons are used throughout; no numerical tolerances or external dependencies are required. The all-\(n\) results have analytic proofs in RESULT.md. Testing finitely many markets is not a substitute for those proofs. The finite program does not exhaust three-by-three prunings that may delete above-reference edges, except for the explicit witness.
