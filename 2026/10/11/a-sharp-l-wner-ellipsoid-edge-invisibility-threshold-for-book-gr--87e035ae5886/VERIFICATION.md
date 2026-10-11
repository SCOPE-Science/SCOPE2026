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

# Verification details

The attached `verify_book_ellipsoid.py` is a complete standard-library Python 3 program. Run it directly with `python3 verify_book_ellipsoid.py`. It computes, using exact rational arithmetic for each \(m=2,3,\ldots,12\): the normalized weighted graph Laplacian, its inverse restricted to the zero-sum space, explicit orthogonal projectors onto the hub-antisymmetric, hub-versus-leaves and leaf-difference spaces, all three covariance eigenvalue identities, all three inverse-eigenvalue identities, and both types of edge-root leverage. It verifies all corresponding ellipsoid inequalities, the exact number of contacting edge pairs and the strict noncontact inequality for \(m\ge4\). All eleven parameter instances passed; successful execution ends with `EXACT_CHECKS_PASS`.

The mathematical proof is complete for all integers \(m\ge2\) and relies on the graph covariance eigen-decomposition, the exact leverage identities and the sign-averaged determinant–trace minimality certificate. The finite tests do not constitute an exhaustive proof for infinitely many graph orders, a general-purpose optimization oracle, or independent mathematical review. The source literature's earlier general D-optimality conditions are explicitly acknowledged; the result concerns their evaluated book-graph specialization only.
