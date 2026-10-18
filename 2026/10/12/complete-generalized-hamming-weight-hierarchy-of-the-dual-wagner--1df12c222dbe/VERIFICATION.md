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

The exact CodeTables 14-by-23 Wagner generator, retrieved at the assigned Git blob, has rank 14 and independently verified primal minimum distance 5 (all 2^14 primal words). Its dual is ker(G), dimension 9. For every coordinate set X, dim ker(G_X)=|X|-rank(G_X), so d_r=min{|X|:nullity>=r}. A separately written exact XOR-rank implementation exhausted all 2^23=8,388,608 subsets and gave d_1..d_9=(8,12,15,17,18,20,21,22,23), proving both minima and exclusions without sampling; no statement is made about other [23,9] codes.

## originality

PASS

The distinct original scientific result is the ENTIRE nine-coordinate generalized-weight hierarchy for the dual of the unique binary [23,14,5] Wagner code. A known 24-point Sidon maximum implies the d_6=20/projective-plane consequence, explicitly excluded from the novel part; remaining hierarchy entries are not established by the CodeTables ordinary-distance entry, Simonis uniqueness, or Kurz–Landjev–Rousseva dimension<=7 extremal bounds. Best-of-knowledge only: complete Simonis 2000 text inaccessible (institutional VPN disconnected), unindexed earlier exact hierarchy remains possible.

## value

PASS

The code is the unique extremal [23,14,5] binary object, and its dual generalized weights quantify all support thresholds for information access, puncturing/shortening, and projective multisets. Nine simultaneous exact minima constitute a natural complete invariant of a motivated nontrivial code, not an arbitrary tiny instance or a recomputation of the ordinary distance; the already known Sidon consequence is separately credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
