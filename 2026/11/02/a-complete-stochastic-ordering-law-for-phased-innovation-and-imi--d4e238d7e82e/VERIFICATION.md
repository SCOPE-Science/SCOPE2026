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

Run `python CHECK.py` in the folder containing the extracted files. NumPy, SciPy and SymPy are required. The checker returns exact commutator identity and two-person example assertions, plus independent finite random multi-phase semigroup comparisons. The observed successful counts were 1,503 exact commutator assertions, 7 exact example assertions and 43,774 finite numerical assertions (45,284 total).

The numerical tests use double precision with explicitly stated error margins; the symbolic identities and two-person example use exact arithmetic. These are finite diagnostics. The all-population, all-duration, and all-finite-phase claims are proved in RESULT.md using an exact semigroup identity and stochastic monotonicity. Historical priority is provisional, not independently certified.
