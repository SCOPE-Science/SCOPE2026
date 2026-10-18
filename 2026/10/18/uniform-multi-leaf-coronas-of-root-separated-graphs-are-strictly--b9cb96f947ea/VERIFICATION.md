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

Run `python check.py` with Python 3 and SymPy. The script enumerates the exact independence polynomial of 19 small path/cycle-corona graphs and checks equality with a separate symbolic implementation of the substitution identity. It computes Routh–Hurwitz principal minors with rational arithmetic for 60 scalar polynomials covering degrees 1–10 and parameters 1/4, 1/3, 1/2, 3/4, 1, 4, checks the elementary integer inequality and additional boundary examples. These finite tests support but do not establish the infinite theorem, proved in RESULT.md by factorization and imaginary-axis exclusion. No external credential or network input is needed.
