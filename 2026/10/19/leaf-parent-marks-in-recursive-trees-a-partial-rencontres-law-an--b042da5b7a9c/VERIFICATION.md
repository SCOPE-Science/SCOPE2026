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

# Reproduction and boundaries

Execute `python3 verification/verify_leaf_parents.py` with a standard Python 3 interpreter. The script enumerates all recursively labeled trees for orders 2 through 8 and checks leaf-parent cylinder probabilities (up to three prescribed edges), the fixed-point-indicator field for each parent, protection probabilities for each labeled vertex, and all between-parent covariances. Its observed final line is `TOTAL_EXACT_ASSERTIONS 6196`.

The analytic proof relies on deleting specified leaves and their forced edges, which leaves a tree on the other birth labels; the count `(n-r-1)!` is not inferred from the enumerations. Fixed-dimensional joint Poisson convergence uses factorial moments and does not apply to all growing parent labels at once. Historical root and total protected-node identities are known in the cited 2015 literature.

No independent audit or independently authenticated certificate has been performed.
