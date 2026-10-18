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

# Reproducibility checks

Run `python3 CHECK.py` using Python 3 with standard library only. The run performs 18 finite period-24 independent mass-inverse edge comparisons across nine mesh ratios and verifies the limiting closed forms and a centered numerical derivative. All programmed assertions passed on the supplied source. The finite comparisons differ from the infinite formulas by less than `2e-6`; this is finite-volume convergence evidence, not a proof or exhaustive certificate.

The analytical proof depends on the uniformly invertible bi-infinite signed mass matrix, its explicit decaying two-step inverse for a pair of adjacent sources, the exact cell integral of an affine sign-changing function, and knotwise attainment of the global Lipschitz slope. The included checker does not certify all infinite recurrences symbolically. No independent audit has been performed.
