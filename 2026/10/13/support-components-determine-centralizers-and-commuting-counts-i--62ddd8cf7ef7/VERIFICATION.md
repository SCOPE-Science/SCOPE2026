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

Run `python3 verify.py` using the Python 3 standard library. The program constructs graphs from every possible edge subset and computes each ordered vertex-coordinate pair directly. For the adjoint-rank enumerator it builds an edge-by-vertex matrix and runs independent finite-field Gaussian elimination, rather than trusting the support-rank formula. It checks \(\mathbf F_2\) and \(\mathbf F_3\) for every simple graph on at most four vertices and checks \(\mathbf F_4\) for every simple graph on at most three vertices. The latter field is implemented as \(\mathbf F_2[\alpha]/(\alpha^2+\alpha+1)\), so the characteristic-two extension-field case is nontrivial.

A second set of tests compares the two finite sums in the induced-component polynomial identity for every graph on at most five vertices, at the integer field sizes 2, 3 and 5. All 1,442 labeled trees on at most six vertices are used to test the two-state forest recurrence against direct subset evaluation at these same three field sizes.

The run emits `VERIFY_OK` only after all assertions succeed. The attached script needs no network, packages, or data files. These tests are finite; only the mathematical proof establishes the theorem for every graph and finite field.
