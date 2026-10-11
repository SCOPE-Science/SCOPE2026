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

## Reproducible mathematical checks
Run `python3 CHECK.py` using only the Python standard library. It enumerates each nonzero ternary vector and every ordered pair up to dimension five; checks the exact support-functional criterion against the two direct half-step norm tests; uses exact rational probabilities at \(\rho=1/4\) to test the weighted failure estimate; checks the optimized Chernoff expression and several nearby parameter values; and checks the formula in a finite range of dimensions.

Observed output:

`VERIFY_OK exact_pairs=65708 exact_weighted_dimensions=5 rho=1/4 unique_chernoff_bias_checked=1 asymptotic_base=1.093836321356`

The only proof of the universal assertion is the analytic derivation in `RESULT.md`, including the product probability calculation, the graph mass-transfer lemma, and the derivative factorization. The finite enumeration is not an exhaustive search of all dimensions or all real vectors. No computer-assisted infinite certification or independent external validation is claimed.
