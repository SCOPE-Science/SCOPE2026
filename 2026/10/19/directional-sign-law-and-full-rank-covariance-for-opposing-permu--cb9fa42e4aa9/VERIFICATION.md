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

# Reproducibility and limits

The file `verify.py` is fully standalone and uses only the Python standard library. Run `python3 verify.py` after extraction. It exhaustively enumerates uniform permutations at every size from two through seven, checking all pairwise joint indicators against the closed joint-probability formula using exact rational arithmetic. It independently tests the sign pattern through size twelve, rational Gaussian-elimination determinants through size eight, and the positive-coefficient Hessenberg determinant recurrence through size twelve. The observed output was `PASS: 663 exact probability/sign/determinant assertions; n<=7 exhaustive words, n<=12 formulas`.

The all-size proof is in RESULT.md. Finite computation cannot establish universal sign inequalities or infinite-size nonsingularity. No independent audit was performed; references are not independent correctness or priority certification.
