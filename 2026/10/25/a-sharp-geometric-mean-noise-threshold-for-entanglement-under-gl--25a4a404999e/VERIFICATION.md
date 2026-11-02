---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Exact stationary Lindblad resolvent r∫exp(−rt)e^(tL)(|00><00|)dt gives positive trace-one X matrix with rational entries A,B_a,B_b,S_a,S_b. A no-reset timewise nonnegative identity (1−e^(−4at))(1−e^(−4bt))+4e^(−2(a+b)t)sin²(2Jt) and Cauchy–Schwarz rule out the competing PPT branch for the stationary mixture. The remaining branch equals −P(r) divided by positive (r+2a+2b)² d_a d_b; symbolic independent exact simplification checked this identity. For J²≤ab, polynomial coefficients nonnegative and constant positive; for J²>ab, descending coefficient signs have exactly one variation and P(0)>0>P(∞), so exactly one positive root. Expanding offdiagonal J/r and single-bit-flip populations a/r,b/r yields concurrence asymptotic. Independent symbolic checks and several four-parameter numerical root counts corroborated; mathematical argument covers all positive parameters.

## originality

PASS

Best-of-knowledge analysis compares the exact final theorem and logical implications with relevant primary full texts and published research records; known methods and special cases explicitly credited. No decisive coverage found in inspected theorem statements. Unindexed literature can still dominate; negative search is not proof of priority. See four structured comparisons and source-inspection details. A general separability theorem for this quantum channel or an overlooked quantum-reset extension might imply the quartic threshold by reduction.

## value

PASS

This isolates the precise robustness threshold for full-system reset-generated entanglement under two independent local bit-flip baths: the geometric-mean coupling J²>ab, rather than sum of rates, is sharp. It provides a unique finite reset-rate phase boundary and a nonzero but decaying strong-reset concurrence, physically motivated beyond elementary application of a generic PPT test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
