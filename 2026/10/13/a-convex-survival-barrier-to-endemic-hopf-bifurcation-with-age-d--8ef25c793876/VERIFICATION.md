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

The nonlinear equation, equilibrium and characteristic determinant were independently re-derived from the stated kernels. The essential new lemma is proved by writing each exponential tilt of the convex survival function as a nonnegative mixture of truncated linear functions, then evaluating their cosine transforms. This proves the nonnegative real part for **all frequencies**, not by numerical sampling.

The companion program `verify.py` builds the hyperexponential finite-dimensional closure with rational rates, weights and parameters, checks the sign of eigenvalue real parts in each sampled case, and tests the uniform and gamma special-case inequalities. Execute `python verify.py` with Python 3, NumPy installed, in the folder containing the file. Expected output begins with `VERIFY_OK`.

These computations do not certify infinitely many parameters or nonlinear global convergence. The claimed local exponential stability is restricted to exponentially integrable residence-time survival kernels and sufficiently small compatible bounded incidence histories. All scientific review here is same-model only; independent audit has not been performed.
