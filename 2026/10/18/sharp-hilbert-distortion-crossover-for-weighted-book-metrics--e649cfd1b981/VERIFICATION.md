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

The stand-alone script `verify_weighted_book_bm.py` uses only the Python 3 standard library and tests the new exact theorem. Execute from this directory with `python3 verify_weighted_book_bm.py`.

In the completed run, it printed `EXACT_BOOK_BM_CHECKS_PASS 63 parameter cases, 25200 rational comparisons, 286 vertices`. It checks rational \(H\) values from \(1/12\) through \(1\) and integer \(m\) from \(2\) through \(8\). For selected small dimensions it independently solves the intersections of full polytope facet systems with exact rational row reduction to check the claimed outer quadratic maximum. It also checks that every one of 25,200 trial rational ellipsoidal shapes is no better than the proposed optimizer, and compares two known edge cases.

Finite checks do not establish the all-dimensional, all-real-parameter claim. The general certificate is the explicit dual-ball transformation, symmetry-averaging inequality, exact inner/outer quadratic radii, and sign analysis of the one-variable derivatives in RESULT.md. No numerical optimizer or software-generated log is used as a substitute for the proof. Independent audit has not been performed.
