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

Run `python VERIFY.py` with installed NumPy and SymPy. The checker verifies symbolic coefficient-row norm identities, exact rational equivalence of pruning with an angular interval, agreement of direct thin-QR row weights and block SVD with the formulas, and seeded Gaussian frequencies against the derived two-sided probability bounds. The calculation samples 480,000 sketch matrices, which are supplementary diagnostics and do not establish a universal asymptotic. The actual theorem uses a Cauchy ratio law and a chi-square two-tail bound; these steps and all hypotheses are written out in `RESULT.md`. The directly computed test matrix is rank two and the second lookahead residual is algebraically zero. No independent audit has been conducted.
