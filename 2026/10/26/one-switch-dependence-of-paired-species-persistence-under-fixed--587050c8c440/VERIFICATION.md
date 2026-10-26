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

The analytical proof is in `RESULT.md`. Reproduce finite checks using `python verify.py` with Python 3 (standard library only). The script enumerates all uniform retained subsets through eight partner species and all feasible degree/overlap parameter families through fifty partner species. Its exact output must match `certificate.json`; it verifies the full sign classification within that finite scope and the five-partner example. There is no claim that finite enumeration proves the theorem for arbitrary sizes. The theorem's unrestricted proof is the cancellation identity (3), its one-turn sign pattern, and the sharp constructive boundary in `RESULT.md`.
