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

The six-step proof in `RESULT.md` explicitly reconstructs the unique stationary process, exact beta-perpetuity endpoint distribution, convergent coefficient series, Gaussian-mixture tail asymptotics, critical squared-exponential moment boundary and weak-reset comparison.

Reproduce the finite exact checks using `python3 CHECK.py`; expected standard output is included verbatim in `CHECK.out`. It tests five parameter tuples through moment order eight via two independently derived recursions with exact rational arithmetic, exact stationary Gaussian even moments, and finite positive endpoint-series/bound checks. It reports 130 successful assertions. This is not a numerical proof of any infinite-asymptotic theorem.

For independent reproduction of analytic constants, evaluate the positive convergent series for \(C\) and compare its partial sums with the rigorous bounds \(v_\star^{-\theta}\le C\le [v_\star(1-c^2)]^{-\theta}\). The displayed analytical derivations rather than external certification support the limiting claims. No independent audit has been performed.
