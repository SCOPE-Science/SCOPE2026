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

The theorem is an analytic consequence of the signed third-derivative Hermite error and a scalar comparison principle. The reproducer `verify.py` requires only Python's standard library and is called with `python3 verify.py`.

The checker runs 27 exact-rational endpoint-pair configurations, each checking masses, support, mean, variance and the third-moment gap. It evaluates positive-pressure Laplace ordering and intermediate mixtures, numerically compares five positive-time trajectories in an exact-moment benchmark by fourth-order Runge–Kutta, and checks the three final roots by bisection. It also certifies the example's fourth-order coefficient as exactly \(729/160000\).

Expected success starts with `VERIFY_OK`. Reported sample terminal removed fractions are approximately \(0.531448376117\) and \(0.774523533215\). These finite tests are reproducible arithmetic illustrations, **not** a proof of inequalities for uncountably many distributions or all positive times. The universal proof is in `RESULT.md`, and the source fluid-limit theorem is an external pre-existing analytic result. No external independent audit has been performed.
