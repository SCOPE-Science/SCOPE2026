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

# Reproducibility and limits

The algebraic steps are explicit in `RESULT.md`; run `python checker.py` with the dependency in `requirements.txt` to verify the exact quotient identity, cubic discriminant, special factorizations, and finite real-root counts. The checker tests finite degrees and sample parameters only; it does not certify the infinite family, novelty, or global source coverage. The all-degree argument uses exact sign algebra, Descartes' rule, cubic root continuity and discriminant crossings. The square-root fold follows from a nonzero simple discriminant crossing and a nondegenerate local minimum. Independent verification remains unperformed.
