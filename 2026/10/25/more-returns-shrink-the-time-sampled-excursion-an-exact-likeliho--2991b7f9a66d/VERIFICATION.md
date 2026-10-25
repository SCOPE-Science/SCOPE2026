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

# Reproducibility

Run `python3 verify.py` using a standard Python 3 interpreter. The script directly enumerates balanced walks for sizes through eighteen steps; it does not use a formula to generate the excursion decomposition. It additionally performs exact-fraction comparisons of the probability masses, strict mean-order inequalities and likelihood-ratio cross products for all supported sizes up to fifty semilength units. A successful run reports 43,394 assertions.

The analytic proof of the likelihood-ratio law and the linear-density limit is in `RESULT.md`. This finite verifier cannot establish either infinite quantification or the uniform geometric tail argument. No independent external audit has been performed.
