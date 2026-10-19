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

# Reproducible mathematical verification

Run `python verify.py` with Python 3 and SymPy. It checks the two contrasting exact 2-by-2 Floquet products for directed and reciprocal examples, their determinants, traces, exact Perron roots, radical threshold inequalities, and symbolically verifies the corresponding parametric trace-commutator laws. It also checks permutation invariance for an additional triple of symmetric positive matrices.

The **general** arbitrary-dimensional permutation-invariance results follow from similarity of invertible products and transpose symmetry, as proved in `RESULT.md`; finite computation does not prove them. The SIS threshold and strict persistence/extinction cases follow from the same exact spectral certificates and comparison/monotone iteration. The numerical or symbolic checks do not establish publication priority. Critical equality, nonscalar recovery and arbitrary nonlinear model variants are not proved.
