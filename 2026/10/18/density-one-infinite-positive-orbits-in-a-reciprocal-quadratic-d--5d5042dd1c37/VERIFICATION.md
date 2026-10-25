---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and exact scope

`verify.py` uses the Python 3 standard library to check both the classical shifted-composite seeds (Mills's earlier result) and the corrected theorem's progression k=41+21t for 0≤t≤300. It evaluates the recurrence, Vieta conic, reciprocal divisibility, strict growth, and coprimality for bounded initial iterates. Its classical shifted-composite checks and k=10 parabolic check are retained as contextual regression tests, *not* as newly claimed mathematics.

The progression's universal correctness follows from the explicit proof for arbitrary t and n in `RESULT.md`; its infinitely many prime-shift parameters rely on Dirichlet's theorem. Finite execution of `verify.py` would not prove those quantifiers. The existing script reports `VERIFY_OK composite_steps=103350 prime_progression_steps=7224 seeds=3445+301` on success. Formal and expert-verification channels remain not performed.
