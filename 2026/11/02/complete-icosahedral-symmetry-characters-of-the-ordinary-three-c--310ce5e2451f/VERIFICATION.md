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

# Exact verification and scope

Run `python3 verify.py` with Python 3 and the standard library. It reconstructs the specified twelve-vertex thirty-edge icosahedral graph and all 140 disconnected triples, then enumerates all 3,906 nonempty cut-complex simplices and the Alexander-dual simplices.

The Alexander-dual signed boundary ranks are computed over the rational numbers, with exact `Fraction` pivots. Their values in dimensions one, two and three are 11, 49 and 30. Independently, the cut-complex boundary ranks in dimensions seven and eight are 330 and 134 over the prime field of characteristic 1009, consistent with rational Betti numbers one and six. The checker exhibits a cycle outside the degree-eight boundary image, checks its boundary directly and verifies its signed image in the homology quotient under all 120 graph automorphisms.

Signed fixed-simplex traces are recalculated under all 120 automorphisms. Rotations have reduced Lefschetz values 5, -3, -1, 0 in order classes 1, 2, 3, 5; opposite-vertex inversion multiplied by those rotations gives -5, 3, 1, 0. The mathematical proof identifies the rational characters from these traces, exact rational Betti numbers and the A5 character table, rather than extrapolating from finite-field computations.

Successful execution prints `ICOSAHEDRAL_THREE_CUT_FULL_EQUIVARIANT_EXACT_OK`. This does not constitute independent validation. No integral homology-representation, quotient-contractibility or unindexed-literature claims are certified.
