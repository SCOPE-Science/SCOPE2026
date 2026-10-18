---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

The specified seven-height word p=(0,2,4,6,1,3,5) has no cyclically adjacent consecutive heights and hence no trivial deletion. Applying the explicit cyclic-height rotation and half-turn symmetry yields the same canonical cyclic representative. Independent bounded enumeration against the Colton-style crossing-exchange pair partition examined all 7·(binomial choice of m,w with gap≥2)=70 candidate triples and found no legal crossing exchange. With no count-preserving move leading away, any reduction to five petals must first increase to nine. The fully explicit path uses T+ to (0,7,6,2,4,8,1,3,5), X(4,2,5) to (0,7,5,3,4,8,1,2,6), then two T− deletions to (0,3,1,4,2), a cyclic rotation of the known five-petal trefoil (3,1,4,2,0). The exact verifier sourced from artifacts/verify_trefoil_excess.py was inspected, and its exhaustive local search and displayed detour were independently reconstructed from definitions. Only the given finite word is exhaustively certified, not arbitrary knots.

## originality

PASS

The original recent question explicitly asks about hard petal diagrams of nontrivial knots, while its abstract and accessible source description focus on hard unknots; the source full text was not obtainable through open access or institutional connection and cannot support a whole-document noncoverage assertion. Colton et al. give the complete move calculus and a known five-petal trefoil but no barrier for this seven-petal word in the materially inspected sections. The explicit exact obstruction and minimal nine-petal detour are a credible best-of-knowledge answer with meaningful recent-preprint priority risk. Resultary lookup failed; this is not a novelty certificate.

## value

PASS

This is a motivated smallest nontrivial-knot obstruction to monotone petal simplification with a complete exact minimax path and sharp two-petal excess. It addresses the problem raised by the contemporaneous petal-move literature, rather than reporting an arbitrary enumerated knot word.

The dated certificate retains the supplied scientific assessment, sources and limitations.
