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

# Reproduction
Run `python VERIFY.py` with Python 3; only the Python standard library is required. The program enumerates the sampled curvature, independently sampled spectral estimator, and gradient minibatch using rational arithmetic. It checks conditional one-step squared-multiplier averages against the analytic gain distribution and verifies cached versus refreshed exact \(k\)-step second moments for seven values of \(\rho\), five of \(\alpha\), both coordinates, and \(k=0,1,\dots,10\). It also checks the sharp cached boundary for the tested parameters, the default refreshed factor polynomial, and the rational witness \(\rho=1/4\).

Observed result: `PASS: exact arithmetic checks 1575 plus rational witness, default phase polynomial`.

The complete infinite-horizon claims are proved algebraically in `RESULT.md`; no finite computation is presented as an infinite proof. The code does not execute floating-point Nyström, which is expressly outside this idealized theorem. Independent audit has not been performed.
