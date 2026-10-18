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

For every blade vertex outside an alliance, neighborhood counts yield 2*s_i>=m_i-1 when center selected and 2*s_i>=m_i+1 when center omitted. These are exactly s_i>=floor(m_i/2) and s_i>=floor(m_i/2)+1. When center omitted the latter sum automatically satisfies the outside center inequality because 2*sum_i s_i>=sum_i m_i+2*r-o >=sum_i m_i+1 (o number odd blades and r>=2). Therefore local thresholds are necessary and sufficient for all sets, whence x*product of upper binomial tails A_m plus product of strict tails B_m; minimum size 1+sum floor(m_i/2), all minimizers include center, count product binomial. Independent direct neighborhood enumeration compared every subset on 2031 checked graph/subset instances; the unbounded theorem follows the local inequalities.

## originality

PASS

Best-of-knowledge originality limited to the specifically unpreempted structural/classification content. The local clique-blade counting and global center redundancy are necessary independent steps; an exact polynomial is not an immediate corollary of available generic bounds.

## value

PASS

Heterogeneous windmills include friendship graphs and generalized windmills and have independent clique blades attached at a universal hub. A full all-set cardinality enumerator and precise minimum-set multiplicities are natural alliance invariants, distinct from the usual scalar extremal number, and allow arbitrary blade sizes; this is a motivated graph family, not an arbitrary slice of a table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
