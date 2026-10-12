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

# Reproducibility and scope

Run `python verify_model.py` with standard Python 3; only `fractions.Fraction` and standard-library functions are used. The actual replay output was:

`VERIFY_OK exact_coefficients=1 threshold_interval=1 direct_backward_equations=1 algebraic_general_cutoff_test=1 checks= 3917`

The code performs exact rational comparisons of the target-five coefficient identities; isolates the positive root of \(253\gamma^2-226\gamma-44\) between the rational endpoints \(1.057\) and \(1.058\); solves the independent Markov backward linear equations and compares with the product expression; and exercises numerous integer capacities and recovery targets. These checks are finite tests. The unrestricted conclusions rest on the symbolic first-passage recurrence, the logarithmic derivative sign and the exact quadratic factorization recorded in RESULT.md. Neither a formal proof assistant nor an independent external audit has been used.
