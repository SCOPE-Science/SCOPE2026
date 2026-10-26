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

The accompanying `check.py` is a Python standard-library verifier. It creates all nonzero Hamming check-column labels, builds the exact adjacency graph for each set of check equations, and executes a maximum-cardinality-search chordality decision with direct perfect-elimination-order verification. The loops enumerate all 31 nonzero augmenting rows in five check dimensions and all 63 singles and 1953 distinct pairs in six dimensions. They test explicit matching constructions in dimensions three through six. Run `python3 check.py` and compare with `check_output.txt`.

Finite exhaustive checking gives exact nonchordality for the listed dimensions and row counts. The extension to arbitrary higher dimensions requires the separate proved canonical-coordinate and induced-subgraph lemmas in `RESULT.md`; no finite test alone establishes those infinite statements. The source code contains no stochastic sampling, solver timeouts, or external dependencies. Scientific originality remains subject to human literature review; no independent audit has been conducted.
