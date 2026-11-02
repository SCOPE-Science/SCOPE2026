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

The enclosed `check.py` runs without third-party libraries using exact `fractions.Fraction` arithmetic and exhaustive finite compositions. Its successful observed output is in `CHECKS.txt`. Specifically, it checks finite Dirichlet–multinomial probability normalization; the joint and marginal singleton event formulas for five colour counts \(m\in\{2,3,4,5,6\}\) and three rational starting masses; the exact positive/negative example covariances; finite endpoint inequalities; and the polynomial positivity certificate for all integers \(4\le t\le50\). The infinite statements for all \(m\ge2\) and \(\alpha>0\) follow from the analytic proof in RESULT.md, not from the bounded enumerations.

The corrected unit-reinforcement normalization, two distinct named colours, sample length \(m+1\), and exceptional two-colour case are explicit in the assumptions. No probabilistic simulation or external computational certification was used. Historical-priority searches may miss obscure older works; independent review has not been performed.
