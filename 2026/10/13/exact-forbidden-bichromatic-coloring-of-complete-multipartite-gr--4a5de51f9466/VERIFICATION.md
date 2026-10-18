---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

A proper color class in K_{n_1,...,n_r} must be contained in one part. Two color classes in different parts induce K_{a,b} and contain the connected bipartite forbidden H exactly when (a,b) dominate its two shore sizes (s,t) in either order. Maximizing per-part classes reduces to exactly two exhaustive regimes: no class of size >=t, or one part allowed large classes while every other part has classes of size <=s-1. The matching lower and upper constructions give chi = sum_i ceil(n_i/(t-1)) for s=1; for s>=2, chi = min{sum_i ceil(n_i/(t-1)), min_j[1+sum_{i!=j}ceil(n_i/(s-1))]}. Boundaries t>=2, r>=2 and n_i>=1 are properly handled; independent partition search checked 270 small tuples, while the two-regime proof covers all parameters.

## originality

PASS

Best-of-knowledge novel complete multipartite bicromatic-H formula and shore-size collapse for arbitrary connected bipartite H; the s=1 star/frugal case is known. Checked contemporaneous (2,F)-avoiding literature and related complete-multipartite published results; no demonstrated implication covers the s>=2 case. Lu–Ying–Song full text was inaccessible after lawful retrieval attempts, so priority risk is explicit.

## value

PASS

A complete exact coloring invariant for the natural and broad class of connected complete multipartite hosts, reducing every connected bipartite H to two shore sizes and a computable sharp two-regime optimum, is a structurally motivated natural classification. Beyond the already known star/frugal slice it settles an infinite parameter family rather than a table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
