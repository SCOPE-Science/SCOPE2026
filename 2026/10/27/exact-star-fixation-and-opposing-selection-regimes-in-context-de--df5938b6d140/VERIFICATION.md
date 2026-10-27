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

# Verification notes

The finite-state equations are derived in `RESULT.md` from the *actual* vertex activation and copying probabilities. The center-0 harmonic equation and center-1 harmonic equation are each verified algebraically, and the difference recursion yields the normalization from both absorbing boundaries. This analytic argument applies for every integer number of leaves at least two and all acceptance probabilities in \((0,1]\).

Run `python verify.py` using the standard library. The included code enumerates every labeled configuration for stars with two through eight leaves for five rational probability pairs. The exact fraction-valued one-step harmonic drift, unanimous boundaries, single-seed hub/leaf formulas, and unbiased fixation are all checked. The observed output is: `PASS: 35 rational parameter-star cases, 5080 labeled configurations and 35840 exact transition-drift terms.`

The general all-star proof and the asymptotic limits are mathematical deductions rather than claims of exhaustion by finite enumeration. The checker does not test every real parameter or arbitrarily large size. Comparison with uninspected wider literature may require further independent publication-priority assessment.
