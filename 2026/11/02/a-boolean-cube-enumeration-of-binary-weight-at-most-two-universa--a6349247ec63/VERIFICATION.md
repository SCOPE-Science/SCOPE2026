---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For all k>=2, build the overlap digraph on binary (k-1)-words of weight <=2, with a labeled edge for each k-word of weight <=2. The graph is balanced and strongly connected, and a unique zero-word self-loop fixes the starting rotation. The fixed-first-edge BEST/last-exit theorem counts cycles by rooted directed in-arborescences; since all outdegrees are 1 or 2, local factorials are 1. Weight-2 vertices have forced shift-plus-zero edges. Contracting their paths leaves each singleton index j=0..m-1 (m=k-1) with Z(j)=j-1 (0 maps to root) or O(j)=m-1-j. If low j<=floor((m-1)/2) selects O, the nonempty interval [j,m-1-j] is forward invariant, forbidding root access. If all lows select Z, either choice at every high j decreases index and reaches root; highs are independent. There are floor(m/2) high indices, giving U_k=2^floor((k-1)/2). Each cycle has k ones by double-counting the total factor weight k+2C(k,2)=k^2. Independent index-choice exhaustive calculation checked k=2..14, not the full theorem.

## originality

PASS

Best-of-knowledge O PASS for the precise assessed final statement. Reviewed the actual final package and compared statements/implications with primary literature and published SCOPE/Resultary semantic results, using aliases, broader cases, tables and corollary checks. A Boolean-cube enumeration of binary weight-at-most-two universal cycles: the cited prior results cover background tools, objects and/or weaker observables; no identified theorem implies the complete evaluated final statement. Negative search is not a novelty proof; primary-source limitations and risks are explicit.

## value

PASS

This gives a complete all-k enumeration and canonical Boolean-cube bijection of the entire natural set of rotation classes of weight-[0,2] binary universal cycles. Existence and generic BEST machinery were known; evaluating and classifying every tour for a meaningful constrained language is a standalone nontrivial enumeration, useful as a benchmark for random generation and higher-weight work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
