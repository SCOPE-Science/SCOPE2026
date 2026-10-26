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

The analytical proof is given in RESULT.md. Run `python verify_equivalence.py` using Python 3 with no external packages. Its observed output was:

```
PASS 1227 exact/numeric checks; nonzero mismatch cases=12; triangle spectral equality=27/50
```

The program exhaustively tests all 16 binary profiles on the four-cycle and all 64 binary profiles on the complete tripartite three-uniform hypergraph, and all eight on the triangle. Most tests are exact rational comparisons of accumulated payoffs and spectral identities. A smaller number evaluate finite-strength logistic probabilities numerically. These finite checks do not certify the infinite family of graphs and hypergraphs; that part follows from the incidence-kernel argument in RESULT.md. The independent audit has not been performed.
