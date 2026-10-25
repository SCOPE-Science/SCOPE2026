---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Each τ-stable chessboard face comprises d diagonal singleton orbits and e off-diagonal paired orbits; oriented augmented chain sign is -(-1)^(d+e). Off-diagonal chosen pairs form a labeled simple graph H; both row and column occupancies are deg_H(i). Independent diagonal inclusion/exclusion gives (-1)^|E(H)|(1-1)^#{i:deg_H(i)<r}, so only r-regular H survive, each with nr/2 edges. Thus reduced Lefschetz=-(-1)^(nr/2)R(n,r), including nr odd case. Absolute trace yields Betti sum bound; r=2 two-regular cycle decomposition gives EGF; at r=n-1 Singh sphere theorem gives orientation sign (-1)^(C(n+1,2)+1). Independently enumerated invariant off-diagonal/diagonal orbits and labeled regular graphs for n2..4/all caps: traces 1;0,1;-3,-3,-1 (exact matches), without using saved log. Infinite validity comes from binomial cancellation, not finite enumeration.

## originality

PASS

Bounded statement-and-implication comparisons with published primary and related research did not identify coverage of the precise new assertion, and the distinct contribution is established by the indicated independently checked argument; priority remains subject to specifically recorded access risks.

## value

PASS

The factor-interchange action is a natural extra symmetry of higher chessboard/matching complexes, distinct from independent row/column relabelings. The all-(n,r) signed regular-graph Lefschetz identity creates a reusable link between finite combinatorial counts and topological characters; its extremal orientation and uniform Betti lower bound are motivated consequences, rather than rebranding known nonequivariant homotopy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
