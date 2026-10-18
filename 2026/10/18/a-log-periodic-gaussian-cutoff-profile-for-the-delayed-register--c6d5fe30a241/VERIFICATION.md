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

Run `python3 verify.py` with Python standard library. The checker independently evolves exact finite-state distributions for short registers using `fractions.Fraction`, compares the transition-law total variation against the two-binomial closed formula, checks time monotonicity and complete-block reduction, and evaluates elementary constraints of the phase function. Observed result: `PASS: 1366 finite exact-rational or deterministic assertions`.

The finite enumeration does not prove any assertion about the \(k\to\infty\) limit. The analytic proof uses independent multiplier histories, Lindeberg convergence of the log likelihood, bounded convergence for total variation, and Hellinger/chi-squared cutoff estimates. No independent scientific audit or external certification was carried out.
