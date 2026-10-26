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

The accompanying `verify.py` was executed using a standard Python 3 interpreter without optional packages and completed normally. Its final line was:

```text
VERIFY_OK; seven base certificates; all n=10..500; 1092 socket concatenations
```

For each table, it reconstructs the graph from first principles and checks: unique \(3n\) undirected edges; four neighbours for every edge; distinct colours at every pair of adjacent edges; exact richness based on the colours of all four neighbours; and a rich neighbour for every edge. It checks the four-column common prefix before testing compositions.

The evidence for all infinitely many \(n\) is the separate five-column locality and common-prefix gluing proof in `RESULT.md`, plus the elementary decomposition of every \(n\ge10\). The finite tests neither enumerate all possible colourings nor establish historical novelty. The checking code has no external data or software dependencies.
