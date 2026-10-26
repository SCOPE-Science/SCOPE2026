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

# Verification

`verify.py` uses standard-library `itertools.permutations`, `fractions.Fraction` and `collections.Counter`. Executing `python verify.py` exhausts all cyclic-order representatives with the zero offset first for periods two through eight; compares two independently implemented min-plus erosions, checks the all-period lower formula in these instances, and checks every stated exact maximum and its multiplicity. The observed terminal line was `VERIFY_OK`. This verifies the finite census, not the infinite-time/small-hole theorem.

The infinite-time escape-rate identity is established separately by the positive-renewal Perron argument in `RESULT.md`; the fixed-period small-hole expansion follows analytically from the simple Perron eigenvalue and controlled matrix tails. No independent audit or external validation is claimed.
