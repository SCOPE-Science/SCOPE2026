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

The supplementary `checks.py` is a self-contained scientific consistency program. Running `python checks.py` requires Python 3 and SymPy and checks the symbolic coboundary, fixed-point equations, critical center-manifold quadratic jet and explicit stationary/traveling states. It also performs 400 deterministic pointwise numerical drift tests and one 200,000-step approach diagnostic. At preparation it returned `PASS 411 exact/symbolic, pointwise numerical and limiting-regime checks` and the observed quantity `n(z_n-z*)` was about `-1.9975183367` versus the theorem's `-2`.

The correctness claim rests on the analytical proof in `RESULT.md`: no finite simulation can certify a universal orbit dichotomy or asymptotic limit. In particular, the program does not establish existence/uniqueness of the center manifold, which follows from the classical smooth map center-manifold theorem; nor does it provide external or independent validation. The tested trajectory is an illustration, not an exhaustive census.
