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

The full integer coefficient calculation is reproducible with `python check_weighted_theta.py` (Python 3 standard library only). It computes every relevant five-by-five determinant for the four projected-volume polynomials, checks their complete symbolic monomial dictionaries, and confirms the exact cancellation identity and selected exact rational specializations. The source's unweighted tuple of determinant sums is recovered.

The checker does not constitute an independent scientific audit. Its finite determinant enumeration is exhaustive for the fixed seven-column matrix and therefore supplies complete coefficient evidence. The assertions over all positive weights follow from the polynomial identity and the exact analytic optimization in `RESULT.md`, not from a finite parameter grid. No universality outside the defined path-constant weight family, and no optimality over arbitrary projection directions, is claimed.
