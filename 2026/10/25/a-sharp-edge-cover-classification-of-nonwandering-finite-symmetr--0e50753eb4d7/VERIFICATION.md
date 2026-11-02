---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For the specified compact binary-shift quotient, classify large-time orbit transition pairs: p may go to any target; an x rising front can approach p or a falling y front; a y front can approach p or a rising x; a finite island can approach only p. Growing island blocks realize opposite-front arcs, and inverse shifts realize p->target; a finite list of arcs is realized at the same diverging times with distinct source configurations. A nonwandering A in F_n yields, after convergent point assignments and m_j tending to infinity unless A={p}, an in/out-cover of A using at most n distinct arcs. The converse realizes any such edge cover simultaneously. Bipartite edge-cover theorem gives min size 2|A|-maximum_matching, with infinity when isolated on either side. A={p,two distinct islands} has threshold 4. Independently enumerated small matching/edge-cover examples; not exhaustive dynamic verification.

## originality

PASS

Đorić October 2026 full primary text explicitly classifies F_2(g) in Proposition 7 but does not supply a general F_n exact threshold for all finite A. The all-level in/out transition correspondence and edge-cover formula give new quantitative conclusions including n=4 on three points; these are not entailed by the F_2 classification alone. Standard bipartite edge-cover identity is acknowledged prior math. Semantic published-finding search yielded no dominating equivalent theorem.

## value

PASS

The original system is a canonical example of unexpected nonwandering finite-set behavior, for which the literature treats only level 2. A complete sharp computationally tractable hierarchy for all finite configurations, with a strict three-to-four-particle onset, addresses the natural generalization and illustrates extra approximating points vanishing in the Hausdorff limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
