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

# Reproducibility and limitations

Run `python3 verify.py` with Python 3 standard library. The embedded exact checker prints `PASS 1642 assertions` and the fourteen strict signs at sample size 14. It independently sums the exact multinomial probability weights for all compositions into three box counts at every sample size from 2 through 21 and compares the result with the general moment formula. It also checks four dominant-base inequalities, the algebraic power bounds, selected witnesses at sizes 150, 160, 200, and 300, and the complete two-box covariance signs for a finite test range.

The infinite-family statement for every integer \(t\ge15\), the three-box minimality, and the open-neighborhood persistence rely on the explicit arguments in RESULT.md; finitely many checker assertions cannot by themselves establish any of these quantified claims. All arithmetic in the checker uses exact Python integers and combinatorial coefficients. The investigation does not certify uniqueness against every historical source and does not constitute independent mathematical validation.
