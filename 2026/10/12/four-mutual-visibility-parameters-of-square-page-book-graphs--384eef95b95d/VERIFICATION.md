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

The full 2r nonspine page set I is total-visible by explicit spine-only internal geodesics; selecting spine x in mutual set allows at most one a_i and selecting spine y at most one b_i. Cardinality bounds rule out spine-containing maxima for r>=3; direct geodesic blockage handles r=2 boundary. Thus all four values 2r with unique maximizer I. Independent breadth-first all-shortest-path and all-subset tests for r=2,3,4 reproduced maxima 4,6,8 and exactly one maximizing set for all variants; infinite r follows from structural proof.

## originality

PASS

Cicerone et al give four visibility variants and C5-page shared-edge book separation rather than exact C4 all-variant equality. A 2025 later characterization could imply a special case but inspected abstract does not establish that implication. The square C4 result is a natural transition with a unique maximizing configuration, not the related but distinct dual general-position problem.

## value

PASS

Shared-edge books are a canonical test family for mutual-visibility variants. The C4 page transition yields complete equality of four separately motivated invariants with a unique common extremizer, in contrast to known C5 separation; the result is a natural structural characterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
