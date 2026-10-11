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

# Verification and reproducibility

Run `python verify.py` with Python 3.9 or later and no external packages. It checks the defining parameter relations and exact common-denominator polynomial identity over multiple independent rational parameter families by coefficient comparison; it checks the logarithmic crossover differential identity algebraically through rational-function coefficients. Successful execution prints `CHECK_OK`. These checks are supplementary and are not a replacement for the infinite-time/global proof in `RESULT.md`.

The analytic proof uses (i) compact simplex invariance; (ii) absence of positive equilibria and planar index exclusion of cycles; (iii) a one-sided attracting center manifold with stable transverse eigenvalue; (iv) a fast-variable variation-of-constants estimate uniform near the critical parameter; and (v) integration of an exact differential transform followed by an arbitrary-neighborhood limit. The endpoint and crossover limits are mathematical claims, not numerical extrapolations. Independent audit has not been performed.
