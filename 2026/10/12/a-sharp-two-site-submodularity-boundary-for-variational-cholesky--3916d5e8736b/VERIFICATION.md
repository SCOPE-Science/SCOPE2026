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

# Reproduction and limits

Run `python3 verify.py` using Python's standard library. The actual standalone program reconstructed the kernel, single-pivot Nyström matrices and their inverses in exact rational arithmetic for 2170 parameter/data configurations. It checks the exact analytic defect up to floating-point transcendental logarithm evaluation, tests monotonicity, the strict witness and two limiting families. The observed terminal line was `VERIFY_OK exact_rational_matrix_reconstructions= 2170 asymptotic_cases=10`.

The infinite parameter ranges, precise threshold, strict positivity, and ordered weak-submodularity infimum are proved algebraically in `RESULT.md`, not inferred from this finite test. The script does not certify global literature uniqueness, general GP data distributions, higher pivot counts, or any unperformed independent audit.
