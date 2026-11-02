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

The accompanying `check.py` was run against the exact source included with this finding. It verifies the third-tensor contraction, second-moment fold \(q\leftrightarrow2/3-q\), third-moment separation polynomial, strict witness feasibility, and exact witness moments. Independent surface-coordinate quadrature validates the moment predictions in several configurations. The proof of injectivity for the full continuous parameter domain is algebraic; numerical sampling is diagnostic, not a completeness certificate.

Checks require Python with `sympy` and `numpy`. Scientific limitations: the observed metric is ambient spherical great-circle distance; data are exact population moments; the region class consists only of uniform spherical latitude zones. No independent mathematical audit has been performed.
