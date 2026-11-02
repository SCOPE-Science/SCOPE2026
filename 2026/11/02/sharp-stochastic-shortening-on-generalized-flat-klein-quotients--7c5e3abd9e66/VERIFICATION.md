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

Run `python3 check.py` with Python 3 and no third-party packages. The source is embedded beside this document. The checks operate on directly evaluated shortest-deck paths and independently derived integral formulas rather than assuming the desired coupling.

Observed output:

```text
EXACT_CUTOFF_RATIONAL_MOMENTS_PASSED
INDEPENDENT_QUADRATURE_AND_BRANCH_MATCH_PASSED
UNIT_SQUARE_EXACT_SECOND_MOMENT_PASSED
DIRECT_DECK_MINIMUM_AND_STOCHASTIC_COUPLING_PASSED
SEVEN_HALVES_CUTOFF_ASYMPTOTIC_PASSED
ALL_CHECKS_PASSED
```

The checker confirms exact rational cases and numerical agreement for representative periods. The mathematical proof in `RESULT.md` establishes the arbitrary-dimensional quantifiers and the analytic non-smoothness; finite simulations, quadrature and asymptotic numeric ratios are not proofs of those universal claims. Independent audit is not performed.
