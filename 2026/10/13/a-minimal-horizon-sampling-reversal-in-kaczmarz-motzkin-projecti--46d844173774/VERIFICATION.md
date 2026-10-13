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

# Reproducibility

From the directory containing this document, run `python3 verify.py`. Only Python's standard-library `fractions` and `itertools` are required.

The check uses exact fractions and reconstructs the two-step sample experiment directly from the matrix and selection rule. It tests all 22 nontrivial winner/competitor comparisons by proving each squared-residual margin strictly positive on the entire interval \([1/2,3/2]\): the quadratic is evaluated at both endpoints and any interior vertex. It also checks the full quadratic coefficients of all three expectations, the projection paths, exact determinant and row norms, and both strict difference inequalities.

These exact calculations establish the rational-algebra components of the proof for all real \(t\) in the interval; the separate general first-step monotonicity argument is the nested-uniform-subset coupling in `RESULT.md`. No infinite-dimensional conclusion, performance benchmark, or independent validation is claimed.
