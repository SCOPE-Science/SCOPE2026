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

# Verification of finite dimer-occupation covariance rank

The companion `verify.py` is standalone Python 3 code using only the standard library. Running `python3 verify.py` generated `PASS 294 exact assertions: jammed n=4..12, finite-time n=4..7, rational covariance ranks.`

The script calculates terminal states by enumerating maximal matchings independently of attempt permutations; for the first four nontrivial sizes it cross-checks against all edge-order permutations. At finite times it uses \(q=1/2\) for independent early-attempt indicators, conditions uniformly on the ordering of the early edges, accumulates the exact state probabilities with `fractions.Fraction`, forms the full covariance matrix, and computes its exact rank by rational elimination. This independently tests the finite-time and terminal support-based conclusions for the reported sizes.

The unrestricted theorem follows instead from the support characterization and maximal-matching induction written in `RESULT.md`. Finite enumerations cannot establish the all-size quantifiers or prove novelty. No independent external scientific audit or validation has been performed.
