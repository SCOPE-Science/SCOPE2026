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
The proof derives the universal result from normalized molecules, exact admissible Lipschitz potentials, finite-group symmetrization, and a zero-invariants representation argument. These are fully symbolic and do not depend on a numerical solver.

Run `python3 check_projection.py` with the standard Python library. The checker executes exact-rational molecule and dual-potential comparisons on ten explicit finite clustered metrics, totaling 263 cases. This is a finite sanity check, not an exhaustive check of all cluster counts or radii. The theorem assumes strictly positive within-cluster radii no larger than the normalized cross-cluster distance and treats only real scalars.
