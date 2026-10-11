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

# Reproducibility and mathematical limits

The accompanying self-contained `verify.py` (Python 3 standard library) was executed against the actual candidate's formulas. It tests all fourteen odd dimensions from 5 through 31, including all 504 defining facet contacts, inversion of the shape operator, equality of the positive John-weight inverse-shape identity, cyclic determinant product, and low-dimension asymptotic ratios. Invoke `python3 verify.py` in the directory containing that file.

The infinite-dimensional theorem rests instead on the five analytic steps detailed in `RESULT.md`: strict scalar monotonicity and a root-of-unity filter; two exact inverse-matrix entries; positive first- and second-contact moments; Fourier determinant; and the factored small-root gap with a derivative limit. Floating-point tests cannot prove these steps for all odd dimensions. The exact leading constant is proved algebraically and numerically sampled only. The source comparisons do not constitute independent novelty certification or independent mathematical validation.
