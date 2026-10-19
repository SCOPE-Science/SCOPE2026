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

# Reproduction and limits

Run `python check.py` with Python 3.9 or later; no third-party dependencies are required. It reconstructs full finite graph partition functions using exact rational arithmetic and independently compares each result against the pinned-core expression, including a five-vertex alternative core. It also checks exact coefficients, sign factorization, and bounds for the paw threshold polynomial. The expected output confirms 88 exact partition comparisons and all further checks.

The exact symbolic factorizations and hyperbolic-cosine argument appear in RESULT.md. Finite arithmetic verifies examples, not the general all-parameter theorem; the paper proof supplies the latter. The logarithmic optimizer assumes \(\theta\ne1/2\), while the equal-risk case is handled separately. At the unique threshold the two integer allocations tie. The result assumes fixed core, undirected simple edges, homogeneous finite log-linear rationality and stationary sampling; no conclusion concerns the mixing time or global unrestricted network design.
