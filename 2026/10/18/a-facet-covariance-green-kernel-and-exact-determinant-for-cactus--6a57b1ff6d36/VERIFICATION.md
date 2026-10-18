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

# Reproducible mathematical checks

The accompanying `verify.py` is a standard-library exact-arithmetic verifier. It generates every rooted integral 1-Lipschitz potential for ten distinct small unweighted cactus graphs and retains precisely those whose unit-difference tight-edge subgraph is connected. It computes their zero-sum covariance directly. Separately, it builds a weighted Laplacian with an edge resistance of \(r/(r-1)\) on even cycles and one elsewhere, then computes its Moore--Penrose inverse with exact rational elimination. It compares all matrix entries, every ordered pair's potential-difference variance with effective resistance, the predicted facet count and exact centered determinant.

The ten cases include trees, odd cycles, even cycles, two cycles attached at a vertex, and cycles connected by a bridge. Exact numerical values include 36 facets, trace \(29/9\), and determinant \(8/243\) for the triangle--square bouquet. The entry point `python3 verify.py` needs no third-party packages and returns `ALL EXACT FINITE CHECKS PASSED` on success.

These finite computations test implementation and sample consequences; the all-dimensional theorem depends on the proof using the cactus block structure, projection covariance and weighted Matrix--Tree Theorem. There is no computational claim about noncactus graphs or every finite cactus.
