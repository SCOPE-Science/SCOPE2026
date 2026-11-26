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

# Verification and reproducibility

The standalone Python 3 program `verify.py` has no external dependencies. Run `python3 verify.py`. It checks the coefficient at the stated minimum weight at even orders 6 through 42 by enumerating independent zero supports and counting proper three-colourings of the inequality graph. It also enumerates all four-symbol assignments at the target weight at orders 6, 8 and 10. The expected outcome is `VERIFY_OK direct_labelings_n=6,8,10 all_minimum_counts_n=6..42_even cases=19`.

These finite computations do not prove the universal statement. The proof in `RESULT.md` derives the optimal weights and counts all corresponding supports by alternating tracks on the lifted strip. In the two-run case it checks agreement between the two forced three-periodic colourings at the shared vertices; the shared vertices need not lie in a common triangle.
