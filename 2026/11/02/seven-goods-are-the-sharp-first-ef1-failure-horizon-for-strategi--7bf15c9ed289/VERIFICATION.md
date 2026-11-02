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

Run `python3 verify.py certificate.json` from this directory. It uses only Python 3's standard library and exact integer arithmetic.

The verifier tests that each agent strictly ranks all 128 bundles; recomputes the complete subgame-perfect continuation sets using two independent directions (top-down memoization and bottom-up state traversal); compares both sets at each of 128 states; establishes exactly two root outcomes; and verifies the single root outcome \((41,68,18)\), or \((\{g_1,g_4,g_6\},\{g_3,g_7\},\{g_2,g_5\})\), has an EF1 violation by agent B against A.

It then recursively builds a specific complete off-path strategy profile that supports that root allocation and checks unilateral one-shot deviations at every encountered history, including 13,700 tree nodes. Perfect-information backward induction (and the one-shot deviation principle for finite games) turns those node checks into the stated pure SPNE witness. The exact B-to-A utility comparison is 1092 against the minimum 1161 after deleting an A-good. The executable checks the stored `certificate.json` against independent recomputation.

# Limits

The code verifies the seven-good finite certificate. The \(m\le2n\) protection for all monotone valuations is proved analytically in RESULT.md, not established by finite enumeration. The calculations do not prove publication priority, uniqueness of the unfair equilibrium, or a characterization of all possible valuation matrices.
