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

# Verification

Run `python3 check.py` in the same directory as the extracted `RESULT.md`. The program uses Python's standard library, exact integer and rational arithmetic, and produces a nonzero exit status if an asserted identity fails.

A direct independent enumeration covers every permutation of size 3 through 8 and every admissible three-window pattern. Further finite checks cover all six forced-cycle coefficient formulas and the claimed rank and sign properties through size 120. Successful execution reported `PASS 77483 exact assertions; direct all-permutation enumeration through n=8`.

The all-size proof is the directed-path contraction argument plus the displayed forced fixed-point, transposition and three-cycle counts in `RESULT.md`. Neither finite enumeration nor a successful script constitutes an independent or exhaustive historical originality check. No independent audit has been conducted.
