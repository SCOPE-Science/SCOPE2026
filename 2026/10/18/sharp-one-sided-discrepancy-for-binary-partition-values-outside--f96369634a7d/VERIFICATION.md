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

# Reproducible checks

Run `python3 verify.py` with Python 3.9 or later; no third-party packages are required. The executed source checked all 16 transition edges for both exact integer potential inequalities; separately generated 120,001 binary-partition coefficients modulo 16 to check 60,000 index obstructions and cumulative counts; checked 120,000 state bounds; verified the sharp global witness at 17; and checked nine explicit arbitrarily large digit-cutoff values. Each check completed successfully.

The finite checks are corroborative. The infinite upper bound and liminf rely on the algebraic transition table and telescoping potential inequalities displayed in RESULT.md, and the exceptional-set classification depends on cited published theorems about ternary quadratic-form representations and binary-partition congruences. The scientific review is same-model, and no independent mathematical audit or priority certificate has been produced.
