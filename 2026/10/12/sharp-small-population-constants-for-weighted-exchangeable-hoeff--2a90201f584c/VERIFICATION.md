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

# Reproducible verification
Run `python check.py` with Python 3 and SymPy. The file checks the exact hypergeometric moments for all nontrivial parameter pairs with population sizes 2 through 6, differentiated tilted variances and polynomial nonnegativity identities, Bernoulli-case comparisons, and rational bounds for the square-root/logarithmic comparison. Actual execution returned `PASS: polynomial identities, exact hypergeometric moments (N=2..6), and analytic bounds`. The full continuous-tilt result additionally uses the published reduction and Kearns--Saul theorem, and the explicit elementary power-series comparison in RESULT.md. Finite checks alone do not certify the continuum. No independent audit or separate formal proof was performed.
