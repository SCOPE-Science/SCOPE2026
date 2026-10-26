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

# Verification record

Execute `python3 verify.py` using standard Python with no third-party libraries. It reconstructs all nonzero recurrence orbits of all \(127\) normalized polynomials of degrees one through seven, proving exact finite-cycle closure for those cases and checking the sharp density envelope and lower-bound uniqueness within that enumeration. It separately compares exact finite MAP Bayes risks against derived central-binomial formulae for the rules \(1+z\) and \(1+z^2\), and checks both strict/weak tail inequalities for eight explicit polynomials over eight observation lengths. All probabilities are rational and calculated using `fractions.Fraction`.

Observed output from the actual embedded program:

`VERIFY_OK: 127 closed recurrence kernels; 40 exact Bayesian errors; 64 exact error-sandwich checks; alpha(1+z)=1, alpha(1+z^2)=1/2, alpha(1+z+z^2)=2/3`

The proof of unrestricted degrees and observation horizons is mathematical: reversible finite-state recurrence, exact posterior-likelihood comparisons, binomial large deviations, and cycle double counting. The computational enumeration is supporting reproducibility, not an infinite proof.

The source-priority comparison was based on accessible primary sections and published abstracts; full texts of two plausible references were incomplete or inaccessible. No independent audit has been performed.
