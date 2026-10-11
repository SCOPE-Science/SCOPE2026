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
Run `python3 verify.py` with Python 3's standard library. It constructs the complete graph with eight diagonal and six axial facets for eleven rational parameters, uses exact fractions for geometric masses and ridge conductances, and checks seven eigenvectors spanning the antipodally even subspace for each parameter. Successful output:

`VERIFY_OK exact even facet-network eigenvectors, 11 rational parameters`

Separate independent rational-matrix diagonalizations reproduced the eigenvalue multiplicities at parameters \(6/5\), \(3/2\), \(7/4\), \(2\), \(5/2\), and \(14/5\). Direct planar convex-hull calculations agreed with the exact face-area formulas at parameters \(6/5\), \(3/2\), \(2\), \(5/2\), \(14/5\). These tests are finite; the symbolic proof of the facet geometry, invariant subspaces, eigenvalue ordering, and unique optimizer covers every real \(1<c<3\).

No independent audit or certification is asserted.
