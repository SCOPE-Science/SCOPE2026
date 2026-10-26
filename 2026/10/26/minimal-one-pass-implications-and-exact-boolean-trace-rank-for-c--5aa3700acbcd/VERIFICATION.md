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

## Reproducible finite checks
Execute `python3 verify.py`. The program enumerates every vertex subset on cycles of orders \(3\) to \(15\), constructs all maximal independent sets by direct adjacency and domination tests, computes closure by intersections of containing objects, and compares these values with the proposed one-pass Horn consequences. It also checks shattering by enumerating all candidate vertex subsets and their realized traces, and checks the predicted rule counts.

## Limitations
All enumeration is finite, and does not establish formulas for larger orders. Their proof is in RESULT.md. No independent audit is represented or claimed.
