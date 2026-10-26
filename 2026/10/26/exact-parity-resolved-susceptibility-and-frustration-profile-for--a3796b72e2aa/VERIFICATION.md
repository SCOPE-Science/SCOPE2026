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

The supplied Python verifier explicitly builds all transitions of the signed-copying process on the 4-, 8- and 12-vertex ladders, solves the invariant finite-state linear system, and separately computes the Fourier resolvent for six ladder sizes. Observed absolute errors are below 5e-8. This is finite evidence only. The paper's all-size proof uses the covariance recurrence, Fourier Green kernel and finite voter duality. The script requires numpy and scipy; it does not provide machine formalization or independent scientific validation.
