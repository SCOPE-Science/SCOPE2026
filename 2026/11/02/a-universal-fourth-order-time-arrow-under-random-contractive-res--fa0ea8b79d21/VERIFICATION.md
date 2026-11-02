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

The standalone `verify_time_arrow.py` uses independent matrix exponentiation for the exact polynomial semigroup on degrees zero through three. It passed 520 deterministic (seeded) tests involving arbitrary signed four-atom contraction laws and reflection, positive contraction and zero contraction one-atom laws. It independently computes mixed fourth moments by the semigroup and checks the factorized formula, strict positive sign, and unique-peak comparisons.

The analytic proof, not the finite tests, establishes the uncountably many contraction laws, all positive times, and exact positivity. The correlated observation-noise extension is proved by polynomial expansion and stationarity; it is not claimed to be numerically tested. Publication priority remains a separate issue and is not independently audited.
