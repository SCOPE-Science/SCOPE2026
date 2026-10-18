---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

PASS: Work with omitted matching-index sets U={i:a_i outside S}, V={i:b_i outside S}. If |U|>=2, shared omission with V destroys distinct traces after deletion of one selected matched sensor; likewise for |V|>=2, so either U=V={i} or U cap V=empty. In disjoint case, a missing a_i has selected B trace q-1; it must survive any single selected deletion, forcing q>=3 when U,V nonempty; if U empty all selected A remain and q>=2 suffices, and symmetrically. These necessary conditions imply complement and crown nonempty, different traces after each possible removal. They yield the exact binomial-sum all-set polynomial and min values 4(n3),6(n4,n5),n(n>=6), with specified counts. A new literal implementation exhaustively checked all subsets of Cr_n and its graph complement for n=3..7, including all selected single-vertex deletions (21824 candidate subsets). Infinite proof relies on trace classification, not finite checks.

## originality

PASS

PASS best-of-knowledge: 2023 introducing paper defines simultaneous stable location-domination in graph and complement, but the full omitted-index classification and generating polynomial for matching-deleted complete bipartite graphs are not supplied by the general results inspected.

## value

PASS

PASS: Full classification and exact cardinality spectrum of a natural family under a genuine fault-tolerant, complement-simultaneous locating invariant provides reusable structural information and sharp n>=6 transversal description.

The dated certificate retains the supplied scientific assessment, sources and limitations.
