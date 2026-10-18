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

PASS. The indexed edge-deleted bipartite adjacency yields exactly x_i=0⇒Y−y_i≥2 and y_i=0⇒X−x_i≥2. For n≥4 weight ≤3 impossible: if both shore sums positive then a shore total ≤1 forces a zero on the other shore to see ≤1; if all labels on one shore, weight≥n. For weight4, shore totals (1,3),(3,1) fail; (0,4),(4,0) occur only when n=4 as one-shore all-one assignments; (2,2) forces simultaneous zero indices and hence identical side patterns with either one 2 or two 1s. For n3 the only weight3 minima are the two all-one shore functions; Cr2 is two disjoint edges and each K2 has three weight2 patterns, yielding 9. Thus claimed values and counts are exact for all n≥2. Independent bounded-weight enumeration n=2..7 recovered (4,9),(3,2),(4,12),(4,15),(4,21),(4,28), independently from package's exhaustive checker through n6. The arbitrary-n result follows from the shore-total proof.

## originality

PASS

Best-of-knowledge PASS for the complete crown minimum-Italian labeling classification and its n=2,3,4 transitions. The definition Roman-{2}/Italian domination predates the claim, and Shao–Zhao 2026's Italian polynomial applies to paths, trees, and cycles, not complete matching-deleted bipartite crowns except the C6 boundary's known scalar. Existing Resultary all-function Roman-{2} weight enumerator concerns complete multipartite graphs including Knn before deletion; a crown for n≥3 is not complete multipartite. A published perfect Roman crown minimum has n paired-2 patterns but cannot imply all two-pair-1 Italian optimizers. Plausible Klostermeyer–MacGillivray 2019 article was accessed only to publisher/indexed text; full lawful Oxford request returned vpn_disconnected and complete overlap remains a material risk, not automatic failure.

## value

PASS

PASS. Exact count and entire support structure of minimizing Roman-{2} functions on the natural perfect-matching-deleted K_nn family is a motivated extremal domination invariant; deletion creates boundary behavior at n3/n4 and a stable combinatorial two-family census. Not merely the known scalar on complete bipartite graphs, and not a needlessly arbitrary finite slice. Does not purport to determine the full domination polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
