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

The attached `verify_tree_kernel.py` ran successfully in Python with SymPy. Its exact identities reproduce the two subcritical spectral endpoint formulas, the critical upper boundary, and the rational \(q=4\) example. It checks the critical rank-one positivity matrix for indices zero through eight and exhibits an exact negative supercritical principal minor with \(q=4\), \(r=3/4\), \(b=1/5\).

These finite and symbolic checks do not replace the proof for infinitely many vertices and parameters. The unlimited-index determinant limit, full adjacency spectrum, and critical necessity and sufficiency are proved in RESULT.md; the underlying general positive-matrix characterization is credited to Vergara, Theorem 1.2 (arXiv:1907.11476). The preexisting spherical representation framework and radial multiplier results are credited separately. No independent audit was performed.
