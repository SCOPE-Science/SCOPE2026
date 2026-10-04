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
The proof was checked from Cox-ring graded-piece counts and the Reid--Tai specialization. `verify_aut_dimension_bounds.py` directly enumerates weighted monomials and all nontrivial age-test elements for every \(2\le r\le30\), confirms the canonical and terminal triangles, verifies the closed automorphism-dimension formulas, and checks every maximizing equality case. It prints `VERIFY_OK`. The finite computation is a regression check only; the infinite theorem rests on the written inequalities.
