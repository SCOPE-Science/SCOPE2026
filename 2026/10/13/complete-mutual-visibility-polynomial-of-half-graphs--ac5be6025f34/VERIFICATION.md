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

# Verification

The program `verify.py` runs under stock Python 3 and requires no external dependency. It builds each half graph from its edge definition and separately tests every selected set using unrestricted-versus-selected-interior-forbidden breadth-first search distances. A second implementation checks the boundary conditions, and a third constructs the coefficient formula.

The captured `verification_output.txt` documents 87,360 exhaustive subsets for orders 3 through 8 (2n vertices in each graph), with no discrepancies. It also reports formula consistency through n=50, including the polynomial's coefficient sum and maximum-degree coefficient. The finite computations are corroboration, not a proof for unbounded n. The proof of the general identity is the explicit geodesic-and-counting argument in `RESULT.md`. Neither an independent external audit nor a formal proof certificate has been performed.
