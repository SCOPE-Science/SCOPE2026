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

Run `python verify.py` in the directory containing the accompanying source file. An executed run reported `VERIFY_OK 203`. The verifier uses exact rational arithmetic for the finite-dimensional volume polynomial and Mahler ratios, and floating-point log-sum-exp arithmetic for large-dimensional saddle diagnostics.

The exact reference values for unit Minkowski addition to the cube are \(14\), \(136/3\), \(418/3\), and \(6184/15\) in dimensions \(2\) through \(5\), respectively. The rate checks use dimensions \(100,300,1000,3000\). The root and limiting rate are evaluated by bisection and direct substitution.

Finite checks do not establish uniqueness of the asymptotic root or the fact that all global maximizing parameters converge. Those assertions follow from the analytic derivative sign argument, uniform Stirling/Laplace bounds, and the two exponential escape estimates in `RESULT.md`. Independent audit has not been performed.
