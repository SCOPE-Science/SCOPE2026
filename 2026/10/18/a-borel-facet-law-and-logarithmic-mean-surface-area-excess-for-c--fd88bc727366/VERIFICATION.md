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

# Verification and reproducibility

Run `python3 check.py` with Python 3 and no third-party dependencies. The program enumerates every Prüfer code for \(3\le n\le6\), verifies each tree incidence Gram determinant and every facet Gram minor using integer-preserving Bareiss elimination, tests exact expected cut counts and Euclidean surface area by direct full-ensemble averaging, and checks sharp deterministic star/path bounds. There are 1,440 labeled-tree instances. Numeric large-order evaluations at \(100\), \(1000\), and \(10000\) provide asymptotic consistency checks only; rigorous uniform error bounds are proved in `RESULT.md`, not inferred from the numeric ratios.

The codimension-one intrinsic Euclidean metric, the uniform Cayley tree model, and the uniform-over-facets sampling rule are part of the claim. The Borel distribution proof and nonuniform-integrability conclusion are analytic. No external independent mathematical audit or formal certification is asserted.
