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

The mathematical proof derives the existence inequality from the Euclidean circumcircle through two opposite points in the Poincare disk, evaluates its angular measure, integrates the intrinsic hyperbolic-area weight, and establishes a unique disk-probability maximizer and sharp asymptotics. Computation supports but does not certify these infinite-parameter assertions.

Run `python verify.py` in this directory. The executable uses standard-library arithmetic and independent geometric tests, exact rational checks of the crucial radicand identity, numerical differentiation of the elementary primitive, direct radial quadrature, Monte Carlo area sampling, and tail and optimizer sanity checks. Its observed outcome was `ALL_CHECKS_PASSED`.

The test is not a computer-assisted exhaustive proof of the continuum assertions. Independent mathematical audit is not performed. Historical-priority checking is necessarily incomplete.
