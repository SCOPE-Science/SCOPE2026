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

# Reproducibility and scientific limits

Run `python verify.py` with Python 3 and no third-party dependencies. The checker builds vertices and edges independently, forms the full weighted Laplacian, exactly inverts a rank-one gauge regularization over rational numbers, and constructs the edge-gradient projection matrix entry by entry. It verifies the predicted absolute row sums for every generated oriented edge in ten finite examples, plus matrix symmetry and the squared-diagonal idempotence identity. Homogeneous clique-product identities are checked for many finite dimensions and clique sizes. Floating-point auxiliary comparisons test the claimed ordering of candidate optimized rows.

The analytic proof in RESULT.md, not numerical or finite exact enumeration, justifies all dimensions, all positive real conductances, and the unique maximizing conductance ratios. The checker is not a general symbolic proof and cannot exclude unknown historical equivalents. No independent audit has been performed.
