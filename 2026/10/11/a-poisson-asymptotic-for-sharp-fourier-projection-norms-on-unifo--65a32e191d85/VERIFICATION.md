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

The included `verify.py` enumerates uniform set partitions for parameter pairs `(n,k)=(2,3),(2,4),(3,3),(4,2),(4,3)`. It checks partition counts, exact mean overlap, rational absolute row-sum norm, and (when at most 280 partitions) the full projection-matrix idempotence, trace and sharp norm using NumPy. Run `python3 verify.py`; expected terminal marker `VERIFY_OK`. It also prints the closed-form asymptotic constant for selected block sizes and its limit. Only analytic factorial-moment arguments establish the infinite-parameter convergence.

The exact tested endpoint norms are `9/5`, `24/7`, `243/70`, `80/21`, and `11178/1925` in the displayed parameter order. The source documents concern harmonic structure and extremal families; the scientific novelty risk is a prior equivalent Poisson-overlap asymptotic formulated probabilistically.
