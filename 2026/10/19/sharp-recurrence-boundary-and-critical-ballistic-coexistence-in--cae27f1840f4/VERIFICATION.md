---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The supplementary `checks.py` is a self-contained scientific consistency program. Running `python checks.py` requires Python 3 and SymPy and checks the symbolic coboundary, fixed-point equations, critical center-manifold quadratic jet and explicit stationary/traveling states. It also performs 400 deterministic pointwise numerical drift tests and one 200,000-step approach diagnostic. At preparation it returned `PASS 411 exact/symbolic, pointwise numerical and limiting-regime checks` and the observed quantity `n(z_n-z*)` was about `-1.9975183367` versus the theorem's `-2`.

The correctness claim rests on the analytical proof in `RESULT.md`: finite simulation cannot certify the universal orbit dichotomy or asymptotic limit. Existence of a local center manifold of the specified finite differentiability follows from the discrete-map center-manifold theorem, not from the program. No uniqueness or existence of a single infinitely differentiable center manifold is claimed. The trajectory is illustrative and does not provide independent validation.
