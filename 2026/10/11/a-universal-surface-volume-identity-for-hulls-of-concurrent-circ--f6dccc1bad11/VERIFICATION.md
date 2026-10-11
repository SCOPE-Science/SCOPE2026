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

# Verification record

The analytic proof is in `RESULT.md`; this section records supplementary reproducible checks.

`python verify.py` performed direct three-dimensional convex hull reconstruction from sampled points on the original circular disks and independent numerical integration of each ruled patch's area Jacobian. It returned `VERIFY_OK`, with polyhedral approximation relative errors below `1.1e-4` for the sampled cases. It checked 2,030 seeded random positive-gap vectors against the strict Jensen maximum. The verifier runs from its own packaged directory, requiring Python 3, NumPy and SciPy. Its tests are finite and do not constitute an exhaustive proof of arbitrary dimensions or angles. The mathematical claim is established by the exact section and patch calculations in `RESULT.md`.

Independent audit has not been performed.
