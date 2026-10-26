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

The standalone checker reconstructs both generator families over \(\mathbb F_{37}\), checks row rank, evaluates the published NMDS criteria over all required subsets, and computes every Euclidean hull dimension by exact modular Gaussian elimination. It verifies the two source-paper examples, all count totals, and the full lists of NMDS parameter pairs with hull dimension one. The executed checker returned `VERIFY_OK`.

Scope limits: the NMDS iff criteria are cited from the primary paper rather than reproved here; the hull-rank computation and finite census are independently recomputed. No independent audit or external certification is claimed. The full text of one related generalized Roth-Lempel hull paper remained inaccessible, and this limitation is retained as a literature-overlap risk.
