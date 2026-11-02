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

# Reproduction and limits

Execute `python3 verify.py` from the directory containing this file. The script uses Python 3 standard-library `fractions`, `itertools` and `math` only. It independently constructs exact dense Schur complements and enumerates all subsets and randomized elimination orders in stated small dimensions. It checks the exact two-value trace law, survival probabilities, the difference identity and selected asymptotic diagnostics. The delivered checker should report `PASS 9345 checks (exact-rational equalities and finite asymptotic diagnostics)`.

The numerical tests are finite. The universal claim for arbitrary \(n\) and the asymptotic separation follow from the Sherman–Morrison reduction, elementary conditional probabilities, algebraic factorization and explicit limiting calculations given in RESULT.md. No numerical tolerance or external numerical solver is used to validate the exact finite-dimensional assertions.

The literature comparison is a self-review. Neither independent verification nor external certification has been performed.
