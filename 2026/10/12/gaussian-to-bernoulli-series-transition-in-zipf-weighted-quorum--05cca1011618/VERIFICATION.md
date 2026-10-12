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

The self-contained program `verification/check.py` runs on Python 3 without nonstandard packages and finishes by printing `PASS: 159 independent finite exact and asymptotic checks`. A fresh invocation completed successfully from the candidate package directory.

It enumerates ternary observation bins at two nested thresholds for seven integer-weight profiles and four rational threshold pairs, verifying the first two moments and the complete two-level covariance identity using `fractions.Fraction` (140 exact assertions). It also checks centered Bernoulli second-through-fourth cumulants at four rational levels (12 exact assertions). Seven deterministic checks confirm movement toward the predicted power-sum normalizing constants for representative exponents across the three regimes.

These computations do not establish asymptotic normality, convergence of the infinite Bernoulli series, the local inverse relation, or the non-Gaussianity theorem. Those require the proofs in `RESULT.md`. No independent scientific audit or external formal certification has been performed.
