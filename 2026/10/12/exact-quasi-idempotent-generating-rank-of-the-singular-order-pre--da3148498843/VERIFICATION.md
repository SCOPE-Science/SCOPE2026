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

The included `checker.py` constructs the sixteen-state max-plus transfer matrix directly from four forbidden local pairs and verifies its exact identity \(T^9=T^4+4\) entrywise. Combined with associativity, this gives a proof for all subsequent exponents, not an extrapolation from experimental samples. The checker also compares the derived closed rank with direct dynamic evaluation for \(4\le n\le100\), enumerates all generator subsets and compares local clauses against exact top-rank multiplication closure for \(4\le n\le8\), and checks an explicit ten-generator family for \(n=9\).

Small enumerations test the modeling and boundary conditions but do not independently prove every infinite-dimensional implication; the mathematical proof of equivalence between generation and the graph clauses is given in `RESULT.md`. The exact tropical matrix equality is a finite certificate and is fully re-executed from source, without external packages. The statement concerns singular full order-preserving transformations and does not claim an independent audit.
