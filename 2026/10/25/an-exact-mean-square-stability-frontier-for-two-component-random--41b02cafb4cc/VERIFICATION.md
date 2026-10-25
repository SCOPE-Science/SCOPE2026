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

The analytic covariance recursion is stated in `RESULT.md`. The included `verify.py` reconstructs the three-dimensional covariance operator and verifies the determinant factorization symbolically. It also verifies the exact example polynomial, proves that the cubic factor has no positive root, and uses a Sturm sequence to certify one positive quartic root in \( (1,3/2)\). The reported decimal root is a numerical approximation only.

Scope limits: the checks concern two rank-one quadratic components, nonparallel directions, constant steps, and epoch-start states. They do not establish stability for other shuffling schemes, higher-dimensional or higher-rank components, nonquadratic losses, noise, or momentum. Independent audit and external validation have not been performed.
