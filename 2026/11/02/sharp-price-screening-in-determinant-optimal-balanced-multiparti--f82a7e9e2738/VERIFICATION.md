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

# Verification notes

Execute `python3 verify.py` with Python 3 and the standard library. The verifier rebuilds reduced Laplacians from independently constructed graph edges and uses rational Gaussian elimination for their determinants; it compares them with the analytic weighted tree product. It additionally tests exact threshold equivalence, exact rational derivative signs, and the positive quadratic root on a grid of integer dimensions and rational prices. Finite evaluations are a diagnostic, not a proof of the infinite-family theorem.

Proof-critical checks: (1) the edge-weight to grounded Laplacian map is injective for simple graphs; (2) the orthogonal eigenspace decomposition accounts for all \(rm\) dimensions; (3) cost elimination yields the exact derivative numerator \(C+Lt-At^2\); (4) the linear coefficient \(L\) is negative at and beyond the boundary, so no overlooked positive local optimum survives; (5) the critical-window result is a direct limit of the exact root condition.

No external audit or certification has been carried out. A possible previously published equivalent price-allocation theorem under different terminology is not ruled out.
