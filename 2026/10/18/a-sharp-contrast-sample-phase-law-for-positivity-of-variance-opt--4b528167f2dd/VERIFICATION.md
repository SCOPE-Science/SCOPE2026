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

# Reproduction and boundaries

Run `python3 verify.py` using Python 3. The standalone program assembles the stated four-row model from rational entries for every Bernoulli realization in five small finite configurations. It reconstructs two eigenvalues from each assembled matrix, compares them with the formulas, checks exact positive-definiteness probabilities and their conditioning on an invertible raw sketch, verifies the entrywise control weights by covariance ratios, and independently sums the binomial Frobenius risks. A separate finite-parameter check compares binomial tails with the predicted central-limit profile.

The program executed successfully with 18,761 checks. These finite checks can identify algebraic or transcription errors but are not an exhaustive verification of arbitrary sketch counts, parameters, or asymptotics. The all-parameter formulas and limiting probability statements follow instead from the projector decomposition, independent binomial counts, exact variance identities, and standard limit theorems in `RESULT.md`.

The most relevant accessible predecessor was read through its control-variate formula, optimal weights, positivity warning and algorithm discussion. Complete inspection of the 2026 motivating preprint was unavailable; the documented novelty assessment is therefore conditional on the accessible primary and secondary scientific evidence. No external scientific audit or certification has been performed.
