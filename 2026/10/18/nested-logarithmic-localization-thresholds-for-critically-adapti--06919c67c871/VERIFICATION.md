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

# Reproducibility and mathematical limits

Run `python checker.py` in an environment satisfying `requirements.txt` (SymPy 1.14.0). The checker verifies, by symbolic differentiation, the potential-curvature identities for the comparison tails \(x^{-1}t^{-\beta}\) and \(x^{-1}t^{-1}(\log t)^{-\gamma}\), as well as the leading third-level comparison terms, with additional finite substitutions. The reported execution passed these checks.

Analytical checks not reducible to finite computational enumeration are: (i) recurrence of Brownian motion and finite almost-sure reset time under an eventually positive bounded hazard, (ii) Green-occupation/regenerative normalization, (iii) monotonicity of the half-line Feynman–Kac hitting expectation in the killing intensity, (iv) eventual ordering of curvature comparators under the quantitative remainder hypotheses, and (v) convergence or divergence of the explicit integral tests including equality. These are proved or justified in `RESULT.md` and no numerical run replaces them.

No result is claimed for arbitrary oscillatory smaller-order hazards or for higher dimensions. The logarithmic density and survival-tail results are exponent limits, not exact prefactor asymptotics.
