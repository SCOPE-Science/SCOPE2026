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

# Verification and limits

The included `verify.py` first computes the generalized Cantor word by two independent finite procedures: uniform substitution and a base-\(q\) digit-membership test. It then enumerates distinct factors of length \(q^k\) in a sufficiently long substitution prefix, independently calculates each candidate's proper borders through a standard KMP prefix-function computation, and compares the exact set to the theorem's explicit formula and its reversals.

The program tests every pair \((q,k)\) with \(3\le q\le7\), \(1\le k\le4\), plus \((3,5)\), \((3,6)\), \((4,5)\), and \((5,5)\). Observed final line:

`VERIFY_OK independent_digit_vs_substitution cases=24 complete_borders=yes`

Each constructed prefix has two additional substitution levels beyond the requested factor length; testing a longer finite prefix is not a proof that all infinite factors have appeared there. Completeness for all integers in the theorem follows instead from the substitution-block proof in `RESULT.md`. No external or independent scientific audit was performed.
