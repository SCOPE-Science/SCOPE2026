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

Run `python3 verify.py`. The program uses only the Python standard library, creates exact polynomial rational functions by backward induction on adoption states, and verifies all six five-node reflection-class expressions, all eight strict exclusion differences, the crossover difference, and the three-/four-site minimality formulas. It independently recomputes the expected completion time with exact rational arithmetic for every two-seed pair of paths with three to five vertices at eight rational values of the imitation-to-innovation ratio.

Observed output: `PASS: 37 symbolic identities/positivity statements and 152 independent exact-rational cross-checks.` The algebraic sign argument in the proof establishes the result over the entire positive continuum; the test sample alone would not. Source comparison in the scientific review remains historically provisional; no independent validation was performed.
