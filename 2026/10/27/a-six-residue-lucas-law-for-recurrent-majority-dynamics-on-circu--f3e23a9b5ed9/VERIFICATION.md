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

# Reproducible verification

Run `python verify_prism_majority.py` with Python 3.10+ and SymPy. This constructs the local two-time majority transition predicate independently of precomputed tables, enumerates its 256 directed pair states and exactly 400 transitions, finds six cycle-bearing strongly connected components and computes their characteristic polynomials symbolically. A separate implementation enumerates all binary configurations for every prism circumference 3 through 10, checking the fixed-state and twice-periodic formulas. See `verification-output.txt` for the actual execution output.

The finite symbolic transfer calculation certifies the exact general recurrence, because it represents every cyclic pair of valid times at **every** circumference, not merely the enumerated small cases. The explicit matrix rule and its finite factorization are presented in `RESULT.md`. The full-state searches are cross-checks; neither their finiteness nor any run log alone proves an infinite claim. No independent external audit was performed.
