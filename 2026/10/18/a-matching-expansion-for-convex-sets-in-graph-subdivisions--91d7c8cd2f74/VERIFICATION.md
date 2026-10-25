---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Fixing selected original vertices A, every subdivided edge internal to G[A] is forced selected; selected subdivision edges internal to B=V\A must form a matching, and each B-vertex not covered by that matching independently chooses none or one selected cross edge into A. These necessary and sufficient conditions prove the generating polynomial bijectively for arbitrary finite simple G, including disconnected graphs. In K_n, choose |A|=a and j-matching in K_{n-a}; the support for a>=1 is the full interval [a(a+1)/2, n+a(a-1)/2], and summing gaps max(0,2a-n) gives floor((n-1)^2/4); a=0 gives no additional positive sizes. For any connected G, a proper convex set must omit at least one original vertex; its internal edges exclude >=delta(G) originals, and each omitted vertex supports at most one extra selected subdivision edge, giving |C|<=|V|+|E|-delta(G), attained by omitting one min-degree vertex and selecting exactly one cross subdivision. Independent brute all 8 graphs on 3 vertices, all 64 on 4 vertices, and seven five-vertex graphs reproduced the matching-expansion coefficients.

## originality

PASS

Dourado–Grippo–Lin–Protti 2026 develop general P3-convex counting algorithms, hardness and special classes including trees and threshold graphs, but the inspected primary full HTML does not state the all-graph one-subdivision matching decomposition, complete-subdivided-clique coefficient polynomial or quadratic gap count. Hamming graph Carathéodory work concerns a different graph family and invariant.

## value

PASS

The natural one-subdivision operation turns P3-convexity into a matching-and-boundary decomposition giving a complete all-coefficient count. The complete-graph specialization yields an exact striking cardinality-gap spectrum and a general connected-graph extremal size law; these are motivated combinatorial enumerative invariants, not just a particular computer count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
