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

# Reproduction and scope

Run `python verify.py` with Python 3, NumPy, and SymPy. The deterministic checker, using a fixed pseudo-random seed, returned:

`PASS: 12310 deterministic exact and matrix identities`

It verifies inverse covariance formulas for memory sizes one through eight, exact noisy-residual average and coefficient identities, projected-column least-squares formulas, output decomposition, and Tikhonov operator norm bounds across 2,250 numerical instances, plus finite inverse-radius moment identities in exact symbolic form.

The checker is **not** an independent audit and cannot certify divergence of any expectation by finite sampling. The proof uses the full Gaussian density on every projected complement and integrability of the radial singularity; finite tests only corroborate algebra. Input displacements must have full column rank; oracle errors must be independent isotropic nondegenerate Gaussian at fixed input locations. The theorem asserts no adaptive iteration trajectory guarantee.
