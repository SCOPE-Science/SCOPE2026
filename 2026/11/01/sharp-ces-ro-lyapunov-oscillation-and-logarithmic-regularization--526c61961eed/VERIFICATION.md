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

# Reproducibility and limits

Run `python3 verify.py` with Python 3.9 or later. The checker uses only built-in libraries (`math`, `fractions`) and tests finite signed block identities, coordinate tangent expansion counts, exact phase endpoints and extrema, and the convergence of finite arithmetic means to the predicted alternating block-end and phase values in samples. It reports `ALL_CHECKS_PASSED` on the supplied tested parameters. It does not perform a formal or independent proof check; the infinite statements rely on the analytic argument in `RESULT.md`.

The source derivative block identity is Nakano--Soma--Yamamoto, arXiv:2206.09508v1, equations (2.4), (3.1), (3.2). The checker verifies this algebraic block surrogate, not the existence of the source's wandering rectangles; that existence is a separately cited established theorem.
