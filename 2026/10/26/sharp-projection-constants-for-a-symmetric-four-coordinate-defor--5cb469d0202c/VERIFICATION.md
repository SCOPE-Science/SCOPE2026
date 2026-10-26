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

# Verification evidence

The standalone `checker.py` uses Python 3 standard-library rational arithmetic and is invoked with `python checker.py`. At ten rational values from zero to one it checks the left-inverse relation, four exact optimal row sums, the two lower-bound inequalities for 25 additional symmetric left inverses per parameter, and the explicit Banach–Mazur witness at unit-ball vertices. It printed PASS for all ten parameters.

These tests do not establish the continuum theorem or historical originality. The all-parameter proof is the analytic symmetrization and affine dual-certificate argument in `RESULT.md`. No external independent validation has been performed.
