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
## Reproducibility

Run `python3 verify.py` with the standard Python interpreter (no third-party dependencies). Expected final line: `DIAMOND_SQZERO_NILCLEAN_OK 6 families 7800 fibers`.

The checker constructs the complete incidence basis and tests \(e^2=e\) via literal convolution. It then counts the solutions of \((a-e)^2=0\) for each binary diagonal and each tuple of arm coefficients in the six named cases. The irrelevant long-interval coefficient can be held fixed because the only nonzero possible coefficient in the squared strict radical is the long interval. The checker uses binary-field arithmetic, prime-field arithmetic and separately implemented quartic-field arithmetic. It also maximizes observed fibers and compares the result with the sharp expression. The proof in `RESULT.md`, not the enumeration, establishes the result for arbitrarily large \(r\) and arbitrary prime powers.

## Verification boundaries

No numerical enumeration is claimed to cover infinitely many fields or all posets. The package contains one mathematical finding only. Literature priority was not independently certified.
