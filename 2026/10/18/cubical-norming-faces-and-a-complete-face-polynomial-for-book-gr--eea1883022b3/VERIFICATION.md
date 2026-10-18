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

# Reproducibility and limits

Run `python3 verify_book_faces.py` using Python 3 and no external dependencies. The checker constructs normalized dual vertices from the three allowed hub heights, independently identifies extreme normalized integer potentials via connected tight-edge graphs, intersects every defining Lipschitz inequality, and obtains exact face dimensions using integer Gaussian elimination. It checks \(m=2,3,4,5,6\) and terminates with `ALL EXACT BOOK-GRAPH FACE CHECKS PASSED`.

The finite checks do **not** establish the theorem for untested \(m\). The all-parameter proof is the case analysis for arbitrary support functionals in `RESULT.md`. No independent scientific audit or external certification has been performed.
