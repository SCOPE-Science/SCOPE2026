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

# Reproducibility

Run `python verify.py` with an ordinary Python 3 interpreter; it requires only the standard library. It reconstructs finite graph independent-set polytopes, forms nonnegative fractional-coloring dual inequalities, enumerates feasible basic solutions by exact Gaussian elimination over rational numbers, identifies optimal dual supports, and verifies that every coordinate outside the optimal support admits a positive feasible displacement in the scaled stable-set polytope (via all dual-vertex inequalities). The expected final line is `VERIFY_OK`.

The checked graphs are the edgeless three-vertex graph; the triangle; the three-vertex path; an edge with an isolate; the five-cycle; and the four-clique with an isolate. Exact factors are respectively \(1,3,2,2,5/2,4\), with corresponding center-space dimensions \(0,0,0,1,0,1\). The mathematical proof in `RESULT.md` applies to every finite simple graph. The computations do not enumerate all graphs or independently certify the theorem; no external review has been performed.
