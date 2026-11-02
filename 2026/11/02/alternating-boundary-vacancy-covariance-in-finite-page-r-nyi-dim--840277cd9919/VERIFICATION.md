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

Run `python3 verify.py` with Python 3. The program uses the standard library only and performs exact rational checks of the marginal recurrence, joint recurrence, closed form and sign for lengths 3 through 120, independently enumerates edge-priority permutations at sizes 1 through 8, and checks normalized exact covariance values at 30, 50, 70, 90 and 120. In this reviewed computation it printed `PASS: 390 exact assertion groups`.

The mathematical derivation in RESULT.md handles all lengths. Exhaustive checks cover only the specified finite sizes; the sampled asymptotic ratios do not prove convergence. No external/independent proof verification or literature-priority certification was undertaken.
