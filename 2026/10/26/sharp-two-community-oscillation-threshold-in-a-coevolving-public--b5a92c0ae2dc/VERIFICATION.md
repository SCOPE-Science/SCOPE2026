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

# Verification notes

An independent external audit has not been performed. Run the bundled `verify.py` using a Python 3 standard-library interpreter. It checks optimized original payoffs using `fractions.Fraction`, constructs symmetric row-stochastic matrices for multiple group sizes and parameter triples, verifies exact two-cycle identities and failure of the specified branch beyond the analytic cutoff, and checks a perturbed orbit against the predicted contraction for sixteen steps.

During the current check, `python3 verify.py` returned:

`PASS: 116 exact cycle/critical/perturbation cases; explicit original-payoff comparisons; nondegenerate four-agent witness`

The proof in `RESULT.md` supplies the unrestricted-in-\(s\) algebraic argument. Finite exact testing does not by itself certify the infinite family, or historical originality. Equality at the threshold is decided analytically by the motivating model's specified tie-to-defection rule. No interval certification of all model variants or external evaluation is claimed.
