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

# Reproducibility

Run `python3 verify.py` with Python 3; the program uses only the standard library. It performs exhaustive direct neighbour-colour checks, a complete canonical K_{3,4} 3-colour impossibility search (13,122 cases), all 2^20 one-colour K_{4,5} possibilities (maximum six edges), and all explicit construction families in the recorded finite ranges. The expected console output is supplied as `verify_output.txt`.

These finite enumerations fully prove the specific finite impossibility claims by complete finite search, independently of the analytic arguments. They are **not** purported to prove the infinite-family theorem, whose quantified inequalities and constructions are in RESULT.md. All supplied matrices have been checked directly against the definition. No external or independent audit is asserted.
