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

The four boundary sentences have ranks 1, 2, 3, 3. Nonzero idempotents are exactly e_ii, and a nonzero unit has one or two endpoint idempotents detectable by the stated atoms. Thus the covers in the last three sentences exist exactly for n <= 2, 3, 4, respectively; e_12 squares to zero when n >= 2, giving the first cutoff. For the tail, copy all coordinate equalities of the first two moves. Copy exactly on the last move whenever the total is at most five indices (including when the move introduces two fresh indices to a prefix with at most three). Otherwise the three edges have six distinct endpoints, and the last edge can reuse a previous row as its row while keeping a fresh column: row and column sets remain disjoint. The new edge is distinct, and every product of the three units, including squares, is zero. This preserves all multiplication and equality atoms including those with named zero, in either play direction. It proves the infinite tail, independently of any enumeration. Representation sizes are n^2+1. Independent replay: `python3 /workspace/branches/independent_checks.py 5` computes rank-three types directly from finite multiplication tables for n=1..6, returning five distinct initial types and equality at 5 and 6. The frozen three checkers and recorded outputs were inspected, not executed.

## originality

PASS

The distinct supported claim is the exact finite unrestricted-variable rank-three partition in the zero-named ternary relational language. A later Resultary extension directly repeats that partition and explicitly treats cutoff five as previously established; its new cutoff six is for three reusable variables at arbitrary depth. This is real overlap, not evidence of an earlier independent covering result. The same-day strictly upper-triangular result uses a different family with no nonzero idempotents. The closest inspected primary results concern automorphisms/categoricity and algebraic identities/varieties, not the claimed finite rank threshold.

## value

PASS

A sharp logical cutoff for the whole matrix-unit family is useful for comparing finite semigroup presentations at bounded relational depth. It improves on the naive six-index copying bound and explains exactly which coordinate coincidence a rank-three observer cannot see. The four distinct lower boundaries and infinite tail make this more than a finite type tally.

The dated certificate retains the supplied scientific assessment, sources and limitations.
