---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

PASS: On connected simple G, summing period-three updates makes the per-vertex firing count harmonic, hence uniformly 1 or 2 for primitive cycles. For one firing, each phase s(v) requires predecessor-neighbor count a_v>=1 and height 0<=u_v<a_v. Counting edges gives chip energy m+h(s)+sum u_v and full integer interval [m+h(s),2m-n]; complementation x->2d-1-x yields high interval [2m,3m-n-h(s)]. Phase rotations divide by three; resulting polynomial, reciprocity and endpoints follow. Independent direct F^3 enumeration matched phase polynomial on triangle, C4, K4 and B2; K4 coefficients 12 each.

## originality

PASS

PASS with substantial prior credit: Prisner (1994) Lemma 6.7 already characterizes activity-1/p phase partitions and Proposition 6.8 establishes cycle-divisibility period existence. The final claim is not novelty of existence or phases; it is a closed arbitrary-graph energy-weighted orbit enumerator, exact gap-free two-band support and endpoint multiplicities, with book-graph binomial cumulative refinement. Full Prisner transcription had missing symbols, leaving equivalence risk.

## value

PASS

PASS qualified: a natural conserved-chip statistic for primitive parallel three-cycles receives an exact all-connected-graph generating function and sharp forbidden energy gap. The known general phase construction does not state this evaluated graph-wide mass distribution; the explicit band structure is independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
