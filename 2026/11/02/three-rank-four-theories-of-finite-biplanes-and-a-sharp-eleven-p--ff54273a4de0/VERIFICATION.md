---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The square incidence matrix identity MM^T=(k-2)Id+2J and equal row and column sums give the dual pair counts. For k>=5, a distinct same-sort triple has all seven non-triple extension cells nonempty; the remaining cell is present iff its triple overlap t is 1. Each distinct same-sort pair permits both t values (choose inside one of its two common blocks but outside their intersection, or outside both); mixed triple cells stay nonempty after exclusions, and equalities are answered by the corresponding named object. Recursing on sets of extension types gives uniform rank-two pair types by atomic diagram, uniform rank-three singleton types by sort, and the common rank-four empty-tuple type. For rank three the four opposite-sort pair cells are all positive already at k>=4. The point outside a block pair separates k=3 at rank three; the rank-four formula asserting exactly one such point separates k=4, since u(k)=(k-2)(k-3)/2. The k=3 design is all 3-subsets of four points; at k=4 complementing blocks gives the unique Steiner triple system on seven points: label a noncollinear triple a,b,c and their pair completions d,e,f. For the seventh point g the remaining lines through a,b,c are respectively afg,beg,cdg, and the last line is def. For the Paley representative D={1,3,4,5,9} mod 11, the ten unordered pairs have circular distances 1 through 5 exactly twice each, giving the required directed difference multiplicities. Monotonicity of v(k) proves minimality within biplanes, not among arbitrary relational structures. Inspected both C++ sources and the recorded rank-three/rank-four transcripts; they compare four examples and were not executed or used as proof of the arbitrary-parameter conclusion.

## originality

PASS

The rank-three collapse tail materially overlaps a same-day stronger three-variable result, and is not credited here as a distinct contribution in isolation. The supported distinct claim is the sharp rank-four classification in the specified biplane language and its eleven-per-sort representative bound. The strongest inspected comparisons do not give the four-move extension profiles or this cutoff.

## value

PASS

For a standard design class the theorem pins down the first rank that sees the k=4 boundary, handles arbitrary quantifier alternation in the specified language, and yields a sharp constant-size representative within biplanes, including those at unknown parameters if they exist. This is more than recomputing the types of familiar small designs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
