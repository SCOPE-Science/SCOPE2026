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

The companion `verify.py` was executed with Python 3. Its generated `verification_output.txt` records **129 passed exact-rational checks**: row-stochasticity and eigenvalues of the three-allele switching matrix, mutant-family first and second factorial moments, variance and autocorrelation constants, and finite-population size-biased Q-mean identities. For finite Q examples, the verifier uses an auxiliary mean-one, variance-two bounded offspring distribution solely to test the general size-bias algebra; it does **not** substitute this distribution for the Poisson clone-family model.

The infinite-time result is proved analytically in `RESULT.md`: the critical population Gamma limit, uniform contrast moment estimates, conditional finite-window central limit step, and geometric finite-past approximation are separate arguments, not extrapolations of numerical samples. Remaining non-computational limitations include literature-priority checks and any independent mathematical audit.
