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
The theorem has a full analytic proof in `RESULT.md`. The bulk Laplace factors satisfy the two telegraph backward equations, absorbing boundary, reset self-consistency and boundedness. Geometric renewal has strictly positive denominators because \(p\in(0,1)\), \(s>0\), and the excursion/wall transforms lie strictly below or at one. Its difference therefore has the exact sign of \(s(\vartheta-a_\kappa E)/(s+r a_\kappa E)\). For negative initial orientation, \(\vartheta=\exp(-t)\), \(E=\exp(-c\sinh t)\), and strict decrease of \(t/\sinh t\) gives the one-switch law; no count of finite sample points is used in its derivation.

The accompanying `verify.py` was executed with Python 3 and passed 12,118 deterministic checks using only the standard library, including centered finite-difference residuals of both backward equations, numerical comparisons of exact rational identities, predicted sign regions and four explicit sign reversals. No Monte Carlo or finite enumeration is represented as an infinite proof. The published renewal formulas were independently reconstructed in the proof; earlier sources were compared for implications. This verification is not an independent external audit.

Limitations: no claims about time-domain stochastic dominance except the proved absence of such an ordering in the crossing regime; no claims beyond the one-dimensional model or for protocols with unequal wall-time distributions.
