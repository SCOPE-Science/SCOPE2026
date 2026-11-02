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

# Verification record

Run `python3 verify_binary_ancestor_neighborhoods.py` with Python 3.10 or later and no third-party dependencies. It reconstructs the graph independently using a heap-indexed binary tree, enumerates all closed-neighborhood traces and checks the exact support classification and coefficients. For heights one through four every support of size up to four is checked; for height five every support of size up to three is checked. It also computes Littlestone dimensions for heights one through four by exhaustive memoized version-space recurrence. The expected terminal marker is `ALL_ANCESTOR_INCIDENCE_NEIGHBORHOOD_CHECKS_PASS`.

The checker confirms height-by-height coefficients \([1,2]\), \([1,7,16]\), \([1,15,62,16]\), \([1,31,218,112]\), and \([1,63,754,576]\), together with adaptive depths \(1,2,3,4\) on the first four heights. These are exhaustive only over the stated finite ranges. The general shattering formula, absence of larger supports, exact adaptive rank, chordal bipartiteness and diameter statements are mathematical claims with proofs in `RESULT.md`, not consequences of the finite checker alone.
