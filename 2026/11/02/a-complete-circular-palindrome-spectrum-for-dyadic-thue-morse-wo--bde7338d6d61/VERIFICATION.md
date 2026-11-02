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

## Executed verification
`checker.py` enumerates all circular factors of each finite Thue–Morse iterate at ranks 1–9; it computes distinct palindrome and antipalindrome sets without using the closed formulas, then compares the predicted count at every length for ranks 3–9 and the closed totals for ranks 2–9. Executed results were:

| Rank | Word length | Distinct circular palindromes | Distinct circular antipalindromes |
| --- | ---: | ---: | ---: |
| 1 | 2 | 2 | 2 |
| 2 | 4 | 6 | 4 |
| 3 | 8 | 12 | 8 |
| 4 | 16 | 20 | 20 |
| 5 | 32 | 44 | 36 |
| 6 | 64 | 76 | 84 |
| 7 | 128 | 172 | 148 |
| 8 | 256 | 300 | 340 |
| 9 | 512 | 684 | 596 |

All finite assertions passed. Exhaustive finite checks cannot establish the unbounded-rank theorem. The proof's crucial all-rank facts are the two injective morphic descriptions, the prohibition of length-five palindromes, and the exact two-word overlap at length two. Independent audit not performed.
