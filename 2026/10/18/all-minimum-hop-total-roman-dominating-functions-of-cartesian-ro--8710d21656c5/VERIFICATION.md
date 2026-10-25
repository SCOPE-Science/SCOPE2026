---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Case distinction by number t of label-two cells proves lower bound min(mn,m+n,n+2,m+2,6) on K_m square K_n. Equality for t=0,1,2 forces all-one, defender cross, same-row/column, or opposite-defender patterns; at t=3 weight six and total positive support excludes triangles for m,n>=4, leaving 2x2 L. These six feasible disjoint families yield all minima, including tied exceptional widths and exact labeled counts. Read RESULT.md and verify.py at immutable commit; direct checker enumerates small-weight labelings on 13 boards (reported replay not treated as infinite proof).

## originality

PASS

Independent best-of-knowledge statement/implication comparisons distinguish this final theorem from relevant prior source claims. Previously known summation, size, geometric existence, and binary subcases are credited; no absolute priority guarantee is claimed.

## value

PASS

All minimum labelings, not just the extremal weight, of a canonical 2-parameter graph product form a natural classification with nontrivial width-2, width-3, width-4 transitions and exact multiplicities. Such extremizer families are reusable in domination enumerations and graph product comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
