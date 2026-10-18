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

# Reproducibility and limitations

Run `python3 verify.py` using Python 3.10 or later (standard library only). The program independently compares endpoint-parameter enumeration, direct relational admissibility, and evaluation of (T1)--(T8). Expected final line: `VERIFY_OK`. Exhaustive relational checks reach \(n=4\) dual points; direct quadruple-axiom checks reach four chain elements; parameter counts and exact reduct-fiber bounds reach \(n=5\) dual points. These tests are finite corroboration only. The general proof appears in `RESULT.md`; no computer enumeration is used to infer statements for all \(n\).

The interpretation of tense operations, the dual representation theorem, and the exact domains and assumptions are stated in `RESULT.md`. The available evidence does not constitute an independent mathematical or priority audit.
