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

The exact exponent-matrix characterization was replayed on finite exponent boxes for several fixed prime supports by `verify.py`. For each tested integer, the script compares direct divisibility by the divisor count with the criterion that every shifted exponent is supported on the same prime set and that the resulting valuation-column sums fit inside the original exponents.

The asymptotic proof is analytic and appears in `RESULT.md`. The numerical ratios printed by the checker are sanity checks only and are not treated as evidence for the infinite limit.
