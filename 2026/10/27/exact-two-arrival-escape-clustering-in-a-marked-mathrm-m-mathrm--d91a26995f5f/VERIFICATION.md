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

# Verification and reproducibility

The research claim is proved in `RESULT.md`. Run `python3 verification.py` in the same directory as the embedded files; no nonstandard Python modules are required. The recorded standard output is `verification_output.txt`.

The script checks 840 exact rational conditions over 56 interior rational parameter pairs. These include consistency of the two independent marginal calculations, equality of two formulas for the joint probability, the exact covariance and correlation, nonnegative cells of the joint law, and bounded nonnegative finite partial sums of the double geometric series. A 51-term finite sum is bracketed between its value and a closed rigorous geometric remainder bound. The program also simulates three finite independent arrival/service/customer-mark processes (12,000 paths per parameter setting) and compares empirical marginal and joint escape probabilities with the exact formulas; those simulation checks use a loose deterministic tolerance suitable only for corroboration.

The exact symbolic identities and all-parameter stochastic conclusions are established algebraically in the proof and are not inferred from a finite parameter grid or random samples. In particular the verification program does not certify any positive exposure threshold or a general-service queue, and it provides no independent human validation.
