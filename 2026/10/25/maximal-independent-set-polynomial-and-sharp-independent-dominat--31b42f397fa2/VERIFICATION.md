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

## Reproducibility and limits
Run `python3 verify.py` with Python 3 and the `networkx` module. The program builds the token graph from the host-edge symmetric-difference adjacency, finds maximal independent sets directly as cliques in the complement, compares the resulting complete size distribution to the derived polynomial, and independently checks total count, minimum size, and number of minimizing sets. The run completed with `VERIFY_OK pairs= 15 distinct_maximal_independent_sets= 6947`. All pairs \(2\le m\le n\le6\) are covered by the finite check. The proof in `RESULT.md`, not the limited test, establishes the formula for arbitrary \(m,n\) in the claimed domain. No independent audit has been performed.
