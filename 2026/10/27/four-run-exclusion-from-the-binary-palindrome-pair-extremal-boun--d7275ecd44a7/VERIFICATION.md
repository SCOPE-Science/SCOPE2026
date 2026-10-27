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

Run `python3 checker.py` in this directory. It uses Python's standard library only and independently builds every four-run binary word of lengths 4 through 13. For each it counts distinct palindrome-pair factors by enumerating all substrings and all palindrome splits, compares with the closed formula, and confirms strict separation from the three-run witness count. It also checks the three-run construction at lengths 3 through 13.

The checker reports `EXACT_CHECK_OK 715 four-run words, plus three-run witnesses`. The finite length 4–9 table comprises 126 positive quadruples and is exhaustively covered by the checker. The proof's algebraic arguments cover all n at least 10 without computational dependence. No search beyond these finite boundaries is asserted, and no external validation has been performed.
