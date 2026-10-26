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

Run `python3 check_sparse_words.py` from the directory containing this document and the checker. The self-contained script uses only the Python standard library and should print:

`SPARSE_FIXED_WEIGHT_PATH_EXACT_OK 36 moment_checks 27 asymptotic_checks 9`

For five small fixed-weight binary paths it enumerates all marked subsets, counts occurrences of fixed two- and three-point patterns, and compares first/second falling-factorial and pairwise cross moments against sums of the exact hypergeometric incidence probabilities. It checks nine large finite one-pattern expectation values at three sparsity exponents. All 36 assertions completed successfully during development.

The finite checks establish exact instances of the incidence formula and combinatorial moment expansion. They cannot establish the general mixed-moment limit, local-pattern saturation, effective Hanf locality, or the spectrum classification; the complete arguments for those statements are in RESULT.md. No machine-checked infinite proof or independent validation is claimed. The sample size and tested parameter values are finite.
