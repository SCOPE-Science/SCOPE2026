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

# Reproduction

Execute `python3 verify_mas.py` under Python 3 using only the standard library. The script implements a greedy-independent subsequence membership predicate by scanning the source word and tests deletion minimality directly, and separately evaluates the algebraic greedy-cost criterion. It exhausts all binary candidate words of length at most \(2m+1\) for each \(m\in\{1,\ldots,8\}\), checks the bivariate coefficient recurrence for these cases, and verifies the first twelve total counts. The successful run ends with `VERIFY_OK`.

# Scope of checks

The brute-force checks certify only the stated finite ranges. They cannot prove that the rational enumeration or exponential asymptotic holds for all \(m\); those statements are established by the symbolic proof in `RESULT.md`. The independent audit status above refers only to external scientific validation, which has not occurred.
