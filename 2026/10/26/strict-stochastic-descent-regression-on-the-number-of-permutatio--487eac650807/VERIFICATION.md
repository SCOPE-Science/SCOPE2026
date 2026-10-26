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

Execute `python verify_records_descents.py` in the directory containing the supplied standalone file. Python standard library only. The script independently enumerates all permutations through size eight, compares the exact joint distribution with the insertion recurrence, and checks strict adjacent stochastic orders, rational upper-tail probabilities, mean-descents and the exact covariance identity for all sizes through 48. It reports 36,848 exact rational tail tests.

The proof beyond the finite checked cases is fully mathematical: exact uniform gap insertion; induction coupling conditional independent Bernoulli vectors with Newton inequalities; coordinatewise antitone monotone recursion; and the covariance recurrence. No independent audit, Lean certification, or extrapolation from finite experiments is asserted.
