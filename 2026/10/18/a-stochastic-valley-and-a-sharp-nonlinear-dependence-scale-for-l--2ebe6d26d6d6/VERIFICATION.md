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

Run `python3 verify.py` from the directory containing this package. It compares every conditional probability against independently enumerated Prüfer words for sizes four through eight, and separately checks exact rational occupancy distributions, strict stochastic upper-tail relations, expected values, zero covariance, and positive nonlinear dependence for sizes four through nineteen. Successful execution reports `2842 exact assertions`. The script uses only Python 3 standard libraries. Finite enumerations are not infinite proofs; the mathematical arguments for stochastic inequalities and asymptotic correlation ratio appear in RESULT.md. Independent audit has not been performed.
