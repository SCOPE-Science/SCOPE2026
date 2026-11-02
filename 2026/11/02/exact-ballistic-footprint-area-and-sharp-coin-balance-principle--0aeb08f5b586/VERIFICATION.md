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

# Reproduction of the geometric area calculation

Execute `python3 VERIFY.py` with Python 3.9 or later; no nonstandard library is required. The program checks the closed inverse-sine area formula against midpoint integration of the intersecting ellipse profiles over 54 independent nondegenerate parameter pairs, checks their crossing locations and strict fixed-speed optima, samples the underlying dispersion relation on 2,160 independent wave-vector pairs, and tests the equal-ellipse boundary and near-full-speed asymptotic. It checks the globally sharp quadratic imbalance bound at each parameter pair. Its successful output is `PASS: 6837 independent geometric, dispersion, and optimization checks`.

These computational checks are finite and numerical; they are not an exhaustive search or an independent theorem certificate. The infinite-parameter proof is the explicit ellipse-arc integration, trigonometric reduction, sign of the exact derivative, global quadratic inequality, and endpoint expansion in RESULT.md. The ellipse support theorem used as a premise is published as arXiv:2408.09578v1, equations (14)–(19), and arXiv:2408.09578v2, appendix D. The work does not establish an initial-state-uniform probability density lower bound, nor does it extend to other quantum-walk architectures.
