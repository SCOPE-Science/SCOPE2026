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

# Reproducibility and proof boundaries

Execute `python3 verify.py` with Python 3 and no third-party modules. The program generates every parent tuple of a uniform recursive tree for orders \(2\le n\le9\), forms the joint histogram of root leaf-children and total leaves, and compares it with an independently generated Eulerian polynomial expansion. It also checks the full set of admissible falling-factorial transform identities, root/global covariance, and exact global leaf variance using integer and rational arithmetic.

A successful execution prints `VERIFY_OK` and `COV_OK`, with 46,233 total trees. This is a finite exact check, not a proof by enumeration for arbitrary size. The general theorem is proved separately by deletion/reconstruction of marked root leaf-children and the Eulerian growth recurrence. The asymptotic joint limit follows from the standard 1-dependent descent central limit theorem plus dominated factorial-transform convergence; it is not empirically established by the finite tests. The star-tree boundary is essential when all nonroot vertices are prescribed leaves, and the two-vertex covariance is zero rather than the nontrivial-order value.
