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
# Verification details

The standalone script `verify.py` uses exact `fractions.Fraction` arithmetic; invoke `python3 verify.py` in the directory containing `verify.py`. Its completed exact run printed:

```
VERIFY_OK rational_weight_profiles=154population_size_profiles=1120integer_occupancy_vectors=42000independent_exact_lottery_tests=560periodicity_tests=770two_agent_modular_tests=1827
```

The independent finite checks compare the raw chore-removal inequalities with the Adams priority-vector construction; for at most three agents an additional solver enumerates exact rational convex mixtures of all admissible occupancy vectors. They also verify the claimed translation of admissible sets by the rational entitlement numerator vector and the two-agent residue formula. No random seed, floating-point approximation, or external library is required.

This is finite corroboration only. Infinite quantifiers, all positive real weights, and exact score-tie boundaries are justified by the mathematical proof in `RESULT.md`, not by enumeration. External independent validation has not been performed.
