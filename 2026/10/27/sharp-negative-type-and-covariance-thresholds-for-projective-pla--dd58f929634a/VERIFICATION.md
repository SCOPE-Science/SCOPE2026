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

# Verification and limitations

- Systematically reconstructed the four eigenspaces of powered distance and Gaussian Gram matrices from the incidence identities and multiplicities.
- Checked the unique-root argument, negativity of the antisymmetric distance eigenvalue, and the endpoint rank counts.
- Executed python plane_covariance_check.py: 66 finite assertions passed for q=2,3,5.
- Checked the p=1 covariance factorizations and the rank N+1 at the nontrivial bandwidth endpoint.
- Finite computations are numerical diagnostics, not certification of the all-orders theorem.
