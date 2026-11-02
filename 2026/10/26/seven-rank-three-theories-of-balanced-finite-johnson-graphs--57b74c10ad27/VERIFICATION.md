---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For nonempty vertex-transitive simple graphs, the three-move Ehrenfeucht–Fraïssé winning criterion is equality of all possible distinct-ordered-pair edge indicators and sets of third-vertex adjacency patterns. The first chosen vertex can be matched by transitivity, the second determines a pair profile, and the third can be matched exactly when its four-bit extension mask is present. For Johnson k-sets, intersection distance d=1,2,≥3 gives the claimed edge/nonedge masks by exchanging elements of I=A∩B, X=A\B, Y=B\A and Z=ground\(A∪B). The unique disjoint k=3,n=6 exception is a pigeonhole obstruction to a third vertex nonadjacent to both; with n≥7 an extra element supplies one. For k=2 the outside-element thresholds are n=5 and n=6; k=1 complete-graph threshold is n=3. Independent brute-force subset enumeration checked masks and seven distinct profiles in representative bounded cases. The arbitrary-size assertion follows from the constructive proof, not extrapolation.

## originality

PASS

The exact all-parameter claim was compared by statement and implication against all identified strongly related primary works; known constructions, setup theorems and restricted subclasses are acknowledged as prior. The four structured comparisons and source inspections distinguish unproven priority from a concrete known coverage implication. Under a best-of-knowledge standard the unlocated stronger result is a stated risk, not an invented negative full-text finding.

## value

PASS

A complete two-parameter, unbounded-family classification for an exact logical complexity measure in distance-regular graphs is useful on its own. It identifies a large rank-three indistinguishability collapse and an exceptional small case, not merely a list of finite computations. It does not imply anything about rank four, counting logic or richer betweenness signatures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
