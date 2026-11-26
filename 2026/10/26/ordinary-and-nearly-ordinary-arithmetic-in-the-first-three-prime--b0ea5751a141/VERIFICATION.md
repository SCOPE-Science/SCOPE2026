---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

# Exact characteristic-five verification

Run `python3 verify.py` under Python 3.10+ with SymPy. The script computes in the prime field of order five. It checks the listed singular witnesses for the four excluded parameters, verifies the three unit chart ideals for the remaining parameter, and computes the Hasse–Witt determinant of the smooth degree-eight member. It ends with `p=5 k=4 smooth genus=21 det=4 ordinary`. The arithmetic interpretation of the determinant is in `RESULT.md`. No computations for other primes are part of this certificate.
