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

Run `python checker.py` from the directory containing this document and the checker. The observed result is `ALL_CHECKS_OK independent finite instances 4..20; explicit witnesses 4..600; checked groups 613`.

The checker enumerates **all** independent dominating subsets and three-subset combinations for every path size from \(4\) through \(20\); this finite check is separate from the symbolic argument. At every applicable size through \(600\), it builds the explicit construction recursively from the stated bases, checks independence and domination for each of the three sets and checks the minimum of the three symmetric-difference distances. It also enumerates the five independent dominating sets for \(n=6\).

The infinite exact statement follows from the universal three-word counting bound and the correctness of the repeatable insertion at the three residue-class bases. Numerical replay alone would not prove the arbitrary-size assertion. All arguments are elementary finite combinatorics and do not assume randomized testing, a SAT solver or third-party packages.
