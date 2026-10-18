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

# Reproducible finite verification

Execute `python3 verify.py` from the same directory as these documents; the program uses only the Python standard library. It independently generates every graph on one through five labelled original vertices, constructs its one-subdivision, tests every possible subdivision-vertex subset against the defining external-neighbor condition, and compares the resulting coefficient counts with a separately implemented matching expansion. All 1,099 graph comparisons passed.

For each of the 771 connected graph instances with at least two originals, the observed largest proper convex-set cardinality equals the subdivision order minus the original graph's minimum degree. The program also checks the complete-graph closed polynomial by direct enumeration through order five, and its coefficient support, quadratic absent-size count and extremal coefficient from order two through 25. All checks passed.

These are finite checks only. The all-graph matching bijection, complete-graph coefficient identities and support-gap theorem are proved mathematically in RESULT.md; the program is corroboration, not an infinite or independent certification. No independent audit has been performed.
