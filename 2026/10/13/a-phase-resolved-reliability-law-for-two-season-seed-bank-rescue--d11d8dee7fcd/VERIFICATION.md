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

# Reproduction of checks

Run `python3 verify_seed_bank.py` from a directory containing the extracted source file. Python 3 and its standard library suffice; no downloaded datasets, network access, private file paths, or external dependencies are needed.

Expected final output:

`VERIFY_OK exact_profiles= 2592 strict_convexity_cases= 29808 optimal_windows= 2594 direct_outcome_expansions= 720 support_boundary_cases= 1600`

The checker enumerates finite exact-rational parameter families, cohort sizes and candidate allocations. It compares the analytical failure expression to the complete direct conditional-outcome enumeration for small cohorts, verifies strict discrete convexity and integer minimizers, tests the explicit finite-budget lower/upper bounds, and samples both support boundaries. The scientific proof, not the number of finite checks, justifies statements quantified over arbitrary \(N\ge1\), real model probabilities, and irrational allocation fractions. No independent scientific audit has been performed.
