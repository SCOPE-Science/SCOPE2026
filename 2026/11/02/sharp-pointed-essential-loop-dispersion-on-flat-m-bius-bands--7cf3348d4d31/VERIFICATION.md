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

# Reproducibility and proof checks

The full proof in `RESULT.md` uses universal-cover parity and elementary exact integration. The stand-alone `checker.py` (Python standard library only) independently enumerates a bounded selection of covering-group elements at 504 exact-rational coordinates; these tests agree with the analytically proved global deck minimum. Eleven rational shape parameters confirm the algebraic uniform moments. The sharp-deficit factorization is verified by exact rational polynomial multiplication, and the critical value and atom probability are exact fractions. Eight direct Simpson quadratures numerically check moment expressions from the defining probability law.

Execute `python checker.py` from the extracted package directory. It reports `ALL_CHECKS_PASSED` when these checks complete. The finite orbit enumeration and numerical quadrature are not asserted to exhaust all real parameters or prove the universal result; the proof in `RESULT.md` does so separately. The sole literature lead is publicly dated December 11, 2019, not the date of a later revision. No independent mathematical audit or historical priority certification has been performed.
